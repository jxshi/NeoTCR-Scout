"""Top-level NeoTCR-Scout v0.1 workflow orchestration."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path

try:  # pragma: no cover - optional dependency path
    import pandas as pd
except Exception:  # pragma: no cover - minimal environment fallback
    pd = None  # type: ignore[assignment]

from neotcr_scout.database import search_tcr_database
from neotcr_scout.input import ProjectInput, load_project
from neotcr_scout.mhc_binding import ACADEMIC_LICENSE_NOTICE, MHCBindingPrediction, predict_mhc_binding
from neotcr_scout.peptide import MutantPeptide, generate_mutant_peptides
from neotcr_scout.reference import get_reference_sequence
from neotcr_scout.relationship import related_mutations
from neotcr_scout.report import generate_html_report, generate_markdown_report
from neotcr_scout.scoring import TCRCandidate, rank_tcr_candidates
from neotcr_scout.similarity import build_similarity_hit


@dataclass(frozen=True)
class WorkflowResult:
    """Filesystem-oriented result for the minimal v0.1 workflow."""

    project: ProjectInput
    output_dir: Path
    peptides: list[MutantPeptide]
    mhc_binding: list[MHCBindingPrediction]
    tcr_candidates: list[TCRCandidate]
    report_path: Path
    artifacts: dict[str, Path]


def run_project(input_path: str | Path, out_dir: str | Path) -> WorkflowResult:
    """Run ``input.yaml`` → reproducible TSV/JSON/Markdown/HTML artifacts."""

    project = load_project(input_path)
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return run_validated_project(project, output_dir)


def run_validated_project(project: ProjectInput, out_dir: str | Path) -> WorkflowResult:
    """Run a validated project model."""

    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    protein_sequence = project.protein_sequence or get_reference_sequence(project.gene)
    if not protein_sequence:
        raise ValueError("protein_sequence is required for genes without a built-in demo reference sequence")

    peptides = generate_mutant_peptides(project.gene, project.mutation, protein_sequence, project.peptide_lengths)
    binding: list[MHCBindingPrediction] = []
    for allele in project.hla:
        binding.extend(predict_mhc_binding(peptides, allele))

    selected_bindings = sorted(binding, key=lambda item: item.rank_percent)[:10]
    raw_tcr_hits = []
    for prediction in selected_bindings:
        for hit in search_tcr_database(prediction.peptide, prediction.hla):
            metadata = dict(hit.metadata)
            metadata["query_gene"] = project.gene
            metadata["query_mutation"] = project.mutation
            raw_tcr_hits.append(replace(hit, metadata=metadata))
    candidates = rank_tcr_candidates(raw_tcr_hits)

    peptide_rows = [asdict(peptide) for peptide in peptides]
    binding_rows = [asdict(prediction) for prediction in binding]
    raw_hit_rows = [_entry_to_row(hit) for hit in raw_tcr_hits]
    candidate_rows = [asdict(candidate) for candidate in candidates]
    similarity_rows = _build_similarity_rows(peptides, raw_tcr_hits)
    exact_hit_rows = [row for row in raw_hit_rows if row.get("query_peptide") == row.get("epitope")]
    related_rows = [{"query": item, "source": "data/mutation_groups/ras.yaml"} for item in related_mutations(project.gene, project.mutation)]

    artifacts = {
        "peptides": output_dir / "peptides.tsv",
        "mhc_binding": output_dir / "mhc_binding.tsv",
        "tcr_hits": output_dir / "tcr_hits.tsv",
        "evidence_score": output_dir / "evidence_score.tsv",
        "similarity_hits": output_dir / "similarity_hits.tsv",
        "related_mutations": output_dir / "similar_mutations.tsv",
        "evidence": output_dir / "evidence.json",
        "report_md": output_dir / "report.md",
        "report": output_dir / "report.html",
    }
    _write_tsv(artifacts["peptides"], peptide_rows)
    _write_tsv(artifacts["mhc_binding"], binding_rows)
    _write_tsv(artifacts["tcr_hits"], raw_hit_rows)
    _write_tsv(artifacts["evidence_score"], candidate_rows)
    _write_tsv(artifacts["similarity_hits"], similarity_rows)
    _write_tsv(artifacts["related_mutations"], related_rows)

    evidence = {
        "project": project.project,
        "gene": project.gene,
        "mutation": project.mutation,
        "hla": project.hla,
        "artifacts": {key: str(path) for key, path in artifacts.items()},
        "databases": ["VDJdb", "IEDB", "TCR3D"],
        "mhc_binding_methods": sorted({prediction.method for prediction in binding}),
        "third_party_tool_notice": ACADEMIC_LICENSE_NOTICE,
        "related_mutations": related_rows,
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
        "tcr_hits": raw_hit_rows,
        "exact_hits": exact_hit_rows,
        "similarity_hits": similarity_rows,
        "tcr_candidates": candidate_rows,
        "related_mutations": related_rows,
        "third_party_tool_notice": ACADEMIC_LICENSE_NOTICE,
        "markdown_report": artifacts["report_md"],
    }
    generate_markdown_report(report_project, artifacts["report_md"])
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


def _build_similarity_rows(peptides: list[MutantPeptide], entries: list[object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for peptide in peptides:
        for entry in entries:
            hit = build_similarity_hit(
                query_peptide=peptide.mutant_peptide,
                matched_epitope=entry.epitope,
                query_hla=str(entry.metadata.get("query_hla", "")),
                matched_hla=entry.hla,
                source=entry.source,
                mutation_index=peptide.mutation_index,
            )
            rows.append(asdict(hit) | {"candidate_id": entry.identifier})
    return sorted(rows, key=lambda row: (float(row["similarity_score"]), int(row["blosum62_score"])), reverse=True)


def _entry_to_row(entry: object) -> dict[str, object]:
    metadata = dict(entry.metadata)
    return {
        "identifier": entry.identifier,
        "source": entry.source,
        "epitope": entry.epitope,
        "hla": entry.hla,
        "tra_cdr3": entry.tra_cdr3,
        "trb_cdr3": entry.trb_cdr3,
        "trbv": entry.v_gene,
        "trbj": entry.j_gene,
        "organism": metadata.get("organism", ""),
        "disease": metadata.get("disease", ""),
        "assay": metadata.get("assay", ""),
        "evidence_level": entry.evidence,
        "query_peptide": metadata.get("query_peptide", ""),
        "query_hla": metadata.get("query_hla", ""),
        "gene": metadata.get("gene", ""),
        "mutation": metadata.get("mutation", ""),
        "pubmed_id": metadata.get("pubmed_id", ""),
        "url": metadata.get("url", ""),
        "provenance": metadata.get("provenance", ""),
    }


def _write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if pd is not None:
        pd.DataFrame(rows).to_csv(path, sep="\t", index=False)
        return
    if not rows:
        path.write_text("\n", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
