STATUS: proposed

## Setting and assumption ladder

Let \(W_t=(X_t,Y_t,O_t)\), where \(X_t\) is the pre-call context, \(Y_t\) is the authoritative label, and \(O_t=(\widehat Y_t,S_t)\) is the potential output and confidence score of one cheap model. The cheap-source counterfactual loss is

\[
\ell_t=\mathbf 1\{\widehat Y_t\neq Y_t\}.
\]

At each round the available actions are:

- \(E\): skip the model, pay unit expert cost, and release \(Y_t\).
- \(C\): call the model for cost \(c_M>0\) and release \(\widehat Y_t\) without observing \(Y_t\).
- \(A\): call the model, decide to audit before seeing \(Y_t\), pay unit expert cost, correct an error for additional cost \(\kappa\ge 0\), and release the corrected label.

Thus final released-label loss and total round cost are

\[
\lambda_t=\ell_t\mathbf 1\{a_t=C\},
\]

\[
g_t=c_M\mathbf 1\{a_t\in\{C,A\}\}
+\mathbf 1\{a_t\in\{E,A\}\}
+\kappa\ell_t\mathbf 1\{a_t=A\}.
\]

Every model call, expert call, audit, and paid correction is included. Let \(G=c_M+1+\kappa\).

**Information timeline.** Given history \(\mathcal F_{t-1}\), \(X_t\) is revealed. The model-call gate \(D_t\in\{E,M\}\) is measurable with respect to \(\sigma(\mathcal F_{t-1},X_t)\). If \(D_t=M\), the model cost is incurred and \(O_t\) is revealed. The post-call choice \(C\) or \(A\) is measurable with respect to \(\sigma(\mathcal F_{t-1},X_t,O_t)\), before \(Y_t\) is revealed. The expert label becomes observable only under \(E\) or \(A\); correction and release occur afterward, followed by the update. Comparator policies obey the identical timeline.

The policy library \(\Pi=\{\pi_1,\ldots,\pi_N\}\) consists of deterministic two-stage policies. Each \(\pi\) has a pre-call gate \(d_\pi(X)\in\{E,M\}\) and, when it calls the model, a post-call rule \(h_\pi(X,O)\in\{C,A\}\). It contains the always-expert policy \(\pi_E\). Randomized policies are distributions \(q\in\Delta(\Pi)\).

The assumption ladder was:

1. Bounded but arbitrary arrivals: rejected for this mechanism because an audited prefix need not represent the unaudited suffix.
2. I.i.d. arrivals with unrestricted routers: rejected because a router class can shatter the audited prefix and have uncontrolled deployment risk.
3. I.i.d. arrivals with a finite deterministic class: direct conservative empirical selection can have linear cost loss at a risk-boundary discontinuity.
4. Active rung: i.i.d., finite registered class, known expert, positive error budget, with randomized safe-policy mixing. The third obstruction is escaped by an algorithm choice, not a margin or optimizer-local assumption.

**Assumption A1 — stationary, action-independent arrivals**

- Mathematical statement: \(W_1,\ldots,W_T\overset{\mathrm{i.i.d.}}{\sim}P\) for an unknown \(P\). The potential \(O_t\) is defined independently of the routing action; calling the model reveals it but does not change \((Y_t,O_t)\).
- Operational meaning: the item population and deployed model are stationary, and routing does not alter the correct label or model response.
- Diagnostic or falsification: rolling two-sample tests, change-point tests, residual autocorrelation, and repeated-call stability checks can falsify stationarity or action independence.
- Required by: transfer from the audited prefix to the deployment suffix and concentration around the distribution-aware comparator.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A2 — bounded accounting and authoritative expert**

- Mathematical statement: \(\ell_t\in\{0,1\}\), \(c_M>0\) and \(\kappa\ge0\) are known, and the unit-cost expert always returns \(Y_t\), yielding zero released loss. Hence \(0\le g_t\le G\).
- Operational meaning: invoices have bounded known components and the designated expert is the reference standard.
- Diagnostic or falsification: reconcile call/audit/correction logs against invoices; test expert reliability using duplicate adjudication.
- Required by: concentration, complete cost accounting, and the globally safe policy.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A3 — preregistered learnable routing class**

- Mathematical statement: \(\Pi\) is fixed before the stream, finite with \(2\le N<\infty\), and contains \(\pi_E\).
- Operational meaning: deployment chooses among a registered library of router versions rather than fitting an unrestricted router on the calibration prefix.
- Diagnostic or falsification: inspect the router registry and hashes; post-prefix creation or modification of a policy violates the assumption.
- Required by: simultaneous policy evaluation and the explicit comparator.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A4 — positive risk service level**

