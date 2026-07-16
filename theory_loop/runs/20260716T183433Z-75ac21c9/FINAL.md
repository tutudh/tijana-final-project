# Surviving proof candidate — pending human review

This artifact was produced by an autonomous loop. It is a model-
generated proof candidate that passed 2 independent fresh-context review(s). It is NOT an established theorem or novelty claim until a human reviews and
promotes it.

- Run: 20260716T183433Z-75ac21c9
- Candidate: calls/0001-propose
- Proof: calls/0002-prove
- Calls made: 4; total cost: $0.00

## Theorem candidate

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

## Proof candidate

STATUS: complete

## Exact theorem

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

## Notation and standing assumptions

Let \(P\) denote the marginal law of \(S\), and put \(b=b(S)\). For \(x\in[0,1-\gamma]^K\), define the population deferral cost and released-risk functionals

\[
d(x)=\mathbb E[1-x_{b(S)}],
\qquad
r(x)=\mathbb E[x_{b(S)}m(S)].
\]

At time \(t\), abbreviate

\[
z_t=x_{t,b_t},\qquad q_t=1-z_t,\qquad
W_t=\widetilde L_t=\frac{D_tL_t}{q_t},
\]

so that \(q_t\ge\gamma\) and

\[
g_t=e_{b_t}(-1+\lambda_tW_t),
\qquad
h_t=z_tW_t-\bar\epsilon.
\]

Let

\[
d_0=\inf_{\substack{a:[0,1]\to[0,1]\ {\rm Borel}\\
\mathbb E[a(S)m(S)]\le\epsilon}}
\mathbb E[1-a(S)],
\]

so \(C_T^\star=T(c_M+d_0)\).

We use

\[
u=\epsilon^{-1},\qquad \Lambda=2u,
\]

and the shorthand

\[
P_T=\sqrt{KT\ell_T},\qquad
A_T=\sqrt{\frac{T\ell_T}{\gamma}},\qquad
B_T=\frac{\ell_T}{\gamma},\qquad
H_T=P_T+A_T+B_T.
\]

The proof below establishes the theorem with, for example, \(C_0=100\).

## Lemmas

### Lemma 1 — Borel-to-bin coarsening and reveal-floor comparison

Let \(a:[0,1]\to[0,1]\) be Borel and feasible for the original benchmark. For every bin \(B_j\) of positive probability define

\[
x_j=\mathbb E[a(S)\mid S\in B_j],
\]

and set \(x_j=0\) on null bins. Then

\[
\mathbb E[x_{b(S)}]=\mathbb E[a(S)]
\]

and

\[
r(x)\le \mathbb E[a(S)m(S)]+\frac{L}{K}\le\bar\epsilon.
\]

Consequently, if

\[
d_\gamma^\star
=
\min_{\substack{x\in[0,1-\gamma]^K\\r(x)\le\bar\epsilon}}d(x),
\]

then

\[
d_\gamma^\star\le d_0+\gamma.
\]

**Proof.**

Fix a positive-probability bin \(B_j\), and write

\[
\mu_j=\mathbb E[m(S)\mid S\in B_j].
\]

The release-mass identity follows directly from conditional expectation. Moreover,

\[
x_j\mu_j-\mathbb E[a(S)m(S)\mid S\in B_j]
=
\mathbb E[a(S)(\mu_j-m(S))\mid S\in B_j].
\]

The diameter of a bin is at most \(1/K\), so A3 gives

\[
|\mu_j-m(S)|\le \frac{L}{K}
\quad\text{on }B_j.
\]

After multiplying by \(P(S\in B_j)\) and summing,

\[
r(x)-\mathbb E[a(S)m(S)]\le\frac{L}{K}.
\]

Also \(r(x)\le1\), hence \(r(x)\le\min\{1,\epsilon+L/K\}=\bar\epsilon\).

Now set \(x^\gamma=(1-\gamma)x\). Then \(x^\gamma\in[0,1-\gamma]^K\),

\[
r(x^\gamma)=(1-\gamma)r(x)\le\bar\epsilon,
\]

and

\[
d(x^\gamma)
=1-(1-\gamma)\mathbb E[a(S)]
=d(a)+\gamma\mathbb E[a(S)]
\le d(a)+\gamma.
\]

Apply this to an infimizing sequence of Borel policies \(a\). Compactness of \([0,1-\gamma]^K\) and continuity of \(d,r\) give existence of the minimum defining \(d_\gamma^\star\). Thus

\[
d_\gamma^\star\le d_0+\gamma.
\qquad\square
\]

### Lemma 2 — Exact penalty for the floor-constrained binned program

There is \(\lambda^\star\ge0\) such that, for every \(x\in[0,1-\gamma]^K\),

\[
d(x)-d_\gamma^\star
+
\lambda^\star(r(x)-\bar\epsilon)
\ge0,
\]

and

\[
0\le\lambda^\star\le\frac1{\bar\epsilon}\le\frac1\epsilon.
\]

**Proof.**

The problem is a finite-dimensional convex program with compact feasible domain and affine objective and constraint. The point \(x=0\) satisfies

