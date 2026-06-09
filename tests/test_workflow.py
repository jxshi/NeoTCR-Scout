from pathlib import Path

from neotcr_scout import (
    generate_mutant_peptides,
    load_project,
    predict_mhc_binding,
    rank_tcr_candidates,
    search_tcr_database,
)
from neotcr_scout.similarity import levenshtein_distance, normalized_similarity
from neotcr_scout.workflow import run_project


def test_load_project_yaml_contract():
    project = load_project("examples/kras_g12d_hla_a1101.yaml")
    assert project.project == "KRAS_G12D_HLA_A1101"
    assert project.gene == "KRAS"
    assert project.mutation == "G12D"
    assert project.hla == ["HLA-A*11:01"]
    assert project.peptide_lengths == [8, 9, 10, 11]


def test_generate_kras_g12d_peptides_contains_expected_windows():
    peptides = {candidate.sequence for candidate in generate_mutant_peptides(
        gene="KRAS",
        mutation="G12D",
        wt_sequence="MTEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
        lengths=[8, 9, 10, 11],
    )}
    assert "VVVGADGVGK" in peptides
    assert "VVGADGVGK" in peptides
    assert "VVVGADGVGKS" in peptides


def test_similarity_metrics():
    assert levenshtein_distance("VVVGADGVGK", "VVVGACGVGK") == 1
    assert normalized_similarity("VVVGADGVGK", "VVVGACGVGK") == 0.9


def test_core_function_pipeline_returns_ranked_candidates():
    peptides = generate_mutant_peptides("KRAS", "G12D", "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV")
    bindings = predict_mhc_binding(peptides, "HLA-A*11:01")
    best = sorted(bindings, key=lambda binding: binding.rank_percent)[0]
    hits = search_tcr_database(best.peptide, best.hla)
    ranked = rank_tcr_candidates(hits)
    assert ranked
    assert ranked[0].score >= ranked[-1].score


def test_workflow_writes_requested_artifacts(tmp_path: Path):
    result = run_project("examples/kras_g12d_hla_a1101.yaml", tmp_path)
    expected = [
        "peptides.tsv",
        "mhc_binding.tsv",
        "tcr_hits.tsv",
        "similarity_hits.tsv",
        "evidence.json",
        "report.html",
    ]
    for filename in expected:
        assert (tmp_path / filename).exists()
    assert result.tcr_candidates
    assert "NeoTCR-Scout v0.1 evidence report" in (tmp_path / "report.html").read_text(encoding="utf-8")


def test_netmhcpan_tool_from_env_is_called_and_parsed(tmp_path, monkeypatch):
    executable = tmp_path / "netMHCpan"
    executable.write_text(
        "#!/usr/bin/env python3\n"
        "print('Pos MHC Peptide EL_Rank BindLevel')\n"
        "print('1 HLA-A11:01 VVVGADGVGK 0.21 <= SB')\n",
        encoding="utf-8",
    )
    executable.chmod(0o755)
    monkeypatch.setenv("NEOTCR_SCOUT_NETMHCPAN", str(executable))
    monkeypatch.delenv("NEOTCR_SCOUT_MHCFLURRY_PREDICT", raising=False)

    predictions = predict_mhc_binding(["VVVGADGVGK"], "HLA-A*11:01")

    assert predictions[0].method == "NetMHCpan"
    assert predictions[0].rank_percent == 0.21
    assert predictions[0].binder == "<= SB"


def test_mhcflurry_tool_from_env_is_called_when_netmhcpan_absent(tmp_path, monkeypatch):
    executable = tmp_path / "mhcflurry-predict"
    executable.write_text(
        "#!/usr/bin/env python3\n"
        "print('allele,peptide,affinity,presentation_percentile')\n"
        "print('HLA-A*11:01,VVVGADGVGK,42.0,0.35')\n",
        encoding="utf-8",
    )
    executable.chmod(0o755)
    monkeypatch.setenv("NEOTCR_SCOUT_NETMHCPAN", str(tmp_path / "missing-netMHCpan"))
    monkeypatch.setenv("NEOTCR_SCOUT_MHCFLURRY_PREDICT", str(executable))

    predictions = predict_mhc_binding(["VVVGADGVGK"], "HLA-A*11:01")

    assert predictions[0].method == "MHCflurry"
    assert predictions[0].rank_percent == 0.35
    assert predictions[0].affinity_nm == 42.0


def test_workflow_evidence_records_third_party_license_notice(tmp_path: Path):
    run_project("examples/kras_g12d_hla_a1101.yaml", tmp_path)
    evidence = (tmp_path / "evidence.json").read_text(encoding="utf-8")
    assert "contact the original authors" in evidence
