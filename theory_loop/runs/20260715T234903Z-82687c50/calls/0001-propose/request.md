# Stage: propose — design one new theorem candidate

You are the research designer in an autonomous theory loop targeting an
AISTATS-level contribution. In this single response, propose exactly ONE new
algorithm-plus-theorem candidate for the target in the research brief, ready
for a prover to attack in a separate fresh context that will see only the
contracts, the brief, and your artifact.

Rules:

- Work strictly inside the research constitution and the assumption,
  comparator, and literature policies included below.
- Assumptions must be problem-level and interpretable (for example i.i.d.
  stochastic arrivals, stationarity or explicit mixing, bounded losses and
  costs, distributional regularity of confidence scores stated on the data
  distribution). Optimizer-local or proof-artifact conditions are
  inadmissible. Classify every assumption with an assumption card.
- Attack first: try to break the target at the weakest assumption rung before
  adding anything. Add an assumption only to escape a documented obstruction.
- Do not repeat or trivially perturb any retired candidate listed in context.
  Differ in mechanism, not in constants.
- You may search the literature (lanes and discipline per the literature
  policy) to find mechanisms and to check whether a candidate is already
  known. Record exact sources; mark unverified ones. Absence of found prior
  work is never evidence of novelty.
- The theorem candidate must state BOTH an error guarantee and a cost
  guarantee, with an explicit comparator, horizon, and probability semantics.
  An impossibility theorem (for example an audit-cost lower bound at a weaker
  rung) paired with a positive result at the next admissible rung is welcome.
- If, after honest attack, no admissible non-retired candidate remains, return
  `STATUS: exhausted` and explain why the space is exhausted.

Output format — the FIRST line of your reply must be exactly one of:

STATUS: proposed
STATUS: exhausted

Then use exactly these sections:

## Setting and assumption ladder

(Information timeline per the constitution; one assumption card per active
assumption: mathematical statement, operational meaning, diagnostic or
falsification, required by, optimizer-local yes/no, classification.)

## Algorithm

(Precise, implementable description: state variables, what is observable at
each action time, routing/deferral rule, audit rule, update rule, and which
design choices are algorithm choices rather than problem assumptions.)

## Theorem candidate

(One exact statement with full quantifiers: error guarantee AND cost
guarantee, explicit comparator, horizon, and probability semantics.)

## Why this can work: proof plan

(Key lemmas, the tools you expect to use, and the single riskiest step.)

## Attack log

(The attacks you ran against weaker rungs and against this candidate, and the
obstructions that shaped the final assumptions.)

## Relation to known results

(Nearest results in the literature lanes with exact citations per the
literature policy; state precisely what would be different here.)

# Context: contracts/research-constitution.md

# Research Constitution

This constitution is the invariant boundary for every discovery, search,
proof, and review stage. It is independent of any particular algorithm, rate,
optimizer, or theorem candidate.

1. Define the action-time information timeline. State what is observable before
   each model call, routing action, expert deferral, audit decision, correction,
   release, and update. Online actions and audit probabilities must be
   predictable with respect to the stated filtration.
2. Keep three losses distinct: final released-label loss after any correction,
   counterfactual cheap-source loss used to assess the uncorrected action, and
   estimated or importance-weighted feedback used by the learner.
3. Total cost includes every paid model call, expert deferral, audit, and
   correction. State when each component is incurred and use the same
   accounting in learner and comparator objectives.
4. The learner and comparator use the same action-time observable information
   and action space. Neither sees the current expert label or realized
   cheap-source loss before acting. A distribution-aware stochastic comparator
   may know the data distribution only when this is stated explicitly.
5. State the policy class, horizon, probability space, sources of randomness,
   and whether each guarantee is fixed-horizon, anytime, in expectation, or
   high probability.
6. Separate problem assumptions from algorithm choices and rejected
   proof-only conditions. Every active problem assumption must have a deployment
   interpretation and a diagnostic or falsification route.
