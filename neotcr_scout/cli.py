"""Command-line interface for NeoTCR-Scout."""

from __future__ import annotations

import argparse
from pathlib import Path

from neotcr_scout.workflow import run_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the NeoTCR-Scout v0.1 evidence-mining workflow.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run", help="Run input YAML to report/output artifacts")
    run_parser.add_argument("input", type=Path, help="Project YAML, e.g. examples/kras_g12d_hla_a1101.yaml")
    run_parser.add_argument("--out", required=True, type=Path, help="Output directory, e.g. results/kras_g12d")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        result = run_project(args.input, args.out)
        print(f"Report: {result.report_path}")
        print("Artifacts:")
        for name, path in result.artifacts.items():
            print(f"  {name}: {path}")
        print("Candidate_TCRs:")
        for candidate in result.tcr_candidates:
            print(f"  - {candidate.identifier} ({candidate.source}, score={candidate.score})")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
