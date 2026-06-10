from pathlib import Path

from neotcr_scout import (
    generate_mutant_peptides,
    load_project,
    normalize_hla,
    parse_mutation,
    predict_mhc_binding,
    rank_tcr_candidates,
    search_tcr_database,
)
from neotcr_scout.input import ProjectInput
from neotcr_scout.models import TCREntry
from neotcr_scout.relationship import related_mutations
from neotcr_scout.scoring import score_tcr_entry
from neotcr_scout.similarity import (
    blosum62_score,
    exact_peptide_match,
    levenshtein_distance,
    normalized_similarity,
    one_mismatch_peptide_match,
    two_mismatch_peptide_match,
)
from neotcr_scout.workflow import run_project


def test_load_project_yaml_contract():
    project = load_project("examples/kras_g12d_hla_a1101.yaml")
    assert project.project == "KRAS_G12D_HLA_A1101"
    assert project.gene == "KRAS"
    assert project.mutation == "G12D"
    assert project.hla == ["HLA-A*11:01"]
    assert project.peptide_lengths == [8, 9, 10, 11]


def test_input_validation_and_hla_normalization():
    assert normalize_hla("A*11:01") == "HLA-A*11:01"
    assert normalize_hla("HLA-A1101") == "HLA-A*11:01"
    project = ProjectInput(project="x", gene="kras", mutation="g12d", hla="A1101")
    assert project.gene == "KRAS"
    assert project.mutation == "G12D"
    assert project.hla == ["HLA-A*11:01"]
    assert project.peptide_lengths == [8, 9, 10, 11]


def test_invalid_input_has_clear_error_message():
    try:
        ProjectInput.from_mapping({"project": "x", "gene": "KRAS", "mutation": "12D", "hla": "A1101"})
    except ValueError as exc:
        assert "mutation must use" in str(exc)
    else:
        raise AssertionError("invalid mutation should fail validation")
    try:
        ProjectInput.from_mapping({"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": "bad"})
    except ValueError as exc:
        assert "Invalid HLA allele" in str(exc)
    else:
        raise AssertionError("invalid HLA should fail validation")
    try:
        ProjectInput.from_mapping({"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": "A1101", "peptide_lengths": "9"})
    except ValueError as exc:
        assert "peptide_lengths must be a list" in str(exc)
    else:
        raise AssertionError("invalid peptide_lengths should fail validation")


def test_project_input_is_pydantic_schema_with_expected_fields():
    import pydantic

    assert issubclass(ProjectInput, pydantic.BaseModel)
    schema = ProjectInput.model_json_schema()
    assert set(schema["properties"]) == {
        "project",
        "gene",
        "mutation",
        "protein_sequence",
        "hla",
        "peptide_lengths",
    }
    assert set(schema["required"]) == {"project", "gene", "mutation", "hla"}


def test_project_input_defaults_and_clear_validation_errors():
    defaulted = ProjectInput.from_mapping({
        "project": "quick",
        "gene": "KRAS",
        "mutation": "G12D",
        "hla": "hla-a1101",
    })
    assert defaulted.peptide_lengths == [8, 9, 10, 11]
    assert defaulted.hla == ["HLA-A*11:01"]

    invalid_cases = [
        ({"project": "x", "gene": "KRAS", "mutation": "12D", "hla": "A1101"}, "AA + position + AA"),
        ({"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": []}, "hla must include at least one allele"),
        ({"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": "DRB1*04:01"}, "Invalid HLA allele"),
        (
            {"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": "A1101", "peptide_lengths": "9"},
            "peptide_lengths must be a list",
        ),
        (
            {"project": "x", "gene": "KRAS", "mutation": "G12D", "hla": "A1101", "protein_sequence": "MTEY*"},
            "protein_sequence contains invalid",
        ),
    ]
    for raw, message in invalid_cases:
        try:
            ProjectInput.from_mapping(raw)
        except ValueError as exc:
            assert message in str(exc)
        else:
            raise AssertionError(f"invalid input should fail validation: {raw}")


def test_generate_kras_g12d_peptides_contains_expected_annotations():
    mutation = parse_mutation("G12D")
    assert mutation.position == 12
    peptides = generate_mutant_peptides(
        gene="KRAS",
        mutation="G12D",
        wt_sequence="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
        lengths=[8, 9, 10, 11],
    )
    peptide_by_sequence = {candidate.sequence: candidate for candidate in peptides}
    assert "VVVGADGVGK" in peptide_by_sequence
    assert "VVGADGVGK" in peptide_by_sequence
    assert "VVVGADGVGKS" in peptide_by_sequence
    annotated = peptide_by_sequence["VVVGADGVGK"]
    assert annotated.sequence == "VVVGADGVGK"
    assert annotated.length == 10
    assert annotated.start == 7
    assert annotated.end == 16
    assert annotated.mutation_position == 6
    assert annotated.wildtype_peptide == "VVVGAGGVGK"
    assert annotated.mutant_peptide == "VVVGADGVGK"
    assert annotated.mutation_index == 5
    assert annotated.flanking_context
    assert annotated.sequence_context == "mutated_from_wildtype_sequence"


