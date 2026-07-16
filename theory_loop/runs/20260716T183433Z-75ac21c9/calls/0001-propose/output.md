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