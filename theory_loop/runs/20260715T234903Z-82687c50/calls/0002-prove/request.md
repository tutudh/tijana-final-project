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

# Context: theorem candidate to prove

STATUS: proposed

## Setting and assumption ladder

Consider one cheap model and one authoritative expert. Calling the cheap model costs \(c_M\in[0,1]\) and reveals its prediction \(\widehat Y_t\) and raw score \(S_t\in[0,1]\). Define the unobserved counterfactual cheap-source loss
\[
L_t=\mathbf 1\{\widehat Y_t\neq Y_t\}.
\]
An expert call costs \(1\), returns \(Y_t\), and has zero released-label loss. Correcting an audited error has additional cost \(c_R\in[0,1]\).

Let \(\mathcal F_{t-1}\) contain past model outputs, actions, audit coins, released labels, costs, and expert labels only from deferred or audited rounds. At round \(t\):

1. Before the model call, the learner computes an \(\mathcal F_{t-1}\)-measurable routing policy.
2. It pays \(c_M\), then observes \((\widehat Y_t,S_t)\), but not \(Y_t\) or \(L_t\).
3. It randomizes between cheap routing and expert deferral.
4. Conditional on cheap routing, it chooses an audit probability using only \(\mathcal F_{t-1}\), \((\widehat Y_t,S_t)\), and the routing probability.
5. If deferred or audited, it pays the expert, observes \(Y_t\), and releases \(Y_t\). Otherwise it releases \(\widehat Y_t\).
6. Correction cost \(c_R\) is incurred exactly when an audited cheap prediction is wrong.
7. Only then are calibration and FTRL statistics updated.

Thus routing and audit probabilities are predictable before the current expert label and cheap-source loss.

The assumption ladder is: bounded stationary data with arbitrary score-error relation fails by non-identifiability; the proposed rung adds only global smoothness of the conditional error curve.

**A1 — Stationary stochastic arrivals**

- Mathematical statement: \((S_t,\widehat Y_t,Y_t)_{t\ge1}\) are i.i.d. from an unknown distribution \(P\). The cheap model is fixed during the horizon.
- Operational meaning: workload composition and model behavior do not drift during deployment.
- Diagnostic or falsification: compare score histograms and importance-weighted error estimates across time blocks; apply preregistered change-point or two-sample tests.
- Required by: converting past calibrated risk estimates into conditional risk guarantees for each new routing policy.
- Optimizer-local: `no`
- Classification: `problem`

**A2 — Bounded loss, known costs, safe expert**

- Mathematical statement: \(L_t\in\{0,1\}\); the expert returns \(Y_t\) correctly; \(c_M,c_R\in[0,1]\) and the expert cost \(1\) are fixed and known.
- Operational meaning: expert labels are the deployment reference standard and all paid operations have logged bounded costs.
- Diagnostic or falsification: double-label a random expert sample, adjudicate disagreements, and reconcile model, expert, audit, and correction invoices.
- Required by: released-error validity, concentration, and complete cost accounting.
- Optimizer-local: `no`
- Classification: `problem`

**A3 — Global score-error smoothness**

- Mathematical statement: a version of
  \[
  m(s)=\Pr(L_t=1\mid S_t=s)
  \]
  exists and satisfies \(|m(s)-m(s')|\le L|s-s'|\) for all score-support points, for a finite constant \(L\). No monotonicity or calibration identity such as \(m(s)=1-s\) is assumed.
- Operational meaning: numerically nearby raw scores may be badly calibrated, but their true error rates cannot change arbitrarily abruptly.
- Diagnostic or falsification: on a held-out or importance-weighted audited stream, construct simultaneous binwise error intervals and test whether neighboring-bin differences exceed \(L\) times their separation.
- Required by: competing with all measurable score-routing policies rather than only the algorithm’s histogram class.
- Optimizer-local: `no`
- Classification: `problem`

## Algorithm

Call the method **adaptive calibration-UCB FTRL (ACU-FTRL)**.

For known horizon \(T\), confidence \(\delta\), and target \(\epsilon>0\), set
\[
K=\lceil T^{1/4}\rceil,\qquad
\gamma_t=t^{-1/4},\qquad
z=\log\frac{32KT}{\delta},
\]
and partition \([0,1]\) into \(K\) equal bins \(B_1,\ldots,B_K\).

For each bin \(j\), maintain
\[
N_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\},\quad
H_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\}\frac{O_sL_s}{p_s},\quad
V_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\}\frac1{p_s},
\]
where \(O_s\) indicates that an expert label was observed and \(p_s\) was its predictable probability. When \(O_s=0\), the contribution to \(H\) is recorded as zero without observing \(L_s\).

