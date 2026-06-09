"""NeoTCR-Scout: reproducible neoantigen-specific TCR evidence mining."""

from .database import search_tcr_database
from .input import ScoutProject, load_project
from .mhc_binding import predict_mhc_binding
from .peptide import generate_mutant_peptides
from .report import generate_html_report
from .scoring import rank_tcr_candidates
from .workflow import WorkflowResult, run_project

__all__ = [
    "ScoutProject",
    "WorkflowResult",
    "generate_html_report",
    "generate_mutant_peptides",
    "load_project",
    "predict_mhc_binding",
    "rank_tcr_candidates",
    "run_project",
    "search_tcr_database",
]
__version__ = "0.1.0"
