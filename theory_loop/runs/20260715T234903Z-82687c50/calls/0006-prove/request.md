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

# Context: previous proof attempt (yours to reuse, repair, or discard)

STATUS: complete

## Exact theorem

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

## Notation and standing assumptions

Let
\[
\pi_j=\Pr(S\in B_j),\qquad
\theta_j=\Pr(S\in B_j,L=1)
       =\mathbb E[\mathbf1\{S\in B_j\}m(S)].
\]
Take bins half-open except for the last, so every score belongs to exactly one bin and every bin has diameter at most \(1/K\).

At \(t=1\), set for analysis
\[
D_1=0,\qquad A_1=0,\qquad O_1=1,\qquad p_1=1.
\]
This is the prescribed expert action.

Let \(\mathcal F_{t-1}\) be the learner’s post-round filtration from the statement. For importance-weighted analysis, enlarge it before the current routing coins to
\[
\mathcal G_{t,-}
=
\sigma(\mathcal F_{t-1},S_t,\widehat Y_t,Y_t).
\]
This analytical enlargement reveals \(L_t\), but only to the proof. The algorithm still chooses \(x_t\) from \(\mathcal F_{t-1}\), and \(q_t,p_t\) from the past and current score, never from \(Y_t\) or \(L_t\).

Conditional on \(\mathcal G_{t,-}\),
\[
O_t\sim{\rm Bernoulli}(p_t),\qquad
p_t=\max\{1-x_{t,J_t},\gamma_t\}\ge\gamma_t.
\]
Indeed,
\[
1-x+xq_t(x)=\max\{1-x,\gamma_t\}.
\]

Since \(\gamma_s=s^{-1/4}\),
\[
A_n=\sum_{s=1}^ns^{1/4}\le n^{5/4}.
\tag{1}
\]

A randomized comparator deployment is interpreted as using fresh independent roundwise uniforms, independent of the arrival stream and of the learner. Given \(S_t=s\), it releases the unaudited cheap label with probability \(a(s)\) and otherwise immediately defers. This makes explicit the randomization convention needed for the comparator’s high-probability error statement; it is not an additional distributional assumption.

## Lemmas

### Lemma 1 — One-sided Bernstein–Freedman inequality

Let \(X_s\) be martingale differences with \(X_s\le b\), and let
\[
V_n=\sum_{s=1}^n\mathbb E[X_s^2\mid\mathcal H_{s-1}].
\]
For \(0<\lambda<3/b\),
\[
\exp\left\{
\lambda\sum_{s=1}^nX_s
-\frac{\lambda^2}{2(1-\lambda b/3)}V_n
\right\}
\]
is a nonnegative supermartingale.

If \(V_n\le v\) deterministically, then for \(z>0\),
\[
\Pr\left(
\sum_{s=1}^nX_s>
\sqrt{2vz}+\frac{2bz}{3}
\right)\le e^{-z}.
\tag{2}
\]

#### Proof

For every \(x\le b\) and \(0<\lambda<3/b\),
\[
e^{\lambda x}
\le
1+\lambda x+
\frac{\lambda^2x^2}{2(1-\lambda b/3)}.
\]
For \(\lambda x\le0\), use \(e^u\le1+u+u^2/2\). For \(0\le x\le b\), expand the exponential and use
\(k!\ge2\cdot3^{k-2}\) for \(k\ge2\).

Conditional expectation, the martingale-difference property, and \(1+u\le e^u\) prove the supermartingale claim. Chernoff optimization gives
\[
\Pr\left(\sum_{s=1}^nX_s\ge x\right)
\le
\exp\left\{-\frac{x^2}{2(v+bx/3)}\right\}.
\]
For \(x=\sqrt{2vz}+2bz/3\),
\[
x^2\ge2z(v+bx/3),
\]
which proves (2). ∎

### Lemma 2 — Adaptive importance-weighted underestimation

For a fixed bin \(j\), define
\[
M_{n,j}
=
\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Except on an event of probability at most \(Te^{-z}\), simultaneously for every \(1\le n\le T\),
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{z}{3\gamma_n},
\tag{3}
\]
where
\[
V_{n,j}=\sum_{s=1}^n\frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\]

#### Proof