At \(t=1\), use the expert. For \(t\ge2\), let \(n=t-1\),
\[
\widehat\pi_{t,j}=\frac{N_{t,j}}n,\qquad
\widehat a_{t,j}=\frac{H_{t,j}}n,
\]
and define
\[
r_{t,j}
=
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}{n}
+\sqrt{\frac{z}{2n}},
\qquad
U_{t,j}=\min\{1,\max\{0,\widehat a_{t,j}+r_{t,j}\}\}.
\]
Here \(\widehat a_{t,j}\) estimates the joint error mass
\(\Pr(S\in B_j,L=1)\). The learned conditional calibration is
\[
\widehat m_{t,j}
=
\operatorname{clip}_{[0,1]}
\left(\frac{H_{t,j}}{N_{t,j}\vee1}\right).
\]
The ratios \(U_{t,j}/(\widehat\pi_{t,j}\vee1/n)\), rather than the raw scores, are the confidence-robust calibrated error scores used for routing.

Before seeing \(S_t\), choose the complete routing vector by constrained FTRL:
\[
x_t\in\arg\min_{\substack{x\in[0,1]^K\\
                         \sum_jU_{t,j}x_j\le\epsilon}}
\left\{
\sum_{j=1}^K N_{t,j}(1-x_j)+\frac12\lVert x\rVert_2^2
\right\}.
\]
The first term is cumulative observable expert-deferral cost; the constraint uses cumulative importance-weighted risk feedback. The quadratic term gives deterministic tie-breaking.

After the model call, let \(J_t\) satisfy \(S_t\in B_{J_t}\), set \(x=x_{t,J_t}\), and draw \(D_t\sim\mathrm{Bernoulli}(x)\), where \(D_t=1\) means cheap routing.

- If \(D_t=0\), defer to the expert.
- If \(D_t=1\), audit with probability
  \[
  q_t(x)=
  \begin{cases}
  \displaystyle\frac{[\gamma_t-(1-x)]_+}{x},&x>0,\\
  0,&x=0.
  \end{cases}
  \]

Let \(A_t\) be the audit indicator on a cheap-routed round. Then
\[
O_t=1-D_t+D_tA_t,\qquad
p_t=\Pr(O_t=1\mid\mathcal F_{t-1},S_t)
     =\max\{1-x,\gamma_t\}.
\]
Hence the rule audits only the shortfall between feedback already supplied by expert deferrals and the desired observation floor. Its expected audit probability is
\[
xq_t(x)=[x+\gamma_t-1]_+\le\gamma_t.
\]

The three losses are distinct:

\[
\text{counterfactual cheap loss}=L_t,\qquad
\text{released loss}=R_t=D_t(1-A_t)L_t,\qquad
\text{feedback estimate}=\widetilde L_t=\frac{O_tL_t}{p_t}.
\]

Total cost is
\[
C_T=c_MT+\sum_{t=1}^TO_t
       +c_R\sum_{t=1}^TD_tA_tL_t.
\]

The uniform grid, \(K\), \(\gamma_t\), confidence radii, and quadratic regularizer are algorithm choices. Their audit, estimation, and approximation costs appear separately below.

## Theorem candidate

For a Borel policy \(a:[0,1]\to[0,1]\), let \(a(s)\) be its probability of releasing the cheap label after observing score \(s\). Define the distribution-aware comparator
\[
C_T^\star
=
T\left[
c_M+
\inf_{\substack{a:[0,1]\to[0,1]\ \mathrm{Borel}\\
                  \mathbb E[a(S)m(S)]\le\epsilon}}
\mathbb E[1-a(S)]
\right].
\]
The comparator knows \(P\), but at action time observes only the same model output and score as the learner, never \(Y_t\) or \(L_t\). It has the same deferral, audit, correction, and release actions. Auditing is weakly dominated by immediate expert deferral because both obtain the expert label at the same expert cost while auditing may additionally incur \(c_R\); hence an optimal comparator can use no audits. When deployed on the i.i.d. stream, every feasible comparator has the same \(\epsilon T+O(\sqrt T)\) high-probability released-error semantics.

For \(n\ge1\), define
\[
A_n=\sum_{s=1}^n\gamma_s^{-1},
\]
and, for \(t\ge2\) with \(n=t-1\),
\[
w_t=
\frac{2\sqrt{2KzA_n}}{n}
+\frac{2Kz}{3n\gamma_n}
+2K\sqrt{\frac{z}{2n}}.
\]
Finally let
\[
\begin{aligned}
B_T={}&1+(1+c_R)
 \left(\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}\right)\\
