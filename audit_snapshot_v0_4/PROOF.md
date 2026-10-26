# Exact Parallel Propagation and Throttling with One Leak on a Cycle

Candidate No.41, version 0.3, 26 October 2026.
Ryutaro Yonezu / Yonezu Research Lab. AI-assisted research candidate.

**Author-side proof and recorded finite verification. A user-supplied audit
report finds no model, proof, or computational defect; its separate C code and
raw logs have not been supplied here. No human peer review is claimed.
Historical novelty: INCONCLUSIVE. Publication: HOLD.**

The leak rule, the concept of leaky forcing, and the general idea of minimizing
seed cost plus propagation time are established concepts. They are not claimed
as new here. The scope is the explicit exact time formula for every initial
set, with an elementary reproof using established path facts and the additional
time-preserving observations O1/O2 in KNOWN_FACT_REPROOF_JA.md. No new
propagation principle is claimed. The optimizations are consequences, not
separate innovations. See CITATION_CHECK_JA.md for checked source locations,
and PRIOR_ART.md for inspected versions
and access limitations. This is a mathematical graph model; no claim about
measured hardware, communication systems, or physical time is made.

## 1. Fixed model and definitions

Let C_n be the finite simple undirected cycle with vertices Z/nZ, where n >= 3.
Its edges are {i,i+1}. Choose the initial blue set B before a leak is chosen.
A single fixed vertex x is selected adversarially from ALL vertices, including
both initially blue and initially white vertices. Vertex x cannot perform a
force, but can itself become blue. No vertex or edge is deleted.

Time 0 is the initial coloring. At each integer round, a blue vertex other than
x with exactly one white neighbor forces that neighbor blue. All valid forces
use the coloring at the START of that round and are applied simultaneously.
There are no additional domination steps, hopping moves, or componentwise PSD
forcing rules. The leak never moves. A newly blue vertex can force only in a
subsequent round.

Write p(B;x) for the first round when every vertex is blue, or infinity if the
process stalls. Define

    T(B) = max over x in V(C_n) of p(B;x),
    tau(n,k) = min over |B|=k of T(B),
    m(n,t) = min {|B| : T(B) <= t},
    th_1(C_n) = min over B of (|B| + T(B)).

Here t is a nonnegative integer. Sets with infinite time are excluded from the
last two minima. For k=n, T(B)=tau(n,n)=0. For k=0 or 1, tau(n,k)=infinity.
The subscript in th_1 specifies this fixed one-vertex-leak model; it is not a
claim that this notation is standard or that leaky throttling is a new concept.

Applying every available force is the fastest parallel process: enlarging a
blue set can only make a proposed target already blue or leave its unique-white-
neighbor force available. Thus an explicitly legal round-by-round schedule
gives an upper bound for this simultaneous process as well.

## 2. The block formula for every initial set

An initial blue run is a maximal contiguous run of blue vertices in cyclic
order. For a proper initial set B, retain just the runs of length at least two,
and list them in cyclic order as R_1,...,R_r. Call these the long blue runs.

If r>0, let I_i be the arc strictly between R_i and R_(i+1), with cyclic
indices. Write a_i for the last vertex of R_i before that arc and b_i for the
first vertex of R_(i+1) after it. The endpoints a_i,b_i are distinct, including
when r=1, since a long blue run has at least two vertices and B is proper.

The arc I_i begins and ends with a white vertex. Its other vertices are white
or isolated initial blue vertices. Let W_i be the number of INITIALLY WHITE
vertices in I_i. Then W_i >= 1 and sum_i W_i = n-|B|. The arc length need not
equal W_i: isolated initial blue vertices must not be counted as new work.

**Theorem A (fixed-set time).**

* If B=V, then T(B)=0.
* If B is proper and has no adjacent initial blue vertices, then T(B)=infinity.
* Otherwise,

    T(B) = max_i W_i.                                      (A)

**Proof of the infinite case.** With no adjacent blue vertices, every blue
vertex has two white neighbors. No force is initially valid, even without a
leak. The coloring is already stalled.

**Directional-front observation.** From a nonleaky endpoint a_i, a front may
advance through I_i towards b_i. Each newly colored white vertex costs one
round. An isolated initial blue vertex costs no additional round: when its
neighbor on the arriving side becomes blue at round s, that isolated vertex
can force the next white vertex at round s+1. The next white vertex is therefore
colored one round after the preceding white vertex, with or without an isolated
initial blue vertex between them. Before the first arrival, an isolated blue
vertex has two white neighbors and cannot initiate a front.

