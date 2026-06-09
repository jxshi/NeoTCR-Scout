# NeoTCR-Scout report: KRAS_G12V_HLA_A0301

## 1. Project summary
NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.
It is not a de novo TCR generator or therapeutic TCR design platform.

## 2. Input mutation and HLA
- Gene: `KRAS`
- Mutation: `G12V`
- HLA: `HLA-A*03:01`

## 3. Generated neoantigen peptides
| mutant_peptide | wildtype_peptide | length | mutation_index | flanking_context |
| --- | --- | --- | --- | --- |
| KLVVVGAV | KLVVVGAG | 8 | 7 | TEYKLVVVGAVGVG |
| LVVVGAVG | LVVVGAGG | 8 | 6 | EYKLVVVGAVGVGK |
| VVVGAVGV | VVVGAGGV | 8 | 5 | YKLVVVGAVGVGKS |
| VVGAVGVG | VVGAGGVG | 8 | 4 | KLVVVGAVGVGKSA |
| VGAVGVGK | VGAGGVGK | 8 | 3 | LVVVGAVGVGKSAL |
| GAVGVGKS | GAGGVGKS | 8 | 2 | VVVGAVGVGKSALT |
| AVGVGKSA | AGGVGKSA | 8 | 1 | VVGAVGVGKSALTI |
| VGVGKSAL | GGVGKSAL | 8 | 0 | VGAVGVGKSALTIQ |
| YKLVVVGAV | YKLVVVGAG | 9 | 8 | MTEYKLVVVGAVGVG |
| KLVVVGAVG | KLVVVGAGG | 9 | 7 | TEYKLVVVGAVGVGK |
| LVVVGAVGV | LVVVGAGGV | 9 | 6 | EYKLVVVGAVGVGKS |
| VVVGAVGVG | VVVGAGGVG | 9 | 5 | YKLVVVGAVGVGKSA |
| VVGAVGVGK | VVGAGGVGK | 9 | 4 | KLVVVGAVGVGKSAL |
| VGAVGVGKS | VGAGGVGKS | 9 | 3 | LVVVGAVGVGKSALT |
| GAVGVGKSA | GAGGVGKSA | 9 | 2 | VVVGAVGVGKSALTI |
| AVGVGKSAL | AGGVGKSAL | 9 | 1 | VVGAVGVGKSALTIQ |
| VGVGKSALT | GGVGKSALT | 9 | 0 | VGAVGVGKSALTIQL |
| EYKLVVVGAV | EYKLVVVGAG | 10 | 9 | MTEYKLVVVGAVGVG |
| YKLVVVGAVG | YKLVVVGAGG | 10 | 8 | MTEYKLVVVGAVGVGK |
| KLVVVGAVGV | KLVVVGAGGV | 10 | 7 | TEYKLVVVGAVGVGKS |
| LVVVGAVGVG | LVVVGAGGVG | 10 | 6 | EYKLVVVGAVGVGKSA |
| VVVGAVGVGK | VVVGAGGVGK | 10 | 5 | YKLVVVGAVGVGKSAL |
| VVGAVGVGKS | VVGAGGVGKS | 10 | 4 | KLVVVGAVGVGKSALT |
| VGAVGVGKSA | VGAGGVGKSA | 10 | 3 | LVVVGAVGVGKSALTI |
| GAVGVGKSAL | GAGGVGKSAL | 10 | 2 | VVVGAVGVGKSALTIQ |
| AVGVGKSALT | AGGVGKSALT | 10 | 1 | VVGAVGVGKSALTIQL |
| VGVGKSALTI | GGVGKSALTI | 10 | 0 | VGAVGVGKSALTIQLI |
| TEYKLVVVGAV | TEYKLVVVGAG | 11 | 10 | MTEYKLVVVGAVGVG |
| EYKLVVVGAVG | EYKLVVVGAGG | 11 | 9 | MTEYKLVVVGAVGVGK |
| YKLVVVGAVGV | YKLVVVGAGGV | 11 | 8 | MTEYKLVVVGAVGVGKS |
| KLVVVGAVGVG | KLVVVGAGGVG | 11 | 7 | TEYKLVVVGAVGVGKSA |
| LVVVGAVGVGK | LVVVGAGGVGK | 11 | 6 | EYKLVVVGAVGVGKSAL |
| VVVGAVGVGKS | VVVGAGGVGKS | 11 | 5 | YKLVVVGAVGVGKSALT |
| VVGAVGVGKSA | VVGAGGVGKSA | 11 | 4 | KLVVVGAVGVGKSALTI |
| VGAVGVGKSAL | VGAGGVGKSAL | 11 | 3 | LVVVGAVGVGKSALTIQ |
| GAVGVGKSALT | GAGGVGKSALT | 11 | 2 | VVVGAVGVGKSALTIQL |
| AVGVGKSALTI | AGGVGKSALTI | 11 | 1 | VVGAVGVGKSALTIQLI |
| VGVGKSALTIQ | GGVGKSALTIQ | 11 | 0 | VGAVGVGKSALTIQLIQ |