&+\sum_{t=2}^T
 \left(
 2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
 \right)
+\frac1\epsilon
 \left(
 \frac{LT}{K}+\sum_{t=2}^Tw_t
 \right).
\end{aligned}
\]

**Candidate theorem.** For every \(T\ge16\), \(\epsilon\in(0,1]\), \(\delta\in(0,1/4)\), \(c_M,c_R\in[0,1]\), finite \(L\), and every distribution satisfying A1–A3, ACU-FTRL satisfies, simultaneously with probability at least \(1-\delta\) over the i.i.d. arrivals and all learner routing and audit coins,
\[
\sum_{t=1}^T R_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}},
\]
and
\[
C_T\le C_T^\star+B_T.
\]
Moreover, for a universal constant \(C_0\),
\[
B_T
\le
C_0\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\]
Thus, for fixed \((\epsilon,L,c_M,c_R,\delta)\), released error is
\(\epsilon T+O(\sqrt{T\log T})\) and complete cost regret is
\(O(T^{3/4}\log T)=o(T)\), at the fixed horizon \(T\).

## Why this can work: proof plan

1. **Adaptive importance-weighted calibration.** Conditional on the score and past,
   \[
   \mathbb E[O_tL_t/p_t\mid S_t,L_t,\mathcal F_{t-1}]=L_t.
   \]
   Decompose \(\widehat a_{t,j}-a_j\) into an i.i.d. bin-loss fluctuation and an audit martingale. Freedman’s inequality gives, simultaneously over \(t,j\),
   \[
   a_j=\Pr(S\in B_j,L=1)\le U_{t,j}.
   \]

2. **Per-round population safety.** Since \(x_t\) is computed before the current score and \(U_t^\top x_t\le\epsilon\),
   \[
   \mathbb E[x_{t,J_t}L_t\mid\mathcal F_{t-1}]
   =\sum_ja_jx_{t,j}\le\epsilon.
   \]
   Auditing can only reduce released loss. A stopped Azuma argument then yields the stated realized-error bound.

3. **Comparator discretization.** For any feasible measurable \(a\), set
   \(b_j=\mathbb E[a(S)\mid S\in B_j]\). This preserves expected deferral cost. Lipschitzness gives
   \[
   \sum_ja_jb_j\le\mathbb E[a(S)m(S)]+\frac LK
   \le\epsilon+\frac LK.
   \]

4. **Robust-feasibility scaling without an optimizer margin.** On the confidence event,
   \(U_t^\top b\le\epsilon+L/K+w_t\). Therefore
   \[
   y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
   \]
   is feasible for the round-\(t\) FTRL problem, and its extra expert cost is at most
   \((L/K+w_t)/\epsilon\). This uses the globally safe expert, not strict complementarity or a margin at an unknown threshold.

5. **FTRL cost comparison.** Hoeffding bounds for the fully observed bin frequencies and FTRL optimality imply
   \[
   \mathbb E[1-x_{t,J_t}]
   \le
   \mathbb E[1-a(S)]
   +2K\sqrt{\frac{z}{2(t-1)}}
   +\frac{K}{2(t-1)}
   +\frac{L/K+w_t}{\epsilon}.
   \]

6. **Audit and realized-cost accounting.** The adaptive rule adds at most \(\gamma_t\) expected expert calls and \(c_R\gamma_t\) expected correction cost. A bounded martingale controls realized cost. Balancing
   \[
   \sum_t\gamma_t,\quad
   \sum_t w_t,\quad
   K\sqrt T,\quad
   \frac{T}{K}
   \]
   with \(K=T^{1/4}\) and \(\gamma_t=t^{-1/4}\) gives \(T^{3/4}\) up to logarithms.

The riskiest step is the simultaneous binwise Freedman bound under the feedback probability \(p_t=\max\{1-x_{t,J_t},\gamma_t\}\), because the same importance-weighted observations subsequently determine both \(U_t\) and the FTRL action. A stopped-filtration proof must verify this without conditioning on a future confidence event.

## Attack log

- **A1–A2 without score regularity failed.** Partition the score space into \(M\) regions whose error rates are independently either \(0\) or \(2\epsilon\). A distribution-aware comparator releases cheaply exactly on the safe regions. With \(M\) comparable to \(T\), sublinear expert feedback leaves a constant fraction unidentified: releasing there can violate the error target, while deferring there causes linear cost regret. This is an identifiability obstruction, not a claimed formal lower-bound theorem. It motivated A3.

- **A raw-score threshold was rejected.** No monotonic relationship between score magnitude and error is assumed. Routing uses learned binwise conditional errors, and the continuum comparator may select disjoint score regions.

