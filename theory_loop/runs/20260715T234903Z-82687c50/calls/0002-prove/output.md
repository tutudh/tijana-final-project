STATUS: complete

## Exact theorem

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
\theta_j=\Pr(S\in B_j,L=1).
\]
Thus \(\theta_j=\mathbb E[\mathbf1\{S\in B_j\}m(S)]\).

Bins are taken half-open except for the last bin, so every score has a unique bin and every bin has diameter at most \(1/K\).

For analysis at round \(t\), use an enlarged filtration that reveals the latent current triple \((S_t,\widehat Y_t,Y_t)\) before the routing and audit coins. This is only an analytical filtration: the learner’s decisions remain measurable with respect to the smaller information set in the theorem. Conditional on this enlarged pre-coin filtration,
\[
O_t\sim{\rm Bernoulli}(p_t),\qquad
p_t=\max\{1-x_{t,J_t},\gamma_t\},
\]
and \(p_t\) does not depend on \(L_t\).

At \(t=1\), set analytically
\[
D_1=0,\quad A_1=0,\quad O_1=1,\quad p_1=1.
\]
This is exactly the prescribed initial expert action.

Write
\[
A_n=\sum_{s=1}^n \gamma_s^{-1}
=\sum_{s=1}^n s^{1/4}.
\]
Then
\[
A_n\le n^{5/4}.
\]

All comparator expectations are with respect to the stationary distribution \(P\). The comparator benchmark is deterministic expected cost; the learner’s bound is a high-probability realized-cost bound.

## Lemmas

### Lemma 1 — Bernstein exponential supermartingale

Let \((X_s)\) be martingale differences, \(X_s\le b\), and let
\[
V_n=\sum_{s=1}^n\mathbb E[X_s^2\mid\mathcal G_{s-1}].
\]
For \(0<\lambda<3/b\),
\[
\exp\left\{
\lambda\sum_{s=1}^nX_s
-\frac{\lambda^2}{2(1-\lambda b/3)}V_n
\right\}
\]
is a nonnegative supermartingale.

If \(V_n\le v\) deterministically, then
\[
\Pr\left(
\sum_{s=1}^nX_s
>
\sqrt{2vz}+\frac{2bz}{3}
\right)\le e^{-z}.
\]

#### Proof

For \(x\le b\) and \(0<\lambda<3/b\),
\[
e^{\lambda x}
\le
1+\lambda x+
\frac{\lambda^2x^2}{2(1-\lambda b/3)}.
\]
For \(x\le0\), this follows from \(e^u-1-u\le u^2/2\). For \(0\le x\le b\), expand the exponential and use
\(k!\ge2\cdot3^{k-2}\) for \(k\ge2\).

Taking conditional expectations and using
\(\mathbb E[X_s\mid\mathcal G_{s-1}]=0\), followed by \(1+u\le e^u\), proves the supermartingale assertion.

Chernoff optimization gives the standard Freedman bound
\[
\Pr\left(\sum_{s=1}^nX_s\ge x\right)
\le
\exp\left(
-\frac{x^2}{2(v+bx/3)}
\right).
\]
For
\[
x=\sqrt{2vz}+\frac{2bz}{3},
\]
direct expansion shows
\[
x^2\ge2z(v+bx/3).
\]
Hence the displayed probability is at most \(e^{-z}\). ∎

### Lemma 2 — Adaptive importance-weighted underestimation

Fix a bin \(j\), and define
\[
M_{n,j}
=
\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Simultaneously for every \(1\le n\le T\),
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{z}{3\gamma_n}
\]
except on an event of probability at most \(Te^{-z}\).

#### Proof

