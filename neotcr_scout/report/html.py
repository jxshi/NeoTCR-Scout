"""HTML report rendering."""

from __future__ import annotations

from html import escape
from pathlib import Path


def _table_row(cells: list[object]) -> str:
    return "<tr>" + "".join(f"<td>{escape(str(cell))}</td>" for cell in cells) + "</tr>"


def render_report(result: object, output_path: Path) -> Path:
    """Render a workflow result to HTML without external runtime dependencies."""

    peptide_rows = []
    for peptide in result.peptides:
        binding = result.binding_by_peptide[peptide.sequence]
        peptide_rows.append(_table_row([peptide.sequence, peptide.length, peptide.mutation_index, binding.rank_percent]))

    tcr_rows = []
    for hit in result.tcr_hits:
        tcr_rows.append(
            _table_row(
                [
                    hit.entry.identifier,
                    hit.entry.tra_cdr3 or "-",
                    hit.entry.trb_cdr3 or "-",
                    hit.entry.epitope,
                    hit.entry.hla or "-",
                    hit.entry.source,
                    hit.peptide_similarity,
                ]
            )
        )

    risk_rows = []
    for risk in result.risk_hits:
        risk_rows.append(_table_row([risk.protein, risk.peptide, risk.mismatches, risk.risk_level]))

    structural_rows = []
    for metric, value in result.structural_metrics.items():
        structural_rows.append(_table_row([metric, value]))

    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>NeoTCR-Scout report</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #1f2937; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 1.5rem; }}
    th, td {{ border: 1px solid #d1d5db; padding: 0.5rem; text-align: left; }}
    th {{ background: #f3f4f6; }}
    .badge {{ background: #e0f2fe; border-radius: 999px; padding: 0.15rem 0.5rem; }}
  </style>
</head>
<body>
  <h1>NeoTCR-Scout report</h1>
  <p><strong>Mutation:</strong> {escape(result.mutation.label)} &nbsp; <strong>HLA:</strong> {escape(result.hla)}</p>

  <h2>1. Neoantigen candidates</h2>
  <table><tr><th>Peptide</th><th>Length</th><th>Mutation index</th><th>Rank %</th></tr>
  {''.join(peptide_rows)}
  </table>

  <h2>2. Candidate TCRs</h2>
  <table><tr><th>ID</th><th>TRA CDR3</th><th>TRB CDR3</th><th>Epitope</th><th>HLA</th><th>Source</th><th>Similarity</th></tr>
  {''.join(tcr_rows)}
  </table>

  <h2>3. pMHC structure</h2>
  <p>Method: {escape(result.pmhc.method)}; artifact: {escape(str(result.pmhc.pdb_path or 'not generated'))}</p>

  <h2>4. Structural triage</h2>
  <table><tr><th>Metric</th><th>Value</th></tr>{''.join(structural_rows)}</table>

  <h2>5. Risk analysis</h2>
  <table><tr><th>Protein</th><th>Peptide</th><th>Mismatches</th><th>Risk</th></tr>
  {''.join(risk_rows)}
  </table>
</body>
</html>
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    return output_path
