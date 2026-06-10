# NeoTCR-Scout

> **NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.**

NeoTCR-Scout helps academic researchers move from a cancer mutation and HLA allele to traceable neoantigen peptide candidates, MHC-I binding evidence or clearly marked fallback provenance, local TCR evidence hits, transparent evidence scores, and Markdown/HTML reports.

**NeoTCR-Scout is not a de novo TCR generator. It is not a therapeutic TCR design platform.** It does not design TCRs, claim therapeutic efficacy or safety, replace licensed prediction tools, or make clinical recommendations.

## Purpose

NeoTCR-Scout is built for research teams that need a reproducible, evidence-first way to prioritize neoantigen-specific TCR discovery experiments. The v0.1 workflow is intentionally narrow:

```text
mutation + HLA
  -> mutant peptides
  -> MHC binding status/prediction
  -> local VDJdb-style evidence search
  -> transparent evidence scoring
  -> traceable TSV artifacts
  -> Markdown/HTML report
```

Use NeoTCR-Scout when you want to ask:

> Given a mutation and HLA allele, what mutant peptides, MHC binding evidence, and traceable TCR evidence already exist or look similar enough to prioritize follow-up experiments?

Do not use NeoTCR-Scout as a clinical decision system, therapeutic design system, or automated TCR generation system.

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone <repository-url>
cd NeoTCR-Scout
pip install -e .
```

For local workflow development with optional third-party Python libraries, install the workflow extras:

```bash
pip install -e ".[workflow]"
```

The base package depends on Pydantic for input validation. Typer, Pandas, and Jinja2 are optional workflow extras, and lightweight fallbacks keep the demo runnable in restricted academic notebook or CI environments.

## Quick start

Run the canonical KRAS G12D / HLA-A*11:01 demo directly from CLI flags:

```bash
neotcr-scout run --gene KRAS --mutation G12D --hla HLA-A*11:01 --out results/kras_g12d
```

You can also run from a project YAML file:

```bash
neotcr-scout run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

Equivalent module invocation:

```bash
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

## Example input/output

### Example input

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

### Example output

A successful run writes traceable artifacts to the selected output directory:

```text
results/kras_g12d/
├── peptides.tsv
├── mhc_binding.tsv
├── tcr_hits.tsv
├── evidence_score.tsv
├── report.md
└── report.html
```

Core artifacts:

- `peptides.tsv`: mutation-containing peptide windows with wild-type controls and flanking context.
- `mhc_binding.tsv`: MHC-I binding status or prediction rows with tool/fallback provenance.
- `tcr_hits.tsv`: exact or local evidence hits from configured database adapters.
- `evidence_score.tsv`: rule-based evidence scores with human-readable explanations.
- `report.md` and `report.html`: readable summaries for review and experiment planning.

Additional reproducibility artifacts such as `similarity_hits.tsv`, `similar_mutations.tsv`, and `evidence.json` may also be written by current workflow modules.

## Workflow diagram

```text
Project YAML or CLI flags
   ↓
Input validation and HLA normalization
   ↓
Mutation-to-peptide engine
   ↓
NetMHCpan/MHCflurry adapter or explicit fallback provenance
   ↓
VDJdb / IEDB / TCR3D / NeoTCR / local evidence adapters
   ↓
Exact, one-mismatch, two-mismatch, Levenshtein, and BLOSUM62 similarity checks
   ↓
Transparent rule-based evidence scoring
   ↓
Experimental planning suggestions
   ↓
report.md + report.html + TSV/JSON artifacts
```

## Limitations

- NeoTCR-Scout is for academic research prioritization only, not clinical decision-making.
- It does not generate de novo TCR sequences and does not design therapeutic TCR products.
- Seed database records are demo fixtures, not a curated production database.
- MHC fallback scores are deterministic placeholders and must not be interpreted as validated binding predictions.
- Database hits and similarity hits are hypotheses for follow-up; they do not prove antigen recognition, specificity, safety, or therapeutic utility.
- TCR cross-reactivity and functional avidity must be experimentally tested.
- External predictors and databases retain their own licenses, citation requirements, and usage restrictions.

## Third-party MHC binding tools and licenses

This repository is for academic research workflows only. NetMHCpan and MHCflurry are external third-party predictors. NeoTCR-Scout can call them when you provide a licensed/local installation, but it does not grant any rights to use, redistribute, or modify those tools. If you plan to use NetMHCpan or MHCflurry, contact the original authors and comply with their license and citation requirements.

Tool resolution order for `predict_mhc_binding`:

1. `NEOTCR_SCOUT_NETMHCPAN` exact executable path.
2. `tools/netMHCpan` or `tools/netMHCpan/netMHCpan`.
3. `netMHCpan` / `netmhcpan` on `PATH`.
4. `NEOTCR_SCOUT_MHCFLURRY_PREDICT` exact executable path.
5. `tools/mhcflurry/.../mhcflurry-predict`.
6. `mhcflurry-predict` on `PATH`.
7. Deterministic fallback with explicit provenance if no external tool is available.

MHCflurry is available from the OpenVax repository: <https://github.com/openvax/mhcflurry>. See `tools/README.md` for local layout examples.

## Roadmap

- **v0.1**: mutation + HLA input, mutant peptides, MHC-I binding provenance, local TCR evidence search, transparent evidence scoring, TSV artifacts, and Markdown/HTML report.
- **v0.5**: pMHC structure modeling and TCR-facing residue annotation after v0.1 evidence artifacts are stable.
- **v1.0**: off-target peptide risk explorer and deeper TCR3D structural evidence integration.
- **v2.0**: optional AI-assisted TCR design research module, clearly separated from the evidence-guided discovery/prioritization workflow and not part of v0.1.

The project boundary and milestone plan are defined in `PROJECT_SPEC.md`. Contributors should read that file before expanding the implementation. Boltz, AlphaFold, docking, and TCR generation are later milestones, not v0.1 requirements.

## Citation

NeoTCR-Scout is an orchestration workflow. When using it in research, cite this repository and cite the original resources used by your run, including NetMHCpan, MHCflurry, VDJdb, IEDB, TCR3D, NeoTCR-style local curated data, and any downloaded local database snapshots.

Until a formal publication or DOI exists, cite the repository URL and commit hash used for the analysis.

## Development

Run the test suite:

```bash
pytest
```

Run the demo workflow during development:

```bash
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

## License

NeoTCR-Scout code is released under the MIT License. Third-party tools and datasets retain their own licenses and terms.
