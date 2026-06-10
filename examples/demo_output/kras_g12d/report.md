# NeoTCR-Scout report: KRAS_G12D_HLA_A1101

## 1. Project summary
NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.
It is not a de novo TCR generator or therapeutic TCR design platform.

## 2. Input mutation & HLA
- Gene: `KRAS`
- Mutation: `G12D`
- HLA: `HLA-A*11:01`

## 3. Generated neoantigen peptides
| mutant_peptide | wildtype_peptide | length | mutation_index | flanking_context |
| --- | --- | --- | --- | --- |
| KLVVVGAD | KLVVVGAG | 8 | 7 | TEYKLVVVGADGVG |
| LVVVGADG | LVVVGAGG | 8 | 6 | EYKLVVVGADGVGK |
| VVVGADGV | VVVGAGGV | 8 | 5 | YKLVVVGADGVGKS |
| VVGADGVG | VVGAGGVG | 8 | 4 | KLVVVGADGVGKSA |
| VGADGVGK | VGAGGVGK | 8 | 3 | LVVVGADGVGKSAL |
| GADGVGKS | GAGGVGKS | 8 | 2 | VVVGADGVGKSALT |
| ADGVGKSA | AGGVGKSA | 8 | 1 | VVGADGVGKSALTI |
| DGVGKSAL | GGVGKSAL | 8 | 0 | VGADGVGKSALTIQ |
| YKLVVVGAD | YKLVVVGAG | 9 | 8 | MTEYKLVVVGADGVG |
| KLVVVGADG | KLVVVGAGG | 9 | 7 | TEYKLVVVGADGVGK |
| LVVVGADGV | LVVVGAGGV | 9 | 6 | EYKLVVVGADGVGKS |
| VVVGADGVG | VVVGAGGVG | 9 | 5 | YKLVVVGADGVGKSA |
| VVGADGVGK | VVGAGGVGK | 9 | 4 | KLVVVGADGVGKSAL |
| VGADGVGKS | VGAGGVGKS | 9 | 3 | LVVVGADGVGKSALT |
| GADGVGKSA | GAGGVGKSA | 9 | 2 | VVVGADGVGKSALTI |
| ADGVGKSAL | AGGVGKSAL | 9 | 1 | VVGADGVGKSALTIQ |
| DGVGKSALT | GGVGKSALT | 9 | 0 | VGADGVGKSALTIQL |
| EYKLVVVGAD | EYKLVVVGAG | 10 | 9 | MTEYKLVVVGADGVG |
| YKLVVVGADG | YKLVVVGAGG | 10 | 8 | MTEYKLVVVGADGVGK |
| KLVVVGADGV | KLVVVGAGGV | 10 | 7 | TEYKLVVVGADGVGKS |
| LVVVGADGVG | LVVVGAGGVG | 10 | 6 | EYKLVVVGADGVGKSA |
| VVVGADGVGK | VVVGAGGVGK | 10 | 5 | YKLVVVGADGVGKSAL |
| VVGADGVGKS | VVGAGGVGKS | 10 | 4 | KLVVVGADGVGKSALT |
| VGADGVGKSA | VGAGGVGKSA | 10 | 3 | LVVVGADGVGKSALTI |
| GADGVGKSAL | GAGGVGKSAL | 10 | 2 | VVVGADGVGKSALTIQ |
| ADGVGKSALT | AGGVGKSALT | 10 | 1 | VVGADGVGKSALTIQL |
| DGVGKSALTI | GGVGKSALTI | 10 | 0 | VGADGVGKSALTIQLI |
| TEYKLVVVGAD | TEYKLVVVGAG | 11 | 10 | MTEYKLVVVGADGVG |
| EYKLVVVGADG | EYKLVVVGAGG | 11 | 9 | MTEYKLVVVGADGVGK |
| YKLVVVGADGV | YKLVVVGAGGV | 11 | 8 | MTEYKLVVVGADGVGKS |
| KLVVVGADGVG | KLVVVGAGGVG | 11 | 7 | TEYKLVVVGADGVGKSA |
| LVVVGADGVGK | LVVVGAGGVGK | 11 | 6 | EYKLVVVGADGVGKSAL |
| VVVGADGVGKS | VVVGAGGVGKS | 11 | 5 | YKLVVVGADGVGKSALT |
| VVGADGVGKSA | VVGAGGVGKSA | 11 | 4 | KLVVVGADGVGKSALTI |
| VGADGVGKSAL | VGAGGVGKSAL | 11 | 3 | LVVVGADGVGKSALTIQ |
| GADGVGKSALT | GAGGVGKSALT | 11 | 2 | VVVGADGVGKSALTIQL |
| ADGVGKSALTI | AGGVGKSALTI | 11 | 1 | VVGADGVGKSALTIQLI |
| DGVGKSALTIQ | GGVGKSALTIQ | 11 | 0 | VGADGVGKSALTIQLIQ |