\[
r(0)-\bar\epsilon=-\bar\epsilon<0,
\]

because \(\bar\epsilon\ge\epsilon>0\). Slater’s condition therefore gives a dual optimum \(\lambda^\star\ge0\) and

\[
d_\gamma^\star
=
\inf_{x\in[0,1-\gamma]^K}
\{d(x)+\lambda^\star(r(x)-\bar\epsilon)\}.
\]

This identity implies the displayed exact-penalty inequality for every \(x\).

Evaluating the infimum at \(x=0\) gives

\[
d_\gamma^\star
\le d(0)-\lambda^\star\bar\epsilon
=1-\lambda^\star\bar\epsilon.
\]

Because \(d_\gamma^\star\ge0\),

\[
\lambda^\star\bar\epsilon\le1,
\]

which proves the cap. \(\square\)

### Lemma 3 — Pathwise one-sided-barrier primal regret

Suppose

\[
\sqrt{\frac{K\log(1/\gamma)}{T}}\le\frac12.
\]

Then, pathwise, for every \(x\in[0,1-\gamma]^K\),

\[
\sum_{t=1}^T
\langle g_t,x_t-x\rangle
\le
2\sqrt{2(1+\Lambda^2)KT\log(1/\gamma)}.
\]

**Proof.**

For the selected coordinate, write \(q=1-x_{t,b_t}\) and

\[
\alpha=\eta_x g_{t,b_t}q.
\]

Because

\[
g_{t,b_t}q=-q+\lambda_tD_tL_t,
\]

we have

\[
|g_{t,b_t}|^2q^2
\le2(q^2+\lambda_t^2D_tL_t)
\le2(1+\Lambda^2).
\]

Hence the assumed inequality gives \(|\alpha|\le1/2\).

The mirror-descent optimality condition and the three-point Bregman identity imply

\[
\eta_x\langle g_t,x_t-x\rangle
\le
D_\Psi(x,x_t)-D_\Psi(x,x_{t+1})
+
\eta_x\langle g_t,x_t-x_{t+1}\rangle
-D_\Psi(x_{t+1},x_t).
\]

Only coordinate \(b_t\) changes. Write \(d=x_{t+1,b_t}-x_{t,b_t}\) and \(v=d/q\). For \(\psi(x)=-\log(1-x)\),

\[
D_\psi(x_t+d,x_t)=-\log(1-v)-v.
\]

Therefore the last two terms are at most the supremum over \(v<1\) of

\[
-\alpha v+\log(1-v)+v.
\]

For \(\alpha<1\), this supremum equals

\[
-\log(1-\alpha)-\alpha.
\]

For \(|\alpha|\le1/2\),

\[
-\log(1-\alpha)-\alpha\le\alpha^2.
\]

Thus

\[
\eta_x\langle g_t,x_t-x\rangle
\le
D_\Psi(x,x_t)-D_\Psi(x,x_{t+1})
+
\eta_x^2g_{t,b_t}^2q_t^2.
\]

Summing and using \(x_1=0\),

\[
\sum_t\langle g_t,x_t-x\rangle
\le
\frac{D_\Psi(x,0)}{\eta_x}
+
2\eta_x(1+\Lambda^2)T.
\]

Finally,

\[
D_\Psi(x,0)
=
\sum_j[-\log(1-x_j)-x_j]
\le K\log(1/\gamma).
\]

Substitution of the prescribed \(\eta_x\) makes the two terms equal and yields the result. \(\square\)

### Lemma 4 — Pathwise AdaGrad dual regret

For every \(\lambda\in[0,\Lambda]\),

\[
\sum_{t=1}^T h_t(\lambda-\lambda_t)
\le
\frac32\Lambda
\sqrt{1+\sum_{t=1}^T h_t^2}.
\]

**Proof.**

Projection onto an interval is nonexpansive, so

\[
(\lambda-\lambda_{t+1})^2
\le
(\lambda-\lambda_t-\eta_{\lambda,t}h_t)^2.
\]

Rearrangement gives

\[
h_t(\lambda-\lambda_t)
\le
\frac{(\lambda-\lambda_t)^2-(\lambda-\lambda_{t+1})^2}
{2\eta_{\lambda,t}}
+
\frac{\eta_{\lambda,t}h_t^2}{2}.
\]

Since \(\eta_{\lambda,t}\) is nonincreasing and all squared distances are at most \(\Lambda^2\), summation by parts bounds the first sum by

\[
\frac{\Lambda^2}{2\eta_{\lambda,T}}
=
\frac{\Lambda}{2}\sqrt{1+\sum_t h_t^2}.
\]

Writing \(S_t=\sum_{u\le t}h_u^2\),

\[
\sum_t \frac{\eta_{\lambda,t}h_t^2}{2}
=
\frac{\Lambda}{2}
\sum_t\frac{h_t^2}{\sqrt{1+S_t}}
\le
\Lambda(\sqrt{1+S_T}-1),
\]

where the last inequality follows from

