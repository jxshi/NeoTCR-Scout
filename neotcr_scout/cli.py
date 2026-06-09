"""Command-line interface for NeoTCR-Scout."""

from __future__ import annotations

import argparse
from pathlib import Path

from neotcr_scout.workflow import WorkflowInput, run_workflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the NeoTCR-Scout v0.1 discovery workflow.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run", help="Run mutation-to-report workflow")
    run_parser.add_argument("--mutation", required=True, help="Protein mutation, e.g. 'KRAS G12D'")
    run_parser.add_argument("--hla", required=True, help="HLA allele, e.g. 'HLA-A*11:01'")
    run_parser.add_argument("--output", required=True, type=Path, help="HTML report path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        result = run_workflow(WorkflowInput(mutation=args.mutation, hla=args.hla, output=args.output))
        print(f"Report: {result.report_path}")
        print("Candidate_TCRs:")
        for hit in result.tcr_hits:
            print(f"  - {hit.entry.identifier} ({hit.entry.source}, similarity={hit.peptide_similarity})")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