## 4. MHC binding summary
| peptide | hla | rank_percent | binder | method |
| --- | --- | --- | --- | --- |
| KLVVVGAD | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| LVVVGADG | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| VVVGADGV | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| VVGADGVG | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| VGADGVGK | HLA-A*11:01 | 2.8 | non-binder | rule-based-fallback-v0.1 |
| GADGVGKS | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| ADGVGKSA | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| DGVGKSAL | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGAD | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGADG | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| LVVVGADGV | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| VVVGADGVG | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| VVGADGVGK | HLA-A*11:01 | 0.8 | weak | rule-based-fallback-v0.1 |
| VGADGVGKS | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| GADGVGKSA | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| ADGVGKSAL | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| DGVGKSALT | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| EYKLVVVGAD | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGADG | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGADGV | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| LVVVGADGVG | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| VVVGADGVGK | HLA-A*11:01 | 0.8 | weak | rule-based-fallback-v0.1 |
| VVGADGVGKS | HLA-A*11:01 | 2.7 | non-binder | rule-based-fallback-v0.1 |
| VGADGVGKSA | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| GADGVGKSAL | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| ADGVGKSALT | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| DGVGKSALTI | HLA-A*11:01 | 3.4 | non-binder | rule-based-fallback-v0.1 |
| TEYKLVVVGAD | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| EYKLVVVGADG | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| YKLVVVGADGV | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| KLVVVGADGVG | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| LVVVGADGVGK | HLA-A*11:01 | 2.1 | non-binder | rule-based-fallback-v0.1 |
| VVVGADGVGKS | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| VVGADGVGKSA | HLA-A*11:01 | 4.0 | non-binder | rule-based-fallback-v0.1 |
| VGADGVGKSAL | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| GADGVGKSALT | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| ADGVGKSALTI | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |
| DGVGKSALTIQ | HLA-A*11:01 | 4.7 | non-binder | rule-based-fallback-v0.1 |

## 5. Exact TCR database hits
| identifier | source | epitope | hla | tra_cdr3 | trb_cdr3 |
| --- | --- | --- | --- | --- | --- |
| VDJDB-KRAS-G12D-001 | VDJdb | VVGADGVGK | HLA-A*11:01 | CAVNNNDMRF | CASSIRSSYEQYF |
| NEOTCR-KRAS-G12D-001 | NeoTCR | VVVGADGVGK | HLA-A*11:01 | CAVRNNARLMF | CASSLAPGATNEKLFF |

