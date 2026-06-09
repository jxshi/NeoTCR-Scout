"""MHC binding prediction adapters for v0.1."""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from neotcr_scout.peptide import MutantPeptide


@dataclass(frozen=True)
class MHCBindingPrediction:
    peptide: str
    hla: str
    rank_percent: float
    affinity_nm: float | None
    binder: str
    method: str
    evidence: str


def predict_mhc_binding(peptides: list[MutantPeptide] | list[str], hla: str) -> list[MHCBindingPrediction]:
    """Predict peptide-HLA binding with optional tools and deterministic fallback.

    v0.1 first looks for command-line NetMHCpan or MHCflurry installations. If
    neither tool is available, it records a transparent rule-based fallback so
    the workflow remains reproducible in lightweight environments.
    """

    sequences = [peptide.sequence if hasattr(peptide, "sequence") else str(peptide) for peptide in peptides]
    if shutil.which("netMHCpan"):
        return _predict_with_netmhcpan(sequences, hla)
    if shutil.which("mhcflurry-predict"):
        return _predict_with_mhcflurry(sequences, hla)
    return [_rule_based_prediction(sequence, hla) for sequence in sequences]


def _predict_with_netmhcpan(peptides: list[str], hla: str) -> list[MHCBindingPrediction]:
    tmp = Path(".neotcr_scout_netmhcpan_input.pep")
    tmp.write_text("\n".join(peptides) + "\n", encoding="utf-8")
    try:
        completed = subprocess.run(
            ["netMHCpan", "-p", str(tmp), "-a", hla.replace("HLA-", "")],
            check=True,
            capture_output=True,
            text=True,
        )
    finally:
        tmp.unlink(missing_ok=True)
    # NetMHCpan output varies by version; keep raw output as provenance and use
    # fallback scores until a version-pinned parser is added.
    raw = completed.stdout[:500]
    return [
        _rule_based_prediction(peptide, hla, method="netMHCpan-detected-parser-pending", evidence=raw)
        for peptide in peptides
    ]


def _predict_with_mhcflurry(peptides: list[str], hla: str) -> list[MHCBindingPrediction]:
    completed = subprocess.run(
        ["mhcflurry-predict", "--alleles", hla, "--peptides", *peptides],
        check=True,
        capture_output=True,
        text=True,
    )
    raw = completed.stdout[:500]
    return [
        _rule_based_prediction(peptide, hla, method="MHCflurry-detected-parser-pending", evidence=raw)
        for peptide in peptides
    ]


def _rule_based_prediction(
    peptide: str,
    hla: str,
    method: str = "rule-based-fallback-v0.1",
    evidence: str = "No NetMHCpan/MHCflurry executable detected; deterministic fallback used.",
) -> MHCBindingPrediction:
    allele = hla.upper().replace("HLA-", "")
    rank = 5.0
    if allele in {"A*11:01", "A11:01"}:
        if len(peptide) in {9, 10}:
            rank -= 1.3
        if peptide[-1] in {"K", "R"}:
            rank -= 1.9
        if peptide[1] in {"V", "I", "L", "T"}:
            rank -= 0.7
        if "D" in peptide:
            rank -= 0.3
    else:
        if 8 <= len(peptide) <= 11:
            rank -= 0.5
        if peptide[-1] in {"F", "Y", "L", "I", "V", "K", "R"}:
            rank -= 0.4
    rank = max(0.1, round(rank, 2))
    binder = "strong" if rank <= 0.5 else "weak" if rank <= 2.0 else "non-binder"
    return MHCBindingPrediction(
        peptide=peptide,
        hla=hla,
        rank_percent=rank,
        affinity_nm=None,
        binder=binder,
        method=method,
        evidence=evidence,
    )
