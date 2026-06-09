"""Simple human-proteome off-target screening."""

from __future__ import annotations

from neotcr_scout.models import RiskHit
from neotcr_scout.similarity import levenshtein_distance

SEED_HUMAN_PEPTIDES = {
    "TTN": "VVVGADGVGR",
    "MYH6": "VLVGADGVGK",
}


class SimpleRiskEngine:
    """Find 1-2 mismatch peptide neighbors in a small configurable proteome index."""

    def __init__(self, proteome_index: dict[str, str] | None = None) -> None:
        self.proteome_index = proteome_index if proteome_index is not None else SEED_HUMAN_PEPTIDES

    def scan(self, peptide: str, max_mismatches: int = 2) -> list[RiskHit]:
        hits: list[RiskHit] = []
        for protein, human_peptide in self.proteome_index.items():
            if len(human_peptide) != len(peptide):
                continue
            mismatches = levenshtein_distance(peptide, human_peptide)
            if mismatches <= max_mismatches:
                hits.append(
                    RiskHit(
                        peptide=human_peptide,
                        protein=protein,
                        mismatches=mismatches,
                        risk_level="high" if mismatches <= 1 else "medium",
                    )
                )
        return sorted(hits, key=lambda hit: (hit.mismatches, hit.protein))
