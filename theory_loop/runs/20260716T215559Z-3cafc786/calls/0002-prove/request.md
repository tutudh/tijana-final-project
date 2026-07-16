# Stage: prove — attempt a complete proof

You are the prover in an autonomous theory loop. In this single response,
attempt a complete, rigorous proof of the EXACT theorem candidate given in
context. You have fresh eyes: the candidate's proof plan is a suggestion, not
a constraint. A separate independent referee will later check your proof in a
fresh context.

Rules:

- Prove the theorem as stated. You may strengthen the conclusion or simplify
  the algorithm's analysis; you MUST NOT weaken the statement, change the
  comparator, drop a cost component, or add any assumption. If the statement
  is false as written, refute it. If you cannot close a step without a new
  assumption, you are blocked — say exactly why.
- Respect the constitution everywhere: actions and audit probabilities must be
  predictable with respect to the stated filtration; keep released-label loss,
  counterfactual source loss, and estimated feedback distinct; account for
  every cost component on both the learner and comparator sides.
- Derive claimed rates; never assert them. Make constants and logarithmic
  factors explicit where feasible.
- You may search the literature for a specific tool (a concentration
  inequality, an online-LP or regret lemma, a risk-control result). Follow the
  literature policy: record the exact theorem and its assumptions and check
  the conditions one by one against your use. A mismatch is an analogy, not
  reusable proof evidence.
- If reviewer feedback is included in context, address every point explicitly:
  repair the proof or rebut with mathematics. Do not silently drop points.
- Status meanings: `complete` — every lemma and the main argument are fully
  proved and no open obligations remain; `blocked` — a precise obligation
  remains open; `refuted` — the statement is false and you give a concrete
  counterexample or contradiction.

Output format — the FIRST line of your reply must be exactly one of:

STATUS: complete
STATUS: blocked
STATUS: refuted

Then use exactly these sections:

## Exact theorem

(Restate verbatim the statement you prove or refute.)

## Notation and standing assumptions

## Lemmas

(Numbered, each with a full proof and explicit dependencies.)

## Main proof

(The error-guarantee derivation AND the cost-guarantee derivation.)

## Randomness and filtration accounting

(What is measurable when; where each concentration or martingale tool is
applied and why its conditions hold there.)

## Boundary cases and counterexample attempts

(What you tried in order to break the statement, and why it survives.)

## Self-audit

(The weakest steps of this proof, ranked, with what would fix or test them.)

## Open obligations

(Must be empty when STATUS is complete. When blocked: the exact obligation,
plus one targeted literature query if search could plausibly unblock it.)

## Counterexample

(Only when STATUS is refuted: the instance, the violated claim, and which
assumption card fails to exclude it.)

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

An impossibility result paired with a positive result is an acceptable,
potentially stronger, contribution shape. The pairing is again half-filled,
one rung down the rate ladder from last run: the positive half is now the
OBSR theorem at the A1–A3 rung with cost regret `O~(T^{2/3})` (listed under
"What already exists"), and the sought half is a minimax lower bound at the
SAME rung matching `T^{2/3}` — or, failing that honestly, an admissible
algorithm beating the rate. The next section makes this binding.

## This run's target (binding): resolve whether T^{2/3} is optimal

Run 20260716T183433Z-75ac21c9 (OBSR, listed below) achieves, under A1
(i.i.d. arrivals), A2 (perfect unit-cost expert, known bounded costs), A3
(globally Lipschitz conditional error curve `m(s) = Pr(L=1 | S=s)` with
constant `L`), and `epsilon in (0,1]`, with `K = Theta(T^{1/3})` bins and
reveal floor `gamma = T^{-1/3}`: released error
`epsilon*T + O~(T^{2/3})` and cost regret `O~(T^{2/3})` against the
expected-cost benchmark over ALL Borel score-routing policies, using only
release and defer actions, with no phase split and no preregistered library.
Its residual balance is structural, not incidental: the reveal floor charges
`gamma*T` in cost, the importance-weighted dual feedback carries conditional
variance `1/gamma` because a release reveals nothing, and `gamma = T^{-1/3}`
equalizes the two at `T^{2/3}`. The Lipschitz discretization no longer
touches the cost side at all; it is charged to the error budget. The open
question this run must attack: **is `T^{2/3}` the minimax cost-regret rate
for this exact setting, or can an admissible adaptive algorithm achieve
`o(T^{2/3})` — plausibly `O~(sqrt(T))`?**

