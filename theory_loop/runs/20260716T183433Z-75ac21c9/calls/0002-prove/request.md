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
potentially stronger, contribution shape. For this run the pairing is
already half-filled: the positive half is the existing ACU-FTRL theorem at
the A1–A3 rung (listed under "What already exists"), and the sought half is
a minimax lower bound at the SAME rung matching its `T^{3/4}` rate — or,
failing that honestly, an admissible algorithm beating the rate. The next
section makes this binding.

## This run's target (binding): resolve whether T^{3/4} is optimal

Run 20260715T234903Z-82687c50 (ACU-FTRL, listed below) achieves, under A1
(i.i.d. arrivals), A2 (perfect unit-cost expert, known bounded costs), A3
(globally Lipschitz conditional error curve `m(s) = Pr(L=1 | S=s)` with
constant `L`), and `epsilon in (0,1]`: released error
`epsilon*T + O~(sqrt(T))` and cost regret
`O~((1 + c_R + (1+L)/epsilon) T^{3/4})` against the expected-cost benchmark
over ALL Borel score-routing policies, with fully adaptive audits (floor
`t^{-1/4}`, shortfall-only) and no phase split. The open question this run
must attack: **is `T^{3/4}` the minimax cost-regret rate for this exact
setting, or can an admissible adaptive algorithm achieve `o(T^{3/4})`?**

**Primary target — a minimax lower bound with exact setting parity.** The
theorem shape is a trade-off statement: there exist constants `c0 > 0`,
`c1(epsilon, L) > 0`, an explicit exchange rate `eta > 0`, and a finite
family of instances, each satisfying A1–A3 with the SAME stated
`(epsilon, L)`, such that every algorithm obeying the protocol below
satisfies

```
max over the family of
  ( E[C_T] - C_T^star + eta * ( E[sum_t R_t] - epsilon*T ) )
  >= c1 * T^{3/4},
```

equivalently: any algorithm whose expected released error is at most
`epsilon*T + c0*T^{3/4}` on EVERY instance of the family must have expected
cost regret at least `(c1/2) * T^{3/4}` on at least one instance.
Expectation semantics suffice: an expectation lower bound already
contradicts any high-probability upper bound, so it closes the gap against
the positive result. Heuristic mechanism (guidance, not mandate): Assouad or
change-of-measure over sign perturbations of `m` around the comparator
threshold — `M` cells of width `w`, height `Delta <= L*w`; identifying one
cell needs about `1/Delta^2` expert labels at flat unit price each, against
per-round misclassification cost about `Delta/lambda`; balancing gives
`T^{3/4}`. Contrast with Lipschitz bandits' `T^{2/3}`, where exploring an
arm costs its gap `Delta` rather than a unit expert fee — the flat label
price is what pushes the rate up, and the relation-to-known-results section
must state this contrast explicitly.

**Setting-parity checklist (binding; violating any item voids the
candidate):**

1. **Instance admissibility.** Every instance in the family is i.i.d. (A1),
   has a perfect unit-cost expert with fixed known costs
   `c_M, c_R in [0,1]` shared across the family (`c_M = c_R = 0` is allowed
   and encouraged for cleanliness) (A2), and has `m` Lipschitz with the SAME
   constant `L` quantified in the theorem (A3). No nonstationary, heavier-
   tailed, or non-Lipschitz instances; a lower bound proved outside the
   positive result's assumption rung resolves nothing. The risk constraint
   must be binding at the comparator on every instance.
2. **Information-protocol parity.** The learner pays `c_M`, observes
   `(Yhat_t, S_t)`, then observes `Y_t` exactly on deferred or audited
   rounds at unit expert cost each (plus `c_R` per corrected audited error),
   and observes nothing about `Y_t` on released rounds. Deferral rounds
   yield labels too — the construction must not treat audits as the only
   label channel; exploration cost on a safe cell is the excess deferral
   (or audit) fee relative to the comparator who releases there. The joint
   law of `(S_t, Yhat_t)` must be identical across all instances in the
   family, so that only paid expert labels carry information about the
   unknown signs; otherwise the divergence accounting must explicitly
   include the model-output channel.
