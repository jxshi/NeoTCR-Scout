"""Rule-based neoantigen candidate generation."""

from __future__ import annotations

import re

from neotcr_scout.models import Mutation, PeptideCandidate

# KRAS canonical protein segment around codons 1-20; enough for v0.1 examples.
KRAS_REFERENCE = "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV"
_MUTATION_RE = re.compile(r"^\s*(?P<gene>[A-Za-z0-9_-]+)\s+(?P<wt>[A-Z])(?P<pos>\d+)(?P<mut>[A-Z])\s*$")


def parse_mutation(text: str) -> Mutation:
    """Parse a mutation label such as ``KRAS G12D``."""

    match = _MUTATION_RE.match(text)
    if not match:
        raise ValueError(f"Unsupported mutation format: {text!r}; expected e.g. 'KRAS G12D'.")
    return Mutation(
        gene=match.group("gene").upper(),
        wildtype=match.group("wt"),
        position=int(match.group("pos")),
        mutant=match.group("mut"),
    )


def _reference_for_gene(gene: str, reference_sequences: dict[str, str] | None = None) -> str:
    references = {"KRAS": KRAS_REFERENCE}
    if reference_sequences:
        references.update({key.upper(): value for key, value in reference_sequences.items()})
    try:
        return references[gene.upper()]
    except KeyError as exc:
        raise ValueError(f"No reference sequence configured for gene {gene!r}.") from exc


def generate_peptides(
    mutation: Mutation | str,
    lengths: tuple[int, ...] = (8, 9, 10, 11),
    reference_sequences: dict[str, str] | None = None,
) -> list[PeptideCandidate]:
    """Generate unique mutant peptide windows that contain the substituted residue."""

    parsed = parse_mutation(mutation) if isinstance(mutation, str) else mutation
    reference = _reference_for_gene(parsed.gene, reference_sequences)
    zero_based = parsed.position - 1
    if zero_based < 0 or zero_based >= len(reference):
        raise ValueError(f"Mutation position {parsed.position} is outside {parsed.gene} reference sequence.")
    observed = reference[zero_based]
    if observed != parsed.wildtype:
        raise ValueError(
            f"Reference mismatch for {parsed.label}: expected {parsed.wildtype} at position "
            f"{parsed.position}, observed {observed}."
        )

    mutant_sequence = reference[:zero_based] + parsed.mutant + reference[zero_based + 1 :]
    candidates: list[PeptideCandidate] = []
    seen: set[str] = set()
    for length in lengths:
        for start in range(max(0, zero_based - length + 1), min(zero_based + 1, len(mutant_sequence) - length + 1)):
            peptide = mutant_sequence[start : start + length]
            if peptide in seen:
                continue
            seen.add(peptide)
            candidates.append(
                PeptideCandidate(
                    sequence=peptide,
                    length=length,
                    mutation_index=zero_based - start,
                    source_mutation=parsed,
                )
            )
    return candidates