Let
\[
X_{s,j}
=
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Conditional on the enlarged pre-coin filtration,
\[
\mathbb E[X_{s,j}\mid\mathcal G_{s,-}]=0,
\qquad X_{s,j}\le1,
\]
and
\[
\mathbb E[X_{s,j}^2\mid\mathcal G_{s,-}]
=
\mathbf1\{S_s\in B_j\}L_s\left(\frac1{p_s}-1\right)
\le \frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\]
Thus \(V_{n,j}\) is a predictable variance upper bound.

Lemma 1 implies that for every \(\mu>0\), with
\[
\lambda=\frac{\mu}{1+\mu/3}\in(0,3),
\]
the process
\[
\exp\left\{
\lambda M_{n,j}
-\frac{\lambda^2}{2(1-\lambda/3)}V_{n,j}
\right\}
\]
is a supermartingale. Ville’s inequality consequently gives
\[
M_{n,j}
\le
\frac{\mu V_{n,j}}2+\frac z\mu+\frac z3
\tag{1}
\]
simultaneously in \(n\), except with probability \(e^{-z}\), for each fixed \(\mu\).

We discretize \(\mu\). Let
\[
\mu_{\min}=\sqrt{\frac{2z}{A_T}},
\qquad
\mu_{\max}=\sqrt{2z},
\qquad
r=1+T^{-1/2},
\]
and take the multiplicative grid from \(\mu_{\min}\) to \(\mu_{\max}\) with ratio \(r\), including both endpoints. Since
\[
A_T\le T^{5/4},
\]
the number \(M\) of grid points satisfies
\[
M\le
2+\frac{(5/8)\log T}{\log(1+T^{-1/2})}
\le T
\]
for \(T\ge16\).

If \(V_{n,j}=0\), then \(M_{n,j}=0\). Otherwise
\(1\le V_{n,j}\le A_T\), and the optimizer of the first two terms on the right of (1) is
\[
\mu^\star=\sqrt{\frac{2z}{V_{n,j}}}\in[\mu_{\min},\mu_{\max}].
\]
Choose a grid point \(\mu=\rho\mu^\star\) with \(1\le\rho\le r\). Then
\[
\frac{\mu V}{2}+\frac z\mu
=
\sqrt{2Vz}\,\frac{\rho+\rho^{-1}}2
\le
\sqrt{2Vz}+\frac{\sqrt{2Vz}}{2T}.
\]
Because \(V_{n,j}\le A_n\le n^{5/4}\),
\[
\frac{\sqrt{2V_{n,j}z}}{2T}
\le
\frac{\sqrt{2z}\,n^{5/8}}{2T}.
\]
For \(z\ge8\), \(T\ge16\), and \(2\le n\le T\),
\[
\frac{\sqrt{2z}\,n^{5/8}}{2T}
\le
\frac{(n^{1/4}-1)z}{3}.
\tag{2}
\]
For \(n=2,3,4\), (2) follows directly from \(T\ge16\); for \(n\ge5\), use \(T\ge n\) and
\[
\frac34n^{-3/8}\le n^{1/4}-1.
\]
At \(n=1\), \(p_1=O_1=1\), hence \(M_{1,j}=0\).

Combining (1) and (2),
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{n^{1/4}z}{3}
=
\sqrt{2V_{n,j}z}+\frac z{3\gamma_n}.
\]
A union bound over at most \(T\) grid points gives failure probability at most \(Te^{-z}\). ∎

### Lemma 3 — Simultaneous one-sided calibration validity

Except on an event of probability at most \(2KTe^{-z}\), for every \(t\ge2\) and every bin \(j\),
\[
\theta_j\le U_{t,j}.
\]

#### Proof

Let \(n=t-1\) and
\[
E_{n,j}=\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s.
\]
Since the triples are i.i.d. and each summand lies in \([0,1]\),
\[
\Pr\left(
\theta_j-\frac{E_{n,j}}n
>
\sqrt{\frac z{2n}}
\right)\le e^{-z}.
\]
A union bound over \(j,n\) costs at most \(KTe^{-z}\).

By Lemma 2, simultaneously over \(n\), except with probability \(Te^{-z}\) per bin,
\[
E_{n,j}-H_{t,j}
\le
\sqrt{2V_{t,j}z}+\frac z{3\gamma_n}.
\]
Therefore
\[
\theta_j
\le
\frac{H_{t,j}}n
+
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}n
+\sqrt{\frac z{2n}}
=
\widehat a_{t,j}+r_{t,j}.
\]
Because \(0\le\theta_j\le1\), clipping preserves this upper bound:
\(\theta_j\le U_{t,j}\). ∎

### Lemma 4 — Population safety and released-error concentration