\[
\frac{S_t-S_{t-1}}{\sqrt{1+S_t}}
\le
2(\sqrt{1+S_t}-\sqrt{1+S_{t-1}}).
\]

Combining the two estimates proves the lemma. \(\square\)

### Lemma 5 — Martingale Bernstein inequality

Let \((\xi_t)\) be martingale differences with \(|\xi_t|\le b\) almost surely and

\[
\sum_{t=1}^T\mathbb E_{t-1}[\xi_t^2]\le V
\]

for deterministic \(V\). Then, for every \(s>0\),

\[
\Pr\left\{
\sum_{t=1}^T\xi_t
>
\sqrt{2Vs}+\frac{bs}{3}
\right\}
\le e^{-s}.
\]

The corresponding lower-tail inequality follows by applying this result to \(-\xi_t\).

**Proof.**

For \(0<\theta<3/b\), expansion of the exponential, the martingale-difference property, and \(|\xi_t|^k\le b^{k-2}\xi_t^2\) give

\[
\mathbb E_{t-1}e^{\theta\xi_t}
\le
\exp\left(
\frac{\theta^2\mathbb E_{t-1}\xi_t^2}
{2(1-\theta b/3)}
\right).
\]

Thus

\[
\exp\left(
\theta\sum_{t=1}^n\xi_t
-
\frac{\theta^2}{2(1-\theta b/3)}
\sum_{t=1}^n\mathbb E_{t-1}\xi_t^2
\right)
\]

is a nonnegative supermartingale. Markov’s inequality and optimization over \(\theta\) yield the stated Bernstein boundary. \(\square\)

### Lemma 6 — High-probability coupled saddle inequality

Let \(x^\star\) minimize the binned floor-constrained program of Lemma 1 and define

\[
U_T=\sum_{t=1}^T[d(x_t)-d(x^\star)],
\qquad
V_T=\sum_{t=1}^T[r(x_t)-\bar\epsilon].
\]

If

\[
\sqrt{\frac{K\log(1/\gamma)}{T}}\le\frac12,
\]

then, with probability at least \(1-\delta\),

\[
U_T+\lambda V_T\le25\epsilon^{-1}H_T
\qquad
\text{for }\lambda\in\{0,\Lambda\}.
\]

On the same event,

\[
U_T\le25\epsilon^{-1}H_T,
\qquad
(V_T)_+\le25H_T.
\]

**Proof.**

Primal regret against \(x^\star\) and dual regret against fixed \(\lambda\) give

\[
\sum_t
\left[
-z_t+x^\star_{b_t}
+\lambda(z_tW_t-\bar\epsilon)
+\lambda_t(\bar\epsilon-x^\star_{b_t}W_t)
\right]
\le A_x+A_\lambda,
\]

where \(A_x\) and \(A_\lambda\) denote the bounds from Lemmas 3 and 4. Therefore

\[
\sum_t[-z_t+x^\star_{b_t}
+\lambda(z_tW_t-\bar\epsilon)]
\le
A_x+A_\lambda+N_T,
\]

with

\[
N_T=\sum_t\lambda_t(x^\star_{b_t}W_t-\bar\epsilon).
\]

The importance estimator satisfies

\[
\mathbb E_{t-1}[z_tW_t]=r(x_t),
\qquad
\mathbb E_{t-1}[x^\star_{b_t}W_t]=r(x^\star)\le\bar\epsilon.
\]

Define

\[
M_T^{(0)}
=
\sum_t\left[
x^\star_{b_t}-z_t
-
\mathbb E_{t-1}(x^\star_{b_t}-z_t)
\right],
\]

\[
M_T^{(r)}
=
\sum_t[z_tW_t-r(x_t)].
\]

Then the left side equals

\[
U_T+\lambda V_T+M_T^{(0)}+\lambda M_T^{(r)}.
\]

The following conditional bounds hold:

\[
|h_t|\le\gamma^{-1},
\qquad
\mathbb E_{t-1}h_t^2\le\frac4\gamma,
\qquad
\mathbb E_{t-1}h_t^4\le\frac4{\gamma^3};
\]

\[
\operatorname{Var}_{t-1}(z_tW_t)\le\gamma^{-1},
\qquad
|z_tW_t-r(x_t)|\le\gamma^{-1};
\]

and, for \(X_t=\lambda_t(x^\star_{b_t}W_t-\bar\epsilon)\),

\[
\mathbb E_{t-1}X_t\le0,\qquad
\mathbb E_{t-1}X_t^2\le\frac{4\Lambda^2}{\gamma},
\qquad
|X_t-\mathbb E_{t-1}X_t|
\le\frac{2\Lambda}{\gamma}.
\]

Lemma 5 and a union bound therefore give

\[
|M_T^{(0)}|
\le
\sqrt{2T\ell_T}+\frac{2\ell_T}{3},
\]

\[
|M_T^{(r)}|
\le
\sqrt{\frac{2T\ell_T}{\gamma}}
+\frac{\ell_T}{3\gamma},
\]

\[
N_T
\le
\Lambda\sqrt{\frac{8T\ell_T}{\gamma}}
+\frac{2\Lambda\ell_T}{3\gamma},
\]

