VERDICT: pass

## Verdict rationale

The proof is mathematically coherent and satisfies the research contracts. The repaired nested filtration correctly supports the adaptive importance-weighted martingales; population safety is converted to realized released-error control without conditioning on future confidence events; and total cost includes model calls, deferrals, audits, and audited-error corrections.

The comparator has information, action, loss, and cost parity. Its no-audit form is correctly shown to weakly dominate audited implementations. The Lipschitz assumption is global, operationally interpretable, and not optimizer-local. The stated \(T^{3/4}\log T\) rate follows from the displayed finite-sample bound with no omitted linear term.

## Step-by-step audit

- **Timeline and predictability — verified.** \(x_t\) is chosen from observable history before \(S_t\); routing and auditing use only the past, current model output, score, and independent coins. Neither uses \(Y_t\) or \(L_t\) before acting.

- **Loss separation — verified.** The proof consistently distinguishes latent cheap loss \(L_t\), released loss \(R_t=D_t(1-A_t)L_t\), and feedback \(O_tL_t/p_t\).

- **Observation probability — verified.** Direct calculation gives
  \[
  p_t=1-x_{t,J_t}+x_{t,J_t}q_t=\max\{1-x_{t,J_t},\gamma_t\},
  \]
  with \(p_t\ge\gamma_t\) and \(xq_t=[x+\gamma_t-1]_+\le\gamma_t\).

- **Proof filtration — verified.** The interlacing
  \[
  \mathscr H_{t-1}\subseteq\mathscr P_t\subseteq\mathscr H_t
  \]
  is genuinely nested and retains all past latent losses. Conditional on \(\mathscr P_t\), the current loss is fixed and only the independent routing/audit coins remain random. This makes both importance-weighting increments valid martingale differences without giving the algorithm latent information.

- **Lemma 1 — verified.** The one-sided exponential inequality is valid for all \(X_s\le b\), including unbounded negative increments. Conditional expectation yields the stated supermartingale, and optimizing the Chernoff parameter gives (6) with the displayed constants.

- **Lemma 2 — verified.** The increment has conditional mean zero, upper bound \(1\), and variance at most \(\mathbf1\{S_s\in B_j\}/p_s\). The deterministic multiplicative grid and Ville union bound validly produce a time-uniform random-variance boundary. The grid has at most \(T\) points for \(T\ge16\), and the rounding remainder is correctly absorbed into \(z/(3\gamma_n)\).

- **Lemma 3 — verified.** The decomposition
  \[
  \theta_j-\frac{H_{t,j}}n
  =
  \left(\theta_j-\frac{E_{n,j}}n\right)+\frac{M_{n,j}}n
  \]
  combines an i.i.d. Hoeffding bound with Lemma 2. Clipping preserves the upper-confidence property because \(\theta_j\in[0,1]\).

- **Lemma 4 — verified.** The confidence mask \(G_t\) is predictable. On \(G_t=1\),
  \[
  \mathbb E[D_tL_t\mid\mathscr H_{t-1}]
  =\sum_jx_{t,j}\theta_j\le\epsilon.
  \]
  Since auditing only decreases released loss, masked Hoeffding–Azuma proves the result without conditioning on the future calibration event.

- **Lemma 5 — verified.** The comparator problem is a fractional-knapsack problem in \(m(S)\). The threshold policy with boundary randomization is Borel, feasible, and optimal by the pointwise sign of \((a-a^\star)(m-\lambda)\). Binning preserves deferral cost, while global Lipschitzness bounds the risk distortion by \(L/K\).

- **Lemma 6 — verified.** The comparator vector \(b\) is deterministic for fixed \(P\). The importance-weighted term has upper increment bound \(\gamma_n^{-1}\) and predictable variance at most \(A_n\); the arrival term is i.i.d., centered, and bounded. The union bound over horizons gives (23).

- **Lemma 7 — verified.** Cauchy–Schwarz gives
  \[
  \sum_jr_{t,j}\le w_t/2.
  \]
  For \(K\ge2\), the bound in Lemma 6 is also at most \(w_t/2\). Combining these with discretization proves robust feasibility. Scaling toward the safe expert incurs exactly the displayed \((L/K+w_t)/\epsilon\) cost penalty and requires no optimizer-local margin.

- **Lemma 8 — verified.** Uniform empirical-frequency concentration is correctly union-bounded. FTRL optimality and \(\|y_t\|_2^2\le K\) yield the \(K/(2n)\) regularization penalty. Two empirical-to-population conversions account for the factor \(2K\). The conditional expectation identity follows from independence of the current score.

- **Lemma 9 — verified.** For
  \[
  W_t=O_t+c_RD_tA_tL_t,
  \]
  conditional expectation is at most
  \[
  1-x_{t,J_t}+(1+c_R)\gamma_t.
  \]
  Since \(W_t\in[0,1+c_R]\), Hoeffding–Azuma gives (37). The separate first-round expert charge is correctly included.

- **Lemma 10 — verified.** A no-audit comparator with final cheap-release probability \(a(S)\) pays expected expert cost \(\mathbb E[1-a(S)]\) and has mean released loss at most \(\epsilon\). Replacing any audited comparator by immediate deferral on the same non-release probability preserves expert-call cost and released-label distribution while removing the nonnegative correction charge.

- **Failure-probability aggregation — verified.** The listed event probabilities sum to
  \[
  (4KT+2T+2)e^{-z}
  =
  \delta\left(\frac18+\frac1{16K}+\frac1{16KT}\right)<\delta.
  \]

- **Main error proof — verified.** Lemma 4 directly yields the claimed fixed-horizon released-error bound on the joint event.

- **Main cost proof — verified.** Summing Lemma 8 inside Lemma 9 gives all terms in \(B_T\). Replacing \(T-1\) by \(T\) and \((T-1)L/K\) by \(LT/K\) only enlarges the bound. The common \(c_MT\) model-call cost appears on both sides.

- **Rate calculation — verified.** With \(K=\lceil T^{1/4}\rceil\), \(\gamma_t=t^{-1/4}\), and \(A_n\le n^{5/4}\), the audit, confidence, empirical-frequency, and discretization sums are all at most \(O(T^{3/4}\log(32T/\delta))\). The explicit inequalities support \(C_0=27\).

- **Admissibility — verified.** A1–A3 are global problem-level assumptions with operational meanings and falsification routes. The binning, audit floor, horizon dependence, regularizer, and confidence construction are correctly classified and charged as algorithm choices.

## Smallest failure

The weakest surviving step is Lemma 2’s time-uniform random-variance boundary, especially the absorption inequality (14). It nevertheless holds: using \(\overline V_{n,j}\le n^{5/4}\), \(T\ge n\), and \(z\ge8\), its left side is at most
\[
\frac{\sqrt{2z}}2n^{-3/8},
\]
which is at most
\[
\frac z3\cdot\frac34n^{-3/8}
\le \frac z3(n^{1/4}-1)
\]
for \(n\ge5\); the cases \(n=2,3,4\) satisfy the inequality directly at the worst permitted values \(T=16,z=8\). The case \(n=1\) has zero martingale increment. Thus the grid-rounding remainder is legitimately absorbed.

## Required author action

None.