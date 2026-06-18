import subprocess
import sys
from pathlib import Path

import pytest

from neotcr_scout import (
    generate_mutant_peptides,
    load_project,
    normalize_hla,
    parse_mutation,
    predict_mhc_binding,
    rank_tcr_candidates,
    search_tcr_database,
)
from neotcr_scout.database import (
    search_iedb,
    search_neotcr,
    search_tcr3d,
    search_tcr_evidence,
    search_vdjdb,
)
from neotcr_scout.input import ProjectInput
from neotcr_scout.models import TCREntry, TCREvidence
from neotcr_scout.relationship import related_mutation_records, related_mutations
from neotcr_scout.scoring import score_tcr_entry
from neotcr_scout.similarity import (
    blosum62_score,
    build_similarity_hit,
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


def test_mutation_parsing_accepts_protein_substitutions_and_rejects_invalid_values():
    parsed = parse_mutation("g12d")
    assert parsed.wildtype == "G"
    assert parsed.position == 12
    assert parsed.mutant == "D"
    assert parsed.label == "G12D"

    for mutation in ["12D", "B12D", "G12G"]:
        try:
            parse_mutation(mutation)
        except ValueError as exc:
            assert "mutation" in str(exc) or "Unsupported" in str(exc)
        else:
            raise AssertionError(f"invalid mutation {mutation} should fail")


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
    pydantic = pytest.importorskip("pydantic")

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


def test_generate_kras_g12d_peptides_reports_required_fields_for_8_to_11mers():
    peptides = generate_mutant_peptides(
        gene="KRAS",
        mutation="G12D",
        wt_sequence="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
        lengths=[8, 9, 10, 11],
    )

    assert {peptide.length for peptide in peptides} == {8, 9, 10, 11}
    assert peptides
    for peptide in peptides:
        assert peptide.sequence == peptide.mutant_peptide
        assert len(peptide.sequence) == peptide.length
        assert len(peptide.wildtype_peptide) == peptide.length
        assert len(peptide.mutant_peptide) == peptide.length
        assert peptide.wildtype_peptide != peptide.mutant_peptide
        assert peptide.mutation_position == peptide.mutation_index + 1
        assert 1 <= peptide.mutation_position <= peptide.length
        assert peptide.wildtype_peptide[peptide.mutation_index] == "G"
        assert peptide.mutant_peptide[peptide.mutation_index] == "D"
        assert peptide.flanking_context


def test_generate_mutant_peptides_handles_terminal_and_custom_mutations():
    sequence = "ACDEFGHIKLMNPQRSTVWY"

    n_terminal = generate_mutant_peptides("GENE1", "A1C", sequence, lengths=[8, 9, 10, 11])
    assert {peptide.length for peptide in n_terminal} == {8, 9, 10, 11}
    assert all(peptide.mutation_position == 1 for peptide in n_terminal)
    assert all(peptide.wildtype_peptide[0] == "A" for peptide in n_terminal)
    assert all(peptide.mutant_peptide[0] == "C" for peptide in n_terminal)

    c_terminal = generate_mutant_peptides("GENE2", "Y20F", sequence, lengths=[8, 9, 10, 11])
    assert {peptide.length for peptide in c_terminal} == {8, 9, 10, 11}
    assert all(peptide.mutation_position == peptide.length for peptide in c_terminal)
    assert all(peptide.wildtype_peptide[-1] == "Y" for peptide in c_terminal)
    assert all(peptide.mutant_peptide[-1] == "F" for peptide in c_terminal)


def test_generate_mutant_peptides_defaults_empty_lengths_to_8_to_11mers():
    peptides = generate_mutant_peptides(
        gene="KRAS",
        mutation="G12D",
        wt_sequence="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
        lengths=[],
    )

    assert {peptide.length for peptide in peptides} == {8, 9, 10, 11}


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
    assert exact_peptide_match(" aaa ", "AAA")
    assert one_mismatch_peptide_match("AAA", "AAV")
    assert two_mismatch_peptide_match("AAA", "AVV")
    assert blosum62_score("VVV", "VVV") > blosum62_score("VVV", "DDD")


def test_similarity_hits_capture_kras_g12d_related_mutation_examples():
    query = "VVVGADGVGK"
    kras_g12v = "VVVGAVGVGK"
    kras_g13d = "VVVGAGDVGK"

    assert one_mismatch_peptide_match(query, kras_g12v)
    assert two_mismatch_peptide_match(query, kras_g13d)
    assert levenshtein_distance(query, kras_g12v) == 1
    assert levenshtein_distance(query, kras_g13d) == 2
    assert normalized_similarity(query, kras_g12v) == 0.9
    assert normalized_similarity(query, kras_g13d) == 0.8
    assert blosum62_score(query, kras_g12v) > blosum62_score(query, kras_g13d)

    g12v_hit = build_similarity_hit(
        query_peptide=query,
        matched_epitope=kras_g12v,
        query_hla="hla-a1101",
        matched_hla="HLA-A*11:01",
        source="KRAS G12V",
        mutation_index=5,
    )
    assert g12v_hit.query_peptide == query
    assert g12v_hit.matched_epitope == kras_g12v
    assert g12v_hit.distance == 1
    assert g12v_hit.similarity_score == 0.9
    assert g12v_hit.mutation_site_match == "no"
    assert g12v_hit.same_hla == "yes"
    assert g12v_hit.source == "KRAS G12V"

    g13d_hit = build_similarity_hit(
        query_peptide=query,
        matched_epitope=kras_g13d,
        query_hla="HLA-A*11:01",
        matched_hla="HLA-A*03:01",
        source="KRAS G13D",
        mutation_index=5,
    )
    assert g13d_hit.distance == 2
    assert g13d_hit.similarity_score == 0.8
    assert g13d_hit.mutation_site_match == "no"
    assert g13d_hit.same_hla == "no"
    assert g13d_hit.source == "KRAS G13D"

def test_database_adapters_return_normalized_tcr_evidence_by_peptide_and_hla():
    required_fields = {
        "source",
        "epitope",
        "hla",
        "tra_cdr3",
        "trb_cdr3",
        "trbv",
        "trbj",
        "organism",
        "disease",
        "assay",
        "pubmed_id",
        "url",
        "evidence_level",
    }
    adapter_cases = [
        (search_vdjdb, "VVGADGVGK", "A1101", "VDJdb"),
        (search_iedb, "GADGVGKSAL", "HLA-A*11:01", "IEDB"),
        (search_tcr3d, "VVVGADGVGK", "HLA-A1101", "TCR3D"),
        (search_neotcr, "VVVGADGVGK", "A*11:01", "NeoTCR"),
    ]

    for adapter, peptide, hla, source in adapter_cases:
        hits = adapter(peptide, hla)
        assert hits, f"{source} adapter should return a fixture hit"
        assert all(isinstance(hit, TCREvidence) for hit in hits)
        assert all(hit.source == source for hit in hits)
        assert all(hit.hla == "HLA-A*11:01" for hit in hits)
        for hit in hits:
            payload = hit.to_dict()
            assert required_fields <= set(payload)
            assert payload["source"]
            assert payload["epitope"]
            assert payload["hla"]
            assert payload["organism"]
            assert payload["disease"]
            assert payload["assay"]
            assert payload["url"]
            assert payload["evidence_level"]


def test_unified_evidence_search_includes_all_seed_adapters_with_query_provenance():
    hits = search_tcr_evidence("VVVGADGVGK", "hla-a1101")
    sources = {hit.source for hit in hits}

    assert {"VDJdb", "IEDB", "TCR3D", "NeoTCR"} <= sources
    assert all(hit.metadata["query_peptide"] == "VVVGADGVGK" for hit in hits)
    assert all(hit.metadata["query_hla"] == "hla-a1101" for hit in hits)


def test_core_function_pipeline_returns_ranked_candidates():
    peptides = generate_mutant_peptides("KRAS", "G12D", "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV")
    bindings = predict_mhc_binding(peptides, "HLA-A*11:01")
    best = sorted(bindings, key=lambda binding: binding.rank_percent)[0]
    hits = search_tcr_database(best.peptide, best.hla)
    ranked = rank_tcr_candidates(hits)
    assert ranked
    assert ranked[0].raw_score >= ranked[-1].raw_score
    assert ranked[0].explanation


def test_database_adapters_return_normalized_tcr_evidence():
    adapters = [
        ("VDJdb", search_vdjdb, "VVGADGVGK"),
        ("IEDB", search_iedb, "VVVGADGVGK"),
        ("TCR3D", search_tcr3d, "VVVGACGVGK"),
        ("NeoTCR", search_neotcr, "VVVGADGVGK"),
    ]
    required_fields = [
        "source",
        "epitope",
        "hla",
        "tra_cdr3",
        "trb_cdr3",
        "trbv",
        "trbj",
        "organism",
        "disease",
        "assay",
        "pubmed_id",
        "url",
        "evidence_level",
    ]
    for expected_source, adapter, peptide in adapters:
        hits = adapter(peptide, "A1101")
        assert hits, f"{expected_source} adapter should return at least one fixture hit"
        evidence = hits[0]
        assert isinstance(evidence, TCREvidence)
        assert evidence.source == expected_source
        assert evidence.hla == "HLA-A*11:01"
        evidence_dict = evidence.to_dict()
        for field in required_fields:
            assert hasattr(evidence, field)
            assert field in evidence_dict


def test_database_adapters_filter_by_hla():
    adapters = [search_vdjdb, search_iedb, search_tcr3d, search_neotcr]
    for adapter in adapters:
        assert adapter("VVVGADGVGK", "HLA-A*02:01") == []


def test_unified_database_search_includes_all_adapters_as_entries():
    hits = search_tcr_database("VVVGADGVGK", "HLA-A*11:01")
    sources = {hit.source for hit in hits}
    assert {"VDJdb", "IEDB", "TCR3D", "NeoTCR"}.issubset(sources)
    assert all(isinstance(hit, TCREntry) for hit in hits)
    assert all(hit.metadata["query_peptide"] == "VVVGADGVGK" for hit in hits)


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


def test_evidence_scoring_applies_all_declared_rules_exactly():
    entry = TCREntry(
        identifier="all-rules",
        tra_cdr3="CAVTEST",
        trb_cdr3="CASSTEST",
        v_gene="TRBV1",
        j_gene="TRBJ1",
        epitope="VVVGADGVGK",
        hla="HLA-A*11:01",
        source="NeoTCR",
        evidence="functional assay; tetramer evidence; clinical evidence; structure available",
        metadata={
            "query_peptide": "VVVGADGVGK",
            "query_hla": "A1101",
            "query_gene": "KRAS",
            "query_mutation": "G12D",
            "gene": "KRAS",
            "mutation": "G12D",
            "structure_id": "demo-structure",
            "pubmed_id": "123456",
        },
    )

    scored = score_tcr_entry(entry)

    assert scored.raw_score == 220
    assert scored.score == 220.0
    assert scored.score_category == "High"
    for reason in [
        "same peptide +50",
        "same HLA +20",
        "same mutation/gene +15",
        "same protein family +5",
        "functional assay +30",
        "tetramer evidence +20",
        "clinical evidence +50",
        "structure available +20",
        "literature PMID +10",
    ]:
        assert reason in scored.explanation


def test_rank_tcr_candidates_places_highest_rule_based_score_first():
    top = TCREntry(
        identifier="top",
        tra_cdr3=None,
        trb_cdr3="CASSTOP",
        v_gene="TRBV1",
        j_gene="TRBJ1",
        epitope="VVVGADGVGK",
        hla="HLA-A*11:01",
        source="NeoTCR",
        evidence="functional assay; tetramer evidence; clinical evidence; structure available",
        metadata={
            "query_peptide": "VVVGADGVGK",
            "query_hla": "HLA-A*11:01",
            "query_gene": "KRAS",
            "query_mutation": "G12D",
            "gene": "KRAS",
            "mutation": "G12D",
            "structure_id": "demo-structure",
            "pubmed_id": "123456",
        },
    )
    lower = TCREntry(
        identifier="lower",
        tra_cdr3=None,
        trb_cdr3="CASSLOW",
        v_gene="TRBV2",
        j_gene="TRBJ2",
        epitope="VVVGAVGVGK",
        hla="HLA-A*11:01",
        source="VDJdb",
        evidence="functional assay",
        metadata={
            "query_peptide": "VVVGADGVGK",
            "query_hla": "HLA-A*11:01",
            "query_gene": "KRAS",
            "query_mutation": "G12D",
            "gene": "KRAS",
            "mutation": "G12V",
        },
    )

    ranked = rank_tcr_candidates([lower, top])

    assert ranked[0].identifier == "top"
    assert ranked[0].raw_score == 220
    assert ranked[1].identifier == "lower"
    assert ranked[1].raw_score < ranked[0].raw_score


def test_relationships_for_kras_g12d():
    related = related_mutations("KRAS", "G12D")
    assert related == ["KRAS G12V", "KRAS G12C", "KRAS G13D", "NRAS G12D", "HRAS G12D"]


def test_related_mutation_records_are_standardized_for_downstream_search():
    records = related_mutation_records("kras", "g12d")

    assert [record.related_query for record in records] == [
        "KRAS G12V",
        "KRAS G12C",
        "KRAS G13D",
        "NRAS G12D",
        "HRAS G12D",
    ]
    first = records[0].to_dict()
    assert first == {
        "query_gene": "KRAS",
        "query_mutation": "G12D",
        "related_gene": "KRAS",
        "related_mutation": "G12V",
        "related_query": "KRAS G12V",
        "relationship_group": "RAS",
        "source": "data/mutation_groups/ras.yaml",
    }
    assert records[2].related_gene == "KRAS"
    assert records[2].related_mutation == "G13D"
    assert records[3].related_gene == "NRAS"
    assert records[3].related_mutation == "G12D"
    assert records[4].related_gene == "HRAS"
    assert records[4].related_mutation == "G12D"


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
    similar_mutations = (tmp_path / "similar_mutations.tsv").read_text(encoding="utf-8")
    assert "query_gene	query_mutation	related_gene	related_mutation	related_query	relationship_group	source" in similar_mutations
    assert "KRAS	G12D	KRAS	G12V	KRAS G12V	RAS	data/mutation_groups/ras.yaml" in similar_mutations
    assert result.tcr_candidates
    report_md = (tmp_path / "report.md").read_text(encoding="utf-8")
    expected_sections = [
        "## 1. Project summary",
        "## 2. Input mutation & HLA",
        "## 3. Generated neoantigen peptides",
        "## 4. MHC binding summary",
        "## 5. Exact TCR database hits",
        "## 6. Similar peptide / related mutation hits",
        "## 7. Evidence score table",
        "## 8. Experimental planning suggestions",
        "## 9. Limitations & warnings",
    ]
    for section in expected_sections:
        assert section in report_md
    similarity_hits = (tmp_path / "similarity_hits.tsv").read_text(encoding="utf-8")
    assert "query_peptide	matched_epitope	distance	similarity_score" in similarity_hits
    assert "mutation_site_match	same_hla	source" in similarity_hits
    assert "### Curated related mutations" in report_md
    assert "KRAS G12V" in report_md
    assert "Synthesize top-ranked mutant peptide candidates" in report_md
    assert "Perform focused cross-reactivity testing" in report_md
    assert "TCR cross-reactivity must be experimentally tested" in report_md
    report_html = (tmp_path / "report.html").read_text(encoding="utf-8")
    assert "NeoTCR-Scout report" in report_html
    assert "Input mutation &amp; HLA" in report_html
    assert "Limitations &amp; warnings" in report_html
    tcr_hits_header = (tmp_path / "tcr_hits.tsv").read_text(encoding="utf-8").splitlines()[0].split("\t")
    for field in ["organism", "disease", "assay"]:
        assert field in tcr_hits_header


@pytest.mark.parametrize(
    "example_path",
    [
        Path("examples/kras_g12d_hla_a1101.yaml"),
        Path("examples/kras_g12v_hla_a0301.yaml"),
        Path("examples/tp53_r175h_hla_a0201.yaml"),
    ],
)
def test_example_inputs_run_successfully_with_pytest(example_path: Path, tmp_path: Path):
    result = run_project(example_path, tmp_path / example_path.stem)

    assert result.peptides
    assert result.mhc_binding
    for artifact_name in ["peptides", "mhc_binding", "tcr_hits", "evidence_score", "report_md", "report"]:
        assert result.artifacts[artifact_name].exists()
    report_md = result.artifacts["report_md"].read_text(encoding="utf-8")
    assert "## 1. Project summary" in report_md
    assert "## 8. Experimental planning suggestions" in report_md


def test_cli_run_command_writes_expected_outputs_and_exits_zero(tmp_path: Path):
    out_dir = tmp_path / "kras_g12d_cli"
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "neotcr_scout.cli",
            "run",
            "examples/kras_g12d_hla_a1101.yaml",
            "--out",
            str(out_dir),
        ],
        cwd=Path.cwd(),
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert out_dir.exists()
    for filename in [
        "peptides.tsv",
        "mhc_binding.tsv",
        "tcr_hits.tsv",
        "evidence_score.tsv",
        "similarity_hits.tsv",
        "similar_mutations.tsv",
        "evidence.json",
        "report.md",
        "report.html",
    ]:
        assert (out_dir / filename).exists(), filename
    assert (out_dir / "report.html").read_text(encoding="utf-8")
    assert "Report:" in completed.stdout


def test_cli_invalid_input_exits_nonzero_without_traceback(tmp_path: Path):
    invalid_yaml = tmp_path / "invalid.yaml"
    invalid_yaml.write_text(
        "project: BAD\n"
        "gene: KRAS\n"
        "mutation: 12D\n"
        "hla:\n"
        "  - HLA-A*11:01\n",
        encoding="utf-8",
    )

    completed = subprocess.run(
        [sys.executable, "-m", "neotcr_scout.cli", "run", str(invalid_yaml), "--out", str(tmp_path / "bad")],
        cwd=Path.cwd(),
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 1
    assert "Error: mutation must use AA + position + AA" in completed.stderr
    assert "Traceback" not in completed.stderr


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
    assert '"NeoTCR"' in evidence
