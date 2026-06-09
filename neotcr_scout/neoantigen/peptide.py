"""Mutation-to-peptide engine for NeoTCR-Scout v0.1."""

from __future__ import annotations

import re
from dataclasses import dataclass

MUTATION_RE = re.compile(r"^(?P<wt>[A-Z])(?P<position>[1-9][0-9]*)(?P<mut>[A-Z])$")


@dataclass(frozen=True)
class ParsedMutation:
    wildtype: str
    position: int
    mutant: str

    @property
    def label(self) -> str:
        return f"{self.wildtype}{self.position}{self.mutant}"


@dataclass(frozen=True)
class MutantPeptide:
    gene: str
    mutation: str
    sequence: str
    length: int
    start: int
    end: int
    mutation_position: int
    mutation_index: int
    wildtype_peptide: str
    mutant_peptide: str
    flanking_context: str
    sequence_context: str


def parse_mutation(mutation: str) -> ParsedMutation:
    """Parse a protein substitution such as ``G12D``."""

    match = MUTATION_RE.match(mutation.strip().upper())
    if not match:
        raise ValueError(f"Unsupported mutation {mutation!r}; expected protein substitution like G12D")
    return ParsedMutation(
        wildtype=match.group("wt"),
        position=int(match.group("position")),
        mutant=match.group("mut"),
    )


def apply_mutation(wt_sequence: str, mutation: str) -> tuple[str, str]:
    """Apply a mutation and return ``(wild_type_sequence, mutant_sequence)``.

    If the provided sequence already contains the mutant residue, the function
    reconstructs the wild-type sequence for reporting.
    """

    parsed = parse_mutation(mutation)
    sequence = wt_sequence.strip().upper()
    index = parsed.position - 1
    if index < 0 or index >= len(sequence):
        raise ValueError(f"Mutation {mutation} is outside the provided protein sequence")
    observed = sequence[index]
    if observed == parsed.wildtype:
        wild_type_sequence = sequence
        mutant_sequence = sequence[:index] + parsed.mutant + sequence[index + 1 :]
    elif observed == parsed.mutant:
        wild_type_sequence = sequence[:index] + parsed.wildtype + sequence[index + 1 :]
        mutant_sequence = sequence
    else:
        raise ValueError(
            f"Sequence mismatch for {mutation}: position {parsed.position} contains {observed}, "
            f"expected wild-type {parsed.wildtype} or mutant {parsed.mutant}."
        )
    return wild_type_sequence, mutant_sequence


def annotate_peptide_window(
    gene: str,
    mutation: str,
    wild_type_sequence: str,
    mutant_sequence: str,
    start: int,
    length: int,
    sequence_context: str,
) -> MutantPeptide:
    """Build a fully annotated peptide window."""

    parsed = parse_mutation(mutation)
    end = start + length
    flank_start = max(0, start - 3)
    flank_end = min(len(mutant_sequence), end + 3)
    mutant_peptide = mutant_sequence[start:end]
    wildtype_peptide = wild_type_sequence[start:end]
    return MutantPeptide(
        gene=gene.upper(),
        mutation=parsed.label,
        sequence=mutant_peptide,
        length=length,
        start=start + 1,
        end=end,
        mutation_position=parsed.position,
        mutation_index=parsed.position - 1 - start,
        wildtype_peptide=wildtype_peptide,
        mutant_peptide=mutant_peptide,
        flanking_context=mutant_sequence[flank_start:flank_end],
        sequence_context=sequence_context,
    )


def generate_mutant_peptides(
    gene: str,
    mutation: str,
    wt_sequence: str,
    lengths: list[int] | tuple[int, ...] = (8, 9, 10, 11),
) -> list[MutantPeptide]:
    """Generate unique peptide windows containing the mutated residue."""

    parsed = parse_mutation(mutation)
    input_sequence = wt_sequence.strip().upper()
    observed = input_sequence[parsed.position - 1] if 0 <= parsed.position - 1 < len(input_sequence) else None
    context = "input_sequence_already_mutant" if observed == parsed.mutant else "mutated_from_wildtype_sequence"
    wild_type_sequence, mutant_sequence = apply_mutation(input_sequence, parsed.label)
    index = parsed.position - 1

    peptides: list[MutantPeptide] = []
    seen: set[str] = set()
    for length in lengths:
        if length <= 0 or length > len(mutant_sequence):
            continue
        min_start = max(0, index - length + 1)
        max_start = min(index, len(mutant_sequence) - length)
        for start in range(min_start, max_start + 1):
            mutant_peptide = mutant_sequence[start : start + length]
            if mutant_peptide in seen:
                continue
            seen.add(mutant_peptide)
            peptides.append(
                annotate_peptide_window(
                    gene=gene,
                    mutation=parsed.label,
                    wild_type_sequence=wild_type_sequence,
                    mutant_sequence=mutant_sequence,
                    start=start,
                    length=length,
                    sequence_context=context,
                )
            )
    return peptides