and

\[
\sum_t h_t^2
\le
\frac{4T}{\gamma}
+
\sqrt{\frac{8T\ell_T}{\gamma^3}}
+
\frac{\ell_T}{3\gamma^2}.
\]

Because \(T\gamma=T^{5/8}\ge1\) and \(\ell_T\ge1\), the last display implies

\[
\sqrt{1+\sum_t h_t^2}
\le5A_T+B_T.
\]

Consequently,

\[
A_\lambda\le\frac32\Lambda(5A_T+B_T).
\]

Also \(\log(1/\gamma)\le\ell_T\), and Lemma 3 gives

\[
A_x
\le
2\sqrt{2(1+\Lambda^2)}P_T.
\]

Substituting \(\Lambda=2/\epsilon\) and collecting the displayed estimates yields, conservatively,

\[
U_T+\lambda V_T\le25\epsilon^{-1}H_T
\]

for \(\lambda=0,\Lambda\).

The \(\lambda=0\) case gives the claimed bound on \(U_T\).

Let \(\bar x=T^{-1}\sum_tx_t\). Lemma 2 gives

\[
U_T+\lambda^\star V_T
=
T[d(\bar x)-d(x^\star)
+\lambda^\star(r(\bar x)-\bar\epsilon)]
\ge0.
\]

If \(V_T>0\), combine this lower bound with the saddle inequality at \(\lambda=\Lambda\):

\[
(\Lambda-\lambda^\star)V_T
\le25\epsilon^{-1}H_T.
\]

Since

\[
\Lambda-\lambda^\star
\ge\frac2\epsilon-\frac1\epsilon
=\frac1\epsilon,
\]

we obtain \(V_T\le25H_T\). If \(V_T\le0\), the positive-part assertion is automatic. \(\square\)

## Main proof

First consider the nontrivial regime

\[
\sqrt{\frac{K\log(1/\gamma)}{T}}\le\frac12.
\]

Use the probability-one event from Lemma 6, augmented by the following two Bernstein events.

Because \(D_t\) is conditionally Bernoulli with conditional mean, after integrating over \(S_t\),

\[
\mathbb E_{t-1}D_t=d(x_t),
\]

Lemma 5 gives

\[
\sum_tD_t
\le
\sum_td(x_t)
+
\sqrt{2T\ell_T}+\frac{\ell_T}{3}.
\tag{1}
\]

Likewise,

\[
R_t=(1-D_t)L_t,\qquad
\mathbb E_{t-1}R_t=r(x_t),
\]

and hence

\[
\sum_tR_t
\le
\sum_tr(x_t)
+
\sqrt{2T\ell_T}+\frac{\ell_T}{3}.
\tag{2}
\]

There are at most eight one- or two-sided Bernstein events in Lemma 6 and (1)–(2). Their total failure probability is at most

\[
8e^{-\ell_T}
=
\frac{8\delta}{16KT}
\le\delta.
\]

### Error guarantee

Lemma 6 gives

\[
\sum_tr(x_t)
=
\bar\epsilon T+V_T
\le
\bar\epsilon T+25H_T.
\]

Using (2),

\[
\sum_tR_t
\le
\bar\epsilon T+25H_T
+\sqrt{2T\ell_T}+\frac{\ell_T}{3}.
\]

Since \(K\ge1\), \(\gamma\le1\), and \(\epsilon^{-1}\ge1\), the final two terms and \(25H_T\) are bounded by

\[
100(1+\epsilon^{-1})^2H_T.
\]

Moreover,

\[
\bar\epsilon
=\min\{1,\epsilon+L/K\}
\le\epsilon+\frac{L}{K}.
\]

Therefore

\[
\sum_tR_t
\le
\epsilon T+\frac{LT}{K}+\mathcal G_T.
\]

### Cost guarantee

From Lemma 6 and (1),

\[
\sum_tD_t
\le
Td(x^\star)+25\epsilon^{-1}H_T
+\sqrt{2T\ell_T}+\frac{\ell_T}{3}.
\]

Lemma 1 gives

\[
d(x^\star)=d_\gamma^\star\le d_0+\gamma.
\]

Thus

\[
C_T
=
c_MT+\sum_tD_t
\le
T(c_M+d_0)+\gamma T+\mathcal G_T
=
C_T^\star+\gamma T+\mathcal G_T.
\]

No \(c_R\) term is incurred because OBSR never audits; each \(D_t=1\) is an expert deferral and costs exactly one.

### The large-step regime

If instead

\[
\sqrt{\frac{K\log(1/\gamma)}{T}}>\frac12,
\]

then, since \(\ell_T\ge\log(1/\gamma)\),

\[
P_T=\sqrt{KT\ell_T}>\frac T2.
\]

For \(C_0=100\), \(\mathcal G_T\ge T\). Pathwise,

\[
\sum_tR_t\le T
\]

and

\[
C_T-C_T^\star
\le(c_MT+T)-c_MT
\le T.
\]

Both asserted bounds therefore hold deterministically in this regime.

### Rates

Let

