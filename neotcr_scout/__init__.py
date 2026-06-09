"""NeoTCR-Scout: rule-based neoantigen-to-TCR discovery workflows."""

from .workflow import WorkflowInput, WorkflowResult, run_workflow

__all__ = ["WorkflowInput", "WorkflowResult", "run_workflow"]
__version__ = "0.1.0"