Let
\[
X_{s,j}
=
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Conditional on \(\mathcal G_{s,-}\),
\[
\mathbb E[X_{s,j}\mid\mathcal G_{s,-}]=0,\qquad X_{s,j}\le1,
\]
and
\[
\mathbb E[X_{s,j}^2\mid\mathcal G_{s,-}]
=
\mathbf1\{S_s\in B_j\}L_s\left(\frac1{p_s}-1\right)
\le\frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\tag{4}
\]
Thus \(V_{n,j}\) is a predictable quadratic-variation upper bound.

For any \(\mu>0\), put
\[
\lambda=\frac{\mu}{1+\mu/3}\in(0,3).
\]
Lemma 1 and Ville’s inequality show that, except with probability \(e^{-z}\),
\[
M_{n,j}
\le
\frac{\mu V_{n,j}}2+\frac z\mu+\frac z3
\tag{5}
\]
simultaneously over \(n\).

Use the deterministic multiplicative grid between
\[
\mu_{\min}=\sqrt{\frac{2z}{A_T}},
\qquad
\mu_{\max}=\sqrt{2z},
\]
with consecutive ratio at most \(r=1+T^{-1/2}\). Its cardinality is at most
\[
2+\frac{(5/8)\log T}{\log(1+T^{-1/2})}
\le
2+\frac54\sqrt T\log T
\le T
\]
for \(T\ge16\). For the last inequality, writing \(u=\sqrt T\ge4\), the difference
\(u^2-2-(5/2)u\log u\) is nonnegative at \(u=4\) and increasing thereafter.

If \(V_{n,j}=0\), then \(M_{n,j}=0\). Otherwise
\(1\le V_{n,j}\le A_T\), so
\[
\mu^\star=\sqrt{\frac{2z}{V_{n,j}}}
\in[\mu_{\min},\mu_{\max}].
\]
Choose a grid point \(\mu=\rho\mu^\star\), \(1\le\rho\le r\). Then
\[
\frac{\mu V}{2}+\frac z\mu
=
\sqrt{2Vz}\frac{\rho+\rho^{-1}}2
\le
\sqrt{2Vz}+\frac{\sqrt{2Vz}}{2T}.
\tag{6}
\]

Here \(z>8\), since \(T\ge16\), \(K\ge2\), and \(\delta<1/4\). For \(2\le n\le T\), using \(V_{n,j}\le A_n\le n^{5/4}\),
\[
\frac{\sqrt{2V_{n,j}z}}{2T}
\le
\frac{(n^{1/4}-1)z}{3}.
\tag{7}
\]
For \(n=2,3,4\), this follows directly from \(T\ge16,z\ge8\). For \(n\ge5\), use \(T\ge n\) and
\[
\frac34n^{-3/8}\le n^{1/4}-1.
\]
At \(n=1\), \(O_1=p_1=1\), so \(M_{1,j}=0\).

Combining (5)–(7) gives
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{n^{1/4}z}{3}
=
\sqrt{2V_{n,j}z}+\frac z{3\gamma_n}.
\]
Unioning over at most \(T\) grid points proves (3). ∎

### Lemma 3 — Simultaneous calibration validity

Except on an event of probability at most \(2KTe^{-z}\), simultaneously for all \(t\ge2\) and bins \(j\),
\[
\theta_j\le U_{t,j}.
\tag{8}
\]

#### Proof

Let \(n=t-1\) and
\[
E_{n,j}
=
\sum_{s=1}^n\mathbf1\{S_s\in B_j\}L_s.
\]
The summands are i.i.d. Bernoulli with mean \(\theta_j\), so
\[
\Pr\left(
\theta_j-\frac{E_{n,j}}n>
\sqrt{\frac z{2n}}
\right)\le e^{-z}.
\]
Unioning over \(j,n\) costs at most \(KTe^{-z}\).

Moreover,
\[
E_{n,j}-H_{t,j}=M_{n,j}.
\]
Lemma 2, unioned over \(K\) bins, therefore gives
\[
\theta_j
\le
\frac{H_{t,j}}n+
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}n
+\sqrt{\frac z{2n}}
=
\widehat a_{t,j}+r_{t,j}.
\]
Since \(0\le\theta_j\le1\), clipping the right side to \([0,1]\) preserves the inequality. ∎

### Lemma 4 — Population safety and released-error concentration

On the event in Lemma 3, except for one additional event of probability \(e^{-z}\),
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\tag{9}
\]

#### Proof

Define
\[
G_t=\mathbf1\{\theta_j\le U_{t,j}\text{ for every }j\},
\qquad t\ge2,
\]
and \(G_1=1\). Since \(\theta\) is a fixed population vector and \(U_t\) depends only on past observations, \(G_t\) is \(\mathcal F_{t-1}\)-measurable.