With probability at least \(1-2KTe^{-z}-e^{-z}\),
\[
\sum_{t=1}^T R_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\]

#### Proof

At \(t\ge2\), define the predictable analytical indicator
\[
G_t=\mathbf1\{\theta_j\le U_{t,j}\text{ for all }j\},
\]
and let \(G_1=1\). Although \(\theta_j\) is unknown to the learner, it is a fixed population quantity, so \(G_t\) is \(\mathcal F_{t-1}\)-measurable.

When \(G_t=1\),
\[
\begin{aligned}
\mathbb E[D_tL_t\mid\mathcal F_{t-1}]
&=\sum_{j=1}^K x_{t,j}\theta_j\\
&\le\sum_{j=1}^Kx_{t,j}U_{t,j}
\le\epsilon.
\end{aligned}
\]
Since \(R_t=D_t(1-A_t)L_t\le D_tL_t\),
\[
\mathbb E[G_tR_t\mid\mathcal F_{t-1}]\le\epsilon G_t\le\epsilon.
\]
The variables
\[
G_tR_t-\mathbb E[G_tR_t\mid\mathcal F_{t-1}]
\]
are martingale differences of conditional range length at most \(1\). Hence Hoeffding–Azuma gives
\[
\sum_{t=1}^T G_tR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

On the event of Lemma 3, \(G_t=1\) for all \(t\), and the left side is exactly \(\sum_tR_t\). This stopping construction avoids conditioning the martingale inequality on a future confidence event. ∎

### Lemma 5 — Existence and discretization of an optimal comparator

There is a Borel optimizer \(a^\star\) attaining the infimum in \(C_T^\star\). Define, for \(\pi_j>0\),
\[
b_j=\mathbb E[a^\star(S)\mid S\in B_j],
\]
and set \(b_j=0\) when \(\pi_j=0\). Then
\[
\sum_j\pi_j(1-b_j)
=
\mathbb E[1-a^\star(S)]
\tag{3}
\]
and
\[
\sum_j\theta_jb_j
\le
\epsilon+\frac LK.
\tag{4}
\]

#### Proof

By A3, the Lipschitz version of \(m\) on the score support admits a Borel Lipschitz extension to \([0,1]\). Thus \(m(S)\) may be treated as a Borel random variable.

An optimizer is obtained by releasing on the lowest values of \(m(S)\). If \(\mathbb E[m(S)]\le\epsilon\), take \(a^\star\equiv1\). Otherwise choose a threshold \(\lambda>0\) and \(\rho\in[0,1]\) such that
\[
a^\star(s)
=
\mathbf1\{m(s)<\lambda\}
+\rho\,\mathbf1\{m(s)=\lambda\},
\qquad
\mathbb E[a^\star(S)m(S)]=\epsilon.
\]
Existence follows by taking a quantile of the finite measure
\(\mathbb E[m(S)\mathbf1\{m(S)\in\cdot\}]\).

For any feasible \(a\),
\[
(a-a^\star)(m-\lambda)\ge0
\]
pointwise. Hence
\[
\mathbb E[am]-\mathbb E[a^\star m]
\ge
\lambda\big(\mathbb E[a]-\mathbb E[a^\star]\big).
\]
The left side is nonpositive, so
\(\mathbb E[a]\le\mathbb E[a^\star]\). Thus \(a^\star\) is optimal.

Equation (3) follows from conditional expectation.

Within bin \(j\), all support points are at distance at most \(1/K\), so the oscillation of \(m\) is at most \(L/K\). Therefore
\[
\begin{aligned}
\sum_j\theta_jb_j-\mathbb E[a^\star(S)m(S)]
&=
\sum_j\pi_j\left(
\mathbb E[m\mid B_j]\mathbb E[a^\star\mid B_j]
-\mathbb E[a^\star m\mid B_j]
\right)\\
&\le \frac LK\sum_j\pi_j
=\frac LK.
\end{aligned}
\]
Feasibility of \(a^\star\) proves (4). ∎

### Lemma 6 — Comparator-directed upper estimate

For the fixed vector \(b\) from Lemma 5, except on an event of probability at most \(2Te^{-z}\), simultaneously for every \(t\ge2\), with \(n=t-1\),
\[
b^\top\left(\frac{H_t}{n}-\theta\right)
\le
\frac{\sqrt{2A_nz}}n
+\frac{2z}{3n\gamma_n}
+\sqrt{\frac z{2n}}.
\tag{5}
\]

#### Proof

Decompose
\[
b^\top H_t-nb^\top\theta
=
\sum_{s=1}^n b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)
+
\sum_{s=1}^n
\big(b_{J_s}L_s-b^\top\theta\big).
\]

