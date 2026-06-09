"""Sequence similarity utilities for v0.1 evidence mining."""

from __future__ import annotations


def levenshtein_distance(left: str, right: str) -> int:
    """Compute Levenshtein edit distance."""

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
            current.append(
                min(
                    previous[j] + 1,
                    current[j - 1] + 1,
                    previous[j - 1] + (left_char != right_char),
                )
            )
        previous = current
    return previous[-1]


def normalized_similarity(left: str, right: str) -> float:
    """Return 0-1 edit similarity, where 1 is an exact match."""

    max_length = max(len(left), len(right))
    if max_length == 0:
        return 1.0
    return round(1 - levenshtein_distance(left, right) / max_length, 3)
