"""Configurable local TSV/CSV adapter for user-provided TCR evidence."""

from __future__ import annotations

import csv
from pathlib import Path

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREvidence, TCREntry


def load_local_evidence(path: str | Path) -> list[TCREvidence]:
    """Load local TCR evidence from a TSV or CSV file."""

    evidence_path = Path(path)
    delimiter = "\t" if evidence_path.suffix.lower() in {".tsv", ".txt"} else ","
    with evidence_path.open(encoding="utf-8", newline="") as handle:
        return [TCREvidence(**_normalize_record(row)) for row in csv.DictReader(handle, delimiter=delimiter)]


def search_local(path: str | Path, peptide: str, hla: str) -> list[TCREntry]:
    """Search a local evidence file by peptide substring/near match and HLA."""

    normalized_hla = normalize_hla(hla)
    hits: list[TCREntry] = []
    for index, evidence in enumerate(load_local_evidence(path), start=1):
        if evidence.hla and normalize_hla(evidence.hla) != normalized_hla:
            continue
        if evidence.epitope in peptide or peptide in evidence.epitope or _hamming(evidence.epitope, peptide) <= 2:
            hits.append(TCREntry.from_evidence(evidence, identifier=str(evidence.metadata.get("identifier") or f"local-{index}")))
    return hits


def _normalize_record(row: dict[str, str]) -> dict[str, object]:
    record = {key: (value if value != "" else None) for key, value in row.items()}
    record.setdefault("source", "local")
    record.setdefault("metadata", {})
    return record


def _hamming(left: str, right: str) -> int:
    if len(left) != len(right):
        return 999
    return sum(a != b for a, b in zip(left, right))