For the first sum, at fixed \(n\), the increments are martingale differences bounded above by
\[
p_s^{-1}\le\gamma_s^{-1}\le\gamma_n^{-1}.
\]
Their predictable quadratic variation is at most
\[
\sum_{s=1}^n \frac1{p_s}\le A_n.
\]
Lemma 1 therefore gives
\[
\sum_{s=1}^n b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)
\le
\sqrt{2A_nz}+\frac{2z}{3\gamma_n}
\]
except with probability \(e^{-z}\).

The second sum consists of i.i.d. centered variables in \([-1,1]\), with the uncentered variables in \([0,1]\). Hoeffding’s inequality gives the upper bound \(\sqrt{nz/2}\) except with probability \(e^{-z}\).

Union over \(n\le T-1\) proves (5) with failure probability at most \(2Te^{-z}\). ∎

### Lemma 7 — Robust comparator feasibility

On the event of Lemma 6, for every \(t\ge2\),
\[
U_t^\top b\le\epsilon+\frac LK+w_t.
\tag{6}
\]
Consequently,
\[
y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
\]
is feasible for the round-\(t\) FTRL problem, and
\[
\sum_j\pi_j(1-y_{t,j})
\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon}.
\tag{7}
\]

#### Proof

Since \(H_{t,j}\ge0\) and \(r_{t,j}\ge0\),
\[
U_{t,j}\le \frac{H_{t,j}}n+r_{t,j}.
\]
Moreover,
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
\tag{8}
\]
Here Cauchy–Schwarz was used, followed by
\[
\sum_jV_{t,j}=\sum_{s=1}^n\frac1{p_s}\le A_n.
\]

Because \(K=\lceil T^{1/4}\rceil\ge2\), the right side of (5) is at most \(w_t/2\). Combining this with (8) and Lemma 5,
\[
U_t^\top b
\le
\theta^\top b+w_t
\le
\epsilon+\frac LK+w_t.
\]
This proves (6), and hence \(U_t^\top y_t\le\epsilon\).

Finally,
\[
\begin{aligned}
\pi^\top(1-y_t)
&=\pi^\top(1-b)
+\left(1-\frac{\epsilon}{\epsilon+L/K+w_t}\right)\pi^\top b\\
&\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon},
\end{aligned}
\]
which is (7). ∎

### Lemma 8 — FTRL deferral comparison

Except on an event of probability at most \(2KTe^{-z}\), simultaneously for all \(t\ge2\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
\le
\mathbb E[1-a^\star(S)]
+2K\sqrt{\frac z{2(t-1)}}
+\frac{K}{2(t-1)}
+\frac{L/K+w_t}{\epsilon}.
\tag{9}
\]

#### Proof

Hoeffding’s inequality and a union bound give
\[
\max_j|\widehat\pi_{t,j}-\pi_j|
\le
d_n:=\sqrt{\frac z{2n}}
\]
simultaneously over \(t,j\), except with probability \(2KTe^{-z}\).

By FTRL optimality against the feasible \(y_t\),
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
\]
For every \(u\in[0,1]^K\),
\[
|\pi^\top(1-u)-\widehat\pi_t^\top(1-u)|
\le Kd_n.
\]
Thus
\[
\pi^\top(1-x_t)
\le
\pi^\top(1-y_t)+2Kd_n+\frac K{2n}.
\]
Apply (7). Since the current score is independent of \(\mathcal F_{t-1}\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
=\pi^\top(1-x_t).
\]
This proves (9). ∎

### Lemma 9 — Complete realized-cost concentration

Except with probability \(e^{-z}\),
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+\sum_{t=2}^T
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]\\
&+(1+c_R)\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\tag{10}
\]

