"""Mutation-to-peptide engine for NeoTCR-Scout v0.1."""

from __future__ import annotations

import re
from dataclasses import dataclass

AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")
DEFAULT_PEPTIDE_LENGTHS = (8, 9, 10, 11)
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
    # 1-based mutation position within this peptide window.
    mutation_position: int
    # 0-based mutation index within this peptide window.
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
    wildtype = match.group("wt")
    mutant = match.group("mut")
    if wildtype not in AMINO_ACIDS or mutant not in AMINO_ACIDS:
        raise ValueError(f"Unsupported mutation {mutation!r}; amino acids must be canonical one-letter codes")
    if wildtype == mutant:
        raise ValueError(f"Unsupported mutation {mutation!r}; wild-type and mutant amino acids must differ")
    return ParsedMutation(
        wildtype=wildtype,
        position=int(match.group("position")),
        mutant=mutant,
    )


def apply_mutation(wt_sequence: str, mutation: str) -> tuple[str, str]:
    """Apply a mutation and return ``(wild_type_sequence, mutant_sequence)``.

    If the provided sequence already contains the mutant residue, the function
    reconstructs the wild-type sequence for reporting.
    """

    parsed = parse_mutation(mutation)
    sequence = _normalize_protein_sequence(wt_sequence)
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
    mutation_index = parsed.position - 1 - start
    if mutation_index < 0 or mutation_index >= length:
        raise ValueError(
            f"Peptide window {start + 1}-{end} does not contain mutation position {parsed.position}"
        )
    return MutantPeptide(
        gene=gene.upper(),
        mutation=parsed.label,
        sequence=mutant_peptide,
        length=length,
        start=start + 1,
        end=end,
        mutation_position=mutation_index + 1,
        mutation_index=mutation_index,
        wildtype_peptide=wildtype_peptide,
        mutant_peptide=mutant_peptide,
        flanking_context=mutant_sequence[flank_start:flank_end],
        sequence_context=sequence_context,
    )


def generate_mutant_peptides(
    gene: str,
    mutation: str,
    wt_sequence: str,
    lengths: list[int] | tuple[int, ...] | None = DEFAULT_PEPTIDE_LENGTHS,
) -> list[MutantPeptide]:
    """Generate peptide windows of the requested lengths containing the mutated residue.

    Each returned row preserves its window provenance even when repetitive
    sequence context yields the same mutant peptide sequence at multiple
    positions. By default, v0.1 emits 8-, 9-, 10-, and 11-mers.
    """

    parsed = parse_mutation(mutation)
    input_sequence = _normalize_protein_sequence(wt_sequence)
    observed = input_sequence[parsed.position - 1] if 0 <= parsed.position - 1 < len(input_sequence) else None
    context = "input_sequence_already_mutant" if observed == parsed.mutant else "mutated_from_wildtype_sequence"
    wild_type_sequence, mutant_sequence = apply_mutation(input_sequence, parsed.label)
    index = parsed.position - 1

    peptides: list[MutantPeptide] = []
    for length in _normalize_lengths(lengths):
        if length > len(mutant_sequence):
            continue
        min_start = max(0, index - length + 1)
        max_start = min(index, len(mutant_sequence) - length)
        for start in range(min_start, max_start + 1):
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


def _normalize_lengths(lengths: list[int] | tuple[int, ...] | None) -> list[int]:
    """Return peptide lengths as integers with clear errors for bad inputs."""

    if not lengths:
        return list(DEFAULT_PEPTIDE_LENGTHS)
    normalized: list[int] = []
    seen: set[int] = set()
    for value in lengths:
        try:
            length = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"peptide length {value!r} is not an integer") from exc
        if length <= 0:
            raise ValueError("peptide lengths must be positive integers")
        if length not in seen:
            normalized.append(length)
            seen.add(length)
    return normalized


def _normalize_protein_sequence(sequence: str) -> str:
    """Return an uppercase protein sequence with clear validation errors."""

    normalized = sequence.strip().upper().replace(" ", "")
    if not normalized:
        raise ValueError("Protein sequence must not be empty")
    invalid = sorted(set(normalized) - AMINO_ACIDS)
    if invalid:
        invalid_text = "".join(invalid)
        raise ValueError(f"Protein sequence contains invalid amino-acid code(s): {invalid_text}")
    return normalized
