"""Deterministic HLA binding scoring for v0.1 workflows."""

from __future__ import annotations

from neotcr_scout.models import BindingPrediction, PeptideCandidate


class RuleBasedBindingPredictor:
    """Small deterministic scorer that mimics rank-percent output.

    The class is intentionally simple so v0.1 can be useful without requiring
    NetMHCpan or MHCflurry installations. Production runs can replace this with
    an adapter that imports external predictor output while preserving the same
    ``BindingPrediction`` schema.
    """

    def predict(self, peptides: list[PeptideCandidate], hla: str) -> list[BindingPrediction]:
        return [self._score(peptide, hla) for peptide in peptides]

    def _score(self, peptide: PeptideCandidate, hla: str) -> BindingPrediction:
        sequence = peptide.sequence
        hla_normalized = hla.upper().replace("HLA-", "")
        score = 5.0
        if hla_normalized in {"A*11:01", "A11:01"}:
            if len(sequence) in {9, 10}:
                score -= 1.4
            if sequence[-1] in {"K", "R"}:
                score -= 1.8
            if sequence[1] in {"V", "I", "L", "T"}:
                score -= 0.8
            if "D" in sequence:
                score -= 0.3
        else:
            if len(sequence) in {9, 10}:
                score -= 0.5
            if sequence[-1] in {"F", "Y", "L", "I", "V", "K", "R"}:
                score -= 0.5
        rank_percent = max(0.1, round(score, 2))
        return BindingPrediction(
            peptide=sequence,
            hla=hla,
            rank_percent=rank_percent,
            method="rule-based-v0.1",
        )
