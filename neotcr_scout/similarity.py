"""Sequence similarity utilities for v0.1 evidence mining."""

from __future__ import annotations

from dataclasses import dataclass

from neotcr_scout.input import normalize_hla

BLOSUM62: dict[tuple[str, str], int] = {}
_BLOSUM_ROWS = {
    "A": "4 -1 -2 -2 0 -1 -1 0 -2 -1 -1 -1 -1 -2 -1 1 0 -3 -2 0",
    "R": "-1 5 0 -2 -3 1 0 -2 0 -3 -2 2 -1 -3 -2 -1 -1 -3 -2 -3",
    "N": "-2 0 6 1 -3 0 0 0 1 -3 -3 0 -2 -3 -2 1 0 -4 -2 -3",
    "D": "-2 -2 1 6 -3 0 2 -1 -1 -3 -4 -1 -3 -3 -1 0 -1 -4 -3 -3",
    "C": "0 -3 -3 -3 9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1",
    "Q": "-1 1 0 0 -3 5 2 -2 0 -3 -2 1 0 -3 -1 0 -1 -2 -1 -2",
    "E": "-1 0 0 2 -4 2 5 -2 0 -3 -3 1 -2 -3 -1 0 -1 -3 -2 -2",
    "G": "0 -2 0 -1 -3 -2 -2 6 -2 -4 -4 -2 -3 -3 -2 0 -2 -2 -3 -3",
    "H": "-2 0 1 -1 -3 0 0 -2 8 -3 -3 -1 -2 -1 -2 -1 -2 -2 2 -3",
    "I": "-1 -3 -3 -3 -1 -3 -3 -4 -3 4 2 -3 1 0 -3 -2 -1 -3 -1 3",
    "L": "-1 -2 -3 -4 -1 -2 -3 -4 -3 2 4 -2 2 0 -3 -2 -1 -2 -1 1",
    "K": "-1 2 0 -1 -3 1 1 -2 -1 -3 -2 5 -1 -3 -1 0 -1 -3 -2 -2",
    "M": "-1 -1 -2 -3 -1 0 -2 -3 -2 1 2 -1 5 0 -2 -1 -1 -1 -1 1",
    "F": "-2 -3 -3 -3 -2 -3 -3 -3 -1 0 0 -3 0 6 -4 -2 -2 1 3 -1",
    "P": "-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4 7 -1 -1 -4 -3 -2",
    "S": "1 -1 1 0 -1 0 0 0 -1 -2 -2 0 -1 -2 -1 4 1 -3 -2 -2",
    "T": "0 -1 0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1 1 5 -2 -2 0",
    "W": "-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1 1 -4 -3 -2 11 2 -3",
    "Y": "-2 -2 -2 -3 -2 -1 -2 -3 2 -1 -1 -2 -1 3 -3 -2 -2 2 7 -1",
    "V": "0 -3 -3 -3 -1 -2 -2 -3 -3 3 1 -2 1 -1 -2 -2 0 -3 -1 4",
}
_AAS = list(_BLOSUM_ROWS)
for aa, row in _BLOSUM_ROWS.items():
    for bb, score in zip(_AAS, row.split()):
        BLOSUM62[(aa, bb)] = int(score)


@dataclass(frozen=True)
class SimilarityHit:
    query_peptide: str
    matched_epitope: str
    distance: int
    similarity_score: float
    blosum62_score: int
    mutation_site_match: str
    same_hla: str
    source: str


def levenshtein_distance(left: str, right: str) -> int:
    """Compute Levenshtein edit distance."""

    left = _normalize_peptide(left)
    right = _normalize_peptide(right)
    if left == right:
        return 0
    if not left:
        return len(right)
    if not right:
        return len(left)
    previous = list(range(len(right) + 1))
    for i, left_char in enumerate(left, start=1):
        current = [i]
        for j, right_char in enumerate(right, start=1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (left_char != right_char)))
        previous = current
    return previous[-1]


def normalized_similarity(left: str, right: str) -> float:
    """Return 0-1 edit similarity, where 1 is an exact match."""

    left = _normalize_peptide(left)
    right = _normalize_peptide(right)
    max_length = max(len(left), len(right))
    if max_length == 0:
        return 1.0
    return round(1 - levenshtein_distance(left, right) / max_length, 3)


def blosum62_score(left: str, right: str) -> int:
    """Compute a simple ungapped BLOSUM62 score over aligned positions."""

    left = _normalize_peptide(left)
    right = _normalize_peptide(right)
    score = 0
    for aa, bb in zip(left, right):
        score += BLOSUM62.get((aa, bb), -4)
    score -= 4 * abs(len(left) - len(right))
    return score


def exact_peptide_match(query: str, epitope: str) -> bool:
    """Return True when query and matched epitope are identical."""

    return _normalize_peptide(query) == _normalize_peptide(epitope)


def one_mismatch_peptide_match(query: str, epitope: str) -> bool:
    """Return True when equal-length peptides differ at exactly one position."""

    return _mismatch_count(query, epitope) == 1


def two_mismatch_peptide_match(query: str, epitope: str) -> bool:
    """Return True when equal-length peptides differ at exactly two positions."""

    return _mismatch_count(query, epitope) == 2


def build_similarity_hit(
    query_peptide: str,
    matched_epitope: str,
    query_hla: str | None,
    matched_hla: str | None,
    source: str,
    mutation_index: int | None = None,
) -> SimilarityHit:
    query = _normalize_peptide(query_peptide)
    epitope = _normalize_peptide(matched_epitope)
    distance = levenshtein_distance(query, epitope)
    mutation_site_match = "unknown"
    if mutation_index is not None and 0 <= mutation_index < min(len(query), len(epitope)):
        mutation_site_match = "yes" if query[mutation_index] == epitope[mutation_index] else "no"
    same_hla = "yes" if _same_hla(query_hla, matched_hla) else "no"
    return SimilarityHit(
        query_peptide=query,
        matched_epitope=epitope,
        distance=distance,
        similarity_score=normalized_similarity(query, epitope),
        blosum62_score=blosum62_score(query, epitope),
        mutation_site_match=mutation_site_match,
        same_hla=same_hla,
        source=source,
    )


def _mismatch_count(left: str, right: str) -> int:
    left = _normalize_peptide(left)
    right = _normalize_peptide(right)
    if len(left) != len(right):
        return 999
    return sum(a != b for a, b in zip(left, right))


def _normalize_peptide(peptide: str) -> str:
    return peptide.strip().upper().replace(" ", "")


def _same_hla(query_hla: str | None, matched_hla: str | None) -> bool:
    if not query_hla or not matched_hla:
        return False
    return normalize_hla(query_hla) == normalize_hla(matched_hla)