When \(G_t=1\),
\[
\begin{aligned}
\mathbb E[D_tL_t\mid\mathcal F_{t-1}]
&=\sum_{j=1}^Kx_{t,j}\theta_j\\
&\le\sum_{j=1}^Kx_{t,j}U_{t,j}
\le\epsilon.
\end{aligned}
\]
Because \(R_t=D_t(1-A_t)L_t\le D_tL_t\),
\[
\mathbb E[G_tR_t\mid\mathcal F_{t-1}]
\le\epsilon G_t\le\epsilon.
\]
The variables
\[
G_tR_t-\mathbb E[G_tR_t\mid\mathcal F_{t-1}]
\]
are martingale differences with conditional range length at most \(1\). Hoeffding–Azuma gives
\[
\sum_{t=1}^TG_tR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\). On Lemma 3’s event, every \(G_t=1\), proving (9) without conditioning a martingale inequality on a future confidence event. ∎

### Lemma 5 — Comparator attainment and discretization

The infimum defining \(C_T^\star\) is attained by a Borel policy \(a^\star\). If
\[
b_j=
\mathbb E[a^\star(S)\mid S\in B_j]
\]
for \(\pi_j>0\), and \(b_j=0\) for \(\pi_j=0\), then
\[
\sum_j\pi_j(1-b_j)
=
\mathbb E[1-a^\star(S)]
\tag{10}
\]
and
\[
\sum_j\theta_jb_j
\le
\epsilon+\frac LK.
\tag{11}
\]

#### Proof

The Lipschitz version of \(m\) on the score support has a Borel Lipschitz extension to \([0,1]\), clipped to \([0,1]\). Thus \(m(S)\) can be represented by a Borel function.

If \(\mathbb E[m(S)]\le\epsilon\), take \(a^\star\equiv1\). Otherwise select \(\lambda\in(0,1]\) such that
\[
\mathbb E[m(S)\mathbf1\{m(S)<\lambda\}]
\le\epsilon
\le
\mathbb E[m(S)\mathbf1\{m(S)\le\lambda\}].
\]
Choose \(\rho\in[0,1]\) so that
\[
a^\star(s)
=
\mathbf1\{m(s)<\lambda\}
+\rho\mathbf1\{m(s)=\lambda\}
\]
satisfies
\[
\mathbb E[a^\star(S)m(S)]=\epsilon.
\]
For every feasible \(a\),
\[
(a-a^\star)(m-\lambda)\ge0
\]
pointwise. Consequently,
\[
\mathbb E[am]-\mathbb E[a^\star m]
\ge
\lambda\big(\mathbb E[a]-\mathbb E[a^\star]\big).
\]
The left side is nonpositive, hence
\(\mathbb E[a]\le\mathbb E[a^\star]\). Thus \(a^\star\) is optimal.

Equation (10) is conditional expectation. For (11), let
\(\bar m_j=\mathbb E[m(S)\mid S\in B_j]\). On a nonempty bin,
\[
|\bar m_j-m(S)|\le\frac LK
\quad\text{a.s. on }B_j.
\]
Therefore
\[
\begin{aligned}
\sum_j\theta_jb_j-\mathbb E[a^\star(S)m(S)]
&=
\sum_j\pi_j
 \mathbb E\!\left[
 a^\star(S)(\bar m_j-m(S))\mid S\in B_j
 \right]\\
&\le\frac LK\sum_j\pi_j
=\frac LK.
\end{aligned}
\]
Feasibility of \(a^\star\) proves (11). ∎

### Lemma 6 — Comparator-directed importance-weighted bound

For the fixed deterministic vector \(b\) from Lemma 5, except on an event \(\mathcal E_b^c\) of probability at most \(2Te^{-z}\), simultaneously for every \(t\ge2\), with \(n=t-1\),
\[
b^\top\left(\frac{H_t}{n}-\theta\right)
\le
\frac{\sqrt{2A_nz}}n
+\frac{2z}{3n\gamma_n}
+\sqrt{\frac z{2n}}.
\tag{12}
\]

#### Proof

Decompose
\[
\begin{aligned}
b^\top H_t-nb^\top\theta
={}&
\sum_{s=1}^n
b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)\\
&+
\sum_{s=1}^n
\big(b_{J_s}L_s-b^\top\theta\big).
\end{aligned}
\tag{13}
\]