The endpoint a_i is ready initially because its neighbor inside R_i is blue.
The observation holds with reversed orientation from b_i. A front stops at a
leak, after coloring it if it was initially white.

**Upper bound.** Fix any leak x and any arc I_i. If x is one of a_i,b_i, the
opposite endpoint is nonleaky and scans the whole arc in W_i rounds. If x is
inside I_i, both endpoints are nonleaky. Let L and R count the initially
white vertices strictly between x and the respective endpoints. If x is
initially white, then W_i=L+R+1. The two sides finish within L and R rounds,
and x is colored by min(L,R)+1, so the whole arc finishes by
max(L,R,min(L,R)+1)<=W_i. If x is an initially blue singleton, then
W_i=L+R, and the two sides finish by max(L,R)<=W_i. In the latter case
L,R>=1, because the arc begins and ends with white vertices.
If x is elsewhere, neither endpoint nor the arc contains a leak, so a single
front already suffices in W_i rounds. In particular, a leak inside a long blue
run remains blue and does not invalidate the neighboring endpoint's force.

These schedules on different arcs have disjoint white targets. There is no
competition for a forcing endpoint: the two external endpoints of a long run
are distinct, even for a run of length two. The schedules can therefore run
in parallel. Every initially white vertex is blue by max_i W_i.

**Lower bound.** Choose an arc I_i with maximum W_i, and place the leak at b_i.
No force can enter the arc from its b_i end. The only initially active entrance
is a_i. All other initially blue vertices in I_i are isolated and cannot start
propagating until a neighboring white vertex has become blue. List the
initially white vertices in order as w_1,...,w_(W_i). At time zero the
colored prefix of this list is empty. Suppose at the START of a round the
colored members are exactly w_1,...,w_q, with q<W_i. An initially blue
singleton between w_j and w_(j+1), for j>=q+1, still has two white
neighbors. In particular, the singleton just beyond the first uncolored
white vertex w_(q+1) cannot force w_(q+2) in this same round: w_(q+1)
is white at the start of the round. A newly colored vertex also cannot force
until the next round. All noninitial vertices beyond the prefix are white,
and entry from b_i is blocked permanently. Thus the only possible new white
target in the arc is w_(q+1), and the prefix grows by at most one per round.
This proves the induction, including the synchronous-update boundary case.

At least W_i rounds are required. Together with the upper bound this proves
(A). It also gives an explicit worst-case leak: the right boundary endpoint
of a maximum-white-count arc. QED.

## 3. Exact optimum for each seed budget

**Theorem B (complete budget-time frontier).** For n>=3 and 2<=k<n,

    tau(n,k) = ceil((n-k) / floor(k/2)).                    (B)

The conventions tau(n,n)=0 and tau(n,0)=tau(n,1)=infinity complete the formula.

**Lower bound.** For a finite-time proper B with |B|=k, each long blue run
contains at least two seeds. Hence r <= floor(k/2). Theorem A implies

    n-k = sum_i W_i <= r*T(B) <= floor(k/2)*T(B).

Taking the ceiling proves the bound for every initial set, including those
which also contain isolated seeds. Stalled sets cannot improve the minimum.

**Upper bound.** Put W=n-k>0 and r=min(floor(k/2),W). Form r cyclic blue runs,
each containing at least two seeds. Put all k-2r surplus seeds into the first
run. Separate these runs by r nonempty white runs whose lengths are as equal
as possible and total W. There are no isolated blue vertices in this layout.

If W>=floor(k/2), Theorem A gives time ceil(W/floor(k/2)). If W<floor(k/2),
there are W white runs of length one and the time is one, also equal to the
right side of (B). This covers dense configurations and both parities of k.
QED.

**Corollary B1 (every deadline-feasible set).** For integer t>=0, a proper set
B finishes by t against every fixed leak if and only if it has a long blue
run and every inter-run arc has at most t initially white vertices. The full
set always finishes at time zero. This is an exact certificate for each set,
not just for the balanced construction.

**Corollary B2 (minimum seeds at a deadline).** For n>=3 and integer t>=0,

    m(n,t) = min( 2*ceil(n/(t+2)),
                  2*ceil((n-1)/(t+2)) + 1 ).               (C)

**Proof.** By Theorem B, feasibility of a seed budget is n <= k+t*floor(k/2).
For even k=2r the smallest feasible value is 2*ceil(n/(t+2)); for odd k=2r+1
it is 2*ceil((n-1)/(t+2))+1. Values greater than n cannot win the displayed
minimum: for t=0 one parity gives exactly n, and for t>=1 the even candidate
is at most n for n>=3. The odd candidate is at least three, so the infeasible
case k=1 is not introduced. QED.