\[
\kappa=\max\{1,4L/\rho\}.
\]

For \(T\ge16\),

\[
K=\lceil\kappa T^{1/4}\rceil
\le2\kappa T^{1/4}.
\]

Also,

\[
\frac{LT}{K}
\le
\frac{L}{\kappa}T^{3/4}
\le
\frac{\rho}{4}T^{3/4}.
\]

The three stochastic terms have orders

\[
P_T=O_{L,\rho}(T^{5/8}\sqrt{\ell_T}),
\]

\[
A_T=T^{11/16}\sqrt{\ell_T},
\]

\[
B_T=T^{3/8}\ell_T.
\]

If \(\ell_T\le T^{5/8}\), then \(B_T\le T^{11/16}\sqrt{\ell_T}\), and \(P_T\) is smaller than the same rate. If \(\ell_T>T^{5/8}\), then \(T^{11/16}\sqrt{\ell_T}\ge T\), while both error excess and cost regret are pathwise at most \(T\). Hence uniformly in \(\delta\),

\[
\sum_tR_t
\le
\epsilon T+\frac{\rho}{4}T^{3/4}
+
O_{\epsilon,L,\rho}
\left(T^{11/16}\sqrt{\log(T/\delta)}\right)
\]

and

\[
C_T-C_T^\star
=
O_{\epsilon,L,\rho}
\left(T^{11/16}\sqrt{\log(T/\delta)}\right).
\]

For fixed \(\delta\), or for \(\delta=T^{-3}\), this is \(o(T^{3/4})\).

If \(\rho\le2c_0\), then \(\rho T^{3/4}/4\le c_0T^{3/4}/2\). The remaining term is \(o(T^{3/4})\), so for sufficiently large \(T\),

\[
\sum_tR_t\le\epsilon T+c_0T^{3/4}
\]

while \(C_T-C_T^\star=o(T^{3/4})\).

Finally, take \(\delta=T^{-3}\). On the failure event,

\[
\sum_tR_t\le T,\qquad C_T-C_T^\star\le T.
\]

Thus integrating the high-probability bounds adds at most

\[
T\delta=T^{-2},
\]

which is \(O(1)\), and proves the claimed expectation consequences.

## Randomness and filtration accounting

Let \(\mathcal O_{t-1}\) be the learner’s observed history through round \(t-1\): past model outputs, actions, routing coins, expert labels on deferred rounds, and internal randomness.

- \(x_t,\lambda_t\) are \(\mathcal O_{t-1}\)-measurable.
- The current triple \((S_t,\widehat Y_t,Y_t)\) is independent of \(\mathcal O_{t-1}\) by A1.
- After observing \((S_t,\widehat Y_t)\), \(q_t=1-x_{t,b(S_t)}\) is measurable with respect to the action-time information.
- \(D_t\) is then drawn independently with conditional law \(\operatorname{Bernoulli}(q_t)\).
- The learner sees \(L_t\) exactly when \(D_t=1\). Nevertheless \(D_tL_t\), and hence \(W_t\), is always computable: it is zero on \(D_t=0\).

Conditioning first on the complete current triple,

\[
\mathbb E[D_tL_t/q_t\mid
\mathcal O_{t-1},S_t,\widehat Y_t,Y_t]
=L_t.
\]

Because \(x_t\) and \(q_t\) depend on the current observation only through \(S_t\),

\[
\mathbb E[W_t\mid\mathcal O_{t-1},S_t]=m(S_t).
\]

Thus

\[
\mathbb E_{t-1}[z_tW_t]=r(x_t),
\qquad
\mathbb E_{t-1}[x^\star_{b_t}W_t]=r(x^\star).
\]

The released-label loss is not confused with this estimate:

\[
R_t=(1-D_t)L_t,
\qquad
\mathbb E_{t-1}R_t=r(x_t).
\]

Likewise the paid expert action satisfies

\[
\mathbb E_{t-1}D_t=d(x_t).
\]

Every application of Lemma 5 uses the observed-history filtration after the round’s computable update has been appended. Current unobserved labels are used only as latent random variables in defining \(R_t\) and proving conditional expectations; they are never available to the learner before acting.

## Boundary cases and counterexample attempts

- If \(L=0\), the coarsening error is exactly zero. The proof does not divide by \(L\).
- If \(\epsilon=1\) or \(\bar\epsilon=1\), the constraint may be nonbinding. Lemma 2 permits \(\lambda^\star=0\), and the proof remains valid.
- Null-probability bins cause no problem: their coordinates never enter \(d\), \(r\), or the stochastic gradients.
- Arbitrarily rare score regions require no density lower bound. Their effects are weighted by their actual probability in both learner and comparator objectives.
- Very large \(L\) can make \(K\) so large that the barrier stability condition fails. In precisely that regime \(\sqrt{KT\ell_T}\) is already at least order \(T\), and the claimed theorem follows from the deterministic bounds \(R_{1:T}\le T\) and \(C_T-C_T^\star\le T\).
- The potentially dangerous event \(q_t=\gamma\) and \(D_tL_t=1\) produces a \(1/\gamma\) importance estimate. It does not enter the primal regret with that magnitude: the barrier local factor \(q_t\) changes the relevant quantity to \(-q_t+\lambda_tD_tL_t\). It does enter the dual second moment, and this is exactly the source of the \(A_T\) and \(B_T\) terms.
- A possible adaptive-dual counterexample is excluded by keeping \(\lambda_t\) inside the comparator martingale \(N_T\). It is never replaced by a fixed multiplier. The fixed \(\lambda\in\{0,\Lambda\}\) appears only in the valid pathwise dual-regret inequality.
- Deferrals are not treated as missing information: every \(D_t=1\) yields \(L_t\) and costs one. This is the sole feedback and expert-cost channel used by OBSR.

