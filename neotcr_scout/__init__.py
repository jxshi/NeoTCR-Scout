"""NeoTCR-Scout: evidence-guided neoantigen-specific TCR discovery."""

from .database import search_tcr_database
from .input import ProjectInput, ScoutProject, load_project, normalize_hla
from .mhc_binding import predict_mhc_binding
from .neoantigen import annotate_peptide_window, apply_mutation, generate_mutant_peptides, parse_mutation
from .relationship import related_mutations
from .report import generate_html_report, generate_markdown_report
from .scoring import rank_tcr_candidates, score_tcr_entry
from .workflow import WorkflowResult, run_project, run_validated_project

__all__ = [
    "ProjectInput",
    "ScoutProject",
    "WorkflowResult",
    "annotate_peptide_window",
    "apply_mutation",
    "generate_html_report",
    "generate_markdown_report",
    "generate_mutant_peptides",
    "load_project",
    "normalize_hla",
    "parse_mutation",
    "predict_mhc_binding",
    "rank_tcr_candidates",
    "related_mutations",
    "run_project",
    "run_validated_project",
    "score_tcr_entry",
    "search_tcr_database",
]
__version__ = "0.1.0"