**Primary target — a minimax lower bound with exact setting parity.** The
theorem shape is the priced trade-off: there exist constants
`c1(epsilon, L) > 0`, an explicit exchange rate `eta > 0`, and a finite
family of instances, each satisfying A1–A3 with the SAME stated
`(epsilon, L)`, such that every algorithm obeying the protocol below
satisfies

```
max over the family of
  ( E[C_T] - C_T^star + eta * ( E[sum_t R_t] - epsilon*T ) )
  >= c1 * T^{2/3}.
```

The priced form is mandatory as the primary statement. Error slack converts
into cost savings at exchange rate at least one whenever the comparator
defers `Omega(T^{2/3})` mass: releasing deferred mass saves its full unit
fee and adds at most that much error. An unpriced two-sided claim therefore
cannot tolerate slack of larger order than the rate it asserts. The
admissible two-sided corollary ties the constants: any algorithm whose
expected released error is at most `epsilon*T + c0*T^{2/3}` on EVERY
instance of the family must have expected cost regret at least
`(c1/2)*T^{2/3}` on at least one instance, with `c0 = c1/(2*eta)`.
Expectation semantics suffice. A polylogarithmic gap against the upper
bound's `sqrt(log T)` factor is acceptable and must be stated, not hidden.

**Dead constructions (binding; these are the recorded attacks from run
20260716T183433Z-75ac21c9 — do not resubmit them without a new mechanism):**

1. **Paired sign-swap Assouad dies to free labels.** With `M` score pairs
   and one unknown high-error atom per pair, the learner defers one
   arbitrary atom per pair at exactly the comparator's total deferral mass,
   receives labels through ordinary deferrals, and infers the partner atom
   from the pairing constraint. Cumulative excess error before
   identification is `O(sqrt(T))`. Any construction whose unknowns are
   correlated across cells the learner can trade against each other fails
   the same way.
2. **Null-versus-positive-bumps dies to cheap aggregates.** Making the
   comparator release everything removes free labels, but score-independent
   randomized deferral at rate `beta` estimates aggregate bump mass to
   precision `1/sqrt(beta*T)`, and the value of locating bumps is second
   order when baseline error is bounded away from zero. Any construction
   whose instances differ detectably in aggregate error mass fails the same
   way.
3. **Unpriced slack claims are unprovable.** Per the exchange-rate argument
   above, a two-sided statement tolerating error slack `omega(T^{2/3})` is
   false for every construction in which the comparator defers
   `Omega(T^{3/4})` mass; submitting one is an automatic reject.

A surviving construction must therefore locate the hardness on cells the
comparator fully releases (so every label there is bought, not free), keep
the unknowns independent across cells, keep the joint law of
`(S_t, Yhat_t)` identical across the family so that only paid expert labels
carry information, remain indistinguishable in aggregate through both the
model-output channel and score-independent deferral, and survive the priced
accounting. The candidate mechanism to probe first (guidance, not mandate):
localize the floor-versus-variance balance — force any algorithm either to
defer `Omega(gamma)` mass per round on the comparator's release region
(paying `gamma*T`) or to track the binding dual price from labels whose
conditional variance is `Omega(1/gamma)`, and show these cannot both be
avoided at `o(T^{2/3})`.

**Setting-parity checklist (binding; violating any item voids the
candidate):**

1. **Instance admissibility.** Every instance in the family is i.i.d. (A1),
   has a perfect unit-cost expert with fixed known costs
   `c_M, c_R in [0,1]` shared across the family (`c_M = c_R = 0` is allowed
   and encouraged for cleanliness) (A2), and has `m` Lipschitz with the SAME
   constant `L` quantified in the theorem (A3). No nonstationary,
   heavier-tailed, or non-Lipschitz instances; a lower bound proved outside
   the positive result's assumption rung resolves nothing. The risk
   constraint must be binding at the comparator on every instance.
2. **Information-protocol parity.** The learner pays `c_M`, observes
   `(Yhat_t, S_t)`, then observes `Y_t` exactly on deferred or audited
   rounds at unit expert cost each (plus `c_R` per corrected audited
   error), and observes nothing about `Y_t` on released rounds. Deferral
   rounds yield labels too; exploration cost on a safe cell is the excess
   deferral (or audit) fee relative to the comparator who releases there.