## Self-audit

1. **Barrier stability calculation.** This is the most delicate step. It is protected by the explicit condition \(|\eta_xg_{t,b_t}q_t|\le1/2\); outside that condition the proof switches to deterministic bounds.

2. **Adaptive comparator martingale.** The term
   \(\lambda_t(x^\star_{b_t}W_t-\bar\epsilon)\) is essential. Its conditional mean is nonpositive because \(\lambda_t\) is past-measurable and \(x^\star\) is population feasible.

3. **Exact-penalty conversion.** The comparison must use the optimum of the same relaxed, floor-constrained binned program. Comparing directly to an arbitrary smoothed Borel policy would introduce an uncontrolled relaxed-program optimality gap.

4. **Asymptotic interpretation.** The finite-\(T\) theorem is uniform in \(\delta\). The displayed \(o(T^{3/4})\) is under the standard fixed-confidence interpretation, and also holds for the explicitly proposed choice \(\delta=T^{-3}\).

5. **Cost accounting.** Both sides include \(c_MT\). Every learner deferral costs one. Neither side incurs a correction charge under the release/defer action space used here.

## Open obligations

None.

## Review: 0003-review

VERDICT: pass

## Verdict rationale

The theorem and proof are mathematically sound. The coupled saddle argument correctly retains the adaptive dual sequence inside a supermartingale term, the log-barrier geometry removes the primal \(1/\gamma\) variance penalty, and the exact-penalty argument converts the saddle bounds into separate risk and cost guarantees.

The assumptions are admissible problem-level conditions. The comparator has the required information, action, risk, and cost parity. Model calls and expert deferrals are counted on both sides; no audit or correction costs are incurred. Released loss \(R_t\), counterfactual loss \(L_t\), and importance-weighted feedback \(W_t\) remain distinct.

The resulting terms are genuinely \(O(T^{11/16}\sqrt{\log T})\), while binning contributes only \(O(T^{3/4})\) released-error slack. Thus the claimed \(o(T^{3/4})\) cost regret follows.

## Step-by-step audit

1. Setting and filtration — verified.

   \(x_t,\lambda_t\) are past-measurable; \(q_t\) becomes measurable after observing the current score; the deferral coin is then drawn independently. Since routing depends on the current observation only through \(S_t\),

   \[
   \mathbb E[W_t\mid\mathcal O_{t-1},S_t]=m(S_t).
   \]

   Consequently the stated conditional expectations for \(z_tW_t\), \(x^\star_{b_t}W_t\), \(R_t\), and \(D_t\) are correct.

2. Comparator and accounting — verified.

   The comparator is the stipulated distribution-aware Borel score policy. It sees no current label or loss, calls the same cheap source, and uses the same release/defer semantics. Auditing is weakly dominated by deferral because both obtain and release the expert label, while an audited error can additionally incur \(c_R\). Both sides retain \(c_MT\); every learner deferral costs one.

3. Lemma 1 — verified.

   Conditional averaging preserves release mass. Within a bin, Lipschitzness gives \(|m(S)-\mu_j|\le L/K\), yielding the stated risk increase. Scaling by \(1-\gamma\) respects the floor and increases deferral cost by at most \(\gamma\). The infimizing-sequence and compactness argument is valid.

4. Lemma 2 — verified.

   The zero-release point is strictly feasible because \(\bar\epsilon>0\), so Slater duality applies. Evaluating the dual Lagrangian at \(x=0\) gives

   \[
   0\le d_\gamma^\star\le1-\lambda^\star\bar\epsilon,
   \]

   hence \(\lambda^\star\le1/\bar\epsilon\le1/\epsilon\). This is global and does not assume optimizer-local regularity.

5. Lemma 3 — verified.

   The key cancellation is exact:

   \[
   q_tg_{t,b_t}=-q_t+\lambda_tD_tL_t.
   \]

   Therefore \(q_t^2g_{t,b_t}^2\le2(1+\Lambda^2)\), independent of \(1/\gamma\). The prescribed step size makes \(|\alpha|\le1/2\). The one-dimensional Bregman calculation and supremum

   \[
   \sup_{v<1}\{-\alpha v+\log(1-v)+v\}
   =-\log(1-\alpha)-\alpha\le\alpha^2
   \]

   are correct. Telescoping gives the claimed comparator-uniform bound.

