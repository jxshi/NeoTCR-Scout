# NeoTCR-Scout roadmap

NeoTCR-Scout is a discovery workflow platform. The first release deliberately avoids model training and instead prioritizes a reproducible rule-based path that can be validated, benchmarked, and extended.

## v0.1

```text
Mutation → Neoantigen → HLA binding → TCR evidence search → HTML report
```

Implementation principles:

- Keep all module boundaries explicit.
- Normalize TCR records into a shared schema.
- Preserve evidence provenance from VDJdb, IEDB, NeoTCR, McPAS-TCR, TCRdb, TCR3D, and literature imports.
- Make external tools optional adapters rather than hard runtime dependencies.

## v0.5

Add pMHC structure prediction adapters for Boltz and AlphaFold3-style workflows, plus peptide/TCR similarity search.

## v1.0

Add risk analysis against a human proteome index, TCR3D structural priors, and docking triage metrics.
