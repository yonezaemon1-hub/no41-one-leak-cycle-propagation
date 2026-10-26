# External audit request - No.41 v0.4

A user-supplied audit report of v0.1 has been received and is preserved in
AUDIT_REPORT_SUPPLIED_JA.md. It reports no model/proof/computational defect,
with REFERENCES=PARTIAL and NOVELTY=INCONCLUSIVE. Its C source and raw logs
were not supplied. This file lists questions for further audit, not evidence
of human peer review. Do not treat finite checks as an unbounded proof.

## Mathematical questions

1. Does Theorem A hold for EVERY initial set, including initially white leaks,
   leaks at isolated blue vertices, a single long blue run, and long runs of
   length exactly two? Are the simultaneous arc schedules compatible?
2. In the lower bound, can any initially isolated blue vertex initiate a second
   front before the incoming front arrives? Can a force enter the blocked arc
   by any route other than its endpoints? Supply a counterexample if so.
3. Is counting WHITE vertices rather than arc length correct when singleton
   initial blue vertices intervene? Check the C5 example.
4. Is the optimal layout construction valid for both k parities and for n-k
   smaller than floor(k/2)? Check k=n, k=n-1, k=2, k=3 and n=3 separately.
5. Is the parity minimization for m(n,t) correct at t=0 and large t? Does it
   introduce k=1 or allow an infeasible budget greater than n?
6. Verify the integer maximum in equation (E), the domination of odd budgets,
   and the constraints 2r<=c<=n in the upper bound of Theorem C.

## Computation

Run python -I check_hashes.py, then python -I verify.py --max-n 16.
Check that all updates are synchronous, the leak remains fixed, and a leak
can be colored. Confirm that the simulator is independent of the predicted
block-time formula. Counts should be 131,064 initial sets and 1,966,072 fixed
set/leak scenarios. Extra controls and construction checks are not added.
Report exact Python/OS and whether you actually ran the commands.

## Prior-art / equivalence questions

The existing forcing rule and throttling objective are not claimed as new.
Search for the exact fixed-set formula and fixed-budget frontier, including
equivalent formulations under other names and elementary corollaries of known
theorems. The cardinality fact Z_(1)(C_n)=2 is explicitly excluded as a claim.

If an existing theorem subsumes this result, identify its exact statement,
assumptions and an explicit map yielding the displayed formula. Distinguish
eventual forcing equivalence from a time-preserving reduction. In particular,
do not identify vertex leaks with initial-seed deletion, vertex deletion, PSD
forcing, or a moving/dynamic adversary.

PRIOR_ART.md and NOVELTY_SEARCH_JA.md record inspected full texts and journal
versions not yet compared. The central remaining question is whether an
existing theorem yields Theorem A by a time-preserving map, including isolated
blue seeds. The later capacity optimization is not a separate novelty claim.
Please keep REFERENCES, NOVELTY and PROOF separate. A proof
PASS must not silently become a historical-priority or human-peer-review claim.

## Requested report

Return MODEL, PROOF, COMPUTATION, REFERENCES, NOVELTY separately, with concrete
counterexamples or missing proof steps where applicable. Avoid a publication
decision on the author's behalf. No external communication is authorized by
this request file alone.

## Supplied computation evidence: label corrected, raw files not received

The supplied v0.3 self-audit confirms the earlier approximate totals were
n=21,22 alone. The corrected cumulative totals are 8,388,600 / 176,160,760.
The count-label issue is resolved as reported. The C source, build command,
full output and byte hashes have not been received here; the separate C claim
remains a supplied report rather than locally authenticated raw evidence.

## Reproof differential audit

A supplied report has already found no mathematical defect in the reproof.
For this revision, check that PROOF.md Sections 1-5 and KNOWN_FACT_REPROOF_JA.md
Sections 2-7 are unchanged. Check the citation-page ledger against the identified
PDF bytes where accessible. Distinguish author-side citation-location confirmation
from a complete source audit and from evidence of earlier publication. Keep
NOVELTY=INCONCLUSIVE unless a concrete prior theorem or counterevidence is found.

## Status after the v0.3 report

The existing model/proof/computation questions have received reported PASS
results. This v0.4 revision changes records only and requests no new mathematical
claim. The supplied report is self-audit as described by its reporter, not
independent third-party verification. Further literature review, if undertaken,
should address a concrete prior theorem yielding the exact fixed-set time formula.