6. Lemma 4 — verified.

   Projection nonexpansiveness gives the standard varying-step potential inequality. Since \(\eta_{\lambda,t}\) is nonincreasing, summation by parts bounds the potential term by \(\Lambda^2/(2\eta_{\lambda,T})\). The square-root telescoping inequality gives the remaining factor, totaling \(3\Lambda/2\).

7. Lemma 5 — verified.

   The stated conditional-mgf argument yields the usual martingale Bernstein boundary with deterministic variance upper bound. Both tails are available by changing signs.

8. Lemma 6 — verified.

   Adding primal and dual regret produces exactly

   \[
   -z_t+x^\star_{b_t}
   +\lambda(z_tW_t-\bar\epsilon)
   +\lambda_t(\bar\epsilon-x^\star_{b_t}W_t).
   \]

   The last term is retained through \(N_T\); the proof never substitutes a fixed multiplier for \(\lambda_t\). Its conditional drift is nonpositive because \(x^\star\) is feasible.

   The asserted moment bounds follow from \(q_t\ge\gamma\), \(0\le z_t,x^\star_b\le1-\gamma\), and Bernoulli importance weighting. Applying Bernstein to the four stated martingale quantities gives the displayed \(P_T,A_T,B_T\) bounds. The numerical collection fits within \(25\epsilon^{-1}H_T\).

   Finally, affine averaging and Lemma 2 yield \(U_T+\lambda^\star V_T\ge0\). Combining this with \(\lambda=\Lambda\) and \(\Lambda-\lambda^\star\ge1/\epsilon\) correctly controls \((V_T)_+\).

9. Main error guarantee — verified.

   \(R_t\) is bounded and has conditional mean \(r(x_t)\). Bernstein, Lemma 6, and \(\bar\epsilon\le\epsilon+L/K\) give the boxed error bound.

10. Main cost guarantee — verified.

    \(D_t\) is bounded with conditional mean \(d(x_t)\). Bernstein, the \(U_T\) bound, and \(d_\gamma^\star\le d_0+\gamma\) give the boxed cost bound after adding the common model cost.

11. Failure probability — verified.

    Counting two tails each for \(M_T^{(0)}\) and \(M_T^{(r)}\), plus one-sided events for \(N_T\), \(\sum h_t^2\), expert cost, and released loss, gives at most eight events. Thus \(8e^{-\ell_T}\le\delta\).

12. Large-step regime — verified.

    Failure of barrier stability implies \(P_T>T/2\); hence \(\mathcal G_T\ge T\). The pathwise bounds \(\sum R_t\le T\) and \(C_T-C_T^\star\le T\) then prove both claims without concentration.

13. Rates and expectation conversion — verified.

    With \(K=\Theta(T^{1/4})\) and \(\gamma=T^{-3/8}\),

    \[
    P_T=\widetilde O(T^{5/8}),\quad
    A_T=\widetilde O(T^{11/16}),\quad
    B_T=\widetilde O(T^{3/8}),\quad
    \gamma T=T^{5/8}.
    \]

    Therefore cost regret is \(o(T^{3/4})\). Taking \(\delta=T^{-3}\) adds at most \(T\delta=T^{-2}\) when integrating the failure event.

