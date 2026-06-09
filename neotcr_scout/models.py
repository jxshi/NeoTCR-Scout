"""Shared Pydantic-compatible domain models for NeoTCR-Scout."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

try:  # pragma: no cover - exercised when optional dependency is installed
    from pydantic import BaseModel as _PydanticBaseModel
    from pydantic import Field as Field
except Exception:  # lightweight fallback for offline/minimal environments

    class _PydanticBaseModel:
        """Small subset of Pydantic's BaseModel used by the v0.1 models."""

        def __init__(self, **data: Any) -> None:
            annotations = getattr(self, "__annotations__", {})
            for name in annotations:
                if name in data:
                    setattr(self, name, data.pop(name))
                elif hasattr(self.__class__, name):
                    default = getattr(self.__class__, name)
                    setattr(self, name, default() if callable(default) and getattr(default, "_is_default_factory", False) else default)
                else:
                    setattr(self, name, None)
            for name, value in data.items():
                setattr(self, name, value)

        def model_dump(self) -> dict[str, Any]:
            return dict(self.__dict__)

        def dict(self) -> dict[str, Any]:
            return self.model_dump()

    def Field(default: Any = None, default_factory: Any | None = None, **_: Any) -> Any:
        if default_factory is not None:
            def factory_marker() -> Any:
                return default_factory()
            factory_marker._is_default_factory = True  # type: ignore[attr-defined]
            return factory_marker
        return default


BaseModel = _PydanticBaseModel


@dataclass(frozen=True)
class Mutation:
    """A protein-level amino-acid substitution."""

    gene: str
    wildtype: str
    position: int
    mutant: str

    @property
    def label(self) -> str:
        return f"{self.gene} {self.wildtype}{self.position}{self.mutant}"


@dataclass(frozen=True)
class PeptideCandidate:
    """A mutation-centered peptide candidate."""

    sequence: str
    length: int
    mutation_index: int
    source_mutation: Mutation


@dataclass(frozen=True)
class BindingPrediction:
    """A peptide-HLA binding prediction or imported predictor result."""

    peptide: str
    hla: str
    rank_percent: float
    method: str


class TCREvidence(BaseModel):
    """Unified TCR evidence schema across VDJdb, IEDB, TCR3D, local files, and literature."""

    source: str
    epitope: str
    hla: str | None = None
    tra_cdr3: str | None = None
    trb_cdr3: str | None = None
    trbv: str | None = None
    trbj: str | None = None
    organism: str | None = None
    disease: str | None = None
    assay: str | None = None
    pubmed_id: str | None = None
    url: str | None = None
    evidence_level: str | None = None
    gene: str | None = None
    mutation: str | None = None
    structure_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if hasattr(self, "model_dump"):
            return self.model_dump()
        return self.dict()


@dataclass(frozen=True)
class TCREntry:
    """Backward-compatible normalized TCR evidence record."""

    identifier: str
    tra_cdr3: str | None
    trb_cdr3: str | None
    v_gene: str | None
    j_gene: str | None
    epitope: str
    hla: str | None
    source: str
    evidence: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_evidence(cls, evidence: TCREvidence, identifier: str | None = None) -> "TCREntry":
        metadata = dict(evidence.metadata or {})
        if evidence.pubmed_id:
            metadata["pubmed_id"] = evidence.pubmed_id
        if evidence.url:
            metadata["url"] = evidence.url
        if evidence.gene:
            metadata["gene"] = evidence.gene
        if evidence.mutation:
            metadata["mutation"] = evidence.mutation
        if evidence.structure_id:
            metadata["structure_id"] = evidence.structure_id
        return cls(
            identifier=identifier or str(metadata.get("identifier") or f"{evidence.source}:{evidence.epitope}"),
            tra_cdr3=evidence.tra_cdr3,
            trb_cdr3=evidence.trb_cdr3,
            v_gene=evidence.trbv,
            j_gene=evidence.trbj,
            epitope=evidence.epitope,
            hla=evidence.hla,
            source=evidence.source,
            evidence=evidence.evidence_level,
            metadata=metadata,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TCRHit:
    """A mined TCR record with workflow-specific similarity evidence."""

    entry: TCREntry
    peptide_similarity: float
    hla_match: bool
    matched_peptide: str


@dataclass(frozen=True)
class RiskHit:
    """A possible human-proteome off-target match."""

    peptide: str
    protein: str
    mismatches: int
    risk_level: str


@dataclass(frozen=True)
class PMHCResult:
    """pMHC structure artifact and simple residue exposure summary."""

    pdb_path: Path | None
    tcr_facing_residues: dict[str, str]
    method: str