3. **Learner generality.** The bound must hold for every randomized,
   adaptively auditing algorithm over the same action set (release / defer /
   audit-and-correct). The learner may know `T`, `epsilon`, `L`, `delta`,
   the score marginal, and the entire instance family up to the unknown
   sign pattern. Extra learner knowledge strengthens the lower bound; do
   not manufacture hardness by hiding structure the positive result does
   not hide.
4. **Benchmark parity.** The comparator is the same expected-cost benchmark
   `C_T^star = T * [ c_M + inf over Borel feasible a of E[1 - a(S)] ]` used
   by ACU-FTRL, computed per instance, with identical cost accounting on
   both sides (`c_M*T` is common and cancels in regret).
5. **Error-slack honesty.** The statement must tolerate error slack of
   order `T^{3/4}` (the `c0*T^{3/4}` above), because cost and error trade
   at a bounded exchange rate; a lower bound that binds only algorithms
   with zero or `O(sqrt(T))` slack is an inadmissible resolution.

**Acceptable alternative resolution.** If the honest attack reveals that
`T^{3/4}` is beatable, an admissible algorithm with cost regret
`o(T^{3/4})` under A1–A3 — same protocol, same benchmark, both guarantees,
no retired crutches (full-audit prefix, preregistered finite library,
optimizer-local margins) — resolves the question in the other direction and
is equally welcome. Not acceptable: a lower bound violating the checklist,
or a positive result that changes the comparator class or assumption rung
to manufacture an improvement.

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
  benchmark over all Borel score policies. Do not re-derive it or propose
  variants that merely re-tune its constants; this run's job is the matching
  lower bound or a strictly better rate.
- The offline LP / dual-price view is an explanatory reformulation, not a
  novelty claim.

## Literature lanes

Online risk control; intermittent or partial-feedback conformal methods;
online calibration and calibeating; label-efficient prediction and selective
sampling; bandits with knapsacks and constrained contextual bandits; online
learning with long-term constraints and online primal-dual methods; online
stochastic linear programming; revenue management; online learning to defer.
For the lower bound specifically: label-efficient prediction lower bounds
(Cesa-Bianchi–Lugosi–Stoltz query-budget tradeoffs); continuum-armed and
Lipschitz bandit lower bounds (Kleinberg's `T^{2/3}`; zooming-dimension
refinements) — note their gap-priced exploration differs from this
problem's flat label price; minimax rates for nonparametric active learning
(Castro–Nowak); bandits-with-knapsacks lower bounds; selective-sampling and
apple-tasting lower bounds; standard adaptive-sampling change-of-measure
tools (Assouad, Fano, divergence decompositions for sequentially chosen
observations). Follow the literature policy's exact-source discipline;
absence of found prior work is never evidence of novelty.

## Honesty

Every model output is a theorem or proof candidate. A reviewer `pass` is a
workflow status, not an established result. Promotion into the paper or the
research-state documents requires human review.

# Context: theorem candidate to prove

STATUS: proposed

## Setting and assumption ladder

One cheap source is called every round. It returns \((\widehat Y_t,S_t)\), with \(S_t\in[0,1]\), after incurring cost \(c_M\). Let

\[
L_t=\mathbf 1\{\widehat Y_t\neq Y_t\}
\]

be its counterfactual loss. An expert has unit cost, returns \(Y_t\), and has zero loss. An audited error would additionally cost \(c_R\), but the proposed algorithm uses expert deferrals, not audits.

Let \(\mathcal F_{t-1}\) contain all past model outputs, actions, expert labels, and learner randomness. After observing \((\widehat Y_t,S_t)\), the learner chooses a predictable release probability. If it releases, it observes neither \(Y_t\) nor \(L_t\), and the final released-label loss is \(R_t=L_t\). If it defers, it pays one, observes \(Y_t,L_t\), and \(R_t=0\). Thus counterfactual loss \(L_t\), released loss \(R_t\), and estimated feedback remain distinct.