14. External citations — verified and nonessential to the proof.

    The cited results are used only as scoped analogies. Their stated feedback and comparator mismatches are acknowledged. The descriptions agree with the primary texts: [Cesa-Bianchi–Lugosi–Stoltz](https://stoltz.perso.math.cnrs.fr/Publications/CBLS-pmonit.pdf), [Yu–Neely–Wei](https://proceedings.neurips.cc/paper/6741-online-convex-optimization-with-stochastic-constraints.pdf), [Kleinberg](https://proceedings.neurips.cc/paper_files/paper/2004/file/b75bd27b5a48a1b48987a18d831f6336-Paper.pdf), and [Harris–Podimata–Wu](https://papers.neurips.cc/paper_files/paper/2023/file/fcd3909db30887ce1da519c4468db668-Paper-Conference.pdf).

## Smallest failure

The weakest surviving step is the constant and moment bookkeeping in Lemma 6. In particular, the fourth-moment bound and the final coefficient \(25\) are asserted compactly. Direct calculation confirms them: \(|h_t|\le1/\gamma\), \(\mathbb E_{t-1}h_t^4\le4/\gamma^3\), and the individual \(P_T,A_T,B_T\) coefficients remain below \(25\epsilon^{-1}\). Thus this step is terse but not broken.

## Required author action

None.

## Review: 0004-review

VERDICT: pass

## Verdict rationale

The proof is mathematically coherent and establishes both boxed guarantees under admissible A1–A3 assumptions. The comparator has information and action parity, all costs are counted, and released loss, counterfactual loss, and importance-weighted feedback remain distinct.

The key improvement is valid: the log-barrier local norm cancels the \(1/q_t\) magnitude in the primal gradient, while the remaining dual and comparator-estimation variance is explicitly charged through \(A_T\) and \(B_T\). The resulting \(T^{11/16}\) term is genuinely \(o(T^{3/4})\) for fixed confidence or \(\delta=T^{-3}\).

## Step-by-step audit

- Setting and filtration — verified. \(x_t,\lambda_t\) are past-measurable; \(q_t\) is measurable after observing \(S_t\); the routing coin is conditionally independent; unavailable labels are never used by the learner.

- Loss separation — verified. \(L_t\), \(R_t=(1-D_t)L_t\), and \(W_t=D_tL_t/q_t\) have distinct roles.

- Cost accounting — verified. Both learner and comparator pay \(c_MT\); every deferral costs one; neither audits, so no \(c_R\) charge arises. Audit-and-correct is dominated by deferral here.

- Comparator — verified. It is distribution-aware, Borel measurable, uses only the current score, and acts before seeing \(Y_t\) or \(L_t\).

- Lemma 1 — verified. Conditional averaging preserves release mass. Within-bin oscillation of \(m\) is at most \(L/K\), giving the stated risk relaxation. Multiplication by \(1-\gamma\) enforces the reveal floor with cost increase at most \(\gamma\).

- Lemma 2 — verified. Slater holds at \(x=0\). Strong duality yields the exact-penalty inequality. Evaluating the dual objective at \(x=0\) correctly gives \(\lambda^\star\bar\epsilon\le1\).

- Lemma 3 — verified. For the active coordinate,
  \[
  g_{t,b_t}q_t=-q_t+\lambda_tD_tL_t,
  \]
  so its squared local norm is at most \(2(1+\Lambda^2)\) pathwise. The one-dimensional conjugate calculation and the stability condition \(|\alpha|\le1/2\) are correct. The comparator divergence is at most \(K\log(1/\gamma)\).

- Lemma 4 — verified. Projection nonexpansiveness, summation by parts with nonincreasing step sizes, and the square-root telescoping inequality produce the claimed \(3\Lambda/2\) constant.

- Lemma 5 — verified. This is the standard martingale Bernstein/Freedman argument with deterministic variance bound.

- Lemma 6 — verified. Adding primal and dual regret gives the displayed saddle expression with correct signs. The adaptive multiplier remains inside
  \[
  N_T=\sum_t\lambda_t(x^\star_{b_t}W_t-\bar\epsilon),
  \]
  whose conditional mean is nonpositive. The variance, range, and fourth-moment bounds used for \(M_T^{(0)},M_T^{(r)},N_T\), and \(\sum h_t^2\) are valid. The constants collect within \(25\epsilon^{-1}H_T\). Exact penalty then converts the \(\lambda=\Lambda\) inequality into \((V_T)_+\le25H_T\).

- Realized cost conversion — verified. Conditional mean \(\mathbb E_{t-1}D_t=d(x_t)\) and Bernstein yield the realized expert-cost bound.

- Realized error conversion — verified. Because routing depends on the current observation only through \(S_t\),
  \[
  \mathbb E_{t-1}R_t=r(x_t),
  \]
  so the final released-label bound follows without substituting estimated loss for released loss.

- Union bound — verified. The proof uses at most eight Bernstein tails, and \(8e^{-\ell_T}\le\delta\).

- Large-step regime — verified. Failure of barrier stability implies \(P_T>T/2\), making \(\mathcal G_T\ge T\); the deterministic bounds then suffice.

- Rate calculation — verified. With \(K=\Theta(T^{1/4})\) and \(\gamma=T^{-3/8}\),
  \[
  P_T=\widetilde O(T^{5/8}),\quad
  A_T=\widetilde O(T^{11/16}),\quad
  B_T=\widetilde O(T^{3/8}).
  \]
  Also \(LT/K\le(\rho/4)T^{3/4}\). The \(o(T^{3/4})\) statement holds for fixed \(\delta\) and for \(\delta=T^{-3}\), as expressly clarified.

- Expectation conversion — verified. The failure-event contribution is at most \(T\delta=T^{-2}\).

- External results — checked. They are used only as analogies, not proof inputs, and the candidate correctly records their incompatible feedback models and comparators: [partial monitoring](https://pubsonline.informs.org/doi/pdf/10.1287/moor.1060.0206), [stochastic-constraint OCO](https://proceedings.neurips.cc/paper/6741-online-convex-optimization-with-stochastic-constraints.pdf), [continuum-armed bandits](https://proceedings.neurips.cc/paper_files/paper/2004/file/b75bd27b5a48a1b48987a18d831f6336-Paper.pdf), and [strategic apple tasting](https://papers.neurips.cc/paper_files/paper/2023/file/fcd3909db30887ce1da519c4468db668-Paper-Conference.pdf).

## Smallest failure

The weakest surviving step is the adaptive coupled-saddle argument in Lemma 6, specifically control of \(N_T\). It nevertheless holds because \(\lambda_t\) is past-measurable while
\[
\mathbb E_{t-1}[x^\star_{b_t}W_t]=r(x^\star)\le\bar\epsilon.
\]
Thus \(N_T\) is a supermartingale sum with the stated range and variance bounds; the proof never replaces \(\lambda_t\) by a fixed multiplier.

## Required author action

None.
