"""NeoTCR-style local evidence adapter.

This adapter represents locally curated NeoTCR/literature-style records. It is
an evidence source adapter only; it does not generate or design TCRs.
"""

from __future__ import annotations

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence

NEOTCR_SEED = [
    TCREvidence(
        source="NeoTCR",
        epitope="VVVGADGVGK",
        hla="HLA-A*11:01",
        tra_cdr3="CAVRDSNYQLIW",
        trb_cdr3="CASSLGQDTQYF",
        trbv="TRBV7-9",
        trbj="TRBJ2-3",
        organism="human",
        disease="cancer",
        assay="literature-curated T-cell reactivity evidence",
        pubmed_id="demo",
        url="https://example.org/neotcr-local-seed",
        evidence_level="literature evidence",
        gene="KRAS",
        mutation="G12D",
        metadata={"identifier": "NEOTCR-KRAS-G12D-001", "provenance": "NeoTCR-style seed fixture"},
    )
]


def search_neotcr(peptide: str, hla: str) -> list[TCREvidence]:
    """Search NeoTCR-style local records by peptide and normalized HLA."""

    normalized_hla = normalize_hla(hla)
    hits: list[TCREvidence] = []
    for evidence in NEOTCR_SEED:
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if evidence.epitope == peptide or evidence.epitope in peptide or peptide in evidence.epitope:
            hits.append(evidence)
    return hits
