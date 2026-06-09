# NeoTCR-Scout Agent Instructions

These instructions apply to the entire repository.

## Project mission

NeoTCR-Scout is an academic research workflow for neoantigen-specific TCR discovery and prioritization.

It is not a TCR generator, therapeutic design platform, clinical decision system, or AI model-training project.

## Current priority

Keep v0.1 narrow:

```text
mutation + HLA
  -> mutant peptides
  -> MHC binding status/prediction
  -> local VDJdb-style evidence search
  -> transparent evidence scoring
  -> traceable TSV artifacts
  -> Markdown/HTML report
```

Do not add AlphaFold, Boltz, docking, or TCR generation code to v0.1 unless the user explicitly asks for that milestone.

## Architecture expectations

- Prefer small interfaces over large coupled modules.
- Preserve provenance for every generated row and report section.
- Keep external tools as optional adapters.
- If NetMHCpan or MHCflurry is used, preserve the academic-use/license notice and do not imply this repo grants tool licenses.
- Favor deterministic tests with fake tool executables or local fixtures over tests requiring network access.

## Documentation expectations

When changing scope or behavior, update `PROJECT_SPEC.md` first, then code/docs/tests.

## v0.1 release gate

The canonical release demo is:

```bash
neotcr-scout run --gene KRAS --mutation G12D --hla HLA-A*11:01
```

Minimum release artifacts:

```text
results/
├── peptides.tsv
├── mhc_binding.tsv
├── tcr_hits.tsv
├── evidence_score.tsv
├── report.md
└── report.html
```