7. A model output is always a theorem or proof candidate. `COMPLETE_CANDIDATE`
   and a reviewer `PASS` are workflow statuses, not claims that a theorem has
   been established.
8. Novelty assessment and promotion into the paper or research-state documents
   require human review. Absence of located prior work is never evidence of
   novelty.

# Context: contracts/assumption-policy.md

# Assumption Policy

Use an assumption ladder: begin with the weakest interpretable setting, attack
the target, and add only assumptions that escape a documented obstruction.
Every change must appear in the artifact's assumption change log.

## Admissible problem assumptions

Examples include i.i.d. stochastic arrivals, stationarity or an explicit mixing
condition, bounded loss and cost, a known safe expert, a finite or otherwise
learnable policy class, and a globally interpretable realizability or
feasibility condition. An active problem assumption needs a mathematical
statement, operational meaning, diagnostic or falsification method, and the
conclusion that needs it.

## Algorithm choices

Audit floors, forced exploration, clipping, proxy floors, step-size schedules,
and finite grids are design choices. Record their cost, bias, approximation, or
rate effects; do not describe them as properties of the data-generating world.

## Rejected conditions

Strict complementarity, uniqueness of an optimal dual price, optimizer-local
curvature, local nondegeneracy, and a margin defined only around an unknown
optimal policy or optimizer cannot be active theorem assumptions. Also reject
conditions introduced solely to close a proof when they lack an operational
interpretation or diagnostic.

## Assumption card

Each assumption uses this human-readable card:

- Mathematical statement
- Operational meaning
- Diagnostic or falsification
- Required by
- Optimizer-local: `yes` or `no`
- Classification: `problem`, `algorithm`, or `rejected`

# Context: contracts/comparator-policy.md

# Comparator Policy

Audit every comparator along four dimensions.

## Information parity

At round `t`, the comparator uses the same current observable context as the
learner. It does not observe the current expert label or realized cheap-source
loss before its action. If it knows the stationary data distribution, say so.

## Action parity

Use the same model-call, expert, audit, correction, and release semantics. If a
distribution-aware comparator needs no learning audits, the learner's
exploration audits remain part of regret rather than disappearing from cost.

## Complete cost accounting

Count model calls, expert deferrals, audits, and corrections for both learner
and comparator. State whether predictions are precomputed or called
adaptively. Do not equate expert-query savings with total savings when other
components are nonzero.

## Risk and probability parity

Define released-label, counterfactual cheap-source, and estimated-feedback loss
separately. Match the target's horizon and probability semantics and identify
all randomness covered by the guarantee.

# Context: contracts/literature-policy.md

# Targeted Literature Policy

Search has two permitted triggers.

1. **Mechanism search** follows a failed impossibility or algorithm derivation
   when no credible candidate remains. Its input must state the desired result,
   exact obstruction, excluded approaches, and the kind of tool needed.
2. **Proof search** follows a precise blocked lemma, concentration step,
   partial-feedback estimate, regret step, or other proof obligation. It is not
   a broad novelty survey.

Search the most relevant lane first, using this default order when the
obligation does not dictate otherwise:

1. online risk control;
2. intermittent or partial-feedback conformal methods;
3. online stochastic linear programming;
4. revenue management;
5. constrained contextual bandits;
6. online learning with long-term constraints;
7. label-efficient prediction;
8. online selective classification; and
9. online learning to defer.

For every source, record the primary paper and stable URL, exact theorem,
lemma, proposition, or section, arrival and feedback models, comparator,
assumptions, probability semantics, error/cost/regret guarantee, whether the
supporting full text was checked, and a condition-by-condition mapping to the
current obligation. A mismatch is an `analogy`, never reusable proof evidence.

`ref/RELATED_WORK_REPORT_ZH.md` is a search index only. It does not become proof
evidence without verification against the primary full text. Search output
cannot establish novelty or repair a proof.

# Context: research brief

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
