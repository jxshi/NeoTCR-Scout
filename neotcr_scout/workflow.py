"""Top-level NeoTCR-Scout v0.1 workflow orchestration."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from neotcr_scout.database import search_tcr_database
from neotcr_scout.input import ScoutProject, load_project
from neotcr_scout.mhc_binding import ACADEMIC_LICENSE_NOTICE, MHCBindingPrediction, predict_mhc_binding
from neotcr_scout.peptide import MutantPeptide, generate_mutant_peptides
from neotcr_scout.report import generate_html_report
from neotcr_scout.scoring import TCRCandidate, rank_tcr_candidates
from neotcr_scout.similarity import normalized_similarity


@dataclass(frozen=True)
class WorkflowResult:
    """Filesystem-oriented result for the minimal v0.1 workflow."""

    project: ScoutProject
    output_dir: Path
    peptides: list[MutantPeptide]
    mhc_binding: list[MHCBindingPrediction]
    tcr_candidates: list[TCRCandidate]
    report_path: Path
    artifacts: dict[str, Path]


def run_project(input_path: str | Path, out_dir: str | Path) -> WorkflowResult:
    """Run ``input.yaml`` → reproducible TSV/JSON artifacts → HTML report."""

    project = load_project(input_path)
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    peptides = generate_mutant_peptides(project.gene, project.mutation, project.protein_sequence, project.peptide_lengths)
    binding: list[MHCBindingPrediction] = []
    for allele in project.hla:
        binding.extend(predict_mhc_binding(peptides, allele))

    selected_bindings = sorted(binding, key=lambda item: item.rank_percent)[:10]
    raw_tcr_hits = []
    for prediction in selected_bindings:
        raw_tcr_hits.extend(search_tcr_database(prediction.peptide, prediction.hla))
    candidates = rank_tcr_candidates(raw_tcr_hits)

    peptide_rows = [asdict(peptide) for peptide in peptides]
    binding_rows = [asdict(prediction) for prediction in binding]
    candidate_rows = [asdict(candidate) for candidate in candidates]
    similarity_rows = _build_similarity_rows(peptides, candidates)

    artifacts = {
        "peptides": output_dir / "peptides.tsv",
        "mhc_binding": output_dir / "mhc_binding.tsv",
        "tcr_hits": output_dir / "tcr_hits.tsv",
        "similarity_hits": output_dir / "similarity_hits.tsv",
        "evidence": output_dir / "evidence.json",
        "report": output_dir / "report.html",
    }
    _write_tsv(artifacts["peptides"], peptide_rows)
    _write_tsv(artifacts["mhc_binding"], binding_rows)
    _write_tsv(artifacts["tcr_hits"], candidate_rows)
    _write_tsv(artifacts["similarity_hits"], similarity_rows)

    evidence = {
        "project": project.project,
        "gene": project.gene,
        "mutation": project.mutation,
        "hla": project.hla,
        "artifacts": {key: str(path) for key, path in artifacts.items()},
        "databases": ["VDJdb", "IEDB", "TCR3D"],
        "mhc_binding_methods": sorted({prediction.method for prediction in binding}),
        "third_party_tool_notice": ACADEMIC_LICENSE_NOTICE,
        "tcr_candidates": candidate_rows,
    }
    artifacts["evidence"].write_text(json.dumps(evidence, indent=2), encoding="utf-8")

    report_project = {
        "project": project.project,
        "gene": project.gene,
        "mutation": project.mutation,
        "hla": project.hla,
        "output_dir": output_dir,
        "peptides": peptide_rows,
        "mhc_binding": binding_rows,
        "tcr_candidates": candidate_rows,
        "third_party_tool_notice": ACADEMIC_LICENSE_NOTICE,
    }
    report_path = generate_html_report(report_project, artifacts["report"])
    return WorkflowResult(
        project=project,
        output_dir=output_dir,
        peptides=peptides,
        mhc_binding=binding,
        tcr_candidates=candidates,
        report_path=report_path,
        artifacts=artifacts,
    )


def _build_similarity_rows(peptides: list[MutantPeptide], candidates: list[TCRCandidate]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for peptide in peptides:
        for candidate in candidates:
            rows.append(
                {
                    "peptide": peptide.sequence,
                    "candidate_id": candidate.identifier,
                    "candidate_epitope": candidate.epitope,
                    "source": candidate.source,
                    "similarity": normalized_similarity(peptide.sequence, candidate.epitope),
                }
            )
    return sorted(rows, key=lambda row: float(row["similarity"]), reverse=True)


def _write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("\n", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