#### Proof

For \(t\ge2\), let
\[
W_t=O_t+c_RD_tA_tL_t.
\]
Conditional on \(S_t,L_t\) and the past,
\[
\begin{aligned}
\mathbb E[W_t]
&=(1-x_{t,J_t})
+x_{t,J_t}q_t(x_{t,J_t})(1+c_RL_t)\\
&\le
(1-x_{t,J_t})+(1+c_R)\gamma_t,
\end{aligned}
\]
because \(xq_t(x)\le\gamma_t\).

After averaging over the current i.i.d. arrival,
\[
\mathbb E[W_t\mid\mathcal F_{t-1}]
\le
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
+(1+c_R)\gamma_t.
\]
Also \(0\le W_t\le1+c_R\). Hoeffding–Azuma yields
\[
\sum_{t=2}^TW_t
\le
\sum_{t=2}^T\mathbb E[W_t\mid\mathcal F_{t-1}]
+(1+c_R)\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

The first round costs one expert call, and every round costs \(c_M\). Enlarging \(\sum_{t=2}^T\gamma_t\) to \(\sum_{t=1}^T\gamma_t\) proves (10). ∎

### Lemma 10 — Comparator action and risk parity

Any comparator policy with cheap-release probability \(a(S)\) has expected expert-call cost at least \(\mathbb E[1-a(S)]\), correction cost at least zero, and released-error mean \(\mathbb E[a(S)m(S)]\). Equality in the cost lower bound is achieved without audits.

Moreover, every feasible comparator satisfies
\[
\Pr\left(
\sum_{t=1}^T R_t^{\rm comp}
>
\epsilon T+\sqrt{\frac{Tu}{2}}
\right)\le e^{-u}.
\]

#### Proof

A label not released cheaply must be replaced by the expert label, either by deferral or audit, so its expert-call probability is \(1-a(S)\). Auditing has the same unit expert cost as deferral and can additionally incur \(c_R\), hence replacing each audit by a coupled immediate deferral cannot increase cost or error.

Without audit, released error is the cheap-release indicator times \(L\), with mean \(\mathbb E[a(S)m(S)]\). Across i.i.d. rounds and independent comparator coins, these losses are independent \([0,1]\)-valued variables, so Hoeffding gives the stated tail bound. ∎

## Main proof

Intersect the following events:

1. Lemma 3’s simultaneous safety event;
2. Lemma 6’s comparator-directed upper-estimate event;
3. Lemma 8’s bin-frequency event;
4. Lemma 4’s released-error martingale event;
5. Lemma 9’s cost martingale event.

Since
\[
e^{-z}=\frac{\delta}{32KT},
\]
their total failure probability is at most
\[
2KTe^{-z}+2Te^{-z}+2KTe^{-z}+2e^{-z}<\delta.
\]

On this intersection, Lemma 4 directly gives
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\]

For cost, combine Lemmas 8 and 9:
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
&+(1+c_R)\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\]
Since
\[
(T-1)\mathbb E[1-a^\star(S)]
\le
T\mathbb E[1-a^\star(S)]
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

It remains to derive the announced rate. Put
\[
\ell=\log\frac{32T}{\delta}.
\]
For \(T\ge16\),
\[
T^{1/4}\le K\le2T^{1/4},
\qquad
z\le\frac32\ell,
\]
and
\[
\sum_{t=1}^Tt^{-1/4}\le\frac43T^{3/4}.
\]
Also,
\[
\sum_{n=1}^{T-1}n^{-1/2}\le2T^{1/2},\quad
\sum_{n=1}^{T-1}n^{-3/8}\le\frac85T^{5/8},
\]
\[
\sum_{n=1}^{T-1}n^{-3/4}\le4T^{1/4},\quad
\sum_{n=1}^{T-1}n^{-1}\le1+\log T.
\]

Using \(A_n\le n^{5/4}\),
\[
\begin{aligned}
\sum_{t=2}^Tw_t
&\le
\frac{16}{5}\sqrt{2Kz}\,T^{5/8}
+\frac83KzT^{1/4}
+2\sqrt2K\sqrt{zT}\\
&\le
27\,T^{3/4}\ell.
\end{aligned}
\]
Similarly,
\[
\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)
\le 10T^{3/4}\ell,
\]
and
\[
\frac{LT}{K}\le LT^{3/4}.
\]
Finally,
\[
\sqrt{\frac{Tz}{2}}\le T^{3/4}\ell.
\]

