"""TCR3D structural evidence adapter."""

from __future__ import annotations

from neotcr_scout.models import TCREntry

TCR3D_SEED = [
    TCREntry(
        identifier="TCR3D-KRAS-LIKE-001",
        tra_cdr3="CALSDRGSTLGRLYF",
        trb_cdr3="CASSPPSGGYNEQFF",
        v_gene="TRAV19",
        j_gene="TRBJ2-1",
        epitope="VVVGACGVGK",
        hla="HLA-A*11:01",
        source="TCR3D",
        evidence="Local structure-oriented seed record for a KRAS hotspot-like epitope.",
        metadata={"structure_evidence": "TCR-pMHC structural neighbor placeholder"},
    )
]


def search_tcr3d(peptide: str, hla: str) -> list[TCREntry]:
    allele = hla.upper().replace("HLA-", "")
    return [
        entry
        for entry in TCR3D_SEED
        if entry.hla and entry.hla.upper().replace("HLA-", "") == allele and entry.epitope[:4] == peptide[:4]
    ]
