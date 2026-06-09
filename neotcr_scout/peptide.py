"""Mutation-centered peptide generation for NeoTCR-Scout v0.1."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class MutantPeptide:
    gene: str
    mutation: str
    sequence: str
    length: int
    start: int
    end: int
    mutation_position: int
    sequence_context: str


_MUTATION_RE = re.compile(r"^(?P<wt>[A-Z])(?P<position>\d+)(?P<mut>[A-Z])$")


def generate_mutant_peptides(
    gene: str,
    mutation: str,
    wt_sequence: str,
    lengths: list[int] | tuple[int, ...] = (8, 9, 10, 11),
) -> list[MutantPeptide]:
    """Generate unique 8-11mer windows containing a protein substitution.

    ``wt_sequence`` is expected to be the wild-type protein sequence. For the
    common demo case where users paste the already-mutated KRAS G12D sequence,
    the function also accepts a sequence that already contains the mutant amino
    acid at the requested position.
    """

    match = _MUTATION_RE.match(mutation.strip().upper())
    if not match:
        raise ValueError(f"Unsupported mutation {mutation!r}; expected protein substitution like G12D")
    wildtype = match.group("wt")
    mutant = match.group("mut")
    position = int(match.group("position"))
    index = position - 1
    sequence = wt_sequence.strip().upper()
    if index < 0 or index >= len(sequence):
        raise ValueError(f"Mutation {mutation} is outside the provided {gene} sequence")

    observed = sequence[index]
    if observed == wildtype:
        mutant_sequence = sequence[:index] + mutant + sequence[index + 1 :]
        context = "mutated_from_wildtype_sequence"
    elif observed == mutant:
        mutant_sequence = sequence
        context = "input_sequence_already_mutant"
    else:
        raise ValueError(
            f"Sequence mismatch for {gene} {mutation}: position {position} contains {observed}, "
            f"expected wild-type {wildtype} or mutant {mutant}."
        )

    peptides: list[MutantPeptide] = []
    seen: set[str] = set()
    for length in lengths:
        if length <= 0 or length > len(mutant_sequence):
            continue
        min_start = max(0, index - length + 1)
        max_start = min(index, len(mutant_sequence) - length)
        for start in range(min_start, max_start + 1):
            peptide = mutant_sequence[start : start + length]
            if peptide in seen:
                continue
            seen.add(peptide)
            peptides.append(
                MutantPeptide(
                    gene=gene.upper(),
                    mutation=mutation.upper(),
                    sequence=peptide,
                    length=length,
                    start=start + 1,
                    end=start + length,
                    mutation_position=position,
                    sequence_context=context,
                )
            )
    return peptides
