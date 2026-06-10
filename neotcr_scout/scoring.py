"""Transparent rule-based candidate TCR evidence scoring."""

from __future__ import annotations

from dataclasses import dataclass

from neotcr_scout.input import normalize_hla
from neotcr_scout.models import TCREntry
from neotcr_scout.similarity import exact_peptide_match, normalized_similarity

ANTIGEN_GROUPS = {
    "RAS": {"KRAS", "NRAS", "HRAS"},
    "TP53": {"TP53"},
}

SCORE_RULES = {
    "same_peptide": 50,
    "same_hla": 20,
    "same_mutation_gene": 15,
    "same_protein_family": 5,
    "functional_assay": 30,
    "tetramer_evidence": 20,
    "clinical_evidence": 50,
    "structure_available": 20,
    "literature_pmid": 10,
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
    evidence_text = " ".join(
        str(value or "")
        for value in [entry.evidence, entry.metadata.get("assay"), entry.metadata.get("evidence_level")]
    ).lower()

    raw_score = 0
    reasons: list[str] = []

    def add_rule(rule: str, explanation: str) -> None:
        nonlocal raw_score
        points = SCORE_RULES[rule]
        raw_score += points
        reasons.append(f"{explanation} +{points}")

    if exact_peptide_match(query_peptide, entry.epitope):
        add_rule("same_peptide", "same peptide")
    if query_hla and entry.hla and _same_hla(str(query_hla), entry.hla):
        add_rule("same_hla", "same HLA")
    if (
        query_gene
        and query_mutation
        and query_gene.upper() == entry_gene.upper()
        and query_mutation.upper() == entry_mutation.upper()
    ):
        add_rule("same_mutation_gene", "same mutation/gene")
    if query_gene and entry_gene and _same_antigen_group(query_gene, entry_gene):
        add_rule("same_protein_family", "same protein family")
    if "functional" in evidence_text or "activation" in evidence_text:
        add_rule("functional_assay", "functional assay")
    if "tetramer" in evidence_text:
        add_rule("tetramer_evidence", "tetramer evidence")
    if "clinical" in evidence_text:
        add_rule("clinical_evidence", "clinical evidence")
    if entry.metadata.get("structure_id") or "structure" in evidence_text:
        add_rule("structure_available", "structure available")
    if entry.metadata.get("pubmed_id"):
        add_rule("literature_pmid", "literature PMID")

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
