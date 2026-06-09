# NeoTCR-Scout

**NeoTCR-Scout is a reproducible evidence-mining workflow for neoantigen-specific TCR discovery.**

The v0.1 goal is intentionally narrow and useful:

```text
KRAS G12D + HLA-A*11:01
        ↓
generate 8-11mer mutant peptides
        ↓
predict MHC binding with NetMHCpan/MHCflurry when available
        ↓
query VDJdb / IEDB / TCR3D evidence adapters
        ↓
write traceable TSV/JSON artifacts and an HTML candidate-TCR evidence report
```

NeoTCR-Scout is a research workflow platform, not a clinical decision system and not a first-step AI training project. The first version prioritizes reproducibility, provenance, and simple command-line use.

## Quick start

```bash
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```

Expected output directory:

```text
results/kras_g12d/
├── peptides.tsv
├── mhc_binding.tsv
├── tcr_hits.tsv
├── similarity_hits.tsv
├── evidence.json
└── report.html
```

## Input format

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

The parser accepts the small YAML subset needed by v0.1 without requiring PyYAML.

## Five core v0.1 functions

```python
from neotcr_scout import (
    generate_mutant_peptides,
    predict_mhc_binding,
    search_tcr_database,
    rank_tcr_candidates,
    generate_html_report,
)
```

- `generate_mutant_peptides(gene, mutation, wt_sequence, lengths=[8,9,10,11])`
- `predict_mhc_binding(peptides, hla)`
- `search_tcr_database(peptide, hla)`
- `rank_tcr_candidates(results)`
- `generate_html_report(project)`

## Repository layout

```text
NeoTCR-Scout/
├── neotcr_scout/
│   ├── input.py
│   ├── peptide.py
│   ├── mhc_binding.py
│   ├── database/
│   │   ├── vdjdb.py
│   │   ├── iedb.py
│   │   └── tcr3d.py
│   ├── similarity.py
│   ├── scoring.py
│   ├── report.py
│   └── workflow.py
├── examples/
│   ├── kras_g12d_hla_a1101.yaml
│   └── demo_output/
├── data/
│   └── README.md
├── tests/
├── docs/
├── pyproject.toml
├── README.md
└── LICENSE
```


## Third-party MHC binding tools and licenses

This repository is for academic research workflows only. NetMHCpan and MHCflurry are external third-party predictors. NeoTCR-Scout can call them when you provide a licensed/local installation, but it does not grant any rights to use, redistribute, or modify those tools. If you plan to use NetMHCpan or MHCflurry, contact the original authors and comply with their license and citation requirements.

Tool resolution order for `predict_mhc_binding` is:

1. `NEOTCR_SCOUT_NETMHCPAN` exact executable path.
2. `tools/netMHCpan` or `tools/netMHCpan/netMHCpan`.
3. `netMHCpan` / `netmhcpan` on `PATH`.
4. `NEOTCR_SCOUT_MHCFLURRY_PREDICT` exact executable path.
5. `tools/mhcflurry/.../mhcflurry-predict`.
6. `mhcflurry-predict` on `PATH`.
7. deterministic fallback with explicit provenance if no external tool is available.

MHCflurry can be installed from the OpenVax repository: <https://github.com/openvax/mhcflurry>. See `tools/README.md` for local layout examples.

## Database adapters

The v0.1 database layer is deliberately adapter-based:

- `neotcr_scout.database.vdjdb` keeps the VDJdb boundary for local exports containing TCR sequence, epitope, and MHC context.
- `neotcr_scout.database.iedb` keeps the IEDB receptor-query boundary for future programmatic queries.
- `neotcr_scout.database.tcr3d` keeps the structural-evidence boundary for future TCR-pMHC context.

The repository currently includes tiny deterministic seed records only. Production use should replace them with pinned local exports under `data/`, including access dates and checksums.

## Four-week v0.1 implementation priority

1. Week 1: repo skeleton, input parsing, mutant-peptide generation.
2. Week 2: NetMHCpan or MHCflurry adapter hardening and version-pinned parsers.
3. Week 3: download and normalize VDJdb for local search.
4. Week 4: complete HTML report and KRAS G12D demo artifacts.

## Development

```bash
PYTHONPATH=. pytest -q
PYTHONPATH=. python -m neotcr_scout.cli run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d
```
