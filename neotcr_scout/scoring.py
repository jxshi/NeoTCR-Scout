"""Candidate TCR scoring and ranking."""

from __future__ import annotations

from dataclasses import dataclass

from neotcr_scout.models import TCREntry
from neotcr_scout.similarity import normalized_similarity


@dataclass(frozen=True)
class TCRCandidate:
    identifier: str
    source: str
    peptide: str
    epitope: str
    hla: str | None
    tra_cdr3: str | None
    trb_cdr3: str | None
    similarity: float
    evidence: str | None
    score: float


def rank_tcr_candidates(results: list[TCREntry]) -> list[TCRCandidate]:
    """Rank deduplicated TCR evidence records by traceable evidence strength."""

    candidates: dict[str, TCRCandidate] = {}
    for entry in results:
        query_peptide = str(entry.metadata.get("query_peptide", entry.epitope))
        similarity = normalized_similarity(query_peptide, entry.epitope)
        source_bonus = {"VDJdb": 0.15, "IEDB": 0.12, "TCR3D": 0.1}.get(entry.source, 0.05)
        hla_bonus = 0.1 if entry.hla else 0.0
        score = round(min(1.0, similarity * 0.75 + source_bonus + hla_bonus), 3)
        candidate = TCRCandidate(
            identifier=entry.identifier,
            source=entry.source,
            peptide=query_peptide,
            epitope=entry.epitope,
            hla=entry.hla,
            tra_cdr3=entry.tra_cdr3,
            trb_cdr3=entry.trb_cdr3,
            similarity=similarity,
            evidence=entry.evidence,
            score=score,
        )
        current = candidates.get(candidate.identifier)
        if current is None or candidate.score > current.score:
            candidates[candidate.identifier] = candidate
    return sorted(candidates.values(), key=lambda item: item.score, reverse=True)
