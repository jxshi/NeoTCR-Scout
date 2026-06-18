"""NeoTCR seed evidence adapter for locally curated neoantigen-specific TCR rows."""

from __future__ import annotations

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence

NEOTCR_SEED = [
    TCREvidence(
        source="NeoTCR",
        epitope="VVVGADGVGK",
        hla="HLA-A*11:01",
        tra_cdr3="CAVRNNARLMF",
        trb_cdr3="CASSLAPGATNEKLFF",
        trbv="TRBV12-3",
        trbj="TRBJ1-4",
        organism="human",
        disease="cancer",
        assay="curated neoantigen TCR evidence",
        pubmed_id="demo",
        url="local://neotcr-scout/seed/neotcr",
        evidence_level="curated local evidence",
        gene="KRAS",
        mutation="G12D",
        metadata={"identifier": "NEOTCR-KRAS-G12D-001", "provenance": "NeoTCR seed fixture"},
    )
]


def search_neotcr(peptide: str, hla: str) -> list[TCREvidence]:
    """Search NeoTCR seed rows by exact peptide and normalized HLA."""

    normalized_hla = normalize_hla(hla)
    hits: list[TCREvidence] = []
    for evidence in NEOTCR_SEED:
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if evidence.epitope == peptide:
            hits.append(evidence)
    return hits