Collecting terms yields, for example,
\[
B_T
\le
64\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\]
Thus the theorem holds with the universal constant \(C_0=64\).

## Randomness and filtration accounting

The learner’s action-time filtration contains only past observable information. Before \(S_t\), \(x_t\) is determined by past \(N,H,V\), so it is \(\mathcal F_{t-1}\)-measurable. After \(S_t\), \(x_{t,J_t}\), \(q_t\), and \(p_t\) are measurable without access to \(Y_t\) or \(L_t\).

For importance weighting, the proof uses an enlarged filtration that mathematically reveals the latent current \(L_t\) before the routing and audit coins. This does not grant that information to the algorithm. Conditional on this enlarged pre-coin filtration,
\[
\mathbb E\left[\frac{O_tL_t}{p_t}\right]=L_t.
\]
Therefore both
\[
L_t\left(1-\frac{O_t}{p_t}\right)
\quad\text{and}\quad
L_t\left(\frac{O_t}{p_t}-1\right)
\]
are valid martingale differences in their respective orientations.

The adaptive observation probabilities may depend on all prior importance-weighted feedback. Lemma 2 handles this without conditioning on future confidence events: it constructs exponential supermartingales for fixed tuning parameters, applies Ville’s inequality, and only then unions over a deterministic grid.

The released-error proof uses the predictable indicator \(G_t\). Thus concentration is applied to a stopped/predictably masked process, not to a process conditioned on the future event that all confidence bounds succeed.

The three losses remain distinct throughout:

- \(L_t\) enters population risk and importance-weighted calibration;
- \(R_t=D_t(1-A_t)L_t\) is the released-label loss;
- \(O_tL_t/p_t\) is estimated feedback only.

The cost martingale contains every learner-side paid component:
the model call, expert deferrals, audits, and audited-error corrections. The comparator also pays every model call and all expert calls; its optimal representative uses no audits and hence no corrections.

## Boundary cases and counterexample attempts

Empty bins cause no problem: \(\pi_j=\theta_j=0\), and \(b_j\) may be set to zero.

Atoms at bin boundaries are handled by the fixed half-open partition. Atoms of \(m(S)\) at the comparator threshold are handled by the randomization coefficient \(\rho\).

If \(m\equiv0\), the comparator releases every cheap prediction; the confidence radii may initially force deferrals, but all such cost is included in \(B_T\).

If \(\epsilon=1\), the safety constraint and scaling argument remain valid. If \(L=0\), the discretization term vanishes. Costs \(c_M=0,1\) and \(c_R=0,1\) are all covered.

The principal attempted break was adaptivity of \(V_{t,j}\). Substituting a random predictable variance into a fixed-variance Freedman inequality would not be justified. Lemma 2 avoids that invalid substitution through a deterministic tuning grid and Ville’s inequality. The factor \(z/(3\gamma_n)\) supplies exactly the discretization slack needed for the curved variance boundary.

No monotonicity or semantic interpretation of the raw score is used. Lipschitzness enters only in the continuum-to-bin comparator approximation.

## Self-audit

1. The most delicate step is Lemma 2’s variance-adaptive grid argument. Its key numerical requirements are \(T\ge16\), \(z\ge8\), and \(p_t\ge t^{-1/4}\); all three are explicit theorem or algorithm conditions.

2. The cost proof deliberately does not require two-sided simultaneous binwise confidence bounds. Upper control is needed only in the fixed optimal-comparator direction \(b\), where deterministic-variance Freedman suffices. This prevents an unjustified adaptive random-variance upper-tail step.

3. Comparator attainment uses the scalar threshold structure of the one-constraint population problem. The atom-randomization argument covers noncontinuous distributions.

4. The final constant \(64\) is intentionally loose; all powers of \(T\), \(L/\epsilon\), audit cost, and correction cost are retained.

## Open obligations