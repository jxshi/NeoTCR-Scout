# NeoTCR-Scout report: KRAS_G12D_HLA_A1101

## 1. Project summary
NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.
It is not a de novo TCR generator or therapeutic TCR design platform.

## 2. Input mutation and HLA
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

## 4. MHC binding prediction summary
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

## 6. Similar peptide / related mutation hits
| query_peptide | matched_epitope | distance | similarity_score | same_hla | source |
| --- | --- | --- | --- | --- | --- |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| GADGVGKSAL | GADGVGKSAL | 0 | 1.0 | yes | IEDB |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | VDJdb |
| VVGADGVGK | VVGADGVGK | 0 | 1.0 | yes | VDJdb |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSALT | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| VGADGVGKSAL | GADGVGKSAL | 1 | 0.909 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| GADGVGKSA | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVGADGVGKS | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVVGAVGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVVGACGVGK | 1 | 0.9 | yes | TCR3D |
| VVVGADGVGK | VVVGACGVGK | 1 | 0.9 | yes | TCR3D |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| VVVGADGVGK | VVGADGVGK | 1 | 0.9 | yes | VDJdb |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| ADGVGKSAL | GADGVGKSAL | 1 | 0.9 | yes | IEDB |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VVGADGVG | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VGADGVGK | VVGADGVGK | 1 | 0.889 | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVGADGVGKSA | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVVGAVGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVVGACGVGK | 2 | 0.818 | yes | TCR3D |
| VVVGADGVGKS | VVVGACGVGK | 2 | 0.818 | yes | TCR3D |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVVGAVGVGK | 2 | 0.818 | yes | VDJdb |
| LVVVGADGVGK | VVVGACGVGK | 2 | 0.818 | yes | TCR3D |
| LVVVGADGVGK | VVVGACGVGK | 2 | 0.818 | yes | TCR3D |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| VVVGADGVGKS | VVGADGVGK | 2 | 0.818 | yes | VDJdb |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| GADGVGKS | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VVVGADGVG | VVVGAVGVGK | 2 | 0.8 | yes | VDJdb |
| VVVGADGVG | VVVGACGVGK | 2 | 0.8 | yes | TCR3D |
| VVVGADGVG | VVVGACGVGK | 2 | 0.8 | yes | TCR3D |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| DGVGKSAL | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VVGADGVGK | VVVGAVGVGK | 2 | 0.8 | yes | VDJdb |
| VVGADGVGK | VVVGACGVGK | 2 | 0.8 | yes | TCR3D |
| VVGADGVGK | VVVGACGVGK | 2 | 0.8 | yes | TCR3D |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSALT | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VGADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| ADGVGKSA | GADGVGKSAL | 2 | 0.8 | yes | IEDB |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VVVGADGVG | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VGADGVGKS | VVGADGVGK | 2 | 0.778 | yes | VDJdb |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVGADGVGKSA | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| ADGVGKSALTI | GADGVGKSAL | 3 | 0.727 | yes | IEDB |
| VVVGADGV | VVVGAVGVGK | 3 | 0.7 | yes | VDJdb |
| VVVGADGV | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VVVGADGV | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VGADGVGK | VVVGAVGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVVGAVGVGK | 3 | 0.7 | yes | VDJdb |
| LVVVGADGVG | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| LVVVGADGVG | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VGADGVGK | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VGADGVGK | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| DGVGKSALT | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VVGADGVGKS | VVVGAVGVGK | 3 | 0.7 | yes | VDJdb |
| VVGADGVGKS | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VVGADGVGKS | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VVGADGVG | VVVGAVGVGK | 3 | 0.7 | yes | VDJdb |
| VVGADGVG | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VVGADGVG | VVVGACGVGK | 3 | 0.7 | yes | TCR3D |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| VGADGVGKSA | VVGADGVGK | 3 | 0.7 | yes | VDJdb |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| VGADGVGKS | GADGVGKSAL | 3 | 0.7 | yes | IEDB |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| GADGVGKS | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| VVVGADGV | VVGADGVGK | 3 | 0.667 | yes | VDJdb |
| KLVVVGADGVG | VVVGAVGVGK | 4 | 0.636 | yes | VDJdb |
| KLVVVGADGVG | VVVGACGVGK | 4 | 0.636 | yes | TCR3D |
| KLVVVGADGVG | VVVGACGVGK | 4 | 0.636 | yes | TCR3D |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| KLVVVGADGVG | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VVGADGVGKSA | VVVGAVGVGK | 4 | 0.636 | yes | VDJdb |
| VVGADGVGKSA | VVVGACGVGK | 4 | 0.636 | yes | TCR3D |
| VVGADGVGKSA | VVVGACGVGK | 4 | 0.636 | yes | TCR3D |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VGADGVGKSAL | VVGADGVGK | 4 | 0.636 | yes | VDJdb |
| VGADGVGKS | VVVGAVGVGK | 4 | 0.6 | yes | VDJdb |
| VGADGVGKS | VVVGACGVGK | 4 | 0.6 | yes | TCR3D |
| VGADGVGKS | VVVGACGVGK | 4 | 0.6 | yes | TCR3D |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| DGVGKSALTI | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| LVVVGADGV | VVVGAVGVGK | 4 | 0.6 | yes | VDJdb |
| LVVVGADGV | VVVGACGVGK | 4 | 0.6 | yes | TCR3D |
| LVVVGADGV | VVVGACGVGK | 4 | 0.6 | yes | TCR3D |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VVGADGVGKS | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| VGADGVGK | GADGVGKSAL | 4 | 0.6 | yes | IEDB |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| LVVVGADGV | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| GADGVGKSA | VVGADGVGK | 4 | 0.556 | yes | VDJdb |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| DGVGKSALTIQ | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VVVGADGVGKS | GADGVGKSAL | 5 | 0.545 | yes | IEDB |
| VGADGVGKSA | VVVGAVGVGK | 5 | 0.5 | yes | VDJdb |
| VGADGVGKSA | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| VGADGVGKSA | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| KLVVVGADGV | VVVGAVGVGK | 5 | 0.5 | yes | VDJdb |
| KLVVVGADGV | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| KLVVVGADGV | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| LVVVGADG | VVVGAVGVGK | 5 | 0.5 | yes | VDJdb |
| LVVVGADG | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| LVVVGADG | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| VVGADGVGK | GADGVGKSAL | 5 | 0.5 | yes | IEDB |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| KLVVVGADGV | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKSAL | VVGADGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKS | VVVGAVGVGK | 5 | 0.5 | yes | VDJdb |
| GADGVGKS | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| GADGVGKS | VVVGACGVGK | 5 | 0.5 | yes | TCR3D |
| VGADGVGKSAL | VVVGAVGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVVGAVGVGK | 6 | 0.455 | yes | VDJdb |
| VGADGVGKSAL | VVVGACGVGK | 6 | 0.455 | yes | TCR3D |
| VGADGVGKSAL | VVVGACGVGK | 6 | 0.455 | yes | TCR3D |
| YKLVVVGADGV | VVVGACGVGK | 6 | 0.455 | yes | TCR3D |
| YKLVVVGADGV | VVVGACGVGK | 6 | 0.455 | yes | TCR3D |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| GADGVGKSALT | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| YKLVVVGADGV | VVGADGVGK | 6 | 0.455 | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| LVVVGADG | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| ADGVGKSA | VVGADGVGK | 5 | 0.444 | yes | VDJdb |
| KLVVVGADG | VVVGAVGVGK | 6 | 0.4 | yes | VDJdb |
| KLVVVGADG | VVVGACGVGK | 6 | 0.4 | yes | TCR3D |
| KLVVVGADG | VVVGACGVGK | 6 | 0.4 | yes | TCR3D |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVVGADGVGK | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| VVGADGVG | GADGVGKSAL | 6 | 0.4 | yes | IEDB |
| GADGVGKSA | VVVGAVGVGK | 6 | 0.4 | yes | VDJdb |
| GADGVGKSA | VVVGACGVGK | 6 | 0.4 | yes | TCR3D |
| GADGVGKSA | VVVGACGVGK | 6 | 0.4 | yes | TCR3D |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| LVVVGADGVGK | GADGVGKSAL | 7 | 0.364 | yes | IEDB |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| KLVVVGADG | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| ADGVGKSAL | VVGADGVGK | 6 | 0.333 | yes | VDJdb |
| YKLVVVGADG | VVVGAVGVGK | 7 | 0.3 | yes | VDJdb |
| YKLVVVGADG | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| YKLVVVGADG | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| KLVVVGAD | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| ADGVGKSALT | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| VVVGADGVG | GADGVGKSAL | 7 | 0.3 | yes | IEDB |
| GADGVGKSAL | VVVGAVGVGK | 7 | 0.3 | yes | VDJdb |
| GADGVGKSAL | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| GADGVGKSAL | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| KLVVVGAD | VVVGAVGVGK | 7 | 0.3 | yes | VDJdb |
| KLVVVGAD | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| KLVVVGAD | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| ADGVGKSA | VVVGAVGVGK | 7 | 0.3 | yes | VDJdb |
| ADGVGKSA | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| ADGVGKSA | VVVGACGVGK | 7 | 0.3 | yes | TCR3D |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| YKLVVVGADG | VVGADGVGK | 7 | 0.3 | yes | VDJdb |
| TEYKLVVVGAD | VVVGAVGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| ADGVGKSALTI | VVGADGVGK | 8 | 0.273 | yes | VDJdb |
| GADGVGKSALT | VVVGAVGVGK | 8 | 0.273 | yes | VDJdb |
| GADGVGKSALT | VVVGACGVGK | 8 | 0.273 | yes | TCR3D |
| GADGVGKSALT | VVVGACGVGK | 8 | 0.273 | yes | TCR3D |
| EYKLVVVGADG | VVVGAVGVGK | 8 | 0.273 | yes | VDJdb |
| EYKLVVVGADG | VVVGACGVGK | 8 | 0.273 | yes | TCR3D |
| EYKLVVVGADG | VVVGACGVGK | 8 | 0.273 | yes | TCR3D |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| KLVVVGAD | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| DGVGKSAL | VVGADGVGK | 7 | 0.222 | yes | VDJdb |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSALTI | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSALT | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSALT | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSALTI | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| DGVGKSALT | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSAL | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSAL | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| YKLVVVGAD | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| YKLVVVGAD | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| DGVGKSAL | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| EYKLVVVGAD | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| VVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| YKLVVVGAD | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGV | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADGVG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| ADGVGKSAL | VVVGAVGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| DGVGKSALTI | VVGADGVGK | 8 | 0.2 | yes | VDJdb |
| ADGVGKSAL | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| ADGVGKSAL | VVVGACGVGK | 8 | 0.2 | yes | TCR3D |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| LVVVGADG | GADGVGKSAL | 8 | 0.2 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| KLVVVGADGVG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| TEYKLVVVGAD | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| DGVGKSALTIQ | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| DGVGKSALTIQ | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| DGVGKSALTIQ | VVVGAVGVGK | 9 | 0.182 | yes | VDJdb |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| EYKLVVVGADG | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| TEYKLVVVGAD | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| ADGVGKSALTI | VVVGAVGVGK | 9 | 0.182 | yes | VDJdb |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| YKLVVVGADGV | GADGVGKSAL | 9 | 0.182 | yes | IEDB |
| ADGVGKSALTI | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| ADGVGKSALTI | VVVGACGVGK | 9 | 0.182 | yes | TCR3D |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| TEYKLVVVGAD | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALTIQ | VVGADGVGK | 9 | 0.182 | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| DGVGKSALT | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| YKLVVVGAD | VVGADGVGK | 8 | 0.111 | yes | VDJdb |
| ADGVGKSALT | VVVGAVGVGK | 9 | 0.1 | yes | VDJdb |
| EYKLVVVGAD | VVVGACGVGK | 9 | 0.1 | yes | TCR3D |
| EYKLVVVGAD | VVVGACGVGK | 9 | 0.1 | yes | TCR3D |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| YKLVVVGADG | GADGVGKSAL | 9 | 0.1 | yes | IEDB |
| ADGVGKSALT | VVVGACGVGK | 9 | 0.1 | yes | TCR3D |
| ADGVGKSALT | VVVGACGVGK | 9 | 0.1 | yes | TCR3D |

## 7. Evidence score table
| identifier | source | epitope | raw_score | score_category | explanation |
| --- | --- | --- | --- | --- | --- |
| VDJDB-KRAS-G12D-001 | VDJdb | VVGADGVGK | 145 | High | same peptide +50; same HLA +20; same mutation/gene +15; functional assay evidence +30; tetramer evidence +20; literature PMID available +10 |
| IEDB-KRAS-G12D-001 | IEDB | GADGVGKSAL | 75 | Medium | same HLA +20; same mutation/gene +15; functional assay evidence +30; literature PMID available +10 |
| VDJDB-KRAS-G12V-001 | VDJdb | VVVGAVGVGK | 55 | Medium | same HLA +20; same antigen family +5; functional assay evidence +30 |
| TCR3D-KRAS-LIKE-001 | TCR3D | VVVGACGVGK | 45 | Low | same HLA +20; same antigen family +5; structure available +20 |

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