The distribution-aware comparator class is all Borel \(a:[0,1]\to[0,1]\), where \(a(s)\) is the probability of release after observing score \(s\):

\[
C_T^\star
=
T\left[c_M+
\inf_{\substack{a\ \mathrm{Borel}\\
\mathbb E[a(S)m(S)]\le \epsilon}}
\mathbb E[1-a(S)]\right],
\qquad
m(s)=\Pr(L=1\mid S=s).
\]

It knows the stationary distribution but not the current \(Y_t\) or \(L_t\). It calls the same model and uses the same release/defer actions. Auditing is dominated by deferral because both reveal and correct the label while auditing may also incur \(c_R\).

The assumption ladder is A1–A3 exactly.

**A1 — stochastic arrivals**

- Mathematical statement: \((S_t,\widehat Y_t,Y_t)_{t=1}^T\) are i.i.d.
- Operational meaning: the deployment population is stationary and items do not react to previous routing decisions.
- Diagnostic or falsification: compare score, prediction, and audited-error distributions across time blocks; test serial dependence and change points.
- Required by: unbiased stochastic saddle gradients, comparison with the distribution-aware expected benchmark, and martingale concentration.
- Optimizer-local: no.
- Classification: problem.

**A2 — bounded costs and safe expert**

- Mathematical statement: \(L_t\in\{0,1\}\); the expert has deterministic cost \(1\) and loss \(0\); fixed known \(c_M,c_R\in[0,1]\) are shared across time and instances.
- Operational meaning: expert decisions are authoritative and all charged components are bounded and known.
- Diagnostic or falsification: audit expert disagreement and billing logs; verify that expert, model, and correction charges do not vary outside their declared ranges.
- Required by: bounded importance estimates, concentration, and the global safe policy \(a\equiv0\), which bounds an optimal dual multiplier by \(1/\epsilon\).
- Optimizer-local: no.
- Classification: problem.

**A3 — global score regularity**