3. **Learner generality.** The bound must hold for every randomized,
   adaptively auditing algorithm over the full action set (release / defer /
   audit-and-correct), including learners that audit even though OBSR never
   does. The learner may know `T`, `epsilon`, `L`, `delta`, the score
   marginal, and the entire instance family up to the unknown signs. Extra
   learner knowledge strengthens the lower bound; do not manufacture
   hardness by hiding structure the positive result does not hide.
4. **Benchmark parity.** The comparator is the same expected-cost benchmark
   `C_T^star = T * [ c_M + inf over Borel feasible a of E[1 - a(S)] ]` used
   by OBSR, computed per instance, with identical cost accounting on both
   sides (`c_M*T` is common and cancels in regret).
5. **Priced-form honesty.** The primary statement is the `eta`-priced
   trade-off above; the two-sided corollary may only claim slack tolerance
   of the same `T^{2/3}` order, with `c0` tied to `eta`. A lower bound that
   binds only algorithms with zero or `O(sqrt(T))` error slack is an
   inadmissible resolution of the question.

**Acceptable alternative resolution.** If the honest attack reveals that
`T^{2/3}` is beatable, an admissible algorithm with cost regret `o(T^{2/3})`
and released error `epsilon*T + O~(T^{2/3})` under A1–A3 — same protocol,
same benchmark, both guarantees simultaneously, no retired crutches
(full-audit prefix, preregistered finite library, optimizer-local margins) —
resolves the question in the other direction and is equally welcome. Two
honest levers and one dead end are on record. The constraint needs tracking
only at per-round precision `T^{-1/3}`, far looser than `sqrt(T)`-rate
estimation, and this slack is currently unexploited. The flat floor pays for
dual variance on ALL released mass while only bins near the binding price
carry decision-relevant uncertainty, so a floor localized where the price is
uncertain could cut the `gamma*T` charge. But bin-adaptive floors
`gamma_b ~ sqrt(mu_b)` improve only the `epsilon`-dependence of the same
`T^{2/3}` balance, not the exponent; resubmitting that retuning is not a
contribution. Not acceptable: a lower bound violating the checklist, a
positive result that changes the comparator class or assumption rung, or
constant and parameter retunings of OBSR presented as rate improvements.

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
  full-audit prefix, one-shot empirical LP, frozen deployment mixture —
  remains retired.
- Run 20260715T234903Z-82687c50 (ACU-FTRL, pending human review): fully
  adaptive binned calibration (`K = ceil(T^{1/4})` bins, importance-weighted
  UCB on binwise error mass) plus constrained FTRL on cumulative observed
  deferral cost, with audit floor `gamma_t = t^{-1/4}` charging only the
  shortfall over deferral feedback; under A1–A3 it achieves released error
  `epsilon*T + O~(sqrt(T))` and cost regret
  `O~((1 + c_R + (1+L)/epsilon) T^{3/4})` against the expected-cost
  benchmark over all Borel score policies. Superseded on the cost rate by
  OBSR below; note the frontier honestly: ACU-FTRL's error slack
  `O~(sqrt(T))` is smaller than OBSR's `O~(T^{2/3})`, so the two occupy
  incomparable (error, cost) points, and OBSR's proof couples both
  guarantees through the same `sqrt(K T)` term, so its `K`-knob cannot
  recover the `(sqrt(T), T^{3/4})` point. Do not re-derive either result or
  re-tune their constants.
- Run 20260716T183433Z-75ac21c9 (OBSR — One-Sided Barrier Saddle Routing;
  passed 2 fresh-context loop reviews and a line-by-line human-directed
  verification on 2026-07-16; promotion pending): one-sided log-barrier
  mirror descent on binned release probabilities coupled with AdaGrad dual
  ascent on the importance-weighted constraint, reveal floor `gamma`, dual
  cap `Lambda = 2/epsilon`, exact-penalty conversion via
  `Lambda - lambda_star >= 1/epsilon`. Its load-bearing novelty is the
  barrier local-norm cancellation: the gradient satisfies
  `g^2 q^2 <= 2(1 + Lambda^2)` pathwise, so importance weighting never
  costs the primal a `1/gamma` factor. The proved finite-`T` bounds are
  tuning-agnostic: with probability `1 - delta`,
  `sum_t R_t <= epsilon*T + L*T/K + G_T` and
  `C_T <= C_T^star + gamma*T + G_T`, where
  `G_T = O((1 + 1/epsilon)^2 [sqrt(K*T*l) + sqrt(T*l/gamma) + l/gamma])`
  and `l = log(16KT/delta)`. The run artifact's headline tuning
  `K = Theta(T^{1/4})`, `gamma = T^{-3/8}` yields cost regret
  `O~(T^{11/16})`; the session verification checked every `gamma`- and
  `K`-dependence in the proof (barrier stability
  `sqrt(K log(1/gamma)/T) <= 1/2`, `l >= log(1/gamma)`, `T*gamma >= 1`) and
  confirmed that `K = ceil(max{1, 4L/rho} T^{1/3})`, `gamma = T^{-1/3}`
  balances `gamma*T` against `sqrt(T*l/gamma)`, giving released error
  `epsilon*T + O_{epsilon,L,rho}(T^{2/3} sqrt(log(T/delta)))` and cost
  regret of the same order. Cite OBSR at the retuned `T^{2/3}` rate. Do not
  re-derive it, re-tune it, or propose variants that merely move constants.
