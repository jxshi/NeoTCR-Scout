"""TCR3D structural evidence adapter."""

from __future__ import annotations

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence

TCR3D_SEED = [
    TCREvidence(
        source="TCR3D",
        epitope="VVVGACGVGK",
        hla="HLA-A*11:01",
        tra_cdr3="CALSDRGSTLGRLYF",
        trb_cdr3="CASSPPSGGYNEQFF",
        trbv="TRAV19",
        trbj="TRBJ2-1",
        organism="human",
        disease="cancer",
        assay="structure available",
        pubmed_id=None,
        url="https://tcr3d.ibbr.umd.edu/",
        evidence_level="structure available",
        gene="KRAS",
        mutation="G12C",
        structure_id="TCR3D-demo-KRAS-like",
        metadata={"identifier": "TCR3D-KRAS-LIKE-001", "provenance": "TCR3D seed fixture"},
    )
]


def search_tcr3d(peptide: str, hla: str) -> list[TCREvidence]:
    """Search TCR3D-style structural records by peptide prefix and normalized HLA."""

    normalized_hla = normalize_hla(hla)
    hits: list[TCREvidence] = []
    for evidence in TCR3D_SEED:
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if evidence.epitope[:4] == peptide[:4]:
            hits.append(evidence)
    return hits