The first sum is a martingale. For fixed \(n\), each increment is bounded above by
\[
p_s^{-1}\le\gamma_s^{-1}\le\gamma_n^{-1},
\]
and its conditional second moment is at most \(p_s^{-1}\). Hence its predictable quadratic variation is at most
\[
\sum_{s=1}^np_s^{-1}\le A_n.
\]
Lemma 1 gives
\[
\sum_{s=1}^n
b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)
\le
\sqrt{2A_nz}+\frac{2z}{3\gamma_n}
\]
except with probability \(e^{-z}\).

The second sum in (13) consists of i.i.d. centered variables whose uncentered versions lie in \([0,1]\). Hoeffding gives the upper bound
\[
\sqrt{\frac{nz}{2}}
\]
except with probability \(e^{-z}\). Unioning both bounds over \(n\le T-1\) proves (12). ∎

### Lemma 7 — Robust comparator feasibility

On \(\mathcal E_b\), for every \(t\ge2\),
\[
U_t^\top b\le\epsilon+\frac LK+w_t.
\tag{14}
\]
Thus
\[
y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
\tag{15}
\]
is feasible for the round-\(t\) FTRL problem, and
\[
\pi^\top(1-y_t)
\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon}.
\tag{16}
\]

#### Proof

Since \(H_{t,j},r_{t,j}\ge0\),
\[
U_{t,j}\le\frac{H_{t,j}}n+r_{t,j}.
\]
Cauchy–Schwarz and \(p_s\ge\gamma_s\) give
\[
\begin{aligned}
\sum_jr_{t,j}
&\le
\frac{\sqrt{2Kz\sum_jV_{t,j}}}{n}
+\frac{Kz}{3n\gamma_n}
+K\sqrt{\frac z{2n}}\\
&\le
\frac{\sqrt{2KzA_n}}n
+\frac{Kz}{3n\gamma_n}
+K\sqrt{\frac z{2n}}
=\frac{w_t}{2}.
\end{aligned}
\tag{17}
\]
Because \(K\ge2\), the right side of (12) is at most \(w_t/2\). Hence, using Lemma 5,
\[
U_t^\top b
\le
\theta^\top b+w_t
\le
\epsilon+\frac LK+w_t.
\]
This proves (14), and (15) then satisfies \(U_t^\top y_t\le\epsilon\).

Writing \(\alpha_t=\epsilon/(\epsilon+L/K+w_t)\),
\[
\begin{aligned}
\pi^\top(1-y_t)
&=\pi^\top(1-b)+(1-\alpha_t)\pi^\top b\\
&\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon},
\end{aligned}
\]
which proves (16). ∎

### Lemma 8 — Corrected FTRL deferral comparison

Let
\[
\mathcal E_\pi
=
\left\{
\max_j|\widehat\pi_{t,j}-\pi_j|
\le\sqrt{\frac z{2(t-1)}}
\text{ for every }t\ge2
\right\}.
\]
Then
\[
\Pr(\mathcal E_\pi^c)\le2KTe^{-z}.
\tag{18}
\]
On the intersection \(\mathcal E_b\cap\mathcal E_\pi\), simultaneously for all \(t\ge2\),
\[
\begin{aligned}
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
\le{}&
\mathbb E[1-a^\star(S)]
+2K\sqrt{\frac z{2(t-1)}}\\
&+\frac{K}{2(t-1)}
+\frac{L/K+w_t}{\epsilon}.
\end{aligned}
\tag{19}
\]
Consequently, viewed as an unconditional simultaneous claim, its failure probability is at most
\[
(2KT+2T)e^{-z}.
\tag{20}
\]

#### Proof

For fixed \(n,j\), Hoeffding gives
\[
\Pr\left(
|\widehat\pi_{t,j}-\pi_j|>
\sqrt{\frac z{2n}}
\right)\le2e^{-z}.
\]
Unioning over \(j,n\) proves (18).

On \(\mathcal E_b\), Lemma 7 makes \(y_t\) feasible. FTRL optimality therefore yields
\[
n\widehat\pi_t^\top(1-x_t)+\frac12\|x_t\|_2^2
\le
n\widehat\pi_t^\top(1-y_t)+\frac12\|y_t\|_2^2.
\]
Since \(\|y_t\|_2^2\le K\),
\[
\widehat\pi_t^\top(1-x_t)
\le
\widehat\pi_t^\top(1-y_t)+\frac K{2n}.
\tag{21}
\]
On \(\mathcal E_\pi\), for every \(u\in[0,1]^K\),
\[
\left|
\pi^\top(1-u)-\widehat\pi_t^\top(1-u)
\right|
\le
K\sqrt{\frac z{2n}}.
\]
Applying this twice in (21) gives
\[
\pi^\top(1-x_t)
\le
\pi^\top(1-y_t)
+2K\sqrt{\frac z{2n}}
+\frac K{2n}.
\]
Now apply (16). Finally, since \(x_t\) is \(\mathcal F_{t-1}\)-measurable and \(S_t\) is independent of \(\mathcal F_{t-1}\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
=\pi^\top(1-x_t).
\]
This proves (19). Equation (20) follows from (18) and
\(\Pr(\mathcal E_b^c)\le2Te^{-z}\).