- Mathematical statement: the target satisfies fixed \(\epsilon\in(0,1]\).
- Operational meaning: the labeling SLA permits a specified nonzero average error budget.
- Diagnostic or falsification: falsified as an applicable model if the deployment requirement is exactly zero error.
- Required by: safe-policy shrinkage incurs cost proportional to \(1/\epsilon\). Exact zero risk cannot be obtained by this argument.
- Optimizer-local: `no`
- Classification: `problem`

**Choice C1 — prefix length, convexification, and confidence tightening**

- Mathematical statement: use \(n=\min\{T,\lceil T^{2/3}\rceil\}\) paired model–expert rounds, optimize over \(\Delta(\Pi)\), and tighten empirical risk by a uniform confidence radius.
- Operational meaning: front-load a sublinear calibration expense and deploy a stationary randomized router afterward.
- Diagnostic or falsification: directly check audit logs, LP inputs, mixture weights, and randomization frequencies.
- Required by: the proposed \(T^{2/3}\) cost remainder.
- Optimizer-local: `no`
- Classification: `algorithm`

No uniqueness, strict complementarity, local curvature, or margin at the unknown optimizer is assumed. Such conditions would be optimizer-local and are classified as `rejected`.

## Algorithm

Call the algorithm **Audited-Prefix Safe-Mixture LP (APS-LP)**.

For confidence \(\delta\in(0,1)\), set

\[
n=\min\{T,\lceil T^{2/3}\rceil\},\qquad H=T-n,
\qquad
a_n=\sqrt{\frac{\log(12N/\delta)}{2n}}.
\]

**Calibration rounds \(t\le n\).**

1. Call the cheap model and observe \(O_t\).
2. Audit with probability one, predictably before seeing \(Y_t\).
3. Observe \(Y_t\), correct if necessary, release the corrected label, and incur
   \(c_M+1+\kappa\ell_t\). Therefore calibration-round released loss is zero.
4. For every \(\pi\in\Pi\), reconstruct its counterfactual action and record

\[
r_t(\pi)=\ell_t\mathbf 1\{\pi(W_t)=C\},
\]

\[
c_t(\pi)=
\mathbf 1\{\pi(W_t)=E\}
+c_M\mathbf 1\{\pi(W_t)\in\{C,A\}\}
+\mathbf 1\{\pi(W_t)=A\}
+\kappa\ell_t\mathbf 1\{\pi(W_t)=A\}.
\]

Here \(r_t(\pi)\) is counterfactual cheap-source released risk, not the algorithm’s released loss. Because the calibration audit probability is one, the estimated feedback is exactly \(\widetilde r_t(\pi)=r_t(\pi)\); no importance weighting is used.

Define, linearly for \(q\in\Delta(\Pi)\),

\[
\widehat R_n(q)=\frac1n\sum_{t=1}^n\sum_{\pi}q_\pi r_t(\pi),
\qquad
\widehat C_n(q)=\frac1n\sum_{t=1}^n\sum_{\pi}q_\pi c_t(\pi).
\]

If \(a_n\le\epsilon/2\), solve the finite LP

\[
\widehat q\in
\arg\min_{q\in\Delta(\Pi)}\widehat C_n(q)
\quad\text{subject to}\quad
\widehat R_n(q)\le\epsilon-a_n,
\]

using a fixed deterministic tie-break. The expert policy makes this LP feasible. If \(a_n>\epsilon/2\), set \(\widehat q=\delta_{\pi_E}\).

**Deployment rounds \(t>n\).**

Sample \(J_t\sim\widehat q\) independently at the start of the round and execute \(\pi_{J_t}\):

- If its gate chooses \(E\), skip the model, obtain \(Y_t\), and release it.
- Otherwise call the model and observe \(O_t\). Then execute the policy’s predictable \(C/A\) decision.
- Under \(A\), audit before seeing \(Y_t\), correct, and release; under \(C\), release without feedback.

The induced audit probability after observing \((X_t,O_t)\) is the \(\widehat q\)-mass of policies choosing \(A\) there, hence is predictable. Labels observed during deployment may be logged but do not change \(\widehat q\); this independence is deliberate.

## Theorem candidate

For a distribution \(P\), define

\[
R(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi r(\pi;W)\right],
\qquad
C(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi c(\pi;W)\right].
\]

Let the distribution-aware comparator be

\[
q^\star\in\arg\min_{q\in\Delta(\Pi)}
\{C(q):R(q)\le\epsilon\},
\]