## 6. Similar peptide / related mutation hits
### Similar peptide evidence
| query_peptide | matched_epitope | distance | similarity_score | mutation_site_match | same_hla | source |
| --- | --- | --- | --- | --- | --- | --- |
| VVVGADGVGK | VVVGADGVGK | 0 | 1.0 | yes | yes | NeoTCR |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | yes | IEDB |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | yes | VDJdb |
| VVVGADGVGKS | VVVGADGVGK | 1 | 0.909 | yes | yes | NeoTCR |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | yes | IEDB |
| LVVVGADGVGK | VVVGADGVGK | 1 | 0.909 | no | yes | NeoTCR |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | no | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | yes | IEDB |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | yes | VDJdb |
| VVVGADGVG | VVVGADGVGK | 1 | 0.9 | yes | yes | NeoTCR |
| VVVGADGVGK | VVVGAVGVGK | 1 | 0.9 | no | yes | VDJdb |
| VVVGADGVGK | VVVGACGVGK | 1 | 0.9 | no | yes | TCR3D |
| VVVGADGVGK | VVVGACGVGK | 1 | 0.9 | no | yes | TCR3D |
| VVGADGVGK | VVVGADGVGK | 1 | 0.9 | no | yes | NeoTCR |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | no | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | no | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | no | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | no | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | no | yes | VDJdb |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | no | yes | IEDB |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | no | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | no | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | no | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | no | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | no | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | yes | VDJdb |
| VVVGADGVGKS | VVVGAVGVGK | 2 | 0.818 | no | yes | VDJdb |
| VVVGADGVGKS | VVVGACGVGK | 2 | 0.818 | no | yes | TCR3D |
| VVVGADGVGKS | VVVGACGVGK | 2 | 0.818 | no | yes | TCR3D |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVVGAVGVGK | 2 | 0.818 | no | yes | VDJdb |
| LVVVGADGVGK | VVVGACGVGK | 2 | 0.818 | no | yes | TCR3D |
| LVVVGADGVGK | VVVGACGVGK | 2 | 0.818 | no | yes | TCR3D |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | no | yes | VDJdb |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | yes | IEDB |
| VVVGADGVG | VVVGAVGVGK | 2 | 0.8 | no | yes | VDJdb |
| VVVGADGVG | VVVGACGVGK | 2 | 0.8 | no | yes | TCR3D |
| VVVGADGVG | VVVGACGVGK | 2 | 0.8 | no | yes | TCR3D |
| VVVGADGV | VVVGADGVGK | 2 | 0.8 | yes | yes | NeoTCR |
| LVVVGADGVG | VVVGADGVGK | 2 | 0.8 | no | yes | NeoTCR |
| VVGADGVGKS | VVVGADGVGK | 2 | 0.8 | no | yes | NeoTCR |
| VGADGVGK | VVVGADGVGK | 2 | 0.8 | no | yes | NeoTCR |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VVGADGVG | VVVGADGVGK | 2 | 0.8 | no | yes | NeoTCR |
| VVGADGVGK | VVVGAVGVGK | 2 | 0.8 | no | yes | VDJdb |
| VVGADGVGK | VVVGACGVGK | 2 | 0.8 | no | yes | TCR3D |
| VVGADGVGK | VVVGACGVGK | 2 | 0.8 | no | yes | TCR3D |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | no | yes | IEDB |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | no | yes | VDJdb |
| KLVVVGADGVG | VVVGADGVGK | 3 | 0.727 | no | yes | NeoTCR |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | VVVGADGVGK | 3 | 0.727 | no | yes | NeoTCR |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | no | yes | IEDB |
| VVVGADGV | VVVGAVGVGK | 3 | 0.7 | no | yes | VDJdb |
| VVVGADGV | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VVVGADGV | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VGADGVGK | VVVGAVGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKS | VVVGADGVGK | 3 | 0.7 | no | yes | NeoTCR |
| LVVVGADGVG | VVVGAVGVGK | 3 | 0.7 | no | yes | VDJdb |
| LVVVGADGVG | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| LVVVGADGVG | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VGADGVGK | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VGADGVGK | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| LVVVGADGV | VVVGADGVGK | 3 | 0.7 | no | yes | NeoTCR |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VVGADGVGKS | VVVGAVGVGK | 3 | 0.7 | no | yes | VDJdb |
| VVGADGVGKS | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VVGADGVGKS | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VVGADGVG | VVVGAVGVGK | 3 | 0.7 | no | yes | VDJdb |
| VVGADGVG | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VVGADGVG | VVVGACGVGK | 3 | 0.7 | no | yes | TCR3D |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | no | yes | VDJdb |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | no | yes | IEDB |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | no | yes | VDJdb |
| KLVVVGADGVG | VVVGAVGVGK | 4 | 0.636 | no | yes | VDJdb |
| KLVVVGADGVG | VVVGACGVGK | 4 | 0.636 | no | yes | TCR3D |
| KLVVVGADGVG | VVVGACGVGK | 4 | 0.636 | no | yes | TCR3D |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VVGADGVGKSA | VVVGAVGVGK | 4 | 0.636 | no | yes | VDJdb |
| VVGADGVGKSA | VVVGACGVGK | 4 | 0.636 | no | yes | TCR3D |
| VVGADGVGKSA | VVVGACGVGK | 4 | 0.636 | no | yes | TCR3D |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | no | yes | VDJdb |
| VGADGVGKS | VVVGAVGVGK | 4 | 0.6 | no | yes | VDJdb |
| KLVVVGADGV | VVVGADGVGK | 4 | 0.6 | no | yes | NeoTCR |
| VGADGVGKSA | VVVGADGVGK | 4 | 0.6 | no | yes | NeoTCR |
| VGADGVGKS | VVVGACGVGK | 4 | 0.6 | no | yes | TCR3D |
| VGADGVGKS | VVVGACGVGK | 4 | 0.6 | no | yes | TCR3D |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| LVVVGADGV | VVVGAVGVGK | 4 | 0.6 | no | yes | VDJdb |
| LVVVGADGV | VVVGACGVGK | 4 | 0.6 | no | yes | TCR3D |
| LVVVGADGV | VVVGACGVGK | 4 | 0.6 | no | yes | TCR3D |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| LVVVGADG | VVVGADGVGK | 4 | 0.6 | no | yes | NeoTCR |
| GADGVGKS | VVVGADGVGK | 4 | 0.6 | no | yes | NeoTCR |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | no | yes | IEDB |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | no | yes | VDJdb |
| VGADGVGKSAL | VVVGADGVGK | 5 | 0.545 | no | yes | NeoTCR |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| YKLVVVGADGV | VVVGADGVGK | 5 | 0.545 | no | yes | NeoTCR |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | no | yes | IEDB |
| VGADGVGKSA | VVVGAVGVGK | 5 | 0.5 | no | yes | VDJdb |
| VGADGVGKSA | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| VGADGVGKSA | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| KLVVVGADG | VVVGADGVGK | 5 | 0.5 | no | yes | NeoTCR |
| KLVVVGADGV | VVVGAVGVGK | 5 | 0.5 | no | yes | VDJdb |
| KLVVVGADGV | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| KLVVVGADGV | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| LVVVGADG | VVVGAVGVGK | 5 | 0.5 | no | yes | VDJdb |
| LVVVGADG | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| LVVVGADG | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | no | yes | IEDB |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKSA | VVVGADGVGK | 5 | 0.5 | no | yes | NeoTCR |
| GADGVGKS | VVVGAVGVGK | 5 | 0.5 | no | yes | VDJdb |
| GADGVGKS | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| GADGVGKS | VVVGACGVGK | 5 | 0.5 | no | yes | TCR3D |
| VGADGVGKSAL | VVVGAVGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVVGAVGVGK | 6 | 0.455 | no | yes | VDJdb |
| VGADGVGKSAL | VVVGACGVGK | 6 | 0.455 | no | yes | TCR3D |
| VGADGVGKSAL | VVVGACGVGK | 6 | 0.455 | no | yes | TCR3D |
| YKLVVVGADGV | VVVGACGVGK | 6 | 0.455 | no | yes | TCR3D |
| YKLVVVGADGV | VVVGACGVGK | 6 | 0.455 | no | yes | TCR3D |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | no | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | no | yes | VDJdb |
| KLVVVGADG | VVVGAVGVGK | 6 | 0.4 | no | yes | VDJdb |
| KLVVVGADG | VVVGACGVGK | 6 | 0.4 | no | yes | TCR3D |
| KLVVVGADG | VVVGACGVGK | 6 | 0.4 | no | yes | TCR3D |
| YKLVVVGADG | VVVGADGVGK | 6 | 0.4 | no | yes | NeoTCR |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| GADGVGKSAL | VVVGADGVGK | 6 | 0.4 | no | yes | NeoTCR |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | no | yes | IEDB |
| GADGVGKSA | VVVGAVGVGK | 6 | 0.4 | no | yes | VDJdb |
| GADGVGKSA | VVVGACGVGK | 6 | 0.4 | no | yes | TCR3D |
| GADGVGKSA | VVVGACGVGK | 6 | 0.4 | no | yes | TCR3D |
| KLVVVGAD | VVVGADGVGK | 6 | 0.4 | no | yes | NeoTCR |
| ADGVGKSA | VVVGADGVGK | 6 | 0.4 | no | yes | NeoTCR |
| GADGVGKSALT | VVVGADGVGK | 7 | 0.364 | no | yes | NeoTCR |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | no | yes | IEDB |
| EYKLVVVGADG | VVVGADGVGK | 7 | 0.364 | no | yes | NeoTCR |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | no | yes | VDJdb |
| YKLVVVGADG | VVVGAVGVGK | 7 | 0.3 | no | yes | VDJdb |
| YKLVVVGADG | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| YKLVVVGADG | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| YKLVVVGAD | VVVGADGVGK | 7 | 0.3 | no | yes | NeoTCR |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | no | yes | IEDB |
| GADGVGKSAL | VVVGAVGVGK | 7 | 0.3 | no | yes | VDJdb |
| GADGVGKSAL | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| GADGVGKSAL | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| KLVVVGAD | VVVGAVGVGK | 7 | 0.3 | no | yes | VDJdb |
| KLVVVGAD | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| KLVVVGAD | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| ADGVGKSAL | VVVGADGVGK | 7 | 0.3 | no | yes | NeoTCR |
| ADGVGKSA | VVVGAVGVGK | 7 | 0.3 | no | yes | VDJdb |
| ADGVGKSA | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| ADGVGKSA | VVVGACGVGK | 7 | 0.3 | no | yes | TCR3D |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | no | yes | VDJdb |
| TEYKLVVVGAD | VVVGAVGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | unknown | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | no | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | no | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | no | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | no | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | no | yes | VDJdb |
| GADGVGKSALT | VVVGAVGVGK | 8 | 0.273 | no | yes | VDJdb |
| GADGVGKSALT | VVVGACGVGK | 8 | 0.273 | no | yes | TCR3D |
| GADGVGKSALT | VVVGACGVGK | 8 | 0.273 | no | yes | TCR3D |
| EYKLVVVGADG | VVVGAVGVGK | 8 | 0.273 | no | yes | VDJdb |
| EYKLVVVGADG | VVVGACGVGK | 8 | 0.273 | no | yes | TCR3D |
| EYKLVVVGADG | VVVGACGVGK | 8 | 0.273 | no | yes | TCR3D |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | no | yes | VDJdb |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSALTI | VVVGADGVGK | 8 | 0.2 | no | yes | NeoTCR |
| DGVGKSALT | VVVGADGVGK | 8 | 0.2 | no | yes | NeoTCR |
| DGVGKSALTI | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSALTI | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSALT | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSALT | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSALTI | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSAL | VVVGADGVGK | 8 | 0.2 | no | yes | NeoTCR |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| DGVGKSALT | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSAL | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSAL | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| YKLVVVGAD | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| YKLVVVGAD | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| DGVGKSAL | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | unknown | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | unknown | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | unknown | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | unknown | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | unknown | yes | VDJdb |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| EYKLVVVGAD | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| ADGVGKSALT | VVVGADGVGK | 8 | 0.2 | no | yes | NeoTCR |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| ADGVGKSAL | VVVGAVGVGK | 8 | 0.2 | no | yes | VDJdb |
| EYKLVVVGAD | VVVGADGVGK | 8 | 0.2 | no | yes | NeoTCR |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | no | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | no | yes | VDJdb |
| ADGVGKSAL | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| ADGVGKSAL | VVVGACGVGK | 8 | 0.2 | no | yes | TCR3D |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| TEYKLVVVGAD | VVVGACGVGK | 9 | 0.182 | unknown | yes | TCR3D |
| TEYKLVVVGAD | VVVGACGVGK | 9 | 0.182 | unknown | yes | TCR3D |
| DGVGKSALTIQ | VVVGADGVGK | 9 | 0.182 | no | yes | NeoTCR |
| DGVGKSALTIQ | VVVGACGVGK | 9 | 0.182 | no | yes | TCR3D |
| DGVGKSALTIQ | VVVGACGVGK | 9 | 0.182 | no | yes | TCR3D |
| TEYKLVVVGAD | VVVGADGVGK | 9 | 0.182 | unknown | yes | NeoTCR |
| DGVGKSALTIQ | VVVGAVGVGK | 9 | 0.182 | no | yes | VDJdb |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | unknown | yes | IEDB |
| ADGVGKSALTI | VVVGADGVGK | 9 | 0.182 | no | yes | NeoTCR |
| ADGVGKSALTI | VVVGAVGVGK | 9 | 0.182 | no | yes | VDJdb |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | no | yes | IEDB |
| ADGVGKSALTI | VVVGACGVGK | 9 | 0.182 | no | yes | TCR3D |
| ADGVGKSALTI | VVVGACGVGK | 9 | 0.182 | no | yes | TCR3D |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | unknown | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | unknown | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | unknown | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | unknown | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | unknown | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | no | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | no | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | no | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | no | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | no | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | no | yes | VDJdb |
| ADGVGKSALT | VVVGAVGVGK | 9 | 0.1 | no | yes | VDJdb |
| EYKLVVVGAD | VVVGACGVGK | 9 | 0.1 | no | yes | TCR3D |
| EYKLVVVGAD | VVVGACGVGK | 9 | 0.1 | no | yes | TCR3D |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | no | yes | IEDB |
| ADGVGKSALT | VVVGACGVGK | 9 | 0.1 | no | yes | TCR3D |
| ADGVGKSALT | VVVGACGVGK | 9 | 0.1 | no | yes | TCR3D |

