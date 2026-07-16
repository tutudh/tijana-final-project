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