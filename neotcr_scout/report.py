"""v0.1 traceable HTML report writer."""

from __future__ import annotations

from html import escape
from pathlib import Path


def generate_html_report(project: dict, output_path: str | Path | None = None) -> Path:
    """Generate the v0.1 evidence report from a project result dictionary."""

    out = Path(output_path or project["output_dir"] / "report.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    peptides = "".join(
        f"<tr><td>{escape(row['sequence'])}</td><td>{row['length']}</td><td>{row['start']}-{row['end']}</td><td>{escape(row['sequence_context'])}</td></tr>"
        for row in project["peptides"]
    )
    bindings = "".join(
        f"<tr><td>{escape(row['peptide'])}</td><td>{escape(row['hla'])}</td><td>{row['rank_percent']}</td><td>{escape(row['binder'])}</td><td>{escape(row['method'])}</td></tr>"
        for row in project["mhc_binding"]
    )
    candidates = "".join(
        f"<tr><td>{escape(row['identifier'])}</td><td>{escape(row['source'])}</td><td>{escape(row['epitope'])}</td><td>{escape(str(row['hla']))}</td><td>{row['similarity']}</td><td>{row['score']}</td><td>{escape(row.get('evidence') or '')}</td></tr>"
        for row in project["tcr_candidates"]
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>NeoTCR-Scout v0.1 report - {escape(project['project'])}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #1f2937; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1rem 0 2rem; }}
    th, td {{ border: 1px solid #d1d5db; padding: 0.45rem; text-align: left; vertical-align: top; }}
    th {{ background: #f3f4f6; }}
    code {{ background: #f3f4f6; padding: 0.15rem 0.3rem; }}
  </style>
</head>
<body>
  <h1>NeoTCR-Scout v0.1 evidence report</h1>
  <p><strong>Project:</strong> {escape(project['project'])}</p>
  <p><strong>Input:</strong> {escape(project['gene'])} {escape(project['mutation'])}; HLA {escape(', '.join(project['hla']))}</p>
  <p><strong>Scope:</strong> reproducible evidence mining for neoantigen-specific TCR discovery. This is a research report, not a clinical recommendation.</p>
  <p><strong>Third-party tool notice:</strong> {escape(project.get('third_party_tool_notice', 'Users are responsible for third-party tool licenses.'))}</p>

  <h2>1. Mutant peptides</h2>
  <table><tr><th>Peptide</th><th>Length</th><th>Protein positions</th><th>Input context</th></tr>{peptides}</table>

  <h2>2. MHC binding predictions</h2>
  <table><tr><th>Peptide</th><th>HLA</th><th>Rank %</th><th>Binder</th><th>Method</th></tr>{bindings}</table>

  <h2>3. Candidate TCR evidence</h2>
  <table><tr><th>ID</th><th>Source</th><th>Known epitope</th><th>HLA</th><th>Similarity</th><th>Score</th><th>Evidence</th></tr>{candidates}</table>

  <h2>4. Reproducibility artifacts</h2>
  <ul>
    <li><code>peptides.tsv</code></li>
    <li><code>mhc_binding.tsv</code></li>
    <li><code>tcr_hits.tsv</code></li>
    <li><code>similarity_hits.tsv</code></li>
    <li><code>evidence.json</code></li>
  </ul>
</body>
</html>
"""
    out.write_text(html, encoding="utf-8")
    return out