def test_generate_kras_g12d_peptides_covers_8_to_11mers():
    peptides = generate_mutant_peptides(
        gene="KRAS",
        mutation="G12D",
        wt_sequence="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
    )
    lengths = {candidate.length for candidate in peptides}
    assert lengths == {8, 9, 10, 11}
    assert all(candidate.sequence == candidate.mutant_peptide for candidate in peptides)
    assert all(len(candidate.sequence) == candidate.length for candidate in peptides)
    assert all(1 <= candidate.mutation_position <= candidate.length for candidate in peptides)
    assert all(candidate.mutation_index == candidate.mutation_position - 1 for candidate in peptides)


def test_generate_kras_g12d_accepts_already_mutant_sequence():
    peptides = generate_mutant_peptides(
        gene="kras",
        mutation="g12d",
        wt_sequence="MTEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
        lengths=[10],
    )
    annotated = next(candidate for candidate in peptides if candidate.sequence == "VVVGADGVGK")
    assert annotated.gene == "KRAS"
    assert annotated.mutation == "G12D"
    assert annotated.wildtype_peptide == "VVVGAGGVGK"
    assert annotated.mutant_peptide == "VVVGADGVGK"
    assert annotated.sequence_context == "input_sequence_already_mutant"


def test_generate_mutant_peptides_rejects_invalid_mutation_inputs():
    for mutation in ["12D", "B12D", "G12G"]:
        try:
            generate_mutant_peptides("KRAS", mutation, "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV")
        except ValueError as exc:
            assert "mutation" in str(exc)
        else:
            raise AssertionError(f"invalid mutation {mutation} should fail")


def test_similarity_metrics_and_match_types():
    assert levenshtein_distance("VVVGADGVGK", "VVVGACGVGK") == 1
    assert normalized_similarity("VVVGADGVGK", "VVVGACGVGK") == 0.9
    assert exact_peptide_match("AAA", "AAA")
    assert one_mismatch_peptide_match("AAA", "AAV")
    assert two_mismatch_peptide_match("AAA", "AVV")
    assert blosum62_score("VVV", "VVV") > blosum62_score("VVV", "DDD")


def test_core_function_pipeline_returns_ranked_candidates():
    peptides = generate_mutant_peptides("KRAS", "G12D", "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV")
    bindings = predict_mhc_binding(peptides, "HLA-A*11:01")
    best = sorted(bindings, key=lambda binding: binding.rank_percent)[0]
    hits = search_tcr_database(best.peptide, best.hla)
    ranked = rank_tcr_candidates(hits)
    assert ranked
    assert ranked[0].raw_score >= ranked[-1].raw_score
    assert ranked[0].explanation


def test_evidence_scoring_rules_are_transparent():
    entry = TCREntry(
        identifier="demo",
        tra_cdr3=None,
        trb_cdr3="CASSQ",
        v_gene="TRBV1",
        j_gene="TRBJ1",
        epitope="VVVGADGVGK",
        hla="HLA-A*11:01",
        source="VDJdb",
        evidence="functional assay; tetramer evidence",
        metadata={
            "query_peptide": "VVVGADGVGK",
            "query_hla": "HLA-A*11:01",
            "query_gene": "KRAS",
            "query_mutation": "G12D",
            "gene": "KRAS",
            "mutation": "G12D",
            "pubmed_id": "123",
        },
    )
    scored = score_tcr_entry(entry)
    assert scored.raw_score >= 145
    assert scored.score_category == "High"
    assert "same peptide +50" in scored.explanation


def test_relationships_for_kras_g12d():
    related = related_mutations("KRAS", "G12D")
    assert "KRAS G12V" in related
    assert "NRAS G12D" in related


def test_workflow_writes_requested_artifacts_and_reports(tmp_path: Path):
    result = run_project("examples/kras_g12d_hla_a1101.yaml", tmp_path)
    expected = [
        "peptides.tsv",
        "mhc_binding.tsv",
        "tcr_hits.tsv",
        "evidence_score.tsv",
        "report.md",
        "report.html",
        "similarity_hits.tsv",
        "similar_mutations.tsv",
        "evidence.json",
    ]
    for filename in expected:
        assert (tmp_path / filename).exists()
    assert result.tcr_candidates
    report_md = (tmp_path / "report.md").read_text(encoding="utf-8")
    assert "Experimental planning suggestions" in report_md
    assert "TCR cross-reactivity must be experimentally tested" in report_md
    assert "NeoTCR-Scout report" in (tmp_path / "report.html").read_text(encoding="utf-8")


def test_quick_run_without_protein_sequence_uses_builtin_kras_reference(tmp_path: Path):
    project = ProjectInput.from_mapping({
        "project": "quick",
        "gene": "KRAS",
        "mutation": "G12D",
        "hla": ["HLA-A1101"],
    })
    from neotcr_scout.workflow import run_validated_project

    result = run_validated_project(project, tmp_path)

    assert (tmp_path / "report.html").exists()
    assert result.peptides


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
