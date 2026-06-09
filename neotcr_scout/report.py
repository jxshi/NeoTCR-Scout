"""Markdown and HTML report writers for NeoTCR-Scout v0.1."""

from __future__ import annotations

from html import escape
from pathlib import Path

try:  # pragma: no cover - optional dependency path
    from jinja2 import Template
except Exception:  # pragma: no cover - minimal environment fallback
    Template = None  # type: ignore[assignment]

LIMITATIONS = [
    "Database hits do not prove therapeutic safety.",
    "TCR cross-reactivity must be experimentally tested.",
    "NeoTCR-Scout is for research prioritization only, not clinical decision-making.",
]

EXPERIMENTS = [
    "synthesize top mutant peptide",
    "synthesize matched wild-type peptide as control",
    "generate HLA-peptide tetramer",
    "screen TCR-positive T cells or candidate TCRs",
    "perform peptide titration assay",
    "perform cross-reactivity panel",
]


def generate_markdown_report(project: dict, output_path: str | Path | None = None) -> Path:
    """Generate a practical Markdown evidence report."""

    out = Path(output_path or project["output_dir"] / "report.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    top_peptides = sorted(project["mhc_binding"], key=lambda row: float(row["rank_percent"]))[:5]
    lines = [
        f"# NeoTCR-Scout report: {project['project']}",
        "",
        "## 1. Project summary",
        "NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.",
        "It is not a de novo TCR generator or therapeutic TCR design platform.",
        "",
        "## 2. Input mutation and HLA",
        f"- Gene: `{project['gene']}`",
        f"- Mutation: `{project['mutation']}`",
        f"- HLA: `{', '.join(project['hla'])}`",
        "",
        "## 3. Generated neoantigen peptides",
        _markdown_table(project["peptides"], ["mutant_peptide", "wildtype_peptide", "length", "mutation_index", "flanking_context"]),
        "",
        "## 4. MHC binding prediction summary",
        _markdown_table(project["mhc_binding"], ["peptide", "hla", "rank_percent", "binder", "method"]),
        "",
        "## 5. Exact TCR database hits",
        _markdown_table(project["exact_hits"], ["identifier", "source", "epitope", "hla", "tra_cdr3", "trb_cdr3"]),
        "",
        "## 6. Similar peptide / related mutation hits",
        _markdown_table(project["similarity_hits"], ["query_peptide", "matched_epitope", "distance", "similarity_score", "same_hla", "source"]),
        "",
        "## 7. Evidence score table",
        _markdown_table(project["tcr_candidates"], ["identifier", "source", "epitope", "raw_score", "score_category", "explanation"]),
        "",
        "## 8. Experimental planning suggestions",
    ]
    for rank, row in enumerate(top_peptides, start=1):
        peptide = row["peptide"]
        peptide_record = next((item for item in project["peptides"] if item["mutant_peptide"] == peptide), {})
        lines.extend(
            [
                f"### Priority peptide {rank}: `{peptide}`",
                f"- Mutant peptide: `{peptide}`",
                f"- Wild-type control peptide: `{peptide_record.get('wildtype_peptide', 'not available')}`",
                f"- HLA: `{row['hla']}`",
                f"- Reason: binding rank {row['rank_percent']} by {row['method']} and available evidence search context.",
            ]
        )
    lines.append("")
    lines.append("Suggested next experiments:")
    lines.extend(f"- {experiment}" for experiment in EXPERIMENTS)
    lines.extend(["", "## 9. Limitations and warnings"])
    lines.extend(f"- {item}" for item in LIMITATIONS)
    lines.extend(["", f"Third-party tool notice: {project.get('third_party_tool_notice', 'Users are responsible for third-party tool licenses.')}"])
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def generate_html_report(project: dict, output_path: str | Path | None = None) -> Path:
    """Generate an HTML report with the same v0.1 sections as the Markdown report."""

    out = Path(output_path or project["output_dir"] / "report.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    markdown_path = generate_markdown_report(project, project.get("markdown_report") or out.with_suffix(".md"))
    markdown = markdown_path.read_text(encoding="utf-8")
    html_body = _markdown_to_simple_html(markdown)
    html = f"<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\"><title>{escape(project['project'])}</title>"
    html += "<style>body{font-family:system-ui,sans-serif;margin:2rem;color:#1f2937}table{border-collapse:collapse;width:100%;margin:1rem 0 2rem}th,td{border:1px solid #d1d5db;padding:.45rem;text-align:left;vertical-align:top}th{background:#f3f4f6}code{background:#f3f4f6;padding:.1rem .25rem}</style>"
    html += f"</head><body>{html_body}</body></html>\n"
    out.write_text(html, encoding="utf-8")
    return out


def _markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    if not rows:
        return "No records found."
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join(lines)


def _markdown_to_simple_html(markdown: str) -> str:
    html_lines: list[str] = []
    in_table = False
    for line in markdown.splitlines():
        if line.startswith("| ") and line.endswith(" |"):
            cells = [escape(cell.strip()) for cell in line.strip("|").split("|")]
            if all(set(cell) <= {"-", " "} for cell in cells):
                continue
            tag = "th" if not in_table else "td"
            if not in_table:
                html_lines.append("<table>")
                in_table = True
            html_lines.append("<tr>" + "".join(f"<{tag}>{cell}</{tag}>" for cell in cells) + "</tr>")
            continue
        if in_table:
            html_lines.append("</table>")
            in_table = False
        if line.startswith("### "):
            html_lines.append(f"<h3>{escape(line[4:])}</h3>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("# "):
            html_lines.append(f"<h1>{escape(line[2:])}</h1>")
        elif line.startswith("- "):
            html_lines.append(f"<p>• {escape(line[2:])}</p>")
        elif line:
            html_lines.append(f"<p>{escape(line)}</p>")
    if in_table:
        html_lines.append("</table>")
    return "\n".join(html_lines)
