# Research brief: online labeling with joint error and cost guarantees

Venue target: AISTATS 2026. This brief frames the standing goal for every
stage. The research constitution and the assumption, comparator, and
literature policies included in context are binding.

## Problem setting

Items arrive online at rounds `t = 1, ..., T`. For each item the learner
chooses among one or more cheap labeling sources (for example model
predictions with raw confidence scores; losses normalized to `[0, 1]`; costs
possibly heterogeneous and nonzero) and a costly expert whose label is
authoritative (reference instantiation: unit cost, zero loss). The learner may
audit an AI-labeled item: pay the expert cost, observe the true label, and
release the corrected label. Feedback is partial — expert labels are observed
only on deferred or audited items. Decisions and audit probabilities must be
predictable with respect to the natural filtration, and released-label loss,
counterfactual source loss, and estimated feedback must be kept distinct. The
precise instantiation (number of sources, cost structure, score model) is the
designer's choice and must be stated per the constitution.

## Target

An online labeling algorithm and a theorem establishing, simultaneously and
under admissible problem-level assumptions:

1. **Error guarantee**: released-label error at most `epsilon * T + o(T)`
   (high probability preferred; state the exact semantics), and
2. **Cost guarantee**: total cost — every paid model call, expert deferral,
   audit, and correction — at most the cost of an explicit admissible
   comparator plus `o(T)`.

An impossibility result (for example an audit-cost lower bound at a weaker
assumption rung) paired with a positive result at the next admissible rung is
an acceptable, potentially stronger, contribution shape.

## Mechanism directions for this run (binding)

The previous run produced an explore-then-commit theorem (APS-LP, listed
below) whose strength is carried by two crutches: a full-audit calibration
prefix followed by a frozen deployment policy, and a finite preregistered
policy library that treats raw confidence scores as arbitrary given
quantities. This run must explore the two directions that remove exactly
those crutches. A candidate that reduces to explore-then-commit with a
full-audit prefix, or whose policy class is an arbitrary preregistered
finite library over uninterpreted scores, is retired by default and must
not be proposed.

1. **Online calibration of uncertainty — scores are learned, not given.**
   Raw confidence scores carry no assumed meaning. For each cheap source, the
   algorithm must estimate that source's conditional error rate (its
   uncertainty score) from the true losses observed on audited or deferred
   rounds — for example online binning or isotonic-style calibration on the
   score space — and route on the *calibrated* estimate. Distributional
   regularity of the raw score (stated on the data distribution, checkable in
   principle from data) is admissible; a margin or separation condition at an
   unknown optimal threshold is not. Discretization grids, bin widths, and
   calibration update schedules are algorithm choices whose approximation and
   estimation costs must appear explicitly in the bounds.

2. **FTRL-style adaptive selection — no learning/deployment phase split.**
   At each round the routing rule is chosen by follow-the-regularized-leader
   (or online mirror descent / online primal-dual) applied to cumulative
   *estimated* cost and risk built only from feedback observed on audited or
   deferred rounds, with importance weighting driven by the predictable audit
   probabilities. Audit probabilities must be adaptive and may decay over
   time; forced-audit floors are algorithm choices whose cost must be charged
   in full. The cost guarantee must survive adaptivity: sublinear regret in
   total cost against the admissible comparator, with the error constraint
   held anytime or at horizon (state which).

A single candidate combining both directions is preferred; a candidate that
delivers one direction cleanly is acceptable. An impossibility result showing
one direction is unattainable at an admissible rung (for example, no
adaptive-audit algorithm achieves `o(T)` cost regret without a stated
admissible condition) paired with a positive result under that condition is a
strong outcome. Beating APS-LP's `T^{2/3}` cost-regret rate with an adaptive
mechanism, or proving `T^{2/3}` unimprovable for an admissible class, are
both valid targets.

## Assumption discipline (binding)

Admissible assumptions are about the problem itself: i.i.d. or otherwise
stochastic non-adversarial arrivals, stationarity or an explicit mixing
condition, bounded losses and costs, distributional regularity of confidence
scores stated on the data distribution and checkable in principle from data, a
known safe expert. Inadmissible: optimizer-local or proof-artifact conditions
— anything defined only around an unknown optimal policy, price, or threshold
(strict complementarity, uniqueness of an optimal dual price, local
nondegeneracy or curvature at the optimum, a margin defined only at the
unknown optimizer), and any condition introduced solely to close a proof that
lacks an operational interpretation and diagnostic. A borderline condition
must be classified honestly and flagged for human review, never assumed
silently.

## What already exists (do not re-derive as a contribution)

- Candes, Ilyas, and Zrnic, "Probably Approximately Correct Labels": offline
  single-model PAC labeling, multi-model PAC routing, learned uncertainty
  recalibration, and cost-sensitive routing.
- This project's current online theorem: audited price updates control
  finite-horizon released-label error at `epsilon + B_T` with
  `B_T = O(T^{-1/2})` under predictable audits with a probability floor. It
  has NO cost guarantee.
- Run 20260715T214657Z-2d6432b6 (APS-LP, pending human review):
  explore-then-commit with a full-audit prefix of length `T^{2/3}` over a
  finite preregistered policy library; joint high-probability guarantees of
  released error `epsilon*T + O(sqrt(T log T))` and cost regret
  `O(G (1 + 1/epsilon) T^{2/3} sqrt(log(N T)))` against the
  distribution-aware LP comparator over the library. Its mechanism —
  full-audit prefix, one-shot empirical LP, frozen deployment mixture — is
  retired for this run.
- The offline LP / dual-price view is an explanatory reformulation, not a
  novelty claim.

## Literature lanes

Online risk control; intermittent or partial-feedback conformal methods;
online calibration and calibeating; label-efficient prediction and selective
sampling; bandits with knapsacks and constrained contextual bandits; online
learning with long-term constraints and online primal-dual methods; online
stochastic linear programming; revenue management; online learning to defer.
Follow the literature policy's exact-source discipline; absence of found
prior work is never evidence of novelty.

## Honesty

Every model output is a theorem or proof candidate. A reviewer `pass` is a
workflow status, not an established result. Promotion into the paper or the
research-state documents requires human review.
