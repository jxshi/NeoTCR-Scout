"""Input parsing for NeoTCR-Scout v0.1 projects."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ScoutProject:
    """Minimal reproducible v0.1 input contract."""

    project: str
    gene: str
    mutation: str
    protein_sequence: str
    hla: list[str]
    peptide_lengths: list[int] = field(default_factory=lambda: [8, 9, 10, 11])


def load_project(path: str | Path) -> ScoutProject:
    """Load the small YAML subset used by v0.1 example files.

    The parser intentionally supports only simple scalars and list blocks so the
    command-line demo has no mandatory PyYAML dependency. If the input format
    grows, this function is the single place to swap in a stricter YAML parser.
    """

    raw = _parse_simple_yaml(Path(path).read_text(encoding="utf-8"))
    required = ["project", "gene", "mutation", "protein_sequence", "hla"]
    missing = [key for key in required if key not in raw]
    if missing:
        raise ValueError(f"Missing required project field(s): {', '.join(missing)}")
    hla = raw["hla"] if isinstance(raw["hla"], list) else [str(raw["hla"])]
    lengths = raw.get("peptide_lengths", [8, 9, 10, 11])
    if not isinstance(lengths, list):
        raise ValueError("peptide_lengths must be a list of integers")
    return ScoutProject(
        project=str(raw["project"]),
        gene=str(raw["gene"]).upper(),
        mutation=str(raw["mutation"]).upper(),
        protein_sequence=str(raw["protein_sequence"]).upper(),
        hla=[str(allele) for allele in hla],
        peptide_lengths=[int(length) for length in lengths],
    )


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("-"):
            if current_key is None:
                raise ValueError(f"List item without a key: {raw_line!r}")
            result.setdefault(current_key, []).append(_coerce_scalar(stripped[1:].strip()))
            continue
        if ":" not in stripped:
            raise ValueError(f"Unsupported input line: {raw_line!r}")
        key, value = stripped.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        result[current_key] = [] if value == "" else _coerce_scalar(value)
    return result


def _coerce_scalar(value: str) -> str | int | float | bool:
    unquoted = value.strip().strip('"').strip("'")
    if unquoted.lower() in {"true", "false"}:
        return unquoted.lower() == "true"
    try:
        return int(unquoted)
    except ValueError:
        pass
    try:
        return float(unquoted)
    except ValueError:
        return unquoted
