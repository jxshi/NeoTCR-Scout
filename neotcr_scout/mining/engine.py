"""Normalized TCR evidence loading and search."""

from __future__ import annotations

import json
from pathlib import Path

from neotcr_scout.models import TCREntry, TCRHit
from neotcr_scout.similarity import normalized_similarity

DEFAULT_DATABASE = Path(__file__).resolve().parents[2] / "database" / "seed_tcrs.json"


def load_tcr_entries(path: Path = DEFAULT_DATABASE) -> list[TCREntry]:
    """Load normalized TCR entries from a JSON snapshot."""

    records = json.loads(path.read_text(encoding="utf-8"))
    return [TCREntry(**record) for record in records]


class TCRMiningEngine:
    """Search TCR evidence by peptide similarity and optional HLA matching."""

    def __init__(self, entries: list[TCREntry] | None = None) -> None:
        self.entries = entries if entries is not None else load_tcr_entries()

    def search(self, peptides: list[str], hla: str, min_similarity: float = 0.55, limit: int = 10) -> list[TCRHit]:
        hits: list[TCRHit] = []
        normalized_hla = _normalize_hla(hla)
        for entry in self.entries:
            best_peptide = max(peptides, key=lambda peptide: normalized_similarity(peptide, entry.epitope))
            similarity = normalized_similarity(best_peptide, entry.epitope)
            hla_match = _normalize_hla(entry.hla) == normalized_hla if entry.hla else False
            if similarity >= min_similarity or hla_match:
                hits.append(
                    TCRHit(
                        entry=entry,
                        peptide_similarity=similarity,
                        hla_match=hla_match,
                        matched_peptide=best_peptide,
                    )
                )
        return sorted(hits, key=lambda hit: (hit.hla_match, hit.peptide_similarity), reverse=True)[:limit]


def _normalize_hla(hla: str | None) -> str | None:
    if hla is None:
        return None
    return hla.upper().replace("HLA-", "")
