"""Local VDJdb-style evidence adapter."""

from __future__ import annotations

from neotcr_scout.models import TCREntry

VDJDB_SEED = [
    TCREntry(
        identifier="VDJDB-KRAS-G12D-001",
        tra_cdr3="CAVNNNDMRF",
        trb_cdr3="CASSIRSSYEQYF",
        v_gene="TRAV8-4",
        j_gene="TRBJ2-7",
        epitope="VVGADGVGK",
        hla="HLA-A*11:01",
        source="VDJdb",
        evidence="Local v0.1 seed record; replace with pinned VDJdb export in production.",
        metadata={"provenance": "database/vdjdb.py seed"},
    )
]


def search_vdjdb(peptide: str, hla: str) -> list[TCREntry]:
    return [entry for entry in VDJDB_SEED if _same_hla(entry.hla, hla) and _overlaps(entry.epitope, peptide)]


def _same_hla(left: str | None, right: str) -> bool:
    return bool(left) and left.upper().replace("HLA-", "") == right.upper().replace("HLA-", "")


def _overlaps(left: str, right: str) -> bool:
    return left in right or right in left or left[:6] in right or right[:6] in left
