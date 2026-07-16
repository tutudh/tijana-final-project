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