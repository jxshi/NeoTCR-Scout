"""Command-line interface for NeoTCR-Scout."""

from __future__ import annotations

import argparse
from pathlib import Path

try:  # pragma: no cover - optional installed CLI path
    import typer
except Exception:  # pragma: no cover - minimal environment fallback
    typer = None  # type: ignore[assignment]

from neotcr_scout.input import ProjectInput
from neotcr_scout.workflow import run_project, run_validated_project


def _print_result(result: object) -> None:
    print(f"Report: {result.report_path}")
    print("Artifacts:")
    for name, path in result.artifacts.items():
        print(f"  {name}: {path}")
    print("Candidate_TCRs:")
    for candidate in result.tcr_candidates:
        print(f"  - {candidate.identifier} ({candidate.source}, score={candidate.raw_score}, {candidate.score_category})")


if typer is not None:  # pragma: no cover
    app = typer.Typer(help="Run the NeoTCR-Scout v0.1 evidence-guided workflow.")

    @app.command()
    def run(
        input: Path | None = typer.Argument(None, help="Project YAML, e.g. examples/kras_g12d_hla_a1101.yaml"),
        out: Path = typer.Option(Path("results"), "--out", help="Output directory"),
        gene: str | None = typer.Option(None, "--gene", help="Gene symbol for quick-run mode"),
        mutation: str | None = typer.Option(None, "--mutation", help="Protein mutation, e.g. G12D"),
        hla: str | None = typer.Option(None, "--hla", help="HLA allele, e.g. HLA-A*11:01"),
        protein_sequence: str | None = typer.Option(None, "--protein-sequence", help="Protein sequence for quick-run mode"),
    ) -> None:
        if input is not None:
            result = run_project(input, out)
        else:
            if not (gene and mutation and hla):
                raise typer.BadParameter("provide input YAML or --gene --mutation --hla")
            project = ProjectInput.from_mapping(
                {
                    "project": f"{gene}_{mutation}_{hla}".replace("*", "").replace(":", ""),
                    "gene": gene,
                    "mutation": mutation,
                    "hla": [hla],
                    "protein_sequence": protein_sequence,
                }
            )
            result = run_validated_project(project, out)
        _print_result(result)

    def main(argv: list[str] | None = None) -> int:
        app(args=argv)
        return 0

else:

    def build_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Run the NeoTCR-Scout v0.1 evidence-guided workflow.")
        subparsers = parser.add_subparsers(dest="command", required=True)
        run_parser = subparsers.add_parser("run", help="Run input YAML to report/output artifacts")
        run_parser.add_argument("input", nargs="?", type=Path, help="Project YAML, e.g. examples/kras_g12d_hla_a1101.yaml")
        run_parser.add_argument("--out", default=Path("results"), type=Path, help="Output directory, e.g. results/kras_g12d")
        run_parser.add_argument("--gene", help="Gene symbol for quick-run mode")
        run_parser.add_argument("--mutation", help="Protein mutation for quick-run mode, e.g. G12D")
        run_parser.add_argument("--hla", help="HLA allele for quick-run mode, e.g. HLA-A*11:01")
        run_parser.add_argument("--protein-sequence", help="Protein sequence for quick-run mode")
        return parser

    def main(argv: list[str] | None = None) -> int:
        args = build_parser().parse_args(argv)
        if args.command == "run":
            if args.input:
                result = run_project(args.input, args.out)
            else:
                if not (args.gene and args.mutation and args.hla):
                    raise SystemExit("provide input YAML or --gene --mutation --hla")
                project = ProjectInput.from_mapping(
                    {
                        "project": f"{args.gene}_{args.mutation}_{args.hla}".replace("*", "").replace(":", ""),
                        "gene": args.gene,
                        "mutation": args.mutation,
                        "hla": [args.hla],
                        "protein_sequence": args.protein_sequence,
                    }
                )
                result = run_validated_project(project, args.out)
            _print_result(result)
            return 0
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
