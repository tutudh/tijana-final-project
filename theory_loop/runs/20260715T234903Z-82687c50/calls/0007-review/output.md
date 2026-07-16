VERDICT: pass

## Verdict rationale

The proof establishes both guarantees under admissible, globally interpretable assumptions. The learner’s actions are predictable, the proof-only filtration is genuinely nested, and the importance-weighted martingales remain adapted. Released loss, latent cheap-source loss, and estimated feedback are consistently distinguished.

The comparator has information and action parity, pays every model and expert call, and may omit audits by a valid dominance argument. The high-probability event covers arrivals, routing coins, and audit coins. The claimed \(O(T^{3/4}\log T)\) rate follows from the displayed finite-sample bound.

## Step-by-step audit

- Setting and filtration — verified.  
  \(x_t\) is chosen before the current score; routing and auditing depend only on the past, current model output, score, and fresh independent coins. The interlaced fields
  \(\mathscr H_{t-1}\subseteq\mathscr P_t\subseteq\mathscr H_t\)
  retain all latent past losses and make the coin-step martingales adapted. Enlarging the proof filtration does not leak information to the algorithm.

- Observation mechanism — verified.  
  Direct calculation gives
  \[
  \Pr(O_t=1\mid\mathscr P_t)=1-x_{t,J_t}+x_{t,J_t}q_t
  =\max\{1-x_{t,J_t},\gamma_t\}.
  \]
  The audit probability lies in \([0,1]\), the observation floor is valid, and \(xq_t\le\gamma_t\).

- Loss and cost definitions — verified.  
  \(L_t\), \(R_t=D_t(1-A_t)L_t\), and \(O_tL_t/p_t\) are never conflated. The total cost includes model calls, deferrals, audits, and audited-error corrections.

- Assumptions A1–A3 — verified as admissible.  
  They are problem-level, globally stated, non-optimizer-local, operationally interpretable, and equipped with plausible falsification procedures. The grid, audit floor, and regularizer are correctly classified as algorithm choices.

- Lemma 1 — verified.  
  The one-sided exponential inequality is valid for all \(x\le b\), including unbounded negative increments. The supermartingale construction and Bernstein–Freedman tail inversion give the stated constants.

- Lemma 2 — verified.  
  Conditional centering occurs at the coin step after \(S_s,L_s\) are fixed. The upper increment bound \(X_{s,j}\le1\) and predictable variance bound \(1\{S_s\in B_j\}/p_s\) are correct. Ville’s inequality, deterministic tuning grid, grid cardinality, and absorption inequality (14) yield the simultaneous random-variance bound without conditioning on future events.

- Lemma 3 — verified.  
  The i.i.d. bin-loss fluctuation and importance-weighting underestimation are combined in the correct direction. Clipping preserves \(\theta_j\le U_{t,j}\).

- Lemma 4 — verified.  
  The confidence mask is predictable. Independence of the current arrival gives
  \(\mathbb E[D_tL_t\mid\mathscr H_{t-1}]=\sum_jx_{t,j}\theta_j\le\epsilon\).
  Auditing only decreases released loss. The masked Azuma argument avoids illicit conditioning on the future confidence event.

- Lemma 5 — verified.  
  The comparator infimum is attained by the fractional threshold policy on \(m(S)\). The threshold optimality inequality has the correct sign. Binning preserves deferral cost exactly, while global Lipschitzness bounds the risk increase by \(L/K\).

- Lemma 6 — verified.  
  The comparator vector \(b\) is deterministic for fixed \(P\). The importance-weighted term is a valid coin-step martingale with upper bound \(\gamma_n^{-1}\) and variance at most \(A_n\). The arrival term is i.i.d. and bounded. The union over horizons yields (23).

- Lemma 7 — verified.  
  Cauchy–Schwarz gives the stated sum of confidence radii. The constants in \(w_t/2\) dominate both the radius sum and Lemma 6’s deviation when \(K\ge2\). Scaling toward the safe expert produces a feasible vector and costs at most \((L/K+w_t)/\epsilon\), without a margin assumption.

- Lemma 8 — verified.  
  Uniform empirical-bin-frequency concentration is valid. FTRL optimality, the regularizer bound \(\|y_t\|^2\le K\), and two empirical-to-population conversions produce (35). The relevant comparator and frequency events are both included.

- Lemma 9 — verified.  
  Conditional expected paid round cost is
  \[
  1-x_{t,J_t}+x_{t,J_t}q_t(1+c_RL_t),
  \]
  bounded as claimed. The realized cost lies in an interval of length \(1+c_R\), so the Azuma constant is correct. Round 1 and all model calls are included.

- Lemma 10 — verified.  
  A no-audit comparator pays \(c_M+\mathbb E[1-a(S)]\) per round and has mean released loss at most \(\epsilon\). Fresh independent deployment permits Hoeffding concentration. Replacing an audited action by immediate deferral preserves expert-call probability and released-label distribution while removing nonnegative correction cost.

- Main event union — verified.  
  The failure probabilities sum to
  \[
  (4KT+2T+2)e^{-z}<\delta.
  \]
  No martingale inequality is conditioned on one of these future events.

- Main cost comparison — verified.  
  Substituting Lemma 8 into Lemma 9 and comparing with the attained comparator gives exactly \(C_T^\star+B_T\). Exploration audits and corrections remain in regret rather than disappearing.

- Rate calculation — verified.  
  With \(K=\lceil T^{1/4}\rceil\), \(\gamma_t=t^{-1/4}\), and \(A_n\le n^{5/4}\), all four principal contributions are \(O(T^{3/4}\log(T/\delta))\). The displayed integral estimates support (49)–(53), and the coarse universal constant \(C_0=27\) is sufficient.

- Quantifiers and probability semantics — verified.  
  The result is fixed-horizon and simultaneous with probability at least \(1-\delta\) over all stated learner and arrival randomness. The distribution-aware comparator and its expected-cost benchmark are explicitly identified.

## Smallest failure

The weakest surviving step is Lemma 2’s time-uniform random-variance boundary. It nevertheless holds: each deterministic tuning parameter defines an adapted nonnegative supermartingale; the grid is deterministic and has at most \(T\) elements; every possible \(\overline V_{n,j}\in[1,A_T]\) has a grid point within ratio \(1+T^{-1/2}\); and the resulting approximation error is explicitly absorbed into \(z/(3\gamma_n)\). Thus there is no data-dependent tuning or future-event conditioning gap.

## Required author action

None.