with fixed tie-breaking. It knows \(P\) but, on every action, sees only the same current information as APS-LP. It has the same actions and pays the same model, expert, audit, and correction costs. It has no learning audits unless prescribed by its sampled policy.

For an actual comparator run on the same item stream, independently sample \(J_t^\star\sim q^\star\) each round and let \(L_T^\star,C_T^\star\) be its realized released loss and total cost. Define

\[
d_m=\sqrt{\frac{m}{2}\log\frac6\delta},\qquad d_0=0,
\]

and

\[
\Gamma_T=
\begin{cases}
G\!\left[
n+2H a_n(1+\epsilon^{-1})+d_H+d_T
\right],
& a_n\le\epsilon/2,\\[3pt]
GT,&a_n>\epsilon/2.
\end{cases}
\]

**Candidate theorem.** For every \(N\ge2\), every \(P\) satisfying A1–A2, every policy class satisfying A3, every \(\epsilon\in(0,1]\), every horizon \(T\ge1\), and every \(\delta\in(0,1)\), with probability at least \(1-\delta\), jointly over \(W_{1:T}\), APS-LP’s randomization, and the comparator’s independent randomization,

\[
\boxed{\quad
L_T^{\mathrm{APS}}
=\sum_{t=1}^T\lambda_t
\le \epsilon T+d_H
\quad}
\]

and

\[
\boxed{\quad
C_T^{\mathrm{APS}}\le C_T^\star+\Gamma_T.
\quad}
\]

On the same event the comparator itself satisfies the probability-parity bound

\[
L_T^\star\le\epsilon T+d_T.
\]

For fixed \(N,G,\epsilon\), taking \(\delta_T=T^{-2}\) gives probability at least \(1-T^{-2}\),

\[
L_T^{\mathrm{APS}}
\le\epsilon T+O(\sqrt{T\log T}),
\]

\[
C_T^{\mathrm{APS}}
\le C_T^\star+
O\!\left(
G(1+\epsilon^{-1})T^{2/3}\sqrt{\log(NT)}
\right).
\]

Both remainders are \(o(T)\). More generally this remains true when
\(\log(N/\delta_T)=o(T^{2/3})\).

## Why this can work: proof plan

1. **Uniform prefix evaluation.** Hoeffding’s inequality and a union bound over the \(N\) base policies give, with failure probability at most \(\delta/3\),

\[
\sup_{q\in\Delta(\Pi)}
|\widehat R_n(q)-R(q)|\le a_n,
\qquad
\sup_{q\in\Delta(\Pi)}
|\widehat C_n(q)-C(q)|\le Ga_n.
\]

Linearity extends the bound from base policies to every mixture.

2. **Global safe shrinkage.** When \(a_n\le\epsilon/2\), set

\[
\theta=\frac{2a_n}{\epsilon},
\qquad
q^-=(1-\theta)q^\star+\theta\delta_{\pi_E}.
\]

Since \(R(\pi_E)=0\),

\[
R(q^-)\le(1-\theta)\epsilon=\epsilon-2a_n,
\]

so the uniform event implies
\(\widehat R_n(q^-)\le\epsilon-a_n\). Thus \(q^-\) is empirically feasible without any optimizer-local margin. Moreover,

\[
C(q^-)\le C(q^\star)+\theta G.
\]

3. **Population guarantees for the selected LP solution.** Empirical optimality and the two uniform deviations imply

\[
R(\widehat q)\le\epsilon,
\]

\[
C(\widehat q)
\le C(q^\star)+2Ga_n(1+\epsilon^{-1}).
\]

4. **Released-loss concentration.** Calibration contributes zero released loss. Conditional on the prefix, deployment rounds are i.i.d. with mean released loss at most \(\epsilon\). Hoeffding yields

\[
L_T^{\mathrm{APS}}\le \epsilon H+d_H\le\epsilon T+d_H.
\]

5. **Complete cost comparison.** Prefix cost is at most \(nG\). Conditional deployment-cost concentration gives

\[
C_T^{\mathrm{APS}}
\le nG+H C(q^\star)
+2GH a_n(1+\epsilon^{-1})+Gd_H.
\]

A lower-tail bound for the actual comparator gives
\(C_T^\star\ge TC(q^\star)-Gd_T\), producing the stated \(\Gamma_T\). Two analogous comparator bounds establish probability parity. The five events are allocated probabilities \(\delta/3,\delta/6,\delta/6,\delta/6,\delta/6\).

The single riskiest step is the safe-shrinkage-to-actual-comparator calculation: the prover must check that empirical feasibility, all factors of \(G\), and the lower-tail coupling to \(C_T^\star\) remain valid under the two-stage call/audit filtration. No local optimality property is available to repair an error there.

