"""IEDB receptor evidence adapter.

The v0.1 adapter is local and deterministic. It keeps the function boundary that
will later be connected to the IEDB Query API.
"""

from __future__ import annotations

from neotcr_scout.models import TCREntry

IEDB_SEED = [
    TCREntry(
        identifier="IEDB-KRAS-G12D-001",
        tra_cdr3=None,
        trb_cdr3="CASSQDRGYEQYF",
        v_gene="TRBV7-9",
        j_gene="TRBJ2-7",
        epitope="GADGVGKSAL",
        hla="HLA-A*11:01",
        source="IEDB",
        evidence="Local v0.1 seed record; future implementation should call the IEDB Query API.",
        metadata={"provenance": "database/iedb.py seed"},
    )
]


def search_iedb(peptide: str, hla: str) -> list[TCREntry]:
    normalized = hla.upper().replace("HLA-", "")
    return [
        entry
        for entry in IEDB_SEED
        if entry.hla and entry.hla.upper().replace("HLA-", "") == normalized and _shared_core(entry.epitope, peptide)
    ]


def _shared_core(left: str, right: str, core: int = 5) -> bool:
    return any(left[index : index + core] in right for index in range(0, max(1, len(left) - core + 1)))
