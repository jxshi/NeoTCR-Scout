"""Curated mutation relationship helpers for similarity-driven evidence mining."""

from __future__ import annotations

from pathlib import Path

DEFAULT_RELATIONSHIP_FILE = Path(__file__).resolve().parents[1] / "data" / "mutation_groups" / "ras.yaml"


def related_mutations(gene: str, mutation: str, path: str | Path = DEFAULT_RELATIONSHIP_FILE) -> list[str]:
    """Return manually curated related mutation queries for v0.1."""

    mapping = _load_simple_relationship_yaml(Path(path))
    return mapping.get(f"{gene.upper()} {mutation.upper()}", [])


def _load_simple_relationship_yaml(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    mapping: dict[str, list[str]] = {}
    current_key: str | None = None
    in_queries = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped == "queries:":
            in_queries = True
            continue
        if not in_queries:
            continue
        if not stripped.startswith("-") and stripped.endswith(":"):
            current_key = stripped[:-1].strip()
            mapping[current_key] = []
            continue
        if stripped.startswith("-") and current_key:
            mapping[current_key].append(stripped[1:].strip())
    return mapping
