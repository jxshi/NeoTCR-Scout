"""Transparent rule-based candidate TCR evidence scoring."""

from __future__ import annotations

from dataclasses import dataclass

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREntry
from neotcr_scout.similarity import normalized_similarity

ANTIGEN_GROUPS = {
    "RAS": {"KRAS", "NRAS", "HRAS"},
    "TP53": {"TP53"},
}


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
    raw_score: int
    score_category: str
    explanation: str


def score_tcr_entry(entry: TCREntry) -> TCRCandidate:
    """Score one TCR evidence record with explicit rule explanations."""

    query_peptide = str(entry.metadata.get("query_peptide", entry.epitope))
    query_hla = entry.metadata.get("query_hla")
    query_gene = str(entry.metadata.get("query_gene", ""))
    query_mutation = str(entry.metadata.get("query_mutation", ""))
    entry_gene = str(entry.metadata.get("gene", ""))
    entry_mutation = str(entry.metadata.get("mutation", ""))
    evidence_text = " ".join(str(value or "") for value in [entry.evidence, entry.metadata.get("assay"), entry.metadata.get("evidence_level")]).lower()

    raw_score = 0
    reasons: list[str] = []
    if query_peptide == entry.epitope:
        raw_score += 50
        reasons.append("same peptide +50")
    if query_hla and entry.hla and _same_hla(str(query_hla), entry.hla):
        raw_score += 20
        reasons.append("same HLA +20")
    if query_gene and query_mutation and query_gene == entry_gene and query_mutation == entry_mutation:
        raw_score += 15
        reasons.append("same mutation/gene +15")
    elif query_gene and entry_gene and _same_antigen_group(query_gene, entry_gene):
        raw_score += 5
        reasons.append("same antigen family +5")
    if "functional" in evidence_text or "activation" in evidence_text:
        raw_score += 30
        reasons.append("functional assay evidence +30")
    if "tetramer" in evidence_text:
        raw_score += 20
        reasons.append("tetramer evidence +20")
    if "clinical" in evidence_text:
        raw_score += 50
        reasons.append("clinical evidence +50")
    if entry.metadata.get("structure_id") or "structure" in evidence_text:
        raw_score += 20
        reasons.append("structure available +20")
    if entry.metadata.get("pubmed_id"):
        raw_score += 10
        reasons.append("literature PMID available +10")

    return TCRCandidate(
        identifier=entry.identifier,
        source=entry.source,
        peptide=query_peptide,
        epitope=entry.epitope,
        hla=entry.hla,
        tra_cdr3=entry.tra_cdr3,
        trb_cdr3=entry.trb_cdr3,
        similarity=normalized_similarity(query_peptide, entry.epitope),
        evidence=entry.evidence,
        score=float(raw_score),
        raw_score=raw_score,
        score_category=_score_category(raw_score),
        explanation="; ".join(reasons) if reasons else "no rule-based evidence bonuses assigned",
    )


def rank_tcr_candidates(results: list[TCREntry]) -> list[TCRCandidate]:
    """Rank deduplicated TCR evidence records by transparent rule-based score."""

    candidates: dict[str, TCRCandidate] = {}
    for entry in results:
        candidate = score_tcr_entry(entry)
        current = candidates.get(candidate.identifier)
        if current is None or candidate.raw_score > current.raw_score:
            candidates[candidate.identifier] = candidate
    return sorted(candidates.values(), key=lambda item: (item.raw_score, item.similarity), reverse=True)


def _score_category(raw_score: int) -> str:
    if raw_score >= 100:
        return "High"
    if raw_score >= 50:
        return "Medium"
    return "Low"


def _same_hla(left: str, right: str) -> bool:
    try:
        return normalize_hla(left) == normalize_hla(right)
    except ValueError:
        return left.upper().replace("HLA-", "") == right.upper().replace("HLA-", "")


def _same_antigen_group(left_gene: str, right_gene: str) -> bool:
    left = left_gene.upper()
    right = right_gene.upper()
    return any(left in genes and right in genes for genes in ANTIGEN_GROUPS.values())