- **Naive plug-in calibration failed.** Downward estimation errors can make an adaptively selected policy violate the risk constraint. Replacing plug-in estimates with simultaneous joint-error upper bounds makes every deployed policy conditionally safe.

- **Oblivious auditing was wasteful.** A floor \(\gamma_t\) applied after every cheap action wastes labels when FTRL already defers frequently. The chosen rule makes the overall observation probability exactly \(\max\{1-x,\gamma_t\}\), auditing only the shortfall.

- **Faster audit decay failed the variance balance.** With \(K\) bins and observation floor \(t^{-a}\), importance-weighted calibration contributes approximately
  \(\sqrt K\,T^{(1+a)/2}\), audits contribute \(T^{1-a}\), and discretization contributes \(T/K\). Balancing these terms gives \(a=1/4\) and \(K=T^{1/4}\).

- **An exact-boundary comparator initially appeared to require a margin.** Rather than assume separation or strict complementarity at its unknown threshold, the proof scales its binned policy toward the known safe expert, paying the explicit \(1/\epsilon\) sensitivity factor.

- **Cost leakage checks passed.** The comparator also pays every model call. Learner deferrals, audits, and audited corrections are all charged. Exploration audits remain entirely in regret.

- **Phase-split and finite-library checks passed.** Calibration and routing update every round; there is no full-audit prefix or frozen deployment phase. The \(K\)-bin class is a structural approximation to all measurable score policies, not an arbitrary preregistered policy library.

## Relation to known results

- **Offline PAC labeling.** Candès, Ilyas, and Zrnic, [“Probably Approximately Correct Labels”](https://arxiv.org/abs/2506.10908), Theorem 1 and Corollary 1, give high-probability error control on a fixed transductive dataset; Section 2.1 learns recalibrated uncertainty using a small labeled subset. Feedback is collected offline, there is no online cost-regret comparator, and cost-sensitive routing is not accompanied by this candidate’s adaptive regret theorem. Full text checked. The present candidate differs by continuously learning calibration from predictable partial feedback and comparing total sequential cost with a distribution-aware policy.

- **Active sequential risk control.** Xu, Karampatziakis, and Mineiro, [“Active, Anytime-Valid Risk Controlling Prediction Sets”](https://papers.nips.cc/paper_files/paper/2024/file/6eb05d8bc6bd7bb6868c64b5802125bd-Paper-Conference.pdf), Theorem 2, considers an i.i.d. stream, predictable covariate-dependent label probabilities with a floor, and importance-weighted e-processes. It guarantees population risk control simultaneously over time with probability \(1-\alpha\); its label budget is separate and it has no total-cost regret against a routing comparator. Full text checked. It supports the predictability and importance-weighting mechanism, but not the FTRL cost claim.

- **Label-efficient prediction.** Cesa-Bianchi, Lugosi, and Stoltz, [“Minimizing Regret With Label Efficient Prediction,” IEEE TIT 51(6), 2005](https://cesa-bianchi.di.unimi.it/Pubblicazioni/J22.pdf), Theorems 1–2, use Bernoulli label queries and importance-weighted losses for bounded individual outcome sequences. Against the best of finitely many constant predictors, they obtain expected and high-probability regret of order \(T\sqrt{\log N/m}\) with \(m\) queried labels. They have no released-label correction, risk constraint, score calibration, or complete cost comparator. Full text checked. Their query-variance tradeoff is an analogy for the audit term.

- **Constrained online optimization.** Mahdavi, Jin, and Yang, [“Trading Regret for Efficiency: Online Convex Optimization with Long Term Constraints,” JMLR 13, 2012](https://www.jmlr.org/papers/volume13/mahdavi12a/mahdavi12a.pdf), Theorem 8, gives zero cumulative violation and \(O(T^{3/4})\) regret for full-information convex online optimization. It assumes known constraints and Assumption 1, a nonzero boundary-gradient condition. That condition is inadmissible here because it is local to a tightened constraint boundary. Full text checked. ACU-FTRL instead learns the constraint from partial labels and uses upper-confidence feasibility plus scaling toward the safe expert.

- **Concentration tool.** Freedman, [“On Tail Probabilities for Martingales,” Annals of Probability 3(1), 1975](https://projecteuclid.org/euclid.aop/1176996396), Theorem 1.6, is the intended predictable-variance inequality. The original full text was not checked in this run, so this primary citation is marked **unverified**; the exact scalar statement was checked through Tropp’s Theorem 1.1 restatement. It is proof machinery, not evidence of novelty.

No absence-of-prior-work claim is made; novelty and correctness require human review.