This explicitly repairs the reviewer-identified gap: the comparison is asserted only when both the bin-frequency event and Lemma 6’s robust-feasibility event hold. ∎

### Lemma 9 — Complete realized-cost concentration

Except on an event of probability \(e^{-z}\),
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+\sum_{t=2}^T
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]\\
&+(1+c_R)
\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\tag{22}
\]

#### Proof

For \(t\ge2\), let
\[
W_t=O_t+c_RD_tA_tL_t.
\]
Conditional on the current latent arrival and the past,
\[
\begin{aligned}
\mathbb E[W_t\mid\mathcal G_{t,-}]
&=(1-x_{t,J_t})
+x_{t,J_t}q_t(x_{t,J_t})(1+c_RL_t)\\
&\le
1-x_{t,J_t}+(1+c_R)\gamma_t,
\end{aligned}
\tag{23}
\]
because \(xq_t(x)=[x+\gamma_t-1]_+\le\gamma_t\).

Averaging (23) over the current i.i.d. arrival,
\[
\mathbb E[W_t\mid\mathcal F_{t-1}]
\le
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
+(1+c_R)\gamma_t.
\]
Also \(0\le W_t\le1+c_R\). Hoeffding–Azuma therefore gives
\[
\sum_{t=2}^TW_t
\le
\sum_{t=2}^T\mathbb E[W_t\mid\mathcal F_{t-1}]
+(1+c_R)\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

Every round pays \(c_M\), and round \(1\) pays exactly one expert cost. Enlarging \(\sum_{t=2}^T\gamma_t\) to \(\sum_{t=1}^T\gamma_t\) proves (22). ∎

### Lemma 10 — Comparator action, cost, and probability parity

For any feasible Borel \(a\), its fresh-independent no-audit deployment has expected total cost
\[
T\left(c_M+\mathbb E[1-a(S)]\right),
\]
and for every \(u>0\),
\[
\Pr\left(
\sum_{t=1}^TR_t^{\rm comp}>
\epsilon T+\sqrt{\frac{Tu}{2}}
\right)\le e^{-u}.
\tag{24}
\]
Allowing the comparator to audit cannot reduce its cost below the no-audit benchmark.

#### Proof

Under the specified deployment, the comparator immediately defers with probability \(1-a(S)\) and otherwise releases the unaudited cheap label. It therefore pays \(c_M\) always, pays the expert with probability \(1-a(S)\), and pays no correction cost.

Its released loss has mean
\[
\mathbb E[a(S)L]=\mathbb E[a(S)m(S)]\le\epsilon.
\]
The arrivals and comparator uniforms are independent across rounds, so these released losses are independent \([0,1]\)-valued variables. Hoeffding proves (24).

If a comparator audits a cheap-routed item, replacing that audit by immediate deferral produces the same authoritative released label and the same unit expert cost, while removing the possible \(c_R\) correction charge. Thus an optimal comparator uses no audits. ∎

## Main proof

Let the following events hold:

- \(\mathcal E_{\rm cal}\): Lemma 3’s simultaneous calibration event;
- \(\mathcal E_b\): Lemma 6’s comparator-directed event;
- \(\mathcal E_\pi\): Lemma 8’s empirical-frequency event;
- \(\mathcal E_R\): Lemma 4’s masked released-error martingale event;
- \(\mathcal E_C\): Lemma 9’s cost martingale event.

Their total failure probability is at most
\[
\left(2KT+2T+2KT+2\right)e^{-z}.
\]
Since
\[
e^{-z}=\frac{\delta}{32KT},
\]
this is strictly less than \(\delta\).

On \(\mathcal E_{\rm cal}\cap\mathcal E_R\), Lemma 4 gives
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\]

