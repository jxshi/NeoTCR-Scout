"""Top-level NeoTCR-Scout workflow orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from neotcr_scout.mining import TCRMiningEngine
from neotcr_scout.models import BindingPrediction, Mutation, PMHCResult, PeptideCandidate, RiskHit, TCRHit
from neotcr_scout.neoantigen import generate_peptides, parse_mutation
from neotcr_scout.pmhc import PlaceholderPMHCEngine, RuleBasedBindingPredictor
from neotcr_scout.report import render_report
from neotcr_scout.risk import SimpleRiskEngine
from neotcr_scout.structure import StructuralTriageEngine


@dataclass(frozen=True)
class WorkflowInput:
    """User-facing workflow input."""

    mutation: str
    hla: str
    output: Path | None = None


@dataclass(frozen=True)
class WorkflowResult:
    """Complete workflow output bundle."""

    mutation: Mutation
    hla: str
    peptides: list[PeptideCandidate]
    bindings: list[BindingPrediction]
    tcr_hits: list[TCRHit]
    pmhc: PMHCResult
    risk_hits: list[RiskHit]
    structural_metrics: dict[str, float]
    report_path: Path | None = None

    @property
    def binding_by_peptide(self) -> dict[str, BindingPrediction]:
        return {binding.peptide: binding for binding in self.bindings}


def run_workflow(workflow_input: WorkflowInput) -> WorkflowResult:
    """Run the v0.1 rule-based discovery workflow."""

    mutation = parse_mutation(workflow_input.mutation)
    peptides = generate_peptides(mutation)
    bindings = RuleBasedBindingPredictor().predict(peptides, workflow_input.hla)
    prioritized = sorted(bindings, key=lambda binding: binding.rank_percent)
    best_peptide = prioritized[0].peptide

    mining_engine = TCRMiningEngine()
    tcr_hits = mining_engine.search([binding.peptide for binding in prioritized[:8]], workflow_input.hla)
    pmhc = PlaceholderPMHCEngine().predict(best_peptide, workflow_input.hla, workflow_input.output.parent if workflow_input.output else None)
    risk_hits = SimpleRiskEngine().scan(best_peptide)
    structural_metrics = StructuralTriageEngine().score(best_peptide)

    result = WorkflowResult(
        mutation=mutation,
        hla=workflow_input.hla,
        peptides=peptides,
        bindings=bindings,
        tcr_hits=tcr_hits,
        pmhc=pmhc,
        risk_hits=risk_hits,
        structural_metrics=structural_metrics,
        report_path=workflow_input.output,
    )
    if workflow_input.output:
        render_report(result, workflow_input.output)
    return result
