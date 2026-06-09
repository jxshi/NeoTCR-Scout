# NeoTCR-Scout

> **NeoTCR-Scout: an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.**

NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery. It starts from a cancer mutation and HLA allele, generates traceable mutant peptide candidates, records MHC-I binding evidence or fallback provenance, searches local TCR evidence, scores hits transparently, and writes reproducible TSV, Markdown, and HTML artifacts.

NeoTCR-Scout is **not** a de novo TCR generator and **not** a therapeutic TCR design platform. It does not design TCRs, claim therapeutic safety, or make clinical recommendations.

## Purpose

The purpose of NeoTCR-Scout is to help academic researchers prioritize neoantigen-specific TCR discovery experiments using existing evidence. The workflow is intentionally narrow for v0.1:

```text
mutation + HLA
  -> mutant peptides
  -> MHC binding status/prediction
  -> local VDJdb-style evidence search
  -> transparent evidence scoring
  -> traceable TSV artifacts
  -> Markdown/HTML report
```

## Core user story

Input:

- cancer mutation, e.g. `KRAS G12D`
- HLA allele, e.g. `HLA-A*11:01`
- optional protein sequence

Output:

- candidate neoantigen peptides
- MHC-I binding prediction table
- database/literature evidence for related TCRs
- ranked candidate TCR evidence
- experimental planning suggestions
- Markdown and HTML reports

## Installation

```bash
pip install -e .
```

For full-featured local development with third-party Python libraries, use `pip install -e ".[workflow]"`. The package declares Pydantic for input schema validation and keeps lightweight compatibility fallbacks for Typer, Pandas, and Jinja2 so the demo remains runnable in restricted academic notebook or CI environments.

## Quick start

```bash
neotcr-scout run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

Equivalent module invocation:

```bash
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

## Example output

```text
results/kras_g12d/
├── peptides.tsv
├── mhc_binding.tsv
├── tcr_hits.tsv
├── evidence_score.tsv
├── report.md
└── report.html
```

The core artifacts are:

- `peptides.tsv`: mutation-containing peptide windows with wild-type controls and flanking context.
- `mhc_binding.tsv`: MHC-I binding status or prediction rows with tool/fallback provenance.
- `tcr_hits.tsv`: exact or local evidence hits from configured database adapters.
- `evidence_score.tsv`: rule-based evidence scores with human-readable explanations.
- `report.md` and `report.html`: readable summaries for review and experiment planning.

Additional reproducibility artifacts such as `similarity_hits.tsv`, `similar_mutations.tsv`, and `evidence.json` may also be written.

## Example input

```yaml
project: KRAS_G12D_HLA_A1101
gene: KRAS
mutation: G12D
protein_sequence: MTEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV
hla:
  - HLA-A*11:01
peptide_lengths:
  - 8
  - 9
  - 10
  - 11
```

Input validation normalizes HLA forms such as `HLA-A*11:01`, `A*11:01`, and `HLA-A1101` to a consistent representation.

## Workflow diagram

```text
Project YAML
   ↓
Pydantic input validation
   ↓
Mutation-to-peptide engine
   ↓
NetMHCpan/MHCflurry adapter or explicit fallback
   ↓
VDJdb / IEDB / TCR3D / local evidence adapters
   ↓
Exact, one-mismatch, two-mismatch, Levenshtein, and BLOSUM62 similarity
   ↓
Transparent rule-based evidence scoring
   ↓
Experimental planning suggestions
   ↓
report.md + report.html + TSV artifacts
```

## Project boundaries

The project boundary and milestone plan are defined in `PROJECT_SPEC.md`. Contributors and coding agents should read that file before expanding the implementation. The short version: keep v0.1 focused on mutation + HLA → mutant peptides → MHC binding provenance → local database evidence → evidence scoring → report. Boltz, AlphaFold, docking, and TCR generation are later milestones, not v0.1 requirements.

## Third-party MHC binding tools and licenses

This repository is for academic research workflows only. NetMHCpan and MHCflurry are external third-party predictors. NeoTCR-Scout can call them when you provide a licensed/local installation, but it does not grant any rights to use, redistribute, or modify those tools. If you plan to use NetMHCpan or MHCflurry, contact the original authors and comply with their license and citation requirements.

Tool resolution order for `predict_mhc_binding`:

1. `NEOTCR_SCOUT_NETMHCPAN` exact executable path.
2. `tools/netMHCpan` or `tools/netMHCpan/netMHCpan`.
3. `netMHCpan` / `netmhcpan` on `PATH`.
4. `NEOTCR_SCOUT_MHCFLURRY_PREDICT` exact executable path.
5. `tools/mhcflurry/.../mhcflurry-predict`.
6. `mhcflurry-predict` on `PATH`.
7. deterministic fallback with explicit provenance if no external tool is available.

MHCflurry is available from the OpenVax repository: <https://github.com/openvax/mhcflurry>. See `tools/README.md` for local layout examples.

## Current limitations

- Seed database records are demo fixtures, not a curated production database.
- MHC fallback scores are deterministic placeholders and must not be interpreted as validated binding predictions.
- Database hits do not prove therapeutic safety.
- TCR cross-reactivity must be experimentally tested.
- NeoTCR-Scout is for research prioritization only, not clinical decision-making.

## Roadmap

- **v0.1**: evidence mining, MHC-I binding provenance, local TCR evidence search, similarity, scoring, Markdown/HTML report.
- **v0.5**: pMHC structure modeling and TCR-facing residue annotation.
- **v1.0**: off-target peptide risk explorer and TCR3D structural evidence integration.
- **v2.0**: AI-assisted TCR design research module, clearly separated from discovery/prioritization.

## Citation

NeoTCR-Scout is an orchestration workflow. When using it in research, cite this repository and cite the original resources used by your run, including NetMHCpan, MHCflurry, VDJdb, IEDB, TCR3D, and any downloaded local database snapshots.

Until a formal publication or DOI exists, cite the repository URL and commit hash used for the analysis.

## Development

```bash
pytest
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

## License

NeoTCR-Scout code is released under the MIT License. Third-party tools and datasets retain their own licenses and terms.
