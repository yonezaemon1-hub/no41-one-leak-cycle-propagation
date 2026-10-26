# No.41: one-leak propagation on cycles

**Exact Parallel Propagation and Throttling with One Leak on a Cycle**

Ryutaro Yonezu / Yonezu Research Lab. Version 1.0, 26 October 2026.
Unrefereed preprint. AI-assisted preparation. All rights reserved.

This research note states the exact worst parallel completion time for every
initial blue set on a simple undirected cycle with one fixed vertex leak.
The leak cannot force, but may become blue; it is selected after the initial set.

For a proper set with adjacent blue vertices, retain the maximal initial blue
runs of length at least two. The worst time is the maximum number of initially
WHITE vertices in an arc between consecutive retained runs. Isolated initial
blue vertices do not split an arc. With all vertices blue the time is zero;
without adjacent initial blue vertices the process stalls.

The fixed-budget consequence is

    tau(n,k) = ceil((n-k)/floor(k/2)),   2 <= k < n,
    tau(n,n) = 0.

The minimum sum of seed count and worst time is

    ceil(sqrt(8*n)) - 2.

The scope is an explicit exact-time formula and an elementary reproof using
known path robustness plus the additional time-preserving observations O1/O2.
Leaky forcing, throttling, opposing-front propagation and the optimization
framework are established ideas. No new propagation principle or historical
priority is claimed. Historical novelty remains INCONCLUSIVE and source
comparison PARTIAL. An elementary derivation is not evidence of prior publication.

## Download

- [Zenodo record / DOI 10.5281/zenodo.23665101](https://zenodo.org/records/23665101)
- [GitHub Release v1.0](https://github.com/yonezaemon1-hub/no41-one-leak-cycle-propagation/releases/tag/v1.0)
- [Paper PDF](paper/No41_One_Leak_Cycle_v1_0.pdf)
- [Evidence ZIP](artifacts/No41_Evidence_v1_0_20261026.zip)
- [LaTeX source](paper/No41_One_Leak_Cycle_v1_0.tex)

## Files and version history

- The PDF is distributed separately from this evidence ZIP. Its LaTeX source
  is paper/No41_One_Leak_Cycle_v1_0.tex.
- audit_snapshot_v0_4 is the complete frozen candidate v0.4, including proof,
  alternative reproof, source-location checks, supplied audit records, and code.
- PUBLICATION_STATUS.json and RELEASE_NOTES.md record the author's authorization
  for this public preprint. Historical HOLD labels inside the frozen snapshot
  describe the prepublication stage and are preserved as history.
- MATHEMATICAL_CORRESPONDENCE.json identifies the audited mathematical basis.
- SHA256SUMS / check_hashes.py check all bytes and manifest coverage.

The theorem statements and elementary proofs are based on the audited v0.4
material. Publication changes presentation and release status; it does not
upgrade novelty or create new computational evidence.

## Reproduce on a local PC

Python 3.10 or newer, standard library only. No network, paid API, cloud compute,
GPU, or installation is needed for the verification programs. Windows execution
is not established by the stored author-side run.

From the extracted evidence folder:

```text
python -I check_hashes.py
cd audit_snapshot_v0_4
python -I check_hashes.py
python -I verify.py --max-n 16
```

The recorded author-side run covers every labeled initial set and every fixed
leak for n=3..16: 131,064 initial sets, 1,966,072 scenarios, 147 budget entries
and 147 deadline entries; no mismatches. Extra construction and model checks
are not added to those exhaustive totals. Original environment: Python 3.12.14,
Linux, approximately 15 seconds. The default verifier limit is 14; use 16 to
reproduce the stored range. Work grows exponentially.

Supplied self-audit reports also describe a separately written C check through
n=22. Its source and raw logs were not supplied, so it remains reported evidence.
The reporter corrected cumulative n=3..22 totals to 8,388,600 initial sets and
176,160,760 scenarios; the earlier approximate figures covered only n=21,22.
Repeated reports from that process are not independent third-party confirmations.
No human peer review is claimed. Finite verification is not a proof for all n.

## Publication and contact

GitHub: https://github.com/yonezaemon1-hub/no41-one-leak-cycle-propagation

Published as an unrefereed preprint on GitHub and Zenodo on 26 October 2026.
Zenodo DOI: 10.5281/zenodo.23665101. [Publication receipt](publication/PUBLICATION_RECEIPT.json).
The PDF, evidence ZIP and v1.0 tag remain the original publication bytes.
Rights: All rights reserved. Third-party full papers and page images are not
redistributed in this evidence package.

Research inquiries: yonezaemon1+research@gmail.com
