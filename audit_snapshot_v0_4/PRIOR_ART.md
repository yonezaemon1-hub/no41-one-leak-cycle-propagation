# Prior-art comparison and limitations — v0.3

Updated 26 October 2026 after the detailed source review and receipt of a
user-supplied audit. REFERENCES=PARTIAL; NOVELTY=INCONCLUSIVE; publication HOLD.
No historical priority is claimed. Full third-party papers are not redistributed.

## Narrowed possible contribution

The forcing rule, vertex leaks, propagation time, throttling, cycle robustness
with two adjacent seeds, opposing-front propagation, and possible-forces criteria
are known. Theorem A's exact fixed-set time reduction, including isolated initial
blue vertices, is the only retained novelty candidate. This is a small refinement
of known arguments. Theorem B, deadline inversion and Theorem C are consequences.

Butler–Young's known path capacity and layout give a(N,s)=ceil(N/s)-1. Our
algebraic correspondence is tau(n,2r)=a(n,r)-1 and tau(n,2r+1)=a(n-1,r)-1.
The weighted path objective Q(n)=min_S(2|S|+pt(P_n,S)) gives
th_1(C_n)=Q(n)-1=ceil(sqrt(8n))-2 under the candidate timing reduction.
This is our derivation from known capacity, not a formula literally quoted from
the source. Root arithmetic is not an independent innovation. Numeric equality
alone does not establish the leak-model timing reduction in Theorem A.

## Inspected versions and limits

| sources.json ID | Inspected text and relevant scope | Limit |
| --- | --- | --- |
| S1 / S1_final | Dillman–Kenter 2019 preprint; later Alameda–Dillman–Kenter 2024 AJC journal PDF, 19 pages. Section 3.3 Proposition 3.4 p.313 gives opposing-front cycle robustness | Known mechanism; k=2 time n-2 is a direct count. No new mechanism claimed |
| S2 | On leaky forcing and resilience, 21-page arXiv preprint: Theorems 2.3, 2.5 and Corollary 2.7 | Eventual-robustness criteria; final DAM 2022 text not compared page by page |
| S3 | Generalizations of leaky forcing, 12-page author preprint and dissertation Chapter 3 | Eventual vertex/edge/specified/mixed equivalence. Final 2023 journal PDF not obtained in preceding review (HTTP 500); no general time theorem inferred |
| S4 | Bjorkman et al. arXiv:2508.02564v1, definitions, Proposition 2.1(3), main-result scope | Minimum cardinalities do not alone determine time; not a literature-wide exclusion |
| S5_v1 / S5_v4 | Brown et al. v1 Definitions 5.4–5.5 and Proposition 5.7 re-confirmed; v4 introduction | v1's fault removes an initial seed. Do not attribute its time section to v4 or conflate it with a vertex leak |
| S6 | Carlson et al. 20-page author PDF obtained: Section 6, Theorem 7.1 and Lemma 7.2 | PSD/ordinary cycle throttling are related, different rules. Final journal word-for-word comparison not done |
| S7 | Wang author-uploaded manuscript, Section 7 item 3 | Time/throttling terminology and future work for a different family; no cycle novelty certificate |
| S8 | Alameda 2021 dissertation, 89-page public PDF obtained: TOC, full-text phrase searches, related Chapter 2/3 statements and closing sections, Chapter 6 | No same theorem identified in this scope; not an audit of every theorem and cited source |
| S9 | Abbas 12-page 2024 accepted author version obtained: model equivalence, leader selection, Sections V/VI and closing discussion | Distinct from the 8-page ACC 2023 preprint; final journal word-for-word comparison not done |
| S10 | Butler–Young 2013 AJC final PDF, 7 pages, Section 2 pp.66–68 | Known path capacity/layout/weighted framework; No41 correspondence is our derivation |
| S11 | Elias et al. arXiv:2312.10154v2, 16 pages: model, families, conclusion | Leaky PSD rule differs; 2025 final Involve text not compared |
| S12 | Frijio arXiv:2609.22804, primary HTML main statements and scope | PSD edge-edit cardinality changes, not a same-model time result |
| S13 | Moruzzi–Shah–Tripathi arXiv:2509.21529v2 (2026-02-12), primary HTML scope, main cardinality statements and conclusion | Added after audit receipt; grid leaky forts and numbers. No same timing theorem identified in inspected statements |

Acquiring a PDF is distinct from auditing every theorem. Five acquired PDF byte
hashes are recorded in sources.json; papers themselves are not bundled.
The detailed NOVELTY_SEARCH_JA.md is a snapshot from before the supplied audit;
its audit-not-yet-received wording does not describe the current status.

## Alternate formulations and remaining question

The cycle arc proof also gives the same worst parallel time for one edge leak
or one specified-force leak; see the author-side derivation in the detailed
source review. These are relevant aliases. This does not assert parallel-time
equivalence on arbitrary graphs. Edge leaks retain adjacency, unlike edge deletion.
Initial-seed loss and PSD forcing also require an explicit time-preserving map.
The C5 and C6 controls discriminate the rules.

Both search systems and references/aliases involving propagation, parallel time,
deadlines, latency, edge leaks, specified leaks and throttling were considered.
Search misses are not novelty evidence. This is not an exhaustive commercial
citation-database search or a complete comparison of all journal/thesis versions.

The next audit question is whether an existing theorem yields Theorem A by a map
preserving parallel time for arbitrary initial sets, including isolated blue seeds.
Require its theorem number, assumptions and map. A supplied model/proof/computation
PASS does not settle that question. References remain PARTIAL and novelty remains
INCONCLUSIVE even after the previous full-text access gaps were partly closed.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.

## Reproof and citation-location update

The supplied second report finds no mathematical defect in the derivation,
while describing it as an elementary reproof using known facts. The present
scope is explicit statement of the exact worst-time formula; no new principle
is claimed. O1/O2 are additional short arguments, so this is not a quotation-only
application of a prior time theorem. An earlier publication of the same formula
has not been established.

CITATION_CHECK_JA.md and evidence/citation_checks.json identify the actual PDF
bytes and exact page/anchor checks for S1_final, S2, S6, S10 and S14. These
checks close the stated citation-location gaps on the author's side, not the
global prior-art question. Source comparison stays PARTIAL and novelty stays
INCONCLUSIVE.
