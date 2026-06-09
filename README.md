# NeoTCR-Scout

NeoTCR-Scout is a **research workflow platform** for rule-based neoantigen-to-TCR discovery. The project is intentionally positioned as a workflow platform rather than a static database or a first-generation AI model: databases age, models change, but a reproducible workflow can continue to orchestrate better tools as the field evolves.

> **Current scope:** v0.1 focuses on deterministic, rule-based discovery: mutation → neoantigen candidates → HLA binding evidence → TCR database mining → HTML report.

NeoTCR-Scout is for research triage and hypothesis generation only. It is not a clinical decision system.

## Example

Input:

```yaml
Mutation: KRAS G12D
HLA: HLA-A*11:01
```

Run:

```bash
neotcr-scout run --mutation "KRAS G12D" --hla "HLA-A*11:01" --output report.html
```

Output includes:

```yaml
Candidate_TCRs:
  - TCR1
  - TCR2
  - TCR3
Evidence:
  - VDJdb
  - IEDB
  - NeoTCR
  - Literature
pMHC:
  structure.pdb
Risk:
  off_target_score
Report:
  report.html
```

## Architecture

```text
NeoTCR-Scout
├── Input
├── Neoantigen Engine
├── pMHC Engine
├── TCR Mining Engine
├── Similarity Engine
├── Structural Engine
├── Risk Engine
└── Report Engine
```

## Version roadmap

### v0.1 — rule-based discovery

- Parse mutation and HLA input.
- Generate mutation-centered 8-11mer peptide windows.
- Estimate HLA binding with a deterministic rule-based scorer or imported predictor output.
- Mine normalized TCR evidence from local database snapshots.
- Generate a portable HTML report.

### v0.5 — structure-aware discovery

- Add Boltz / AlphaFold3 adapters for pMHC structure prediction.
- Compute peptide residue exposure and TCR-facing residue summaries.
- Add TCR and epitope similarity search.

### v1.0 — risk and docking triage

- Integrate TCR3D-derived structural evidence.
- Add human-proteome off-target peptide search.
- Add docking/interface metrics for prioritized candidates.

### v2.0 — design research track

- Evaluate peptide-to-TCR generation only after the discovery workflow is stable and benchmarked.

## Repository layout

```text
neotcr_scout/
  neoantigen/   # mutation parsing and peptide window generation
  pmhc/         # HLA binding and pMHC structure adapters
  mining/       # normalized TCR evidence loading/search
  similarity/   # sequence similarity scoring
  structure/    # structural triage placeholders/adapters
  risk/         # off-target risk screening
  report/       # report rendering
database/       # small seed data and future database snapshots
examples/       # runnable examples
notebooks/      # exploratory notebooks
docs/           # platform and roadmap docs
tests/          # regression tests
```

## Development

```bash
python -m pip install -e '.[dev]'
pytest
```
