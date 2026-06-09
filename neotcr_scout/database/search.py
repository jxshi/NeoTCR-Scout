"""Unified v0.1 TCR database search."""

from __future__ import annotations

from dataclasses import replace

from neotcr_scout.database.iedb import search_iedb
from neotcr_scout.database.tcr3d import search_tcr3d
from neotcr_scout.database.vdjdb import search_vdjdb
from neotcr_scout.models import TCREntry


def search_tcr_database(peptide: str, hla: str) -> list[TCREntry]:
    """Search VDJdb, IEDB, and TCR3D adapters for traceable TCR evidence."""

    hits: list[TCREntry] = []
    for adapter in (search_vdjdb, search_iedb, search_tcr3d):
        for entry in adapter(peptide, hla):
            metadata = dict(entry.metadata)
            metadata["query_peptide"] = peptide
            metadata["query_hla"] = hla
            hits.append(replace(entry, metadata=metadata))
    return hits
