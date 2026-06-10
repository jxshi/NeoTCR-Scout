"""Local VDJdb-style evidence adapter."""

from __future__ import annotations

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence

VDJDB_SEED = [
    TCREvidence(
        source="VDJdb",
        epitope="VVGADGVGK",
        hla="HLA-A*11:01",
        tra_cdr3="CAVNNNDMRF",
        trb_cdr3="CASSIRSSYEQYF",
        trbv="TRAV8-4",
        trbj="TRBJ2-7",
        organism="human",
        disease="cancer",
        assay="tetramer staining; T-cell activation",
        pubmed_id="demo",
        url="https://vdjdb.cdr3.net/",
        evidence_level="functional assay; tetramer evidence",
        gene="KRAS",
        mutation="G12D",
        metadata={"identifier": "VDJDB-KRAS-G12D-001", "provenance": "VDJdb seed fixture"},
    ),
    TCREvidence(
        source="VDJdb",
        epitope="VVVGAVGVGK",
        hla="HLA-A*11:01",
        tra_cdr3="CAVRDSNYQLIW",
        trb_cdr3="CASSLGQDTQYF",
        trbv="TRBV7-9",
        trbj="TRBJ2-3",
        organism="human",
        disease="cancer",
        assay="T-cell activation",
        pubmed_id=None,
        url="https://vdjdb.cdr3.net/",
        evidence_level="functional assay",
        gene="KRAS",
        mutation="G12V",
        metadata={"identifier": "VDJDB-KRAS-G12V-001", "provenance": "VDJdb seed fixture"},
    ),
]


def search_vdjdb(peptide: str, hla: str) -> list[TCREvidence]:
    """Search VDJdb-style records by exact/near peptide and normalized HLA."""

    normalized_hla = normalize_hla(hla)
    hits: list[TCREvidence] = []
    for evidence in VDJDB_SEED:
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if _within_two_mismatches(peptide, evidence.epitope):
            hits.append(evidence)
    return hits


def _within_two_mismatches(left: str, right: str) -> bool:
    if len(left) != len(right):
        return left in right or right in left
    return sum(a != b for a, b in zip(left, right)) <= 2
