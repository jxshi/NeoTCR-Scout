"""Input parsing and Pydantic-style validation for NeoTCR-Scout projects."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from neotcr_scout.models import BaseModel, Field

AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")
MUTATION_RE = re.compile(r"^(?P<wt>[A-Z])(?P<pos>[1-9][0-9]*)(?P<mut>[A-Z])$")
HLA_RE = re.compile(r"^(?:HLA-)?(?P<locus>[A-Z])\*?(?P<first>[0-9]{2})(?::?(?P<second>[0-9]{2}))$")
DEFAULT_PEPTIDE_LENGTHS = [8, 9, 10, 11]


class ProjectInput(BaseModel):
    """Validated v0.1 YAML schema."""

    project: str
    gene: str
    mutation: str
    protein_sequence: str | None = None
    hla: list[str]
    peptide_lengths: list[int] = Field(default_factory=lambda: list(DEFAULT_PEPTIDE_LENGTHS))

    @classmethod
    def from_mapping(cls, raw: dict[str, Any]) -> "ProjectInput":
        missing = [key for key in ("project", "gene", "mutation", "hla") if key not in raw]
        if missing:
            raise ValueError(f"Missing required project field(s): {', '.join(missing)}")
        hla_values = raw["hla"] if isinstance(raw["hla"], list) else [raw["hla"]]
        lengths = raw.get("peptide_lengths", DEFAULT_PEPTIDE_LENGTHS)
        if not isinstance(lengths, list):
            raise ValueError("peptide_lengths must be a list of integers, e.g. [8, 9, 10, 11]")
        project = cls(
            project=str(raw["project"]),
            gene=str(raw["gene"]).upper(),
            mutation=validate_mutation(str(raw["mutation"])),
            protein_sequence=str(raw["protein_sequence"]).upper() if raw.get("protein_sequence") else None,
            hla=[normalize_hla(str(value)) for value in hla_values],
            peptide_lengths=validate_peptide_lengths(lengths),
        )
        return project


# Backward-compatible public name used by earlier code/tests.
ScoutProject = ProjectInput


def validate_mutation(mutation: str) -> str:
    """Validate mutation format such as ``G12D`` and return uppercase text."""

    normalized = mutation.strip().upper()
    match = MUTATION_RE.match(normalized)
    if not match:
        raise ValueError("mutation must use protein-substitution format like G12D")
    if match.group("wt") not in AMINO_ACIDS or match.group("mut") not in AMINO_ACIDS:
        raise ValueError("mutation amino acids must be one-letter canonical amino-acid codes")
    if match.group("wt") == match.group("mut"):
        raise ValueError("mutation wild-type and mutant amino acids must differ")
    return normalized


def normalize_hla(hla: str) -> str:
    """Normalize common HLA class I formats to ``HLA-A*11:01`` style."""

    compact = hla.strip().upper().replace(" ", "")
    match = HLA_RE.match(compact)
    if not match:
        raise ValueError(
            f"Invalid HLA allele {hla!r}; expected formats like HLA-A*11:01, A*11:01, or HLA-A1101"
        )
    return f"HLA-{match.group('locus')}*{match.group('first')}:{match.group('second')}"


def validate_peptide_lengths(lengths: list[Any]) -> list[int]:
    """Validate peptide lengths and apply v0.1 defaults when empty."""

    if not lengths:
        return list(DEFAULT_PEPTIDE_LENGTHS)
    normalized: list[int] = []
    for value in lengths:
        try:
            length = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"peptide length {value!r} is not an integer") from exc
        if length < 8 or length > 14:
            raise ValueError("peptide lengths must be between 8 and 14 for MHC-I workflows")
        normalized.append(length)
    return normalized


def load_project(path: str | Path) -> ScoutProject:
    """Load and validate the small YAML subset used by v0.1 example files."""

    raw = _parse_simple_yaml(Path(path).read_text(encoding="utf-8"))
    return ProjectInput.from_mapping(raw)


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
