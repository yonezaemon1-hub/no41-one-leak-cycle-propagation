# No.41 candidate: one-leak propagation on cycles

**Exact Parallel Propagation and Throttling with One Leak on a Cycle**

Version 0.4, 26 October 2026. Ryutaro Yonezu / Yonezu Research Lab.
AI-assisted research candidate. No human peer review or historical priority claimed.

| Item | Status |
| --- | --- |
| Model and proof | Author argument complete; supplied audit reports PASS / no defect found |
| Recorded computation | Author-run exhaustive PASS, 3<=n<=16, raw JSON bundled |
| Additional computation | Supplied report states separate C PASS through n=22; C source/logs not received |
| References | PARTIAL; retrieved versions and comparison scope updated |
| Historical novelty / priority | INCONCLUSIVE / NOT CLAIMED |
| Windows execution | NOT PERFORMED |
| Publication | HOLD |

The established vertex-leaky rule is used on a simple undirected cycle C_n.
Choose the initial blue set B; then an adversary fixes one vertex anywhere.
It cannot force, but can become blue. Updates use synchronous parallel rounds.

For each proper B containing adjacent blue vertices, retain the maximal
initial blue runs of length at least two. Count the initially WHITE vertices
in each arc between these runs, including arcs containing isolated blue seeds.
The candidate Theorem A states that the worst time over the leak position is
the largest such white count. With no adjacent blue seeds the process stalls;
with every vertex initially blue it takes zero rounds.

Consequences for n>=3 include:

    tau(n,k) = ceil((n-k)/floor(k/2)),  2<=k<n;
    tau(n,n) = 0;
    min_B (|B| + worst_time(B)) = ceil(sqrt(8*n)) - 2.

The scope is the explicit fixed-set worst-time formula and an elementary
reproof using known path facts plus O1/O2. A new propagation principle is not
claimed. The other formulas are consequences. Historical novelty remains
INCONCLUSIVE; an elementary derivation is not evidence of prior publication.
Leaky forcing, throttling, adjacent-seed cycle robustness, and opposing-front
propagation are established ideas.

## Read and reproduce

1. SUMMARY_JA.md gives the current Japanese summary.
2. PROOF.md gives the fixed model and proof, with an explicit synchronous
   induction and the deadline boundary m(n,t)=2 iff t>=n-2.
3. AUDIT_INTEGRATION_JA.md separates received audit claims from local evidence.
   The original supplied text is in AUDIT_REPORT_SUPPLIED_JA.md.
4. PRIOR_ART.md / sources.json give the updated comparison. NOVELTY_SEARCH_JA.md
   preserves the preceding detailed source review as a dated snapshot.

From the extracted package folder, in Windows PowerShell or a terminal:

```text
python -I check_hashes.py
python -I verify.py --max-n 16
```

Python 3.10 or newer, standard library only. No network, GPU, cloud computation,
or paid API is required. Windows execution has not been tested. The default
--max-n is 14; --max-n 16 reproduces the original author-side range.
The verifier's internal version remains 0.1 because its bytes were not changed.
The computational work grows exponentially; this package does not recommend
repeating the reported n=22 C run in Python.

The original evidence covers 131,064 labeled initial sets, 1,966,072 set/leak
scenarios, 147 budget optima and 147 deadline optima. Controls and constructions
are additional and not included in those exhaustive counts. The original
Python 3.12.14 / Linux run took about 15 seconds. The supplied audit reports a
Python 3.13.17 / Linux re-run at the same range taking about 13.7 seconds.

Keep the supplied C report separate from the original author-run evidence.
The reporter has now corrected the label: 6,291,456 sets / 136,314,880 scenarios
cover n=21,22 only. The stated cumulative n=3..22 totals are 8,388,600 sets /
176,160,760 scenarios. The count-label issue is resolved by that correction;
the C source and raw logs have not been received or authenticated here.

Neither the proof audit nor finite tests certify novelty. Publication remains
the author's separate decision. Research inquiries: yonezaemon1+research@gmail.com.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.

## Changes for the reproof audit

- KNOWN_FACT_REPROOF_JA.md incorporates the audited derivation. Its mathematical
  Sections 2-7 are byte-identical to the supplied derivation.
- CITATION_CHECK_JA.md gives exact viewer/printed pages and short excerpts for
  AJC final, Alameda, Hogben, Butler-Young and Carlson. The machine-readable
  checks and PDF byte hashes are in evidence/citation_checks.json.
- AUDIT_REPROOF_SUPPLIED_JA.md preserves the second supplied report;
  AUDIT_REPROOF_INTEGRATION_JA.md records responses and current limits.
- PROOF.md Sections 1-5, both Python programs, and the original recorded dynamics
  evidence are unchanged. No new dynamics run is claimed.
- Prior third-party PDFs and page images are not bundled. Their public source
  URLs and byte hashes identify what was inspected.

Source locations have author-side confirmation. References remain PARTIAL,
novelty INCONCLUSIVE and publication HOLD. Independent C source/logs remain
unreceived, and the n=22 report is retained as supplied evidence only.

## Version 0.4: record-only update

The supplied v0.3 self-audit reports MODEL/PROOF/COMPUTATION PASS, references
PARTIAL and novelty INCONCLUSIVE. It is preserved in AUDIT_V03_SUPPLIED_JA.md.
It explicitly corrects the count label and says it is not independent third-party
confirmation. Those corrections are recorded without upgrading the evidence.

PROOF.md and KNOWN_FACT_REPROOF_JA.md are preserved in their entirety from v0.3,
including their earlier document-version notes. The citation ledger, source
metadata, both verification programs and the original dynamics log are also
byte-identical. This revision does not change a theorem or perform a new
dynamics run. Its checks concern the record update and package integrity.

See AUDIT_V03_INTEGRATION_JA.md for the resulting status. The author-side source
location checks remain distinct from the reporter's unverified source locations.
References PARTIAL, novelty INCONCLUSIVE and publication HOLD are unchanged.
