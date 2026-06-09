"""Structural triage placeholders for future TCR3D and docking integrations."""

from __future__ import annotations


def _clash_penalty(peptide: str) -> float:
    charged = sum(peptide.count(aa) for aa in ("D", "E", "K", "R"))
    return round(charged / max(len(peptide), 1), 3)


class StructuralTriageEngine:
    """Return deterministic, transparent docking-like triage metrics."""

    def score(self, peptide: str) -> dict[str, float]:
        penalty = _clash_penalty(peptide)
        return {
            "binding_score": round(1.0 - penalty, 3),
            "interface_area": round(550 + 12 * len(peptide), 1),
            "clashes": penalty,
        }