- The offline LP / dual-price view is an explanatory reformulation, not a
  novelty claim.

## Literature lanes

Online risk control; intermittent or partial-feedback conformal methods;
online calibration and calibeating; label-efficient prediction and selective
sampling; bandits with knapsacks and constrained contextual bandits; online
learning with long-term constraints and online primal-dual methods; online
stochastic linear programming; revenue management; online learning to defer.

For this run's question the sharpest anchor is partial monitoring and its
observability classification. Adversarial finite games with a revealing
action sit at `Theta(T^{2/3})` (Cesa-Bianchi–Lugosi–Stoltz; apple tasting is
the standard example), while stochastic apple-tasting variants with extra
structure reach `O~(sqrt(T))` (Harris–Podimata–Wu). Whether this problem's
constrained, distribution-aware-benchmark variant falls on the hard or the
easy side IS the open question, so treat observability arguments as
candidate mechanisms for both directions. Kleinberg's continuum-armed
`T^{2/3}` matches OBSR's exponent through a different mechanism — gap-priced
exploration of arms there, reveal-floor versus dual-feedback variance under
one-sided observability here — and the relation-to-known-results section
must state this contrast explicitly rather than claim kinship. For lower
bounds: label-efficient prediction query-budget tradeoffs
(Cesa-Bianchi–Lugosi–Stoltz); minimax rates for nonparametric active
learning (Castro–Nowak); bandits-with-knapsacks lower bounds;
selective-sampling and apple-tasting lower bounds; standard
adaptive-sampling change-of-measure tools (Assouad, Fano, divergence
decompositions for sequentially chosen observations). For algorithms:
implicit-exploration (IX) and self-normalized importance-weighted
estimators; variance-reduced off-policy evaluation; optimism on constraint
estimates in constrained bandits. Follow the literature policy's
exact-source discipline; absence of found prior work is never evidence of
novelty.

## Honesty

Every model output is a theorem or proof candidate. A reviewer `pass` is a
workflow status, not an established result. Promotion into the paper or the
research-state documents requires human review. The OBSR retuning cited
above was verified in a human-directed session on 2026-07-16, not by the
loop's fresh-context reviews; treat the `T^{2/3}` statement as the standing
positive result for targeting purposes, and re-verify the retuned constants
before any paper claim.

# Context: theorem candidate to prove

STATUS: proposed

## Setting and assumption ladder

**Candidate: Camouflaged Independent-Cell Apple Tasting (CICAT) lower bound.** This is an impossibility candidate, so the “algorithm” below specifies the full learner class quantified by the theorem rather than prescribing one learner.

Fix horizon \(T\ge 8\), risk budget \(\epsilon=1/4\), Lipschitz bound \(L=1\), and

\[
M=\lfloor T^{1/3}\rfloor,\qquad
\delta=\frac{1}{64(M+1)},\qquad
\Theta_T=\{-1,+1\}^{M}.
\]

For \(\theta\in\Theta_T\), write \(\bar\theta=M^{-1}\sum_i\theta_i\). The common score marginal has:

\[
\Pr(S=0)=\tfrac14,\qquad
\Pr(S=\tfrac12)=\tfrac12,\qquad
\Pr\!\left(S=s_i\right)=\frac{1}{4M},
\]

where

\[
s_i=\frac12+\frac{i}{2(M+1)},\qquad i=1,\ldots,M.
\]

The cheap model always outputs \(\widehat Y=0\). Conditional on \(S=s\),

\[
Y=L\sim\operatorname{Bernoulli}(m_\theta(s)),
\]

with support-point means