On \(\mathcal E_b\cap\mathcal E_\pi\cap\mathcal E_C\), combine Lemmas 8 and 9:
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+(T-1)\mathbb E[1-a^\star(S)]\\
&+\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)\\
&+\frac1\epsilon
\sum_{t=2}^T\left(\frac LK+w_t\right)\\
&+(1+c_R)
\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\]
Because
\[
(T-1)\mathbb E[1-a^\star(S)]
\le T\mathbb E[1-a^\star(S)]
\]
and
\[
\sum_{t=2}^T\frac LK\le\frac{LT}{K},
\]
the right side is at most
\[
T\left[c_M+\mathbb E[1-a^\star(S)]\right]+B_T
=C_T^\star+B_T.
\]

It remains to prove the claimed rate. Let
\[
\ell=\log\frac{32T}{\delta}.
\]
For \(T\ge16\),
\[
T^{1/4}\le K\le2T^{1/4},
\qquad
z=\ell+\log K\le\frac32\ell.
\tag{25}
\]
Also,
\[
\sum_{t=1}^Tt^{-1/4}\le\frac43T^{3/4},
\tag{26}
\]
and
\[
\sum_{n=1}^{T-1}n^{-3/8}\le\frac85T^{5/8},\quad
\sum_{n=1}^{T-1}n^{-3/4}\le4T^{1/4},
\tag{27}
\]
\[
\sum_{n=1}^{T-1}n^{-1/2}\le2T^{1/2},\quad
\sum_{n=1}^{T-1}n^{-1}\le1+\log T.
\tag{28}
\]

Using \(A_n\le n^{5/4}\), (25)–(28), and \(\sqrt z\le z\le(3/2)\ell\),
\[
\begin{aligned}
\sum_{t=2}^Tw_t
&\le
\frac{16}{5}\sqrt{2Kz}\,T^{5/8}
+\frac83KzT^{1/4}
+2\sqrt2K\sqrt{zT}\\
&\le27T^{3/4}\ell.
\end{aligned}
\tag{29}
\]
Similarly,
\[
\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)
\le10T^{3/4}\ell.
\tag{30}
\]
Furthermore,
\[
\frac{LT}{K}\le LT^{3/4},
\tag{31}
\]
and
\[
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\le3T^{3/4}\ell.
\tag{32}
\]

Put \(X=T^{3/4}\ell\), \(A=1+c_R\), and
\(Q=(1+L)/\epsilon\). From (29)–(32),
\[
B_T
\le
X\left(11+3A+\frac{L+27}{\epsilon}\right).
\]
Since \(A\ge1\) and
\[
\frac{L+27}{\epsilon}
\le27\frac{1+L}{\epsilon}=27Q,
\]
we obtain
\[
B_T\le27(A+Q)X.
\]
Thus the rate statement holds, for example, with the universal constant
\[
C_0=27.
\]

## Randomness and filtration accounting

Before the model call, \(x_t\) is \(\mathcal F_{t-1}\)-measurable. After observing \(S_t\), the scalar \(x_{t,J_t}\), audit probability \(q_t\), and observation probability \(p_t\) are measurable from the past, current score, and routing probability. None depends on the current \(Y_t\) or \(L_t\).

The proof-only filtration \(\mathcal G_{t,-}\) reveals the latent current arrival before routing and audit coins. Conditional on it,
\[
\mathbb E\left[\frac{O_tL_t}{p_t}\,\middle|\,\mathcal G_{t,-}\right]=L_t.
\]
Thus both orientations
\[
L_t\left(1-\frac{O_t}{p_t}\right),
\qquad
L_t\left(\frac{O_t}{p_t}-1\right)
\]
are legitimate martingale differences. The learner never observes either expression when \(O_t=0\); it merely records the prescribed zero contribution to \(H\).

The current observation probability may depend on all prior importance-weighted feedback. Lemma 2 remains valid because it constructs supermartingales for deterministic tuning parameters and applies Ville’s inequality before unioning over a deterministic grid. It never conditions on a future confidence event or substitutes a random variance into a fixed-variance tail bound.

Released-error concentration uses the predictable mask \(G_t\). Cost concentration is applied directly to the fully accounted round cost
\[
O_t+c_RD_tA_tL_t.
\]

The losses remain separate:

- \(L_t\) is the counterfactual cheap-source loss;
- \(R_t=D_t(1-A_t)L_t\) is final released-label loss;
- \(O_tL_t/p_t\) is importance-weighted feedback.

Every learner round pays the model cost. Expert deferrals, audits, and audited-error corrections are all included in \(C_T\). The comparator also pays every model call and every expert call. Its optimal representative uses no audit and therefore incurs no correction charge.

## Boundary cases and counterexample attempts

Empty bins have \(\pi_j=\theta_j=0\); setting \(b_j=0\) is harmless. Atoms at grid boundaries are assigned uniquely by the half-open convention. Atoms at the optimal comparator threshold are handled by \(\rho\).

