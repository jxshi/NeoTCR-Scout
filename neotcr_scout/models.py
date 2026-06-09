"""Shared domain models for NeoTCR-Scout."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


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


@dataclass(frozen=True)
class TCREntry:
    """Normalized TCR evidence record across source databases."""

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