### Curated related mutations
| query_gene | query_mutation | related_gene | related_mutation | related_query | relationship_group | source |
| --- | --- | --- | --- | --- | --- | --- |
| KRAS | G12D | KRAS | G12V | KRAS G12V | RAS | data/mutation_groups/ras.yaml |
| KRAS | G12D | KRAS | G12C | KRAS G12C | RAS | data/mutation_groups/ras.yaml |
| KRAS | G12D | KRAS | G13D | KRAS G13D | RAS | data/mutation_groups/ras.yaml |
| KRAS | G12D | NRAS | G12D | NRAS G12D | RAS | data/mutation_groups/ras.yaml |
| KRAS | G12D | HRAS | G12D | HRAS G12D | RAS | data/mutation_groups/ras.yaml |

## 7. Evidence score table
| identifier | source | epitope | raw_score | score_category | explanation |
| --- | --- | --- | --- | --- | --- |
| VDJDB-KRAS-G12D-001 | VDJdb | VVGADGVGK | 150 | High | same peptide +50; same HLA +20; same mutation/gene +15; same protein family +5; functional assay +30; tetramer evidence +20; literature PMID +10 |
| NEOTCR-KRAS-G12D-001 | NeoTCR | VVVGADGVGK | 100 | High | same peptide +50; same HLA +20; same mutation/gene +15; same protein family +5; literature PMID +10 |
| IEDB-KRAS-G12D-001 | IEDB | GADGVGKSAL | 80 | Medium | same HLA +20; same mutation/gene +15; same protein family +5; functional assay +30; literature PMID +10 |
| VDJDB-KRAS-G12V-001 | VDJdb | VVVGAVGVGK | 55 | Medium | same HLA +20; same protein family +5; functional assay +30 |
| TCR3D-KRAS-LIKE-001 | TCR3D | VVVGACGVGK | 45 | Low | same HLA +20; same protein family +5; structure available +20 |