The audit rule is always valid: if its numerator is positive,
\[
0<x+\gamma_t-1\le x,
\]
so \(q_t(x)\in[0,1]\). For \(x=0\), deferral observes the label with probability one.

If \(m\equiv0\), the comparator releases every cheap prediction. Early conservative deferrals and audits remain bounded by \(B_T\). If \(L=0\), the continuum-to-bin approximation term vanishes. The cases \(\epsilon=1\), \(c_M\in\{0,1\}\), and \(c_R\in\{0,1\}\) require no modification.

Arbitrary score-error relations without A3 can encode many unrelated score regions, making safe regions statistically unidentified under sublinear feedback. A3 excludes that obstruction globally. No monotonicity or raw-score calibration identity is used.

An exact-boundary comparator does not require a margin, strict complementarity, or uniqueness: Lemma 7 scales its binned policy toward the safe expert and explicitly pays \((L/K+w_t)/\epsilon\).

The reviewer’s smallest-failure construction—exact empirical bin frequencies but an upward importance-weighted deviation—is excluded precisely by \(\mathcal E_b\). The corrected Lemma 8 includes that event rather than attributing the whole comparison solely to frequency concentration.

## Self-audit

1. The most delicate step is Lemma 2’s curved, random-variance boundary. The proof reduces it to deterministic-\(\mu\) Ville bounds and explicitly verifies the grid cardinality and numerical absorption using \(T\ge16\) and \(z>8\).

2. Lemma 8 depends on two logically separate events: empirical frequencies and comparator-directed importance weighting. They are now stated separately and both are included in the main intersection.

3. Comparator attainment relies on a measurable Lipschitz version of \(m\) and threshold randomization on an atom. A direct test is to reduce the comparator problem to the distribution of the scalar \(m(S)\), where the threshold construction is explicit.

4. The comparator’s high-probability statement requires fresh independent roundwise randomization. That convention is now explicit; the deterministic benchmark value itself does not depend on comparator coin realizations.

## Open obligations

None.

# Context: reviewer feedback that must be addressed point by point

VERDICT: revise

## Verdict rationale

The theorem appears mathematically plausible, and the comparator, cost accounting, assumptions, rates, and downstream optimization arguments are largely sound. However, the two importance-weighting arguments are not valid as written.

The claimed analytical sequence \(\mathcal G_{t,-}\) is not a filtration: it reveals the current latent \(Y_t\), but on an unaudited round that label is absent from \(\mathcal F_t\) and hence can disappear from \(\mathcal G_{t+1,-}\). Therefore the exponential process invoked in Lemma 2 is not shown to be adapted, so Lemma 1 and Ville’s inequality cannot be applied. Lemma 6 has the same defect.

This gap is decisive because Lemma 2 supports the released-error guarantee, while Lemma 6 supports comparator feasibility and the cost guarantee. It appears repairable by supplying a genuinely nested proof-only filtration and redoing the martingale arguments, so the appropriate verdict is `revise`, not `reject`.

## Step-by-step audit

- Setting and information timeline — **verified**. The routing vector is chosen from past information, and the realized routing and audit probabilities depend only on the past and current model output, not on \(Y_t\) or \(L_t\).

- Observation probability — **verified**:
  \[
  1-x+xq_t(x)=\max\{1-x,\gamma_t\}.
  \]
  The audit probability lies in \([0,1]\), and the expected audit incidence is at most \(\gamma_t\).

- Separation of losses — **verified**. Counterfactual loss \(L_t\), released loss \(R_t\), and feedback \(O_tL_t/p_t\) are not conflated.

- Assumptions A1–A3 — **verified as admissible**. They are global problem-level assumptions, not optimizer-local conditions. The Lipschitz condition is stated on the data distribution and is not a margin at an optimal threshold.

- Comparator — **verified**. It observes the same current score information, does not see \(Y_t\) before acting, and knows \(P\) explicitly. Auditing is indeed weakly dominated by deferral under the stated cost semantics.

- Complete cost accounting — **verified**. Both parties pay the model-call cost; learner deferrals, audits, and audited-error corrections are charged. Comparator audits are not silently removed from the action space; they are shown to be dominated.

- Lemma 1 — **verified**. The one-sided exponential bound and the stated Bernstein consequence follow with the given, slightly conservative, linear term.