## Attack log

- **Nonstationary suffix attack.** Make every audited-prefix model prediction correct and every unaudited-suffix prediction wrong. A prefix-selected cheap router then violates the error target. This directly motivated A1. It does not establish that all continuously auditing adversarial algorithms are impossible.
- **Adaptive-output attack.** If model responses change depending on whether the system intends to audit, the calibration record does not identify deployment loss. A1 therefore includes action-independent potential outputs.
- **Unrestricted-router attack.** A router class that memorizes the \(n\) audited contexts can have zero empirical risk and arbitrarily high population risk. This motivated the preregistered finite library A3.
- **Risk-boundary cost jump.** Suppose a cheap policy has \(R=\epsilon\) and low cost while the expert has zero risk and unit cost. A deterministic empirical constraint tightened below \(\epsilon\) can discard the cheap policy and suffer \(\Theta(T)\) excess cost. Adding a margin or curvature assumption would be optimizer-local. Convex mixing with the expert instead creates the globally valid \(O(a_n/\epsilon)\) cost bridge.
- **Zero-budget attack.** The same bridge diverges at \(\epsilon=0\). Distinguishing an exactly zero-risk cheap source from one with arbitrarily small positive risk cannot be handled by this theorem, so A4 is explicit.
- **Hidden-cost attack.** Counting only expert calls makes calibration appear free. Here every prefix model call, expert audit, and erroneous-label correction is charged; the comparator uses identical accounting, and the learner’s extra calibration expense remains in \(\Gamma_T\).
- **Comparator-information attack.** The comparator knows \(P\), but not \(Y_t\) or \(\ell_t\) before acting. Its policy is executed through the same pre-call and post-call information nodes. Its lack of learning audits is legitimate, and the learner’s prefix audits appear as regret.
- **Rate attack.** With \(n\) prefix audits, the leading excess cost is \(Gn+GT\sqrt{\log N/n}\). Balancing these terms gives \(n\asymp T^{2/3}\); a shorter prefix worsens estimation cost, while a longer prefix directly increases audit cost.

## Relation to known results

- Angelopoulos, Bates, Fisch, Lei, and Schuster, [“Conformal Risk Control,” Theorem 1, Section 2.1](https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-risk.pdf), control the expected next-sample risk of an exchangeable, fully observed monotone loss family. The guarantee is in expectation, with no routing-cost comparator or partial expert feedback. The full text was checked. APS-LP instead controls realized cumulative released loss and realized total cost, while explicitly charging calibration audits. This source is an analogy for calibration, not proof evidence for the joint theorem.
- Cesa-Bianchi, Lugosi, and Stoltz, [“Minimizing Regret with Label Efficient Prediction,” Theorems 2 and 13](https://stoltz.perso.math.cnrs.fr/Publications/CBLS-LabelEff.pdf), study arbitrary outcome sequences with labels revealed only on queries. Theorem 2 gives high-probability regret of order \(T\sqrt{\log(N/\delta)/m}\) using at most \(m\) labels; Theorem 13 gives a matching expected lower bound against the best constant action. The full text was checked. Their comparator has no risk constraint, expert correction action, or complete labeling-cost objective; their rates nevertheless explain the audit-versus-estimation balance used here.
- Pacchiano, Ghavamzadeh, Bartlett, and Jiang, [“Stochastic Bandits with Linear Constraints,” Theorem 2](https://proceedings.mlr.press/v130/pacchiano21a/pacchiano21a.pdf), obtain high-probability sublinear pseudo-regret for stochastic contextual linear bandits under stage-wise expected constraints and a known safe action with positive slack. Pulled actions reveal their reward and cost. The full text was checked. APS-LP shares the safe-action geometry but replaces linear realizability and stage-wise expected feasibility with audited label feedback, sample-path cumulative error, correction semantics, and total-cost comparison.
- Candès, Ilyas, and Zrnic, [“Probably Approximately Correct Labels,” Theorem 1, Corollary 1, and Section 3](https://arxiv.org/abs/2506.10908), treat a fixed transductive dataset, sample expert labels for calibration, and provide high-probability labeling-error control; Section 3 develops multi-model and cost-sensitive routing. Probabilities are over the labeling procedure rather than an online arrival process, and no online cost-regret theorem against a distribution-aware policy is given. The primary full text was checked. APS-LP’s proposed difference is the online two-stage information structure and a simultaneous realized cost guarantee that explicitly absorbs learning audits and corrections.

These comparisons identify nearby mechanisms only. They do not establish novelty; that requires a broader human-reviewed search and proof verification.