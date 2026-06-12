"""Unified v0.1 TCR database search."""

from __future__ import annotations

from dataclasses import replace
from typing import Callable

from neotcr_scout.database.iedb import search_iedb
from neotcr_scout.database.neotcr import search_neotcr
from neotcr_scout.database.tcr3d import search_tcr3d
from neotcr_scout.database.vdjdb import search_vdjdb
from neotcr_scout.models import TCREntry, TCREvidence

EvidenceAdapter = Callable[[str, str], list[TCREvidence]]
EVIDENCE_ADAPTERS: tuple[EvidenceAdapter, ...] = (search_vdjdb, search_iedb, search_tcr3d, search_neotcr)


def search_tcr_evidence(peptide: str, hla: str) -> list[TCREvidence]:
    """Search VDJdb, IEDB, TCR3D, and NeoTCR adapters for normalized evidence rows."""

    hits: list[TCREvidence] = []
    for adapter in EVIDENCE_ADAPTERS:
        for evidence in adapter(peptide, hla):
            hits.append(_with_query_metadata(evidence, peptide, hla))
    return hits


def search_tcr_database(peptide: str, hla: str) -> list[TCREntry]:
    """Search adapters and return backward-compatible ranked/scoring entries."""

    entries: list[TCREntry] = []
    for evidence in search_tcr_evidence(peptide, hla):
        identifier = str((evidence.metadata or {}).get("identifier") or f"{evidence.source}:{evidence.epitope}")
        entry = TCREntry.from_evidence(evidence, identifier=identifier)
        metadata = dict(entry.metadata)
        metadata["query_peptide"] = peptide
        metadata["query_hla"] = hla
        entries.append(replace(entry, metadata=metadata))
    return entries


def _with_query_metadata(evidence: TCREvidence, peptide: str, hla: str) -> TCREvidence:
    metadata = dict(evidence.metadata or {})
    metadata["query_peptide"] = peptide
    metadata["query_hla"] = hla
    payload = evidence.to_dict() if hasattr(evidence, "to_dict") else dict(evidence.__dict__)
    payload["metadata"] = metadata
    return TCREvidence(**payload)