- Mathematical statement: a version of \(m:[0,1]\to[0,1]\) satisfies
  \[
  |m(s)-m(s')|\le L|s-s'|
  \quad\text{for all }s,s'\in[0,1],
  \]
  for a stated finite \(L\).
- Operational meaning: nearby confidence scores have nearby conditional error rates globally, including away from the optimal routing boundary.
- Diagnostic or falsification: use held-out or cross-fitted expert labels to compare multiscale bin differences against \(L\) times bin separation, with sampling uncertainty.
- Required by: the \(LT/K\) error-only discretization bound against all Borel policies.
- Optimizer-local: no.
- Classification: problem.

No margin, density lower bound, unique dual price, strict complementarity, or optimizer-local curvature is assumed.

The horizon-dependent bin count, reveal floor, dual cap, and step sizes below are algorithm choices. Their respective charges are \(LT/K\) error approximation, \(\gamma T\) comparator smoothing, and importance-weighted variance. They are not assumptions about the data.

## Algorithm

Call the algorithm **One-Sided Barrier Saddle Routing (OBSR)**. Given \(T,\epsilon,L\) and a tuning constant \(\rho\in(0,1)\), set

\[
K=\left\lceil \max\{1,4L/\rho\}T^{1/4}\right\rceil,\qquad
\gamma=T^{-3/8},\qquad
\Lambda=2/\epsilon,
\]

and partition \([0,1]\) into \(K\) equal intervals. Let \(b(s)\) denote the bin containing \(s\), and let

\[
\bar\epsilon=\min\{1,\epsilon+L/K\}.
\]

State variables are a release vector \(x_t\in[0,1-\gamma]^K\), a dual price \(\lambda_t\in[0,\Lambda]\), and the accumulated squared dual gradients. Initialize \(x_1=0\), \(\lambda_1=0\). Use the one-sided log barrier

\[
\Psi(x)=-\sum_{b=1}^K\log(1-x_b).
\]

At round \(t\):

1. From \(\mathcal F_{t-1}\), fix \(x_t,\lambda_t\). Pay \(c_M\), call the cheap source, and observe \((\widehat Y_t,S_t)\). Put \(b_t=b(S_t)\).

2. Set \(q_t=1-x_{t,b_t}\ge\gamma\). Draw a fresh predictable coin \(D_t\sim\mathrm{Bernoulli}(q_t)\).

   - If \(D_t=0\), release \(\widehat Y_t\). Pay no expert or correction cost, observe no label, and incur the unobserved loss \(R_t=L_t\).
   - If \(D_t=1\), defer to the expert, pay one, observe \(Y_t\) and \(L_t\), release \(Y_t\), and incur \(R_t=0\).

   No audit-and-correct action is used.

3. Form the computable importance-weighted counterfactual feedback

   \[
   \widetilde L_t=\frac{D_tL_t}{q_t}.
   \]

   Conditional on the current score and past,
   \(\mathbb E[\widetilde L_t\mid S_t,\mathcal F_{t-1}]=m(S_t)\).

4. Form the primal and dual gradient estimates

   \[
   g_t=e_{b_t}\bigl(-1+\lambda_t\widetilde L_t\bigr),
   \qquad
   h_t=x_{t,b_t}\widetilde L_t-\bar\epsilon.
   \]

5. With
   \[
   \eta_x=
   \sqrt{\frac{K\log(1/\gamma)}
   {2(1+\Lambda^2)T}},
   \]
   update
   \[
   x_{t+1}
   =
   \arg\min_{x\in[0,1-\gamma]^K}
   \left\{\eta_x\langle g_t,x\rangle+
   D_\Psi(x,x_t)\right\}.
   \]

   This is a one-coordinate, one-dimensional convex update.

6. Set
   \[
   \eta_{\lambda,t}
   =
   \frac{\Lambda}{\sqrt{1+\sum_{u=1}^t h_u^2}},
   \qquad
   \lambda_{t+1}
   =
   \Pi_{[0,\Lambda]}
   \bigl(\lambda_t+\eta_{\lambda,t}h_t\bigr).
   \]

The total realized cost is exactly

\[
C_T=c_MT+\sum_{t=1}^T D_t.
\]

## Theorem candidate

**Candidate theorem.** There is a universal constant \(C_0<\infty\) such that the following holds. For every \(T\ge16\), \(\epsilon\in(0,1]\), \(L\ge0\), \(\rho,\delta\in(0,1)\), every \(c_M,c_R\in[0,1]\), and every distribution satisfying A1–A3, run OBSR with the parameters above and define

\[
\ell_T=\log\frac{16KT}{\delta},
\]

\[
\mathcal G_T
=
C_0(1+\epsilon^{-1})^2
\left[
\sqrt{KT\ell_T}
+
\sqrt{\frac{T\ell_T}{\gamma}}
+
\frac{\ell_T}{\gamma}
\right].
\]

Then, with probability at least \(1-\delta\), simultaneously over the i.i.d. data, all routing coins, and all observed expert labels,

\[
\boxed{
\sum_{t=1}^T R_t
\le
\epsilon T+\frac{LT}{K}+\mathcal G_T
}
\]

and

\[
\boxed{
C_T
\le
C_T^\star+\gamma T+\mathcal G_T.
}
\]

In particular,

\[
\sum_{t=1}^T R_t
\le
\epsilon T+\frac{\rho}{4}T^{3/4}
+
O_{\epsilon,L,\rho}\!\left(T^{11/16}\sqrt{\log(T/\delta)}\right),
\]

while

\[
C_T-C_T^\star
=
O_{\epsilon,L,\rho}\!\left(T^{11/16}\sqrt{\log(T/\delta)}\right)
=
o(T^{3/4}).
\]

For any proposed lower-bound constant \(c_0>0\), choosing
\(\rho\le\min\{1/2,2c_0\}\) gives, for all sufficiently large \(T\),

\[
\sum_tR_t\le\epsilon T+c_0T^{3/4}
\quad\text{and}\quad
C_T-C_T^\star=o(T^{3/4}).
\]

Thus this candidate, if proved, rules out the binding \(T^{3/4}\) lower-bound shape. Taking \(\delta=T^{-3}\) also gives the corresponding expectation bounds, up to an additive \(O(1)\).

## Why this can work: proof plan

1. **Borel-to-bin coarsening.** For any feasible Borel \(a\), define
   \(x_b=\mathbb E[a(S)\mid S\in B_b]\). Since \(m\) varies by at most \(L/K\) inside a bin,

   \[
   \mathbb E[x_{b(S)}m(S)]
   \le
   \mathbb E[a(S)m(S)]+L/K.
   \]

   Its release mass is unchanged. Hence binning costs no comparator cost; it only relaxes the error budget by \(L/K\).

2. **Reveal-floor smoothing.** Replace the binned comparator by
   \(x^\gamma=(1-\gamma)x\). It remains feasible, has expert probability at least \(\gamma\), and increases expected cost by at most \(\gamma\) per round.

3. **One-sided barrier lemma.** Although \(\widetilde L_t\) contains \(1/q_t\), the inverse Hessian of \(-\log(1-x_{b_t})\) contributes \(q_t^2\). Consequently,

   \[
   \|g_t\|_{(\nabla^2\Psi(x_t))^{-1}}^2
   \le 2(1+\Lambda^2)
   \]

   pathwise. Primal regret should therefore be
   \(O((1+\Lambda)\sqrt{KT\log(1/\gamma)})\), rather than carrying a \(1/\gamma\) factor.

4. **Variance-adaptive dual lemma.** The dual estimate is unbiased and has conditional second moment \(O(1/q_t)\). Freedman concentration and the AdaGrad update should give

   \[
   O\!\left(
   \Lambda\sqrt{T\log(1/\delta)/\gamma}
   +\Lambda\log(1/\delta)/\gamma
   \right).
   \]

5. **Exact-penalty conversion.** The always-expert policy has constraint value \(-\bar\epsilon\) and cost one. Therefore every optimal dual multiplier for the binned population problem is at most \(1/\bar\epsilon\le1/\epsilon\). With \(\Lambda=2/\epsilon\), the stochastic saddle residual controls both positive constraint violation and cost regret; no optimizer-local dual condition is needed.

6. **Realized quantities.** Apply martingale concentration to replace fractional expected expert cost by \(\sum D_t\), and conditional released risk \(x_{t,b_t}m(S_t)\) by the unobserved realized \(\sum R_t\). Add the common \(c_MT\).

The single riskiest step is the high-probability coupled saddle lemma combining the barrier primal update with the importance-weighted AdaGrad dual update. In particular, its proof must avoid silently replacing the adaptive dual sequence by a fixed multiplier.

## Attack log

- **Below A3:** with an arbitrary measurable \(m\), place independent error probabilities on \(T\) score atoms. Competing with all Borel policies then requires learning linearly many unrelated coordinates. A sublinear joint guarantee is not credible, so global Lipschitz regularity remains necessary.

- **Sign-swap Assouad attack:** take \(M=T^{1/4}\) score pairs and gap \(\Delta=T^{-1/4}\), with the comparator releasing the low-error atom and deferring the high-error atom in each pair. This does not produce the requested lower bound. The learner can initially defer one arbitrary atom per pair, release the other, and keep exactly the comparator’s total cost. Its ordinary deferrals provide \(\Theta(\Delta^{-2})\) labels per pair by calendar time \(M\Delta^{-2}=T^{3/4}\); the cumulative excess error before identification is only
  \(\Delta T^{3/4}=O(\sqrt T)\). Treating audits as the only label channel would incorrectly manufacture the lower bound.

- **Null-versus-positive-bumps attack:** making the null comparator release everything removes free labels, but the learner can estimate aggregate bump mass parametrically and use score-independent randomized deferral. The advantage of locating height-\(\Delta\) bumps is only second order when the baseline error is bounded away from zero. This also failed to support a \(T^{3/4}\) lower bound with honest error slack.

- **No reveal floor:** \(q_t=0\) makes the estimator undefined and permits unbounded dual variance. This obstruction motivates the algorithmic floor \(\gamma\).

- **Euclidean primal update:** its variance scales as \(1/\gamma\), recreating the ACU-FTRL balance. The one-sided log barrier is introduced specifically to cancel this factor in the primal local norm.

- **Charging binning to cost:** conservative bin feasibility would add \(LT/K\) to cost regret and preserve the \(T^{3/4}\) barrier. OBSR instead enlarges only the error budget, so every coarsened Borel comparator remains available without losing release mass.

- **Accounting attack:** model cost \(c_MT\) is paid by both sides and retained in both definitions. Expert labels from deferrals cost one. The algorithm performs no corrections, so it does not omit any \(c_R\) charge.

- **Rare-score attack:** no bin-density lower bound is used. Updates occur on the realized stochastic contexts; rare bins contribute proportionally little to both learner and comparator objectives.

## Relation to known results

- Cesa-Bianchi, Lugosi, and Stoltz, [“Regret Minimization Under Partial Monitoring,” *Mathematics of Operations Research* 31(3), 2006](https://doi.org/10.1287/moor.1060.0206), Theorem 4.1 and Example 3.3. The full primary text was checked. The theorem gives high-probability \(O(T^{2/3}(\log(N/\delta))^{1/3})\) regret against a best fixed action under adversarial finite partial monitoring when a revealing action exists; Example 3.3 identifies apple tasting. It has neither stochastic contexts nor a risk constraint, distribution-aware Borel comparator, or separate error/cost guarantees. It is evidence for the revealing-action obstruction, not a reusable theorem for OBSR.

- Yu, Neely, and Wei, [“Online Convex Optimization with Stochastic Constraints,” NeurIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/file/a11ce019e96a4c60832eadd755a17a58-Paper.pdf), Theorem 2 and Section 4. The full primary text was checked. They obtain \(O(\sqrt T)\) expected regret and violation, and \(O(\sqrt{T\log T})\)-type high-probability bounds, for i.i.d. stochastic constraint functions revealed after every decision. Their feedback is full-function feedback, unlike labels observed only on expert rounds here. Their drift/exact-penalty logic is analogous, but cannot supply the one-sided importance-weighted saddle lemma.

- Kleinberg, [“Nearly Tight Bounds for the Continuum-Armed Bandit Problem,” NeurIPS 2004](https://proceedings.neurips.cc/paper_files/paper/2004/file/b75bd27b5a48a1b48987a18d831f6336-Paper.pdf), Theorems 3.1 and 4.2. The full primary text was checked. For a one-dimensional Lipschitz expected cost, the paper gives \(O(T^{2/3}\log^{1/3}T)\) regret and a matching exponent lower bound against the best fixed arm, with the played arm’s cost observed. There, exploring a near-optimal arm costs its gap \(\Delta\). Here, an extra expert decision has flat unit cost relative to releasing, which is why uniform spatial estimation leads to a \(T^{3/4}\) balance. OBSR does not transfer Kleinberg’s result: it claims that deferral-as-action, exact-penalty slack, and one-sided barrier geometry avoid paying that flat fee as cost regret on every informative sample.

- Harris, Podimata, and Wu, [“Strategic Apple Tasting,” NeurIPS 2023](https://papers.neurips.cc/paper_files/paper/2023/file/fcd3909db30887ce1da519c4468db668-Paper-Conference.pdf), Theorem 3.3. The full primary text was checked. It proves a high-probability \(\widetilde O(\sqrt T)\) strategic-regret result under stochastic contexts, linear response structure, and a density-ratio condition that supplies implicit exploration. Those assumptions and its fixed-policy comparator do not match A1–A3 or the constrained Borel benchmark. It supports the possibility that stochastic apple-tasting feedback can outperform generic revealing-action rates, but is only an analogy.

The proposed contribution would be the barrier-based partial-feedback saddle lemma plus its use to put Lipschitz discretization entirely into released-error slack while obtaining \(o(T^{3/4})\) total-cost regret. No novelty claim is made without human review.
