"""MHC binding prediction adapters for v0.1.

NeoTCR-Scout integrates external predictors only when the user has installed or
provided them. NetMHCpan and MHCflurry are third-party tools; users are
responsible for obtaining and complying with their original licenses.
"""

from __future__ import annotations

import csv
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from neotcr_scout.peptide import MutantPeptide

TOOLS_DIR_ENV = "NEOTCR_SCOUT_TOOLS_DIR"
NETMHCPAN_ENV = "NEOTCR_SCOUT_NETMHCPAN"
MHCFLURRY_ENV = "NEOTCR_SCOUT_MHCFLURRY_PREDICT"
ACADEMIC_LICENSE_NOTICE = (
    "Academic-use workflow notice: NetMHCpan and MHCflurry are external tools. "
    "Before using either predictor, contact the original authors and comply with "
    "their licenses and citation requirements."
)


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
    """Predict peptide-HLA binding with configured tools and fallback.

    Resolution order is:

    1. ``NEOTCR_SCOUT_NETMHCPAN`` exact executable path.
    2. ``tools/netMHCpan`` or ``tools/netMHCpan/netMHCpan`` under the repo root.
    3. ``netMHCpan`` on ``PATH``.
    4. ``NEOTCR_SCOUT_MHCFLURRY_PREDICT`` exact executable path.
    5. ``tools/mhcflurry/.../mhcflurry-predict`` under the repo root.
    6. ``mhcflurry-predict`` on ``PATH``.
    7. deterministic rule-based fallback with explicit provenance.
    """

    sequences = [peptide.sequence if hasattr(peptide, "sequence") else str(peptide) for peptide in peptides]
    netmhcpan = _find_netmhcpan()
    if netmhcpan:
        return _predict_with_netmhcpan(sequences, hla, netmhcpan)
    mhcflurry = _find_mhcflurry_predict()
    if mhcflurry:
        return _predict_with_mhcflurry(sequences, hla, mhcflurry)
    return [_rule_based_prediction(sequence, hla) for sequence in sequences]


def _find_netmhcpan() -> Path | None:
    return _first_existing_executable(
        env_var=NETMHCPAN_ENV,
        local_candidates=(
            Path("tools/netMHCpan"),
            Path("tools/netMHCpan/netMHCpan"),
            Path("tools/netMHCpan/netmhcpan"),
            Path("tools/netMHCpan/netMHCpan-4.1/netMHCpan"),
            Path("tools/netMHCpan/netMHCpan-4.2/netMHCpan"),
        ),
        path_names=("netMHCpan", "netmhcpan"),
    )


def _find_mhcflurry_predict() -> Path | None:
    return _first_existing_executable(
        env_var=MHCFLURRY_ENV,
        local_candidates=(
            Path("tools/mhcflurry/mhcflurry-predict"),
            Path("tools/mhcflurry/bin/mhcflurry-predict"),
            Path("tools/mhcflurry/.venv/bin/mhcflurry-predict"),
            Path("tools/mhcflurry/venv/bin/mhcflurry-predict"),
        ),
        path_names=("mhcflurry-predict",),
    )


def _first_existing_executable(
    env_var: str,
    local_candidates: tuple[Path, ...],
    path_names: tuple[str, ...],
) -> Path | None:
    configured = os.environ.get(env_var)
    if configured:
        configured_path = Path(configured)
        return configured_path if _is_executable_file(configured_path) else None
    tools_dir = Path(os.environ.get(TOOLS_DIR_ENV, "tools"))
    candidates = list(local_candidates)
    if tools_dir != Path("tools"):
        candidates.extend(tools_dir / candidate.relative_to("tools") for candidate in local_candidates)
    for candidate in candidates:
        if _is_executable_file(candidate):
            return candidate
    for name in path_names:
        resolved = shutil.which(name)
        if resolved:
            return Path(resolved)
    return None


def _is_executable_file(path: Path) -> bool:
    return path.is_file() and os.access(path, os.X_OK)


def _predict_with_netmhcpan(peptides: list[str], hla: str, executable: Path) -> list[MHCBindingPrediction]:
    with tempfile.TemporaryDirectory(prefix="neotcr_scout_netmhcpan_") as tmpdir:
        peptide_file = Path(tmpdir) / "peptides.txt"
        peptide_file.write_text("\n".join(peptides) + "\n", encoding="utf-8")
        completed = subprocess.run(
            [str(executable), "-p", str(peptide_file), "-a", _netmhcpan_allele(hla)],
            check=True,
            capture_output=True,
            text=True,
        )
    parsed = _parse_netmhcpan_output(completed.stdout, hla)
    if parsed:
        return parsed
    raw = _truncate_evidence(completed.stdout)
    return [
        _rule_based_prediction(peptide, hla, method="netMHCpan-output-unparsed", evidence=f"{ACADEMIC_LICENSE_NOTICE}\n{raw}")
        for peptide in peptides
    ]


