# NeoTCR-Scout roadmap

NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization. It is not a de novo TCR generator, therapeutic TCR design platform, or clinical decision system.

## v0.1: evidence mining and report

Acceptance criteria:

- `neotcr-scout run examples/kras_g12d_hla_a1101.yaml --out results/kras_g12d` works.
- Outputs include `peptides.tsv`, `mhc_binding.tsv`, `tcr_hits.tsv`, `evidence_score.tsv`, `report.md`, and `report.html`.
- Input schema validates mutation format, normalizes HLA alleles, and defaults peptide lengths to 8-11.
- Peptide outputs include mutant peptide, wild-type peptide, mutation index, and flanking context.
- Similarity outputs include exact/one-mismatch/two-mismatch/Levenshtein/BLOSUM62 evidence.
- Scoring is transparent and rule-based.
- Reports include experimental planning suggestions and limitations.

## v0.5: structure-aware pMHC prioritization

- pMHC structure modeling.
- TCR-facing residue annotation.
- Structure-aware report section.

## v1.0: risk and structural evidence explorer

- Off-target peptide risk explorer.
- TCR3D structural evidence integration.
- Better local database import/normalization workflows.

## v2.0: AI-assisted TCR design research module

Any AI-assisted design work must remain a separate research module with clear warnings and validation requirements.

## Academic-use license note

NetMHCpan and MHCflurry remain third-party tools; users must contact the original authors and follow applicable license, citation, and redistribution terms before using either predictor.
