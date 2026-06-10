"""Curated mutation relationship helpers for similarity-driven evidence mining."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

DEFAULT_RELATIONSHIP_FILE = Path(__file__).resolve().parents[1] / "data" / "mutation_groups" / "ras.yaml"


@dataclass(frozen=True)
class RelatedMutation:
    """Standard related-mutation row used by downstream evidence search/reporting."""

    query_gene: str
    query_mutation: str
    related_gene: str
    related_mutation: str
    related_query: str
    relationship_group: str
    source: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def related_mutation_records(
    gene: str,
    mutation: str,
    path: str | Path = DEFAULT_RELATIONSHIP_FILE,
) -> list[RelatedMutation]:
    """Return curated related mutations as structured rows for downstream search."""

    relationship_path = Path(path)
    curated = _load_simple_relationship_yaml(relationship_path)
    query_gene = gene.strip().upper()
    query_mutation = mutation.strip().upper()
    query_key = f"{query_gene} {query_mutation}"
    group = curated.group or relationship_path.stem.upper()
    records: list[RelatedMutation] = []
    for related_query in curated.queries.get(query_key, []):
        related_gene, related_mutation = _parse_related_query(related_query)
        records.append(
            RelatedMutation(
                query_gene=query_gene,
                query_mutation=query_mutation,
                related_gene=related_gene,
                related_mutation=related_mutation,
                related_query=f"{related_gene} {related_mutation}",
                relationship_group=group,
                source=_source_label(relationship_path),
            )
        )
    return records


def related_mutations(gene: str, mutation: str, path: str | Path = DEFAULT_RELATIONSHIP_FILE) -> list[str]:
    """Return manually curated related mutation query labels for v0.1 compatibility."""

    return [record.related_query for record in related_mutation_records(gene, mutation, path)]


@dataclass(frozen=True)
class _RelationshipYaml:
    group: str | None
    queries: dict[str, list[str]]


def _load_simple_relationship_yaml(path: Path) -> _RelationshipYaml:
    if not path.exists():
        return _RelationshipYaml(group=None, queries={})
    mapping: dict[str, list[str]] = {}
    group: str | None = None
    current_key: str | None = None
    in_queries = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("group:"):
            group = stripped.split(":", 1)[1].strip() or None
            continue
        if stripped == "queries:":
            in_queries = True
            continue
        if not in_queries:
            continue
        if not stripped.startswith("-") and stripped.endswith(":"):
            current_key = stripped[:-1].strip().upper()
            mapping[current_key] = []
            continue
        if stripped.startswith("-") and current_key:
            related_gene, related_mutation = _parse_related_query(stripped[1:].strip())
            mapping[current_key].append(f"{related_gene} {related_mutation}")
    return _RelationshipYaml(group=group, queries=mapping)


def _parse_related_query(value: str) -> tuple[str, str]:
    parts = value.strip().upper().split()
    if len(parts) != 2:
        raise ValueError(f"related mutation query {value!r} must have format 'GENE MUTATION', e.g. KRAS G12D")
    return parts[0], parts[1]


def _source_label(path: Path) -> str:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        return str(path.resolve().relative_to(repo_root))
    except ValueError:
        return str(path)