\[
m_\theta(0)=\frac18-\delta\bar\theta,\qquad
m_\theta(\tfrac12)=\frac12,\qquad
m_\theta(s_i)=\frac12+\theta_i\delta.
\]

Between support points, define \(m_\theta\) by linear interpolation and extend it constantly after \(s_M\). Every \(m_\theta\) is globally \(1\)-Lipschitz: the largest hard-cell slope is \(4\delta(M+1)=1/16\), while the slope from \(0\) to \(1/2\) is below \(1\).

The anchor at \(S=0\) camouflages aggregate error:

\[
\mathbb E_\theta[Y]
=\frac14m_\theta(0)
 +\frac{1}{4M}\sum_i m_\theta(s_i)
 +\frac12m_\theta(\tfrac12)
=\frac{13}{32}
\]

for every \(\theta\). Thus the joint law of \((S,\widehat Y)\) and the score-blind label mean are identical throughout the family.

**Information timeline.** Let \(\mathcal H_{t-1}\) contain all past scores, actions, internal randomness, released labels, costs, and expert labels from deferred or audited rounds.

1. The learner pays \(c_M=0\) and observes \((S_t,\widehat Y_t)\).
2. Using only \((\mathcal H_{t-1},S_t,\widehat Y_t)\) and fresh internal randomness, it chooses release, defer, or audit-and-correct.
3. On release, it outputs \(\widehat Y_t\), pays no expert cost, and never observes \(Y_t\).
4. On defer, it pays one, observes \(Y_t\), and releases the expert label.
5. On audit, it pays one, observes \(Y_t\), corrects if necessary, and releases \(Y_t\). Here \(c_R=0\).
6. Only then may the learner update its state.

Define the three losses separately:

\[
L_t=\mathbf 1\{\widehat Y_t\ne Y_t\}=Y_t
\]

is the counterfactual cheap-source loss,

\[
R_t=L_t\mathbf 1\{A_t=\mathrm{release}\}
\]

is final released-label loss, and any estimate constructed from revealed labels is merely learner feedback and is not used in either \(R_t\) or cost accounting.

**Assumption ladder.**

- With only bounded stationary feedback and no regularity, arbitrarily many unrelated score cells could make regret nearly linear; this does not resolve the A1–A3 rate.
- Adding i.i.d. arrivals but no score regularity leaves the same obstruction.
- At the target A1–A3 rung, global Lipschitzness limits independent cells of gap \(\delta\) to \(M=O(1/\delta)\). Balancing \(M\asymp1/\delta\) with \(T/M\asymp1/\delta^2\) yields the candidate \(T^{2/3}\) obstruction. No stronger assumption is added.

**A1 — i.i.d. stochastic arrivals**

- Mathematical statement: Conditional on fixed \(\theta\), \((S_t,Y_t,\widehat Y_t)_{t=1}^T\) are i.i.d. with the law above.
- Operational meaning: The deployment population is stationary and has no adaptive drift.
- Diagnostic or falsification: Test score frequencies and audited conditional error rates for temporal drift, serial dependence, or change points.
- Required by: Exact parity with OBSR and the product-form sequential KL calculation.
- Optimizer-local: no.
- Classification: problem.

**A2 — bounded costs and perfect expert**

- Mathematical statement: \(L_t\in\{0,1\}\), \(c_M=c_R=0\), and every defer or audit costs exactly one and reveals the authoritative \(Y_t\).
- Operational meaning: Expert review is reliable and has a known normalized fee; the model call and post-audit correction are free in this clean lower-bound instance.
- Diagnostic or falsification: Measure expert disagreement on repeated labels and audit invoices for action-dependent or time-varying costs.
- Required by: Common cost accounting, the reduction of defer and audit to the same revealing action, and A2 parity.
- Optimizer-local: no.
- Classification: problem.

**A3 — global score regularity**