def _predict_with_mhcflurry(peptides: list[str], hla: str, executable: Path) -> list[MHCBindingPrediction]:
    completed = subprocess.run(
        [str(executable), "--alleles", hla, "--peptides", *peptides],
        check=True,
        capture_output=True,
        text=True,
    )
    parsed = _parse_mhcflurry_output(completed.stdout, hla)
    if parsed:
        return parsed
    raw = _truncate_evidence(completed.stdout)
    return [
        _rule_based_prediction(peptide, hla, method="MHCflurry-output-unparsed", evidence=f"{ACADEMIC_LICENSE_NOTICE}\n{raw}")
        for peptide in peptides
    ]


def _parse_netmhcpan_output(output: str, requested_hla: str) -> list[MHCBindingPrediction]:
    predictions: list[MHCBindingPrediction] = []
    header: list[str] | None = None
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or set(line) <= {"-"}:
            continue
        tokens = line.split()
        normalized_tokens = [_normalize_column(token) for token in tokens]
        if "peptide" in normalized_tokens and _rank_column(normalized_tokens) is not None:
            header = normalized_tokens
            continue
        if header is None or len(tokens) < len(header):
            continue
        if len(tokens) > len(header):
            tokens = tokens[: len(header) - 1] + [" ".join(tokens[len(header) - 1 :])]
        row = dict(zip(header, tokens))
        peptide = row.get("peptide")
        rank = _float_from_row(row, ("el_rank", "rank_el", "rank", "rank_ba", "ba_rank"))
        if peptide is None or rank is None:
            continue
        affinity = _float_from_row(row, ("aff_nm", "affinity_nm", "aff", "ic50", "nm"))
        binder = row.get("bindlevel") or _binder_from_rank(rank)
        predictions.append(
            MHCBindingPrediction(
                peptide=peptide,
                hla=row.get("mhc") or row.get("allele") or requested_hla,
                rank_percent=rank,
                affinity_nm=affinity,
                binder=binder,
                method="NetMHCpan",
                evidence=ACADEMIC_LICENSE_NOTICE,
            )
        )
    return predictions


def _parse_mhcflurry_output(output: str, requested_hla: str) -> list[MHCBindingPrediction]:
    sample = output.lstrip()
    if not sample:
        return []
    dialect = csv.excel_tab if "\t" in sample.splitlines()[0] else csv.excel
    predictions: list[MHCBindingPrediction] = []
    for row in csv.DictReader(sample.splitlines(), dialect=dialect):
        normalized = {_normalize_column(key): value for key, value in row.items() if key is not None}
        peptide = normalized.get("peptide")
        if peptide is None:
            continue
        rank = _float_from_row(
            normalized,
            (
                "presentation_percentile",
                "affinity_percentile",
                "prediction_percentile",
                "percentile_rank",
                "rank_percent",
                "rank",
            ),
        )
        affinity = _float_from_row(normalized, ("affinity", "affinity_nm", "ic50", "nm"))
        if rank is None:
            rank = _rank_from_affinity(affinity)
        if rank is None:
            continue
        predictions.append(
            MHCBindingPrediction(
                peptide=peptide,
                hla=normalized.get("allele") or requested_hla,
                rank_percent=rank,
                affinity_nm=affinity,
                binder=_binder_from_rank(rank),
                method="MHCflurry",
                evidence=ACADEMIC_LICENSE_NOTICE,
            )
        )
    return predictions


def _rule_based_prediction(
    peptide: str,
    hla: str,
    method: str = "rule-based-fallback-v0.1",
    evidence: str = f"No NetMHCpan/MHCflurry executable detected; deterministic fallback used. {ACADEMIC_LICENSE_NOTICE}",
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
    return MHCBindingPrediction(
        peptide=peptide,
        hla=hla,
        rank_percent=rank,
        affinity_nm=None,
        binder=_binder_from_rank(rank),
        method=method,
        evidence=evidence,
    )


def _netmhcpan_allele(hla: str) -> str:
    return hla.replace("*", "")


def _normalize_column(column: str) -> str:
    return (
        column.strip().lower().replace("%", "").replace("(", "_").replace(")", "").replace("/", "_").replace("-", "_")
    )


def _rank_column(columns: list[str]) -> str | None:
    for candidate in ("el_rank", "rank_el", "rank", "rank_ba", "ba_rank"):
        if candidate in columns:
            return candidate
    return None


def _float_from_row(row: dict[str, str], keys: tuple[str, ...]) -> float | None:
    for key in keys:
        value = row.get(key)
        if value in (None, "", "NA", "nan"):
            continue
        try:
            return float(value)
        except ValueError:
            continue
    return None


def _rank_from_affinity(affinity: float | None) -> float | None:
    if affinity is None:
        return None
    if affinity <= 50:
        return 0.5
    if affinity <= 500:
        return 2.0
    return 5.0


def _binder_from_rank(rank: float) -> str:
    return "strong" if rank <= 0.5 else "weak" if rank <= 2.0 else "non-binder"


def _truncate_evidence(output: str, limit: int = 500) -> str:
    return output[:limit] if len(output) > limit else output