## 8. Experimental planning suggestions
### Priority peptide 1: `VVGADGVGK`
- Mutant peptide: `VVGADGVGK`
- Wild-type control peptide: `VVGAGGVGK`
- HLA: `HLA-A*11:01`
- Reason: binding rank 0.8 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 2: `VVVGADGVGK`
- Mutant peptide: `VVVGADGVGK`
- Wild-type control peptide: `VVVGAGGVGK`
- HLA: `HLA-A*11:01`
- Reason: binding rank 0.8 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 3: `LVVVGADGVGK`
- Mutant peptide: `LVVVGADGVGK`
- Wild-type control peptide: `LVVVGAGGVGK`
- HLA: `HLA-A*11:01`
- Reason: binding rank 2.1 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 4: `KLVVVGADG`
- Mutant peptide: `KLVVVGADG`
- Wild-type control peptide: `KLVVVGAGG`
- HLA: `HLA-A*11:01`
- Reason: binding rank 2.7 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 5: `LVVVGADGV`
- Mutant peptide: `LVVVGADGV`
- Wild-type control peptide: `LVVVGAGGV`
- HLA: `HLA-A*11:01`
- Reason: binding rank 2.7 by rule-based-fallback-v0.1 and available evidence search context.

Suggested next experiments:
- Synthesize top-ranked mutant peptide candidates and matched wild-type control peptides.
- Confirm peptide-HLA presentation/binding with an orthogonal assay where feasible.
- Generate HLA-peptide tetramers or multimers for candidate-specific T cell enrichment/screening.
- Screen candidate T cells or TCRs with mutant peptide, wild-type peptide, and no-peptide controls.
- Run peptide titration or dose-response assays to estimate functional avidity.
- Test HLA-matched irrelevant peptide controls and HLA-mismatched negative controls.
- Perform focused cross-reactivity testing against related/self-peptide panels before any downstream use.

Practical prioritization notes:
- Start with candidates that combine strong MHC binding, exact/similar peptide evidence, and high evidence scores.
- Treat every candidate as a research hypothesis until antigen specificity and cross-reactivity are experimentally measured.
- Preserve all TSV/JSON artifacts with notebook or LIMS records so each candidate remains traceable to source evidence.

## 9. Limitations & warnings
- Database hits do not prove therapeutic safety.
- TCR cross-reactivity must be experimentally tested.
- NeoTCR-Scout is for research prioritization only, not clinical decision-making.

Third-party tool notice: Academic-use workflow notice: NetMHCpan and MHCflurry are external tools. Before using either predictor, contact the original authors and comply with their licenses and citation requirements.
