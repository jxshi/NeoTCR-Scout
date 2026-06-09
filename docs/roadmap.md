# NeoTCR-Scout v0.1 roadmap

NeoTCR-Scout starts as a small, reproducible discovery workflow:

```text
input mutation + HLA → mutant peptides → MHC binding → TCR evidence search → HTML report
```

## v0.1 acceptance criteria

- Accept `examples/kras_g12d_hla_a1101.yaml` as the canonical demo input.
- Generate 8-11mer KRAS G12D mutant peptides.
- Use NetMHCpan/MHCflurry if installed under `tools/`, configured by environment variable, or available on `PATH`; otherwise write an explicit fallback method into provenance.
- Search VDJdb, IEDB, and TCR3D adapter boundaries.
- Write `peptides.tsv`, `mhc_binding.tsv`, `tcr_hits.tsv`, `similarity_hits.tsv`, `evidence.json`, and `report.html`.

## Why not Boltz/AlphaFold/docking in v0.1?

The first useful milestone is a traceable evidence report. Structure prediction and docking are valuable, but they should not block the minimal workflow. They belong after the input, binding, database normalization, and reporting interfaces are stable.

## Near-term plan

1. Harden input validation and add more mutation examples.
2. Add version-pinned NetMHCpan/MHCflurry output parsers.
3. Normalize a dated VDJdb export into local searchable TSV/JSON.
4. Add IEDB Query API integration behind the existing adapter boundary.
5. Add TCR3D structural provenance tables after the evidence report is stable.

## Academic-use license note

NeoTCR-Scout is intended for academic research workflows. NetMHCpan and MHCflurry remain third-party tools; users must contact the original authors and follow the applicable license, citation, and redistribution terms before using either predictor.
