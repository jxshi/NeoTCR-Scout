"""Input parsing and Pydantic validation for NeoTCR-Scout projects."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from neotcr_scout.models import BaseModel, Field

try:  # pragma: no cover - active when Pydantic is installed
    from pydantic import ConfigDict
except Exception:  # pragma: no cover - fallback keeps minimal installs runnable
    ConfigDict = None  # type: ignore[assignment]

AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")
MUTATION_RE = re.compile(r"^(?P<wt>[A-Z])(?P<pos>[1-9][0-9]*)(?P<mut>[A-Z])$")
HLA_RE = re.compile(r"^(?:HLA-)?(?P<locus>[ABC])\*?(?P<first>[0-9]{2})(?::?(?P<second>[0-9]{2}))$")
DEFAULT_PEPTIDE_LENGTHS = [8, 9, 10, 11]
PROJECT_INPUT_FIELDS = {"project", "gene", "mutation", "protein_sequence", "hla", "peptide_lengths"}
REQUIRED_PROJECT_INPUT_FIELDS = {"project", "gene", "mutation", "hla"}


class ProjectInput(BaseModel):
    """Pydantic-defined input YAML schema for a v0.1 NeoTCR-Scout run.

    Fields:
        project: Human-readable project/run identifier.
        gene: Gene symbol, normalized to uppercase.
        mutation: Protein substitution in AA + position + AA form, e.g. G12D.
        protein_sequence: Optional protein sequence used to generate peptide windows.
        hla: One or more HLA class I alleles normalized to HLA-A*11:01 style.
        peptide_lengths: Peptide lengths to generate, defaulting to 8, 9, 10, and 11.
    """

    if ConfigDict is not None:  # pragma: no branch
        model_config = ConfigDict(extra="forbid")

    project: str
    gene: str
    mutation: str
    protein_sequence: str | None = None
    hla: list[str]
    peptide_lengths: list[int] = Field(default_factory=lambda: list(DEFAULT_PEPTIDE_LENGTHS))

    def __init__(self, **data: Any) -> None:
        """Normalize and validate raw YAML fields before model construction.

        Pydantic enforces the declared field types when installed. The same
        normalization path is also used by the lightweight fallback model so
        restricted test environments still receive identical error messages.
        """

        super().__init__(**_normalize_project_mapping(data, require_all=False))

    @classmethod
    def from_mapping(cls, raw: dict[str, Any]) -> "ProjectInput":
        """Build a project input from parsed YAML with explicit required-field checks."""

        return cls(**_normalize_project_mapping(raw, require_all=True))


# Backward-compatible public name used by earlier code/tests.
ScoutProject = ProjectInput


def validate_mutation(mutation: str) -> str:
    """Validate mutation format such as ``G12D`` and return uppercase text."""

    normalized = mutation.strip().upper()
    match = MUTATION_RE.match(normalized)
    if not match:
        raise ValueError("mutation must use AA + position + AA protein-substitution format, e.g. G12D")
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
            f"Invalid HLA allele {hla!r}; expected class I formats like HLA-A*11:01, A*11:01, or HLA-A1101"
        )
    return f"HLA-{match.group('locus')}*{match.group('first')}:{match.group('second')}"


def validate_protein_sequence(sequence: str | None) -> str | None:
    """Validate and normalize an optional protein sequence."""

    if sequence is None:
        return None
    normalized = sequence.strip().upper().replace(" ", "")
    if not normalized:
        return None
    invalid = sorted(set(normalized) - AMINO_ACIDS)
    if invalid:
        invalid_text = "".join(invalid)
        raise ValueError(f"protein_sequence contains invalid amino-acid code(s): {invalid_text}")
    return normalized


def validate_hla_values(values: Any) -> list[str]:
    """Normalize one HLA string or a list of HLA strings to canonical values."""

    if values is None:
        raise ValueError("Missing required project field(s): hla")
    if not isinstance(values, list):
        values = [values]
    if not values:
        raise ValueError("hla must include at least one allele, e.g. HLA-A*11:01")
    return [normalize_hla(str(value)) for value in values]


def validate_peptide_lengths(lengths: list[Any] | None) -> list[int]:
    """Validate peptide lengths and apply v0.1 defaults when empty."""

    if not lengths:
        return list(DEFAULT_PEPTIDE_LENGTHS)
    if not isinstance(lengths, list):
        raise ValueError("peptide_lengths must be a list of integers, e.g. [8, 9, 10, 11]")
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


def _normalize_project_mapping(raw: dict[str, Any], require_all: bool) -> dict[str, Any]:
    """Normalize raw user input into the ProjectInput schema fields."""

    extra = sorted(set(raw) - PROJECT_INPUT_FIELDS)
    if extra:
        raise ValueError(f"Unsupported project field(s): {', '.join(extra)}")
    if require_all:
        missing = sorted(REQUIRED_PROJECT_INPUT_FIELDS - set(raw))
        if missing:
            raise ValueError(f"Missing required project field(s): {', '.join(missing)}")
    normalized: dict[str, Any] = {}
    if "project" in raw:
        project = str(raw["project"]).strip()
        if not project:
            raise ValueError("project must be a non-empty project identifier")
        normalized["project"] = project
    if "gene" in raw:
        gene = str(raw["gene"]).strip().upper()
        if not gene:
            raise ValueError("gene must be a non-empty gene symbol")
        normalized["gene"] = gene
    if "mutation" in raw:
        normalized["mutation"] = validate_mutation(str(raw["mutation"]))
    if "protein_sequence" in raw:
        normalized["protein_sequence"] = validate_protein_sequence(raw.get("protein_sequence"))
    if "hla" in raw or require_all:
        normalized["hla"] = validate_hla_values(raw.get("hla"))
    if "peptide_lengths" in raw:
        normalized["peptide_lengths"] = validate_peptide_lengths(raw.get("peptide_lengths"))
    elif require_all:
        normalized["peptide_lengths"] = list(DEFAULT_PEPTIDE_LENGTHS)
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
        if value == "":
            result[current_key] = []
        else:
            result[current_key] = _coerce_scalar(value)
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
