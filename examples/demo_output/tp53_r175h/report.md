# NeoTCR-Scout report: TP53_R175H_HLA_A0201

## 1. Project summary
NeoTCR-Scout is an evidence-guided workflow for neoantigen-specific TCR discovery and prioritization.
It is not a de novo TCR generator or therapeutic TCR design platform.

## 2. Input mutation and HLA
- Gene: `TP53`
- Mutation: `R175H`
- HLA: `HLA-A*02:01`

## 3. Generated neoantigen peptides
| mutant_peptide | wildtype_peptide | length | mutation_index | flanking_context |
| --- | --- | --- | --- | --- |
| AAAAAAAH | AAAAAAAR | 8 | 7 | AAAAAAAAAAHAAA |
| AAAAAAHA | AAAAAARA | 8 | 6 | AAAAAAAAAHAAAA |
| AAAAAHAA | AAAAARAA | 8 | 5 | AAAAAAAAHAAAAA |
| AAAAHAAA | AAAARAAA | 8 | 4 | AAAAAAAHAAAAAA |
| AAAHAAAA | AAARAAAA | 8 | 3 | AAAAAAHAAAAAAA |
| AAHAAAAA | AARAAAAA | 8 | 2 | AAAAAHAAAAAAAA |
| AHAAAAAA | ARAAAAAA | 8 | 1 | AAAAHAAAAAAAAA |
| HAAAAAAA | RAAAAAAA | 8 | 0 | AAAHAAAAAAAAAA |
| AAAAAAAAH | AAAAAAAAR | 9 | 8 | AAAAAAAAAAAHAAA |
| AAAAAAAHA | AAAAAAARA | 9 | 7 | AAAAAAAAAAHAAAA |
| AAAAAAHAA | AAAAAARAA | 9 | 6 | AAAAAAAAAHAAAAA |
| AAAAAHAAA | AAAAARAAA | 9 | 5 | AAAAAAAAHAAAAAA |
| AAAAHAAAA | AAAARAAAA | 9 | 4 | AAAAAAAHAAAAAAA |
| AAAHAAAAA | AAARAAAAA | 9 | 3 | AAAAAAHAAAAAAAA |
| AAHAAAAAA | AARAAAAAA | 9 | 2 | AAAAAHAAAAAAAAA |
| AHAAAAAAA | ARAAAAAAA | 9 | 1 | AAAAHAAAAAAAAAA |
| HAAAAAAAA | RAAAAAAAA | 9 | 0 | AAAHAAAAAAAAAAA |
| AAAAAAAAAH | AAAAAAAAAR | 10 | 9 | AAAAAAAAAAAAHAAA |
| AAAAAAAAHA | AAAAAAAARA | 10 | 8 | AAAAAAAAAAAHAAAA |
| AAAAAAAHAA | AAAAAAARAA | 10 | 7 | AAAAAAAAAAHAAAAA |
| AAAAAAHAAA | AAAAAARAAA | 10 | 6 | AAAAAAAAAHAAAAAA |
| AAAAAHAAAA | AAAAARAAAA | 10 | 5 | AAAAAAAAHAAAAAAA |
| AAAAHAAAAA | AAAARAAAAA | 10 | 4 | AAAAAAAHAAAAAAAA |
| AAAHAAAAAA | AAARAAAAAA | 10 | 3 | AAAAAAHAAAAAAAAA |
| AAHAAAAAAA | AARAAAAAAA | 10 | 2 | AAAAAHAAAAAAAAAA |
| AHAAAAAAAA | ARAAAAAAAA | 10 | 1 | AAAAHAAAAAAAAAAA |
| HAAAAAAAAA | RAAAAAAAAA | 10 | 0 | AAAHAAAAAAAAAAAA |
| AAAAAAAAAAH | AAAAAAAAAAR | 11 | 10 | AAAAAAAAAAAAAHAAA |
| AAAAAAAAAHA | AAAAAAAAARA | 11 | 9 | AAAAAAAAAAAAHAAAA |
| AAAAAAAAHAA | AAAAAAAARAA | 11 | 8 | AAAAAAAAAAAHAAAAA |
| AAAAAAAHAAA | AAAAAAARAAA | 11 | 7 | AAAAAAAAAAHAAAAAA |
| AAAAAAHAAAA | AAAAAARAAAA | 11 | 6 | AAAAAAAAAHAAAAAAA |
| AAAAAHAAAAA | AAAAARAAAAA | 11 | 5 | AAAAAAAAHAAAAAAAA |
| AAAAHAAAAAA | AAAARAAAAAA | 11 | 4 | AAAAAAAHAAAAAAAAA |
| AAAHAAAAAAA | AAARAAAAAAA | 11 | 3 | AAAAAAHAAAAAAAAAA |
| AAHAAAAAAAA | AARAAAAAAAA | 11 | 2 | AAAAAHAAAAAAAAAAA |
| AHAAAAAAAAA | ARAAAAAAAAA | 11 | 1 | AAAAHAAAAAAAAAAAA |
| HAAAAAAAAAA | RAAAAAAAAAA | 11 | 0 | AAAHAAAAAAAAAAAAA |

## 4. MHC binding prediction summary
| peptide | hla | rank_percent | binder | method |
| --- | --- | --- | --- | --- |
| AAAAAAAH | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAHA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAHAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAHAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAHAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAHAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AHAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| HAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAH | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAHA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAHAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAHAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAHAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAHAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAHAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AHAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| HAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAAH | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAHA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAHAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAHAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAHAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAHAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAHAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAHAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AHAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| HAAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAAAH | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAAHA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAAHAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAAHAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAAHAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAAHAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAAHAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAAHAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AAHAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| AHAAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |
| HAAAAAAAAAA | HLA-A*02:01 | 4.5 | non-binder | rule-based-fallback-v0.1 |

## 5. Exact TCR database hits
No records found.

## 6. Similar peptide / related mutation hits
No records found.

## 7. Evidence score table
No records found.

## 8. Experimental planning suggestions
### Priority peptide 1: `AAAAAAAH`
- Mutant peptide: `AAAAAAAH`
- Wild-type control peptide: `AAAAAAAR`
- HLA: `HLA-A*02:01`
- Reason: binding rank 4.5 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 2: `AAAAAAHA`
- Mutant peptide: `AAAAAAHA`
- Wild-type control peptide: `AAAAAARA`
- HLA: `HLA-A*02:01`
- Reason: binding rank 4.5 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 3: `AAAAAHAA`
- Mutant peptide: `AAAAAHAA`
- Wild-type control peptide: `AAAAARAA`
- HLA: `HLA-A*02:01`
- Reason: binding rank 4.5 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 4: `AAAAHAAA`
- Mutant peptide: `AAAAHAAA`
- Wild-type control peptide: `AAAARAAA`
- HLA: `HLA-A*02:01`
- Reason: binding rank 4.5 by rule-based-fallback-v0.1 and available evidence search context.
### Priority peptide 5: `AAAHAAAA`
- Mutant peptide: `AAAHAAAA`
- Wild-type control peptide: `AAARAAAA`
- HLA: `HLA-A*02:01`
- Reason: binding rank 4.5 by rule-based-fallback-v0.1 and available evidence search context.

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