In particular, m(n,0)=n, and m(n,t)=2 if and only if t>=n-2.
The latter follows from tau(n,2)=n-2 and the infeasibility of k=0,1.

## 4. Exact additive throttling

**Theorem C.** For every n>=3,

    th_1(C_n) = ceil(sqrt(8*n)) - 2.                       (D)

**Proof.** Let c be an integer cost budget, k the seed count, and t the time.
For a feasible configuration with k+t<=c, Theorem B gives

    n <= k+(c-k)*floor(k/2).

For k=2r the right side is r(c+2-2r). For k=2r+1 it is
r(c+1-2r)+1, which is smaller than or equal to the even expression for the
same r because their difference is r-1>=0. The k=0,1 cases are infeasible.
Thus the maximum possible n at cost c>=3 is bounded by

    max over integer r of r(c+2-2r) = floor((c+2)^2/8).     (E)

For the equality, choose an integer r nearest to (c+2)/4. The distance of
c+2 from the nearest multiple of four is 0, 1, or 2. Completing the square
gives (E): the resulting loss before division by eight is respectively
0, 1, or 4, exactly the residue discarded by the floor. A maximizing r has
1<=r<=floor(c/2) when c>=3.

It follows that c>=ceil(sqrt(8*n))-2. Conversely, set
c=ceil(sqrt(8*n))-2. We have 3<=c<=n, since sqrt(8*n)<=n+2 for n>=3.
Choose a maximizing r as above, and let k=2r, t=c-2r. These are valid
nonnegative integers, with 2<=k<=c<=n. Inequality n<=r(c+2-2r) is exactly
n-k<=r*t. The balanced layout in Theorem B therefore has time at most t and
total cost at most c. This proves equality. QED.

## 5. Two instructive examples and scope checks

1. On C_5, take B={0,1,3}. Every individual white run has length one, but
   T(B)=2. Vertex 3 is an isolated seed, so it does not split the time block.
   With leak x=0, the successive newly blue sets are {2}, then {4}.
   Using only the longest contiguous white run would give a false answer.
2. On C_100, the balanced layout with k=14 has seven blue pairs, two white
   runs of length 13, and five white runs of length 12. Its worst time is 13.
   Theorem B rules out time 12 for every 14-seed layout. The sum is 27,
   matching ceil(sqrt(800))-2.
3. On C_6 with B={0,1}, the ordinary no-leak parallel time is two and the
   worst one-leak time is four. Deleting seed 0 instead leaves one blue
   vertex and stalls. Initial-seed deletion is a different model.
4. Two or more arbitrary leaks allow both neighbors of an omitted vertex
   to be leaks. That vertex can never become blue. Hence the one-leak
   tradeoff does not extend to multiple arbitrary vertex leaks; the only
   robust set for two or more is V. This is a known consequence of the
   degree obstruction, not a new result.

## 6. Verification and remaining audit

The literal simulator in verify.py enumerates every labeled initial subset
and every fixed single-vertex leak for the reported finite range. It compares
the resulting maxima with Theorem A, checks the explicit adversarial endpoint,
then minimizes over ALL sets of each size to test (B), (C), and (D). It also
tests the explicit balanced layouts and model-discrimination examples.

The finite search is a falsification check, not a proof for all n. The proof
above is author-side. The received report in AUDIT_REPORT_SUPPLIED_JA.md
states MODEL=PASS, PROOF=PASS, and COMPUTATION=PASS through n=22, including
a separately written C implementation. We have received the report text, not
that implementation or its raw logs. See AUDIT_INTEGRATION_JA.md for this
provenance distinction and the aggregate-count issue. No human peer review
is claimed. The author-run evidence/verification.json remains the unchanged
n<=16 record; verify.py is byte-identical to v0.1. Windows execution is
unverified. Prior-art search is incomplete and cannot certify historical
novelty or priority. No public release is authorized by this package alone.

A further user-supplied audit of the elementary reproof reports no mathematical
defect and keeps historical novelty INCONCLUSIVE. Its scope and source-access
limitations are retained in AUDIT_REPROOF_SUPPLIED_JA.md. The author-side source
location check is evidence/citation_checks.json; it does not certify the absence
of an earlier time theorem. Sections 1-5 of this proof are unchanged from v0.2.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