## 4. MHC binding prediction summary
| peptide | hla | rank_percent | binder | method |
| --- | --- | --- | --- | --- |
| KLVVVGAV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| LVVVGAVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VVVGAVGV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VVGAVGVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VGAVGVGK | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| GAVGVGKS | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AVGVGKSA | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VGVGKSAL | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGAV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGAVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| LVVVGAVGV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VVVGAVGVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VVGAVGVGK | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VGAVGVGKS | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| GAVGVGKSA | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AVGVGKSAL | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VGVGKSALT | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| EYKLVVVGAV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGAVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGAVGV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| LVVVGAVGVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VVVGAVGVGK | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VVGAVGVGKS | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VGAVGVGKSA | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| GAVGVGKSAL | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| AVGVGKSALT | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VGVGKSALTI | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| TEYKLVVVGAV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| EYKLVVVGAVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGAVGV | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGAVGVG | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| LVVVGAVGVGK | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VVVGAVGVGKS | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VVGAVGVGKSA | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| VGAVGVGKSAL | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| GAVGVGKSALT | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AVGVGKSALTI | HLA-A*03:01 | 4.1 | non-binder | rule-based-fallback-v0.1 |
| VGVGKSALTIQ | HLA-A*03:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |

## 5. Exact TCR database hits
No records found.

## 6. Similar peptide / related mutation hits
No records found.

## 7. Evidence score table
No records found.

## 8. Experimental planning suggestions
### Priority peptide 1: `KLVVVGAV`
- Mutant peptide: `KLVVVGAV`
- Wild-type control peptide: `KLVVVGAG`
- HLA: `HLA-A*03:01`
- Reason: binding rank 4.1 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 2: `VVVGAVGV`
- Mutant peptide: `VVVGAVGV`
- Wild-type control peptide: `VVVGAGGV`
- HLA: `HLA-A*03:01`
- Reason: binding rank 4.1 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 3: `VGAVGVGK`
- Mutant peptide: `VGAVGVGK`
- Wild-type control peptide: `VGAGGVGK`
- HLA: `HLA-A*03:01`
- Reason: binding rank 4.1 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 4: `VGVGKSAL`
- Mutant peptide: `VGVGKSAL`
- Wild-type control peptide: `GGVGKSAL`
- HLA: `HLA-A*03:01`
- Reason: binding rank 4.1 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 5: `YKLVVVGAV`
- Mutant peptide: `YKLVVVGAV`
- Wild-type control peptide: `YKLVVVGAG`
- HLA: `HLA-A*03:01`
- Reason: binding rank 4.1 by rule-based-fallback-v0.1 and available evidence search context.

Suggested next experiments:
- synthesize top mutant peptide
- synthesize matched wild-type peptide as control
- generate HLA-peptide tetramer
- screen TCR-positive T cells or candidate TCRs
- perform peptide titration assay
- perform cross-reactivity panel

## 9. Limitations and warnings
- Database hits do not prove therapeutic safety.
- TCR cross-reactivity must be experimentally tested.
- NeoTCR-Scout is for research prioritization only, not clinical decision-making.

Third-party tool notice: Academic-use workflow notice: NetMHCpan and MHCflurry are external tools. Before using either predictor, contact the original authors and comply with their licenses and citation requirements.
