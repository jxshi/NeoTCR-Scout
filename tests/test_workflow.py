from pathlib import Path

from neotcr_scout.neoantigen import generate_peptides, parse_mutation
from neotcr_scout.similarity import levenshtein_distance, normalized_similarity
from neotcr_scout.workflow import WorkflowInput, run_workflow


def test_generate_kras_g12d_peptides_contains_expected_windows():
    mutation = parse_mutation("KRAS G12D")
    peptides = {candidate.sequence for candidate in generate_peptides(mutation)}
    assert "VVVGADGVGK" in peptides
    assert "VVGADGVGK" in peptides
    assert "VVVGADGVGKS" in peptides


def test_similarity_metrics():
    assert levenshtein_distance("VVVGADGVGK", "VVVGACGVGK") == 1
    assert normalized_similarity("VVVGADGVGK", "VVVGACGVGK") == 0.9


def test_workflow_writes_report(tmp_path: Path):
    output = tmp_path / "report.html"
    result = run_workflow(WorkflowInput(mutation="KRAS G12D", hla="HLA-A*11:01", output=output))
    assert output.exists()
    assert result.tcr_hits
    assert result.pmhc.pdb_path is not None
    assert "NeoTCR-Scout report" in output.read_text(encoding="utf-8")