- Mathematical statement: \(|m_\theta(s)-m_\theta(s')|\le |s-s'|\) for all \(s,s'\in[0,1]\), for every \(\theta\).
- Operational meaning: Nearby confidence scores have nearby conditional cheap-model error probabilities.
- Diagnostic or falsification: On an independently audited sample, construct simultaneous confidence intervals for binwise error rates and test whether adjacent-bin differences exceed score distance plus sampling uncertainty.
- Required by: Exact parity with OBSR and the relation \(M\delta=\Theta(1)\) that produces the \(T^{2/3}\) packing.
- Optimizer-local: no.
- Classification: problem.

No margin, uniqueness, curvature, strict complementarity, or condition defined around an unknown optimal policy is active.

## Algorithm

The theorem quantifies every randomized adaptive learner representable as follows.

Its state is \(Z_{t-1}\), initialized arbitrarily. After observing \(S_t\), it draws

\[
A_t\sim\pi_t(\,\cdot\mid Z_{t-1},S_t,\widehat Y_t),
\]

where \(\pi_t\) is any predictable stochastic kernel on

\[
\{\mathrm{release},\mathrm{defer},\mathrm{audit}\}.
\]

Let

\[
I_t=\mathbf 1\{A_t\in\{\mathrm{defer},\mathrm{audit}\}\}.
\]

Then the total cost is exactly

\[
C_T=\sum_{t=1}^T I_t,
\]

including all expert deferrals and audits. The update is any measurable rule

\[
Z_t=U_t(Z_{t-1},S_t,A_t,I_tY_t,I_t).
\]

Thus the lower bound includes zero audit probability, forced floors, confidence-triggered audits, posterior sampling, sequential tests, and algorithms that know \(T,\epsilon,L\), the score marginal, and the entire family \(\Theta_T\) except the unknown \(\theta\). Audit floors and estimators are algorithm choices; none is assumed of the data.

The distribution-aware comparator uses a Borel release probability \(a:[0,1]\to[0,1]\) and the same current score, action semantics, and costs:

\[
C^\star_{\theta,T}
=T\inf_{\substack{a\ {\rm Borel}\\
\mathbb E_\theta[a(S)m_\theta(S)]\le1/4}}
\mathbb E_\theta[1-a(S)].
\]

Auditing is unnecessary for this comparator because audit and defer have identical cost, feedback-independent final loss, and release semantics.

Its explicit optimum releases the anchor, releases every cell with \(\theta_i=-1\), defers every cell with \(\theta_i=+1\), and releases the boundary atom \(S=1/2\) with probability

\[
\alpha_\theta
=\frac{1/4-r_\theta}{1/4}=1-4r_\theta,
\]

where

\[
r_\theta
=\frac14m_\theta(0)
 +\frac{1}{4M}\sum_{i:\theta_i=-1}m_\theta(s_i)
=\frac{3}{32}-\frac{\delta}{8}
 -\bar\theta\left(\frac1{16}+\frac{\delta}{8}\right).
\]

Since \(r_\theta\in[1/32-\delta/4,5/32]\), one has \(0<\alpha_\theta<1\). Consequently, the comparator’s expected released error is exactly \(T/4\) on every instance: the constraint is binding.

## Theorem candidate

**Theorem (CICAT priced minimax lower bound).** For every integer \(T\ge8\), let \(\mathcal F_T=\{P_\theta:\theta\in\Theta_T\}\) be the finite i.i.d. family above. Every randomized adaptive algorithm obeying the stated protocol satisfies, with exchange rate \(\eta=2\),

\[
\max_{\theta\in\Theta_T}
\left\{
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
+2\left(
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
-\frac{T}{4}
\right)
\right\}
\ge
\frac{1}{2048}T^{2/3}.
\]

Expectations cover the i.i.d. arrivals, Bernoulli labels, and learner randomization. This is a fixed-horizon expected guarantee; the learner may know the horizon and the family.

Consequently, setting

\[
c_1(1/4,1)=\frac1{2048},
\qquad
c_0=\frac{c_1}{2\eta}=\frac1{8192},
\]

any algorithm satisfying

\[
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
\le \frac{T}{4}+\frac1{8192}T^{2/3}
\qquad\text{for every }\theta\in\Theta_T
\]

must, on at least one instance, satisfy the cost lower bound

\[
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
\ge \frac1{4096}T^{2/3}.
\]

Thus, if proved, CICAT and the standing OBSR upper bound would identify the A1–A3 minimax exponent as \(2/3\), leaving a \(\sqrt{\log T}\)-type polylogarithmic gap.

## Why this can work: proof plan

1. **Comparator and supporting price.** At \(\eta=2\), the expected one-round priced costs are

   \[
   \begin{array}{c|cc}
   &\text{release}&\text{reveal}\\
   \hline
   S=0&2m_\theta(0)<1&1\\
   S=s_i,\ \theta_i=-1&1-2\delta&1\\
   S=1/2&1&1\\
   S=s_i,\ \theta_i=+1&1+2\delta&1 .
   \end{array}
   \]

   Hence the explicit constrained comparator is also a minimizer of the \(\eta\)-priced Lagrangian and has binding risk. The theorem’s left side is therefore its Lagrangian regret. Every wrong hard-cell action costs exactly \(2\delta\); anchor mistakes are nonnegative and the boundary atom is neutral.

2. **Adaptive divergence decomposition.** Pair \(\theta\) and \(\theta^{(i)}\), differing only in bit \(i\). Labels can distinguish them only when the learner reveals hard cell \(i\), or through the weak anchor perturbation \(2\delta/M\). The sequential KL chain rule and

   \[
   \operatorname{kl}(\operatorname{Ber}(p),\operatorname{Ber}(q))
   \le \frac{(p-q)^2}{q(1-q)}
   \]

   give

   \[
   D_{\rm KL}(P_\theta^{\mathcal A}\Vert
              P_{\theta^{(i)}}^{\mathcal A})
   \le
   17\delta^2\frac{T}{4M}
   +40\frac{\delta^2T}{M^2}
   <\frac1{100}.
   \]

   This already allows the learner to reveal every occurrence of cell \(i\), so ordinary deferrals and audits are fully covered.

3. **Testing-to-action lemma.** Pinsker gives pairwise total variation below \(0.071\). At every occurrence of cell \(i\), the sum of the probability of revealing under the safe sign and releasing under the unsafe sign is therefore at least \(3/4\). Since the cell occurs with probability \(1/(4M)\), paired expected wrong actions are at least \(3T/(16M)\).

4. **Hypercube averaging.** Averaging each pair over the uniform product prior on \(\Theta_T\), summing over \(i\), and multiplying by the \(2\delta\) priced gap yields

   \[
   \frac1{2^M}\sum_\theta
   \left[\text{priced regret on }\theta\right]
   \ge \frac{3\delta T}{16}
   =\frac{3T}{1024(M+1)}
   \ge \frac1{512}T^{2/3}.
   \]

   Taking the maximum and weakening the constant gives the stated \(1/2048\).

5. **Two-sided conversion.** On the instance attaining the priced lower bound, subtract at most
   \(2c_0T^{2/3}=c_1T^{2/3}/2\) for allowed error slack, leaving the claimed cost regret.

The riskiest step is formalizing the testing-to-action inequality for adaptive kernels after the current score is observed. The intended proof conditions on \(S_t=s_i\), applies data processing to the pre-action transcript, and uses that the algorithm’s action kernel is identical under the paired instances.

## Attack log

- **Aggregate-only two-point construction rejected.** If uncertainty changes only the amount released from a known boundary cell, the binding multiplier makes every boundary mixture have identical priced value. An algorithm need not learn the aggregate at all. This explains why a simple unknown-mean construction cannot prove the mandatory priced statement.

- **Paired sign swaps rejected.** A local constraint “one safe and one unsafe cell” lets a comparator-optimal deferral reveal one sign and determine its partner. CICAT uses a full product hypercube: learning a high-error cell reveals nothing about any other hard bit.

- **Independent signs without camouflage rejected.** Their aggregate error varies with \(\sum_i\theta_i\), exposing a score-blind diagnostic. The anchor cancels this variation exactly. Its per-bit signal is only \(2\delta/M\), and its contribution is included in the KL bound.

- **Fixed number of cells rejected.** With constant \(M\), one-sided stochastic testing gives only \(\Theta(\sqrt T)\). Global Lipschitzness permits \(M\asymp T^{1/3}\) cells at gap \(\delta\asymp T^{-1/3}\), producing \(M\) constant-difficulty tests and total \(T^{2/3}\) priced regret.

- **Free labels attacked.** On unsafe cells, comparator deferrals indeed reveal labels for free. In the paired comparison, however, the corresponding safe instance fully releases that same independent cell; obtaining its label then costs \(2\delta\) in priced regret. Even revealing all \(T/(4M)\) expected occurrences leaves pairwise KL below \(1/100\).

- **Adaptive audits attacked.** With \(c_R=0\), audit and defer have identical information, cost, and released loss. Combining both into \(I_t\) means the proof already grants the learner the strongest possible use of either action.

- **Camouflage leakage attacked.** Auditing the anchor can estimate \(\bar\theta\), but flipping one bit changes its mean by only \(2\delta/M\). Even \(T\) anchor labels contribute \(O(T\delta^2/M^2)=O(T^{-1/3})\) KL per bit.

- **Always-defer and deliberate error slack attacked.** Because \(\eta=2\) is a common supporting price, always deferring safe or anchor mass has nonnegative priced regret. The corollary allows error slack of the full \(T^{2/3}\) order with the required tied constant, rather than hiding it in a smaller-order condition.

No additional problem assumption was introduced during these repairs; the changes are entirely in the hard-instance mechanism.

## Relation to known results

- Cesa-Bianchi, Lugosi, and Stoltz, “Regret Minimization Under Partial Monitoring,” Theorem 5.1, prove expected cumulative regret at least \(n^{2/3}/7\) for an adversarial three-action label-efficient game, against the best fixed action. The full text and theorem were checked. Its arrivals, comparator, and unconstrained loss matrix differ, so it is an analogy rather than proof evidence; CICAT instead uses i.i.d. contextual instances, a distribution-aware risk-constrained comparator, and priced cost/error regret. [Primary paper](https://cesa-bianchi.di.unimi.it/Pubblicazioni/pmonitoring.pdf)

- Grant and Leslie, “Apple Tasting Revisited,” Theorem 1, obtain Bayesian regret \(O(\sqrt{dT\log T})\) for contextual logistic apple tasting with a fixed finite-dimensional parameter and Thompson sampling. The full text was checked. Its global parametric coupling lets every revealing observation inform the same parameter; CICAT’s \(M=\Theta(T^{1/3})\) Lipschitz cells carry independent nonparametric bits, and its comparator is constrained expected cost rather than a Bayesian roundwise oracle. [Primary paper](https://www.lancaster.ac.uk/staff/grantj/AppleTasting.pdf)

- Harris, Podimata, and Wu, “Strategic Apple Tasting,” Theorem B.1, give a high-probability \(\widetilde O(\sqrt T)\) strategic-regret bound under stochastic contexts with a density lower bound and linear rewards. The full text was checked. This again relies on shared finite-dimensional structure and implicit exploration and does not include a released-error constraint or the OBSR comparator. [NeurIPS paper](https://papers.neurips.cc/paper_files/paper/2023/file/fcd3909db30887ce1da519c4468db668-Paper-Conference.pdf)

- Cesari and Colomboni, “Two-Action Apple Tasting with Switching Costs,” Theorem 3, prove the oblivious minimax expected regret is exactly \(\Theta(\sqrt T)\), even with unit switching costs. The full text was checked. It rules out attributing CICAT’s exponent merely to the two-action revealing graph: CICAT’s proposed obstruction is the growing collection of independent Lipschitz score cells plus a constrained distribution-aware benchmark. [Primary preprint](https://arxiv.org/abs/2606.03851)

- Castro and Nowak, “Minimax Bounds for Active Learning,” Theorem 1 and Appendix A, use finite hypothesis testing and adaptive-sampling KL decompositions for Hölder boundary-fragment classes. The full text was checked. Their labels are acquired through actively selected feature locations, their comparator is a Bayes classifier, and their rate depends on boundary/noise assumptions absent here. Only the finite-packing proof architecture is analogous. [Primary paper](https://nowak.ece.wisc.edu/COLT07.pdf)

- Kleinberg, “Nearly Tight Bounds for the Continuum-Armed Bandit Problem,” Theorems 3.1 and 4.2, gives, for Lipschitz exponent one, an \(O(T^{2/3}\log^{1/3}T)\) upper bound and excludes every smaller polynomial exponent in stochastic and adversarial continuum-armed bandits. The full text was checked. Its mechanism is gap-priced spatial search with feedback from the chosen arm; CICAT uses one-sided paid labels and independent score cells straddling a common constraint price. The matching exponent is therefore not evidence of the same phenomenon. [Primary paper](https://www.cs.cornell.edu/~rdk/papers/ContArm.pdf)

- The standing OBSR result from run 20260716T183433Z-75ac21c9 supplies the corresponding \(O_{\epsilon,L}(T^{2/3}\sqrt{\log(T/\delta)})\) high-probability upper bound under the same A1–A3 assumptions and comparator. This rate was supplied in the brief but its internal proof artifact was not independently rechecked in this fresh context.

A targeted search also located An et al., “Efficient Algorithms for Contextual Apple Tasting with Log-Loss,” a DEMO 2026 workshop submission involving logistic contextual models and LLM cascading. Its full text could not be verified because the primary OpenReview PDF presented an access challenge, so its exact theorem and assumption mapping remain **unverified** and it is not used as proof evidence. [OpenReview record](https://openreview.net/forum?id=VlhBTulTYR)

These checks do not establish novelty; that remains for human review.
