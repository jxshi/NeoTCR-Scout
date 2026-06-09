"""IEDB receptor evidence adapter."""

from __future__ import annotations

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence, TCREntry

IEDB_SEED = [
    TCREvidence(
        source="IEDB",
        epitope="GADGVGKSAL",
        hla="HLA-A*11:01",
        tra_cdr3=None,
        trb_cdr3="CASSQDRGYEQYF",
        trbv="TRBV7-9",
        trbj="TRBJ2-7",
        organism="human",
        disease="cancer",
        assay="T-cell response assay",
        pubmed_id="demo",
        url="https://www.iedb.org/",
        evidence_level="functional assay",
        gene="KRAS",
        mutation="G12D",
        metadata={"identifier": "IEDB-KRAS-G12D-001", "provenance": "IEDB seed fixture"},
    )
]


def search_iedb(peptide: str, hla: str) -> list[TCREntry]:
    normalized_hla = normalize_hla(hla)
    hits: list[TCREntry] = []
    for evidence in IEDB_SEED:
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if _shared_core(evidence.epitope, peptide):
            hits.append(TCREntry.from_evidence(evidence, identifier=str(evidence.metadata.get("identifier"))))
    return hits


def _shared_core(left: str, right: str, core: int = 5) -> bool:
    return any(left[index : index + core] in right for index in range(0, max(1, len(left) - core + 1)))