- Lemma 2 — **gap**. The conditional calculation for one round is correct, but \(\mathcal G_{t,-}\) is not nested across \(t\). Consequently, the proof has not constructed a martingale or adapted exponential supermartingale to which Ville’s inequality applies. The random-variance grid calculations are otherwise consistent.

- Lemma 3 — **gap by dependency**. The i.i.d. Hoeffding component and the algebra \(E_{n,j}-H_{t,j}=M_{n,j}\) are correct. Simultaneous calibration validity nevertheless depends on the unproved Lemma 2.

- Lemma 4 — **verified conditional on Lemma 3**. The predictable masking argument avoids conditioning Azuma on a future confidence event. The conditional-risk computation and range-one concentration are correct.

- Lemma 5 — **verified**. Thresholding the scalar \(m(S)\), with randomization at an atom, attains the comparator optimum. The binning argument loses at most \(L/K\) in risk while preserving deferral cost.

- Lemma 6 — **gap**. Its first importance-weighted sum suffers from the same non-nested-filtration problem as Lemma 2. The fixed-\(n\) variance and increment bounds, the i.i.d. Hoeffding bound for the second sum, and the subsequent union bound are correct if a valid martingale filtration is supplied.

- Lemma 7 — **verified conditional on Lemma 6**. The Cauchy–Schwarz bound on \(\sum_jr_{t,j}\), the comparison with \(w_t/2\), feasibility scaling, and the \(1/\epsilon\) cost penalty are correct.

- Lemma 8 — **verified conditional on Lemmas 6–7**. Both empirical-frequency and importance-weighted comparator events are now included. FTRL optimality, the two empirical-to-population conversions, and the regularization penalty \(K/(2n)\) are correct.

- Lemma 9 — **verified**. The full random round cost is bounded and its conditional mean includes deferrals, audits, and corrections. The Azuma–Hoeffding constant is valid for range length \(1+c_R\).

- Lemma 10 — **verified**. Comparator expected cost and high-probability released-error semantics are derived under the explicitly stated fresh independent randomization.

- Main probability union — **verified arithmetically**, conditional on the disputed events being proved. With \(e^{-z}=\delta/(32KT)\), the displayed total is below \(\delta\).

- Main released-error conclusion — **gap by dependency**. It relies on Lemmas 2–3.

- Main cost conclusion — **gap by dependency**. It relies on Lemma 6 through robust comparator feasibility.

- Rate calculation — **verified**. The sums involving \(\gamma_t\), \(w_t\), frequency estimation, and discretization have the asserted \(T^{3/4}\) order. The universal constant \(C_0=27\) is consistent with the displayed coarse bounds.

- External citations — **not load-bearing**. The proof supplies its own concentration lemma and otherwise invokes standard Hoeffding–Azuma bounds; the literature comparisons are not used to close a mathematical step.

## Smallest failure

The smallest broken step is the sentence in Lemma 2:

> “Lemma 1 and Ville’s inequality show that …”

The conditioning fields used there are not a filtration. Specifically,
\[
\mathcal G_{s,-}=\sigma(\mathcal F_{s-1},S_s,\widehat Y_s,Y_s)
\]
contains \(Y_s\). If \(O_s=0\), then \(Y_s\) is not observed and is not included in \(\mathcal F_s\). Thus
\[
\mathcal G_{s,-}\not\subseteq\mathcal G_{s+1,-}
\]
in general.

For a concrete measurability failure, suppose an unaudited cheap release occurs and \(L_s\) remains random conditional on the observable history. Then
\[
X_{s,j}
=\mathbf1\{S_s\in B_j\}L_s
\]
on that event. This variable depends on the discarded latent \(Y_s\), so the accumulated exponential process after round \(s\) need not be measurable with respect to the purported conditioning field at round \(s+1\). It therefore has not been shown to be an adapted supermartingale, and Ville’s inequality is unavailable.

A valid one-round identity
\[
\mathbb E[X_{s,j}\mid\mathcal G_{s,-}]=0
\]
does not by itself establish a martingale when the conditioning fields are non-nested.

## Required author action

1. Define a genuinely nested proof-only filtration that retains all past latent arrivals, including \(Y_s\) and \(L_s\) from unaudited rounds, while preserving the algorithm’s stated observable filtration.

2. Reprove Lemma 2 relative to that filtration, including adaptation of the exponential process and predictability of the variance upper bound used by Ville’s inequality.

3. Reprove the first martingale term in Lemma 6 under the same nested construction.

4. Propagate the corrected event statements and failure probabilities through Lemmas 3, 7, 8, and the main proof. No new problem assumption should be introduced to close this proof-level gap.
