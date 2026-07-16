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
Z_t=(S_t,\widehat Y_t,Y_t),\qquad
\pi_j=\Pr(S\in B_j),\qquad
\theta_j=\Pr(S\in B_j,L=1).
\]
By A1, \(Z_1,Z_2,\ldots\) are i.i.d. By the defining property of the conditional error curve,
\[
\theta_j=\mathbb E[\mathbf1\{S\in B_j\}m(S)].
\]

Take the bins half-open except for the last, so every score belongs to exactly one bin and each bin has diameter at most \(1/K\).

At \(t=1\), define
\[
D_1=0,\qquad A_1=0,\qquad O_1=1,\qquad p_1=1.
\]
Thus round \(1\) is the prescribed expert round and \(R_1=0\).

To repair the filtration defect identified by the reviewer, construct the probability space using, in addition to the i.i.d. \(Z_t\), independent uniforms
\[
U_t^{D},U_t^{A}\sim{\rm Unif}[0,1],
\]
independent across \(t\) and independent of all arrivals. They generate routing and audit coins:
\[
D_t=\mathbf1\{U_t^D\le x_{t,J_t}\},\qquad
A_t=\mathbf1\{U_t^A\le q_t(x_{t,J_t})\}
\]
on cheap-routed rounds, with \(A_t=0\) when \(D_t=0\).

Let
\[
\mathscr P_t
=
\sigma\!\left(
Z_1,\ldots,Z_t,\,
U_1^D,U_1^A,\ldots,U_{t-1}^D,U_{t-1}^A
\right)
\]
be the proof-only pre-coin field, and
\[
\mathscr H_t
=
\mathscr P_t\vee\sigma(U_t^D,U_t^A)
\]
the proof-only post-coin field. Then
\[
\mathscr H_{t-1}\subseteq\mathscr P_t\subseteq
\mathscr H_t\subseteq\mathscr P_{t+1}.
\tag{1}
\]
Unlike the previously criticized \(\mathcal G_{t,-}\), these fields retain every past latent \(Y_s,L_s\), including those from unaudited rounds.

The actual observable field satisfies
\[
\mathcal F_{t-1}\subseteq\mathscr H_{t-1}.
\]
The algorithm still uses only \(\mathcal F_{t-1}\): \(x_t\) is \(\mathcal F_{t-1}\)-measurable, while \(q_t,p_t\) use only the past and the current score. Revealing \(Y_t\) in \(\mathscr P_t\) is solely a proof device and does not alter the algorithm.

Conditional on \(\mathscr P_t\),
\[
O_t\sim{\rm Bernoulli}(p_t),\qquad
p_t=1-x_{t,J_t}+x_{t,J_t}q_t(x_{t,J_t})
=\max\{1-x_{t,J_t},\gamma_t\}.
\tag{2}
\]
In particular,
\[
p_t\ge\gamma_t.
\tag{3}
\]

The constrained objective is strongly convex and the feasible set is nonempty and compact, since \(x=0\) is feasible. Hence \(x_t\) is unique. Standard measurable-argmin reasoning makes it a measurable function of the past statistics, as required.

Finally,
\[
A_n=\sum_{s=1}^ns^{1/4}\le n^{5/4}.
\tag{4}
\]

## Lemmas

### Lemma 1 — One-sided Bernstein–Freedman inequality

Let \((\mathscr K_s)\) be a filtration. Suppose \(X_s\) is \(\mathscr K_s\)-measurable,
\[
\mathbb E[X_s\mid\mathscr K_{s-1}]=0,\qquad X_s\le b,
\]
and \(v_s\) is nonnegative and \(\mathscr K_{s-1}\)-measurable with
\[
\mathbb E[X_s^2\mid\mathscr K_{s-1}]\le v_s.
\]
For \(0<\lambda<3/b\),
\[
\exp\left\{
\lambda\sum_{s=1}^nX_s
-\frac{\lambda^2}{2(1-\lambda b/3)}
 \sum_{s=1}^nv_s
\right\}
\tag{5}
\]
is a nonnegative supermartingale.

If \(\sum_{s=1}^nv_s\le v\) deterministically, then
\[
\Pr\left(
\sum_{s=1}^nX_s>
\sqrt{2vz}+\frac{2bz}{3}
\right)\le e^{-z}.
\tag{6}
\]

#### Proof

For \(x\le b\) and \(0<\lambda<3/b\),
\[
e^{\lambda x}
\le
1+\lambda x+
\frac{\lambda^2x^2}{2(1-\lambda b/3)}.
\tag{7}
\]
For \(\lambda x\le0\), this follows from
\(e^u\le1+u+u^2/2\). For \(0\le x\le b\), expand the exponential and use
\[
k!\ge 2\cdot3^{k-2},\qquad k\ge2.
\]
Taking conditional expectations in (7), using the martingale-difference property and \(1+u\le e^u\), proves (5).

Markov’s inequality applied to (5) yields
\[
\Pr\left(\sum_{s=1}^nX_s\ge x\right)
\le
\exp\left\{-\frac{x^2}{2(v+bx/3)}\right\}.
\]
For \(x=\sqrt{2vz}+2bz/3\),
\[
x^2\ge 2z(v+bx/3),
\]
which proves (6). ∎

### Lemma 2 — Adaptive importance-weighted underestimation under a nested filtration

For bin \(j\), put
\[
M_{n,j}
=
\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right),
\]
and
\[
\overline V_{n,j}
=
\sum_{s=1}^n\frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\]
Except on an event of probability at most \(Te^{-z}\), simultaneously for every \(1\le n\le T\),
\[
M_{n,j}
\le
\sqrt{2\overline V_{n,j}z}
+\frac{z}{3\gamma_n}.
\tag{8}
\]

This lemma uses A2, the observation floor, and the nested proof-only filtration (1).

#### Proof

Define the interlaced filtration
\[
\mathscr K_{2s-2}=\mathscr H_{s-1},\qquad
\mathscr K_{2s-1}=\mathscr P_s,\qquad
\mathscr K_{2s}=\mathscr H_s.
\]
At the arrival-revelation step use increment \(0\), and at the coin step use
\[
X_{s,j}
=
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
This variable is \(\mathscr H_s\)-measurable. Conditional on \(\mathscr P_s\), the score and latent loss are fixed, while (2) gives
\[
\mathbb E[X_{s,j}\mid\mathscr P_s]=0.
\tag{9}
\]
Also \(X_{s,j}\le1\), and
\[
\begin{aligned}
\mathbb E[X_{s,j}^2\mid\mathscr P_s]
&=
\mathbf1\{S_s\in B_j\}L_s
\left(\frac1{p_s}-1\right)\\
&\le
\frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\end{aligned}
\tag{10}
\]
The right side is \(\mathscr P_s\)-measurable. Thus Lemma 1 applies to the interlaced filtration. The accumulated exponential process is adapted because \(\mathscr H_s\) retains all latent variables appearing in every earlier increment.

Fix \(\mu>0\), and set
\[
\lambda=\frac{\mu}{1+\mu/3}\in(0,3).
\]
Then
\[
\frac{\lambda^2}{2(1-\lambda/3)}
=\frac{\lambda\mu}{2}.
\]
Lemma 1 and Ville’s inequality therefore give, except with probability \(e^{-z}\),
\[
M_{n,j}
\le
\frac{\mu\overline V_{n,j}}2+\frac z\mu+\frac z3
\tag{11}
\]
simultaneously over \(n\).

Use a deterministic multiplicative grid on
\[
\left[
\sqrt{\frac{2z}{A_T}},
\sqrt{2z}
\right]
\]
with consecutive ratio at most \(r=1+T^{-1/2}\). Since \(A_T\le T^{5/4}\), its cardinality is at most
\[
2+\frac{(5/8)\log T}{\log(1+T^{-1/2})}
\le 2+\frac54\sqrt T\log T
\le T
\tag{12}
\]
for \(T\ge16\). The last inequality holds at \(T=16\) and remains valid thereafter.

If \(\overline V_{n,j}=0\), then \(M_{n,j}=0\). Otherwise
\[
1\le\overline V_{n,j}\le A_n\le A_T,
\]
so
\[
\mu^\star=\sqrt{\frac{2z}{\overline V_{n,j}}}
\]
lies in the grid interval. Choose a grid point
\(\mu=\rho\mu^\star\) with \(1\le\rho\le r\). Then
\[
\frac{\mu\overline V}{2}+\frac z\mu
=
\sqrt{2\overline Vz}\,
\frac{\rho+\rho^{-1}}2
\le
\sqrt{2\overline Vz}
+\frac{\sqrt{2\overline Vz}}{2T},
\tag{13}
\]
because
\[
\frac{\rho+\rho^{-1}}2-1
=\frac{(\rho-1)^2}{2\rho}\le\frac1{2T}.
\]

Here \(z>8\), since \(T\ge16\), \(K\ge2\), and \(\delta<1/4\). For \(2\le n\le T\),
\[
\frac{\sqrt{2\overline V_{n,j}z}}{2T}
\le
\frac{(n^{1/4}-1)z}{3}.
\tag{14}
\]
For \(n=2,3,4\), this follows directly from
\(\overline V_{n,j}\le n^{5/4}\), \(T\ge16\), and \(z\ge8\). For \(n\ge5\), use \(T\ge n\), \(z\ge8\), and
\[
\frac34n^{-3/8}\le n^{1/4}-1.
\]
At \(n=1\), \(O_1=p_1=1\), so \(M_{1,j}=0\).

Combining (11)–(14),
\[
M_{n,j}
\le
\sqrt{2\overline V_{n,j}z}
+\frac{n^{1/4}z}{3}
=
\sqrt{2\overline V_{n,j}z}
+\frac z{3\gamma_n}.
\]
Unioning over at most \(T\) deterministic grid points proves (8). ∎

### Lemma 3 — Simultaneous calibration validity

Except on an event of probability at most \(2KTe^{-z}\), simultaneously for all \(t\ge2\) and all bins \(j\),
\[
\theta_j\le U_{t,j}.
\tag{15}
\]

This lemma uses A1, A2, and Lemma 2.

#### Proof

Let \(n=t-1\) and
\[
E_{n,j}
=
\sum_{s=1}^n\mathbf1\{S_s\in B_j\}L_s.
\]
The summands are i.i.d. Bernoulli with mean \(\theta_j\). Hence
\[
\Pr\left(
\theta_j-\frac{E_{n,j}}n>
\sqrt{\frac z{2n}}
\right)\le e^{-z}.
\]
A union bound over \(j\) and \(n\le T\) costs at most \(KTe^{-z}\).

Moreover,
\[
E_{n,j}-H_{t,j}=M_{n,j},
\qquad
\overline V_{n,j}=V_{t,j}.
\]
Lemma 2, unioned over \(K\) bins, gives
\[
\theta_j
\le
\frac{H_{t,j}}n+
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}n
+\sqrt{\frac z{2n}}
=
\widehat a_{t,j}+r_{t,j}.
\]
Because \(0\le\theta_j\le1\), clipping the right side to \([0,1]\) preserves the inequality. ∎

### Lemma 4 — Population safety and released-error concentration

On the event of Lemma 3, except for an additional event of probability \(e^{-z}\),
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\tag{16}
\]

This lemma uses A1, the FTRL risk constraint, and Lemma 3.

#### Proof

For \(t\ge2\), define the predictable indicator
\[
G_t=\mathbf1\{\theta_j\le U_{t,j}\text{ for every }j\},
\]
and set \(G_1=1\). Since \(U_t\) depends only on past observations,
\(G_t\) is \(\mathcal F_{t-1}\)-measurable and hence
\(\mathscr H_{t-1}\)-measurable.

The current arrival is independent of \(\mathscr H_{t-1}\). Therefore, when \(G_t=1\),
\[
\begin{aligned}
\mathbb E[D_tL_t\mid\mathscr H_{t-1}]
&=\sum_{j=1}^Kx_{t,j}\theta_j\\
&\le\sum_{j=1}^Kx_{t,j}U_{t,j}
\le\epsilon.
\end{aligned}
\tag{17}
\]
Auditing can only reduce released loss:
\[
R_t=D_t(1-A_t)L_t\le D_tL_t.
\]
Consequently,
\[
\mathbb E[G_tR_t\mid\mathscr H_{t-1}]
\le\epsilon G_t\le\epsilon.
\tag{18}
\]

The variables
\[
G_tR_t-\mathbb E[G_tR_t\mid\mathscr H_{t-1}]
\]
are martingale differences for the nested full filtration
\((\mathscr H_t)\), with conditional range length at most \(1\). Hoeffding–Azuma gives
\[
\sum_{t=1}^TG_tR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\). On the event of Lemma 3, \(G_t=1\) for every \(t\), proving (16). This masking argument does not condition a martingale bound on a future confidence event. ∎

### Lemma 5 — Comparator attainment and discretization

The infimum defining \(C_T^\star\) is attained by a Borel policy \(a^\star\). If
\[
b_j=
\mathbb E[a^\star(S)\mid S\in B_j]
\]
when \(\pi_j>0\), and \(b_j=0\) when \(\pi_j=0\), then
\[
\sum_j\pi_j(1-b_j)
=
\mathbb E[1-a^\star(S)]
\tag{19}
\]
and
\[
\sum_j\theta_jb_j
\le
\epsilon+\frac LK.
\tag{20}
\]

This lemma uses A3 and \(\epsilon>0\).

#### Proof

The Lipschitz version of \(m\) on the support of \(S\) has a Borel Lipschitz extension to \([0,1]\), which may be clipped to \([0,1]\). Hence \(m(S)\) may be represented by a Borel function.

If \(\mathbb E[m(S)]\le\epsilon\), then \(a^\star\equiv1\) is optimal.

Otherwise, define the finite measure
\[
\nu(A)=\mathbb E[m(S)\mathbf1\{m(S)\in A\}].
\]
Choose \(\lambda\in(0,1]\) such that
\[
\nu([0,\lambda))\le\epsilon\le\nu([0,\lambda]).
\]
Choose \(\rho\in[0,1]\) satisfying
\[
\nu([0,\lambda))+\rho\nu(\{\lambda\})=\epsilon,
\]
and set
\[
a^\star(s)
=
\mathbf1\{m(s)<\lambda\}
+\rho\mathbf1\{m(s)=\lambda\}.
\tag{21}
\]
Then
\[
\mathbb E[a^\star(S)m(S)]=\epsilon.
\]

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
The left side is nonpositive by feasibility, and \(\lambda>0\), so
\[
\mathbb E[a]\le\mathbb E[a^\star].
\]
Thus \(a^\star\) attains the optimum.

Equation (19) follows from conditional expectation. For (20), let
\[
\bar m_j=\mathbb E[m(S)\mid S\in B_j].
\]
For \(S\in B_j\) on the score support,
\[
|\bar m_j-m(S)|\le\frac LK.
\tag{22}
\]
Therefore
\[
\begin{aligned}
\sum_j\theta_jb_j-\mathbb E[a^\star(S)m(S)]
&=
\sum_j\pi_j
\mathbb E[
a^\star(S)(\bar m_j-m(S))
\mid S\in B_j]\\
&\le\frac LK\sum_j\pi_j
=\frac LK.
\end{aligned}
\]
Feasibility of \(a^\star\) proves (20). ∎

### Lemma 6 — Comparator-directed importance-weighted bound under the nested filtration

For the deterministic vector \(b\) from Lemma 5, except on an event \(\mathcal E_b^c\) of probability at most \(2Te^{-z}\), simultaneously for every \(t\ge2\), with \(n=t-1\),
\[
b^\top\left(\frac{H_t}{n}-\theta\right)
\le
\frac{\sqrt{2A_nz}}n
+\frac{2z}{3n\gamma_n}
+\sqrt{\frac z{2n}}.
\tag{23}
\]

This lemma uses A1, A2, Lemma 1, and the nested filtration (1).

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
\left(b_{J_s}L_s-b^\top\theta\right).
\end{aligned}
\tag{24}
\]

For the first sum, again use the interlaced filtration
\[
\mathscr H_{s-1}\subseteq\mathscr P_s\subseteq\mathscr H_s.
\]
At the coin step define
\[
Z_s=b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right).
\]
It is \(\mathscr H_s\)-measurable and
\[
\mathbb E[Z_s\mid\mathscr P_s]=0.
\tag{25}
\]
For fixed \(n\) and \(s\le n\),
\[
Z_s\le p_s^{-1}
\le\gamma_s^{-1}\le\gamma_n^{-1},
\tag{26}
\]
and
\[
\begin{aligned}
\mathbb E[Z_s^2\mid\mathscr P_s]
&=
b_{J_s}^2L_s\left(\frac1{p_s}-1\right)\\
&\le\frac1{p_s}
\le\gamma_s^{-1}.
\end{aligned}
\tag{27}
\]
Thus its predictable quadratic variation is at most
\[
\sum_{s=1}^n\gamma_s^{-1}=A_n.
\]
Lemma 1 with \(b=\gamma_n^{-1}\) gives
\[
\sum_{s=1}^nZ_s
\le
\sqrt{2A_nz}+\frac{2z}{3\gamma_n}
\tag{28}
\]
except with probability \(e^{-z}\).

The second sum in (24) consists of i.i.d. centered variables whose uncentered versions lie in \([0,1]\), because \(b\) is a fixed population-dependent vector. Hoeffding gives
\[
\sum_{s=1}^n
\left(b_{J_s}L_s-b^\top\theta\right)
\le\sqrt{\frac{nz}{2}}
\tag{29}
\]
except with probability \(e^{-z}\).

Unioning (28) and (29) over \(n\le T-1\), then dividing by \(n\), proves (23). The exponential processes in (28) are adapted because all past latent losses remain in \(\mathscr H_s\); no latent variable disappears at the next round. ∎

### Lemma 7 — Robust comparator feasibility

On \(\mathcal E_b\), for every \(t\ge2\),
\[
U_t^\top b\le\epsilon+\frac LK+w_t.
\tag{30}
\]
Consequently,
\[
y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
\tag{31}
\]
is feasible for the round-\(t\) FTRL problem, and
\[
\pi^\top(1-y_t)
\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon}.
\tag{32}
\]

This lemma uses Lemmas 5 and 6 and the algorithm’s confidence radii.

#### Proof

Because \(H_{t,j},r_{t,j}\ge0\),
\[
U_{t,j}\le\frac{H_{t,j}}n+r_{t,j}.
\]
Moreover, Cauchy–Schwarz and \(p_s\ge\gamma_s\) give
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
\tag{33}
\]
Since \(K\ge2\), the right side of (23) is at most \(w_t/2\). Hence
\[
\begin{aligned}
U_t^\top b
&\le b^\top\frac{H_t}{n}+\sum_jr_{t,j}\\
&\le b^\top\theta+w_t\\
&\le\epsilon+\frac LK+w_t,
\end{aligned}
\]
where the last line uses Lemma 5. This proves (30), and (31) is therefore feasible.

Writing
\[
\alpha_t=\frac{\epsilon}{\epsilon+L/K+w_t},
\]
we have
\[
\begin{aligned}
\pi^\top(1-y_t)
&=\pi^\top(1-b)+(1-\alpha_t)\pi^\top b\\
&\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon},
\end{aligned}
\]
because \(\pi^\top b\le1\) and
\[
1-\alpha_t
=
\frac{L/K+w_t}{\epsilon+L/K+w_t}
\le\frac{L/K+w_t}{\epsilon}.
\]
∎

### Lemma 8 — FTRL deferral comparison

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
\tag{34}
\]
On \(\mathcal E_b\cap\mathcal E_\pi\), simultaneously for all \(t\ge2\),
\[
\begin{aligned}
\mathbb E[1-x_{t,J_t}\mid\mathscr H_{t-1}]
\le{}&
\mathbb E[1-a^\star(S)]
+2K\sqrt{\frac z{2(t-1)}}\\
&+\frac{K}{2(t-1)}
+\frac{L/K+w_t}{\epsilon}.
\end{aligned}
\tag{35}
\]

This lemma uses A1, Lemma 7, empirical-frequency concentration, and FTRL optimality.

#### Proof

For fixed \(n,j\), Hoeffding gives
\[
\Pr\left(
|\widehat\pi_{t,j}-\pi_j|>
\sqrt{\frac z{2n}}
\right)\le2e^{-z}.
\]
Unioning over \(j,n\) proves (34).

On \(\mathcal E_b\), Lemma 7 makes \(y_t\) feasible. FTRL optimality gives
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
\tag{36}
\]
On \(\mathcal E_\pi\), every \(u\in[0,1]^K\) satisfies
\[
\left|
\pi^\top(1-u)-\widehat\pi_t^\top(1-u)
\right|
\le
K\sqrt{\frac z{2n}}.
\]
Applying this to \(u=x_t\) and \(u=y_t\) in (36),
\[
\pi^\top(1-x_t)
\le
\pi^\top(1-y_t)
+2K\sqrt{\frac z{2n}}
+\frac K{2n}.
\]
Now apply (32).

Because \(x_t\) is measurable with respect to the observable past and \(S_t\) is independent even of the larger field \(\mathscr H_{t-1}\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathscr H_{t-1}]
=\pi^\top(1-x_t).
\]
This proves (35). Both \(\mathcal E_b\) and \(\mathcal E_\pi\) are explicitly required. ∎

### Lemma 9 — Complete realized-cost concentration

Except on an event of probability \(e^{-z}\),
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+\sum_{t=2}^T
\mathbb E[1-x_{t,J_t}\mid\mathscr H_{t-1}]\\
&+(1+c_R)
\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\tag{37}
\]

This lemma uses A1–A2, the audit rule, and Hoeffding–Azuma on the nested full filtration.

#### Proof

For \(t\ge2\), let
\[
W_t=O_t+c_RD_tA_tL_t.
\]
Conditional on \(\mathscr P_t\),
\[
\begin{aligned}
\mathbb E[W_t\mid\mathscr P_t]
&=(1-x_{t,J_t})
+x_{t,J_t}q_t(x_{t,J_t})(1+c_RL_t)\\
&\le
1-x_{t,J_t}+(1+c_R)\gamma_t,
\end{aligned}
\tag{38}
\]
because
\[
xq_t(x)=[x+\gamma_t-1]_+\le\gamma_t.
\]
Taking conditional expectation given \(\mathscr H_{t-1}\),
\[
\mathbb E[W_t\mid\mathscr H_{t-1}]
\le
\mathbb E[1-x_{t,J_t}\mid\mathscr H_{t-1}]
+(1+c_R)\gamma_t.
\tag{39}
\]

Also \(0\le W_t\le1+c_R\). Thus
\[
W_t-\mathbb E[W_t\mid\mathscr H_{t-1}]
\]
is a martingale difference with conditional range length at most \(1+c_R\). Hoeffding–Azuma yields
\[
\sum_{t=2}^TW_t
\le
\sum_{t=2}^T\mathbb E[W_t\mid\mathscr H_{t-1}]
+(1+c_R)\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

Every round pays \(c_M\), and round \(1\) pays exactly one expert cost. Enlarging the audit-floor sum to include \(t=1\) proves (37). ∎

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
\tag{40}
\]
Allowing comparator audits cannot reduce its cost below the no-audit benchmark.

This lemma uses A1–A2 and the stated comparator semantics.

#### Proof

Given \(S_t=s\), use an independent uniform to release the unaudited cheap label with probability \(a(s)\), and otherwise defer immediately. The comparator pays \(c_M\) always, pays the expert with probability \(1-a(S)\), and pays no correction cost.

Its released loss has mean
\[
\mathbb E[a(S)L]
=
\mathbb E[a(S)m(S)]
\le\epsilon.
\]
The arrivals and comparator randomization are independent across rounds, so Hoeffding proves (40).

More generally, suppose a comparator cheap-routes with probability \(x(s)\) and audits with conditional probability \(q(s)\). Its final cheap-release probability is
\[
a(s)=x(s)(1-q(s)),
\]
while its expert-call probability is
\[
1-x(s)+x(s)q(s)=1-a(s).
\]
The no-audit policy that cheap-routes with probability \(a(s)\) and otherwise immediately defers has the same released-label distribution and the same expert-call cost, while deleting the nonnegative correction charge
\[
c_Rx(s)q(s)m(s).
\]
Thus auditing is weakly dominated. ∎

## Main proof

Define the following events:

- \(\mathcal E_{\rm cal}\): the event in Lemma 3;
- \(\mathcal E_b\): the event in Lemma 6;
- \(\mathcal E_\pi\): the frequency event in Lemma 8;
- \(\mathcal E_R\): the released-error martingale event in Lemma 4;
- \(\mathcal E_C\): the cost martingale event in Lemma 9.

Their total failure probability is at most
\[
(2KT+2T+2KT+2)e^{-z}.
\]
Since
\[
e^{-z}=\frac{\delta}{32KT},
\]
this is
\[
\delta\left(
\frac18+\frac1{16K}+\frac1{16KT}
\right)<\delta.
\tag{41}
\]

On \(\mathcal E_{\rm cal}\cap\mathcal E_R\), Lemma 4 gives the error guarantee
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\tag{42}
\]

For cost, combine Lemmas 8 and 9 on
\(\mathcal E_b\cap\mathcal E_\pi\cap\mathcal E_C\):
\[
\begin{aligned}
C_T
\le{}&
c_MT+1
+(T-1)\mathbb E[1-a^\star(S)]\\
&+\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}
+\frac{K}{2(t-1)}
\right)\\
&+\frac1\epsilon
\sum_{t=2}^T\left(\frac LK+w_t\right)\\
&+(1+c_R)
\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\tag{43}
\]
Since
\[
(T-1)\mathbb E[1-a^\star(S)]
\le T\mathbb E[1-a^\star(S)]
\]
and
\[
\sum_{t=2}^T\frac LK\le\frac{LT}{K},
\]
the right side of (43) is at most
\[
T\left[c_M+\mathbb E[1-a^\star(S)]\right]+B_T
=C_T^\star+B_T.
\tag{44}
\]

It remains to derive the displayed rate. Put
\[
\ell=\log\frac{32T}{\delta}.
\]
For \(T\ge16\),
\[
T^{1/4}\le K\le2T^{1/4},
\qquad
z=\ell+\log K\le\frac32\ell.
\tag{45}
\]
The second inequality follows from
\(\log K\le\log2+\frac14\log T\) and
\(\ell>\log(128T)\).

The elementary integral bounds
\[
\sum_{t=1}^Tt^{-1/4}\le\frac43T^{3/4},
\tag{46}
\]
\[
\sum_{n=1}^{T-1}n^{-3/8}\le\frac85T^{5/8},
\quad
\sum_{n=1}^{T-1}n^{-3/4}\le4T^{1/4},
\tag{47}
\]
and
\[
\sum_{n=1}^{T-1}n^{-1/2}\le2T^{1/2},
\quad
\sum_{n=1}^{T-1}n^{-1}\le1+\log T
\tag{48}
\]
will be used.

From \(A_n\le n^{5/4}\),
\[
\begin{aligned}
\sum_{t=2}^Tw_t
&\le
\frac{16}{5}\sqrt{2Kz}\,T^{5/8}
+\frac83KzT^{1/4}
+2\sqrt2K\sqrt{zT}.
\end{aligned}
\tag{49}
\]
Let
\[
X=T^{3/4}\ell.
\]
Using \(K\le2T^{1/4}\), \(z\le\frac32\ell\), and
\(\sqrt z\le z\le\frac32\ell\), the three terms in (49) are respectively at most
\[
\frac{48}{5}X,\qquad 8X,\qquad 6\sqrt2\,X.
\]
Their sum is less than \(27X\), so
\[
\sum_{t=2}^Tw_t\le27X.
\tag{50}
\]

Similarly,
\[
\begin{aligned}
&\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)\\
&\qquad\le
2\sqrt2K\sqrt{zT}
+\frac K2(1+\log T)
\le10X.
\end{aligned}
\tag{51}
\]
Also,
\[
\frac{LT}{K}\le LT^{3/4}\le LX,
\tag{52}
\]
and
\[
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\le3X.
\tag{53}
\]
Since \(X\ge1\), (50)–(53) imply
\[
B_T
\le
X\left[
11+3(1+c_R)+\frac{L+27}{\epsilon}
\right].
\tag{54}
\]
Let
\[
A=1+c_R,\qquad Q=\frac{1+L}{\epsilon}.
\]
Because \(A\ge1\),
\[
11+3A\le27A,
\]
and because \(L\ge0\),
\[
\frac{L+27}{\epsilon}\le27Q.
\]
Thus
\[
B_T
\le
27\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\tag{55}
\]
The universal constant may therefore be taken as
\[
C_0=27.
\]

Equations (41)–(55) prove both simultaneous guarantees and the asserted fixed-horizon asymptotic rates.

## Randomness and filtration accounting

The observable filtration and proof-only filtration serve different purposes.

Before the model call, \(x_t\) is \(\mathcal F_{t-1}\)-measurable. After observing the current model output and score, \(x_{t,J_t}\), \(q_t\), and \(p_t\) are determined without access to \(Y_t\) or \(L_t\). Therefore all learner actions and audit probabilities are predictable in the constitution’s sense.

For analysis, the nested fields
\[
\mathscr H_{t-1}\subseteq\mathscr P_t\subseteq\mathscr H_t
\]
retain every latent arrival forever. Conditional on \(\mathscr P_t\),
\[
\mathbb E\left[\frac{O_tL_t}{p_t}\,\middle|\,\mathscr P_t\right]=L_t.
\]
Hence both
\[
L_t\left(1-\frac{O_t}{p_t}\right)
\quad\text{and}\quad
L_t\left(\frac{O_t}{p_t}-1\right)
\]
are valid coin-step martingale differences in the interlaced filtration.

This directly resolves the reviewer’s objection: the discarded fields
\(\mathcal G_{t,-}\) are not used. The exponential processes in Lemmas 2 and 6 are adapted to a genuinely nested filtration, and the variance bounds are measurable immediately before the corresponding coin increments.

The concentration tools are applied as follows:

- Lemma 2: Ville’s inequality for adapted nonnegative supermartingales, followed by a union bound over a deterministic tuning grid.
- Lemma 3: i.i.d. Hoeffding concentration for true bin-error masses, plus Lemma 2.
- Lemma 6: Bernstein–Freedman for the importance-weighted coin martingale and Hoeffding for the independent arrival sum.
- Lemma 8: two-sided i.i.d. Hoeffding bounds for bin frequencies.
- Lemma 4: Hoeffding–Azuma on the full nested filtration using a predictable confidence mask.
- Lemma 9: Hoeffding–Azuma applied to the complete paid round cost.
- Lemma 10: Hoeffding for an independently randomized comparator deployment.

No concentration inequality is conditioned on a future confidence event.

The three losses remain distinct throughout:

- \(L_t\): latent counterfactual cheap-source loss;
- \(R_t=D_t(1-A_t)L_t\): final released-label loss;
- \(O_tL_t/p_t\): importance-weighted feedback.

Every learner round pays \(c_M\). Expert deferrals, audits, and audited-error corrections are included in \(C_T\). The comparator also pays every model and expert call; its no-audit representative incurs no correction charge.

## Boundary cases and counterexample attempts

Empty bins have \(\pi_j=\theta_j=0\), and setting \(b_j=0\) is harmless. Atoms at bin boundaries are assigned uniquely by the half-open convention. Atoms at the optimal comparator threshold are handled by the randomization parameter \(\rho\).

The audit rule is valid for every \(x\). If its numerator is positive, then
\[
0<x+\gamma_t-1\le x,
\]
so \(q_t(x)\in[0,1]\). If \(x=0\), immediate deferral observes the expert label with probability one.

At \(t=1\), the learner uses the expert, so \(R_1=0\), \(O_1=p_1=1\), and the importance-weighted martingale increment is exactly zero.

If \(m\equiv0\), the comparator releases every cheap label. The learner’s conservative early deferrals and audits are still covered by \(B_T\). If \(L=0\), the continuum-to-bin approximation term vanishes. The endpoint cases \(\epsilon=1\) and \(c_M,c_R\in\{0,1\}\) require no modification.

An exact-boundary comparator does not require strict complementarity, uniqueness, a margin, or optimizer-local curvature. Lemma 7 scales the comparator toward the safe expert and explicitly charges the resulting \(1/\epsilon\) penalty.

The reviewer’s filtration counterexample does break the former proof: under the former non-nested fields, an unaudited \(L_s\) could disappear from the next field. In the repaired construction, \(L_s\) remains in every \(\mathscr P_t,\mathscr H_t\) for \(t>s\), so every accumulated exponential process remains measurable and adapted.

Without A3, many statistically unrelated score regions can remain unidentified under sublinear feedback. A3 blocks this construction through a global, optimizer-independent Lipschitz condition. No monotonicity or raw-score calibration identity is used.

## Self-audit

1. The most delicate step is Lemma 2’s random-variance boundary. It is reduced to deterministic-\(\mu\) supermartingales, a deterministic grid of at most \(T\) values, and the explicit absorption inequality (14).

2. The proof-only filtration is intentionally larger than the learner’s information. Its only role is analysis: actions remain functions of \(\mathcal F_{t-1}\) and the current score. The interlaced construction verifies both adaptation and pre-coin variance measurability.

3. Lemma 8 requires two distinct events: empirical bin-frequency concentration and comparator-directed importance-weighted concentration. Both appear in the event intersection and the final union bound.

4. Comparator attainment depends on selecting a Borel version of the globally Lipschitz conditional error function. A3 supplies such a version on the support, and a Lipschitz extension supplies the needed Borel representative on \([0,1]\).

5. The numerical constant \(C_0=27\) is coarse but follows explicitly from (45)–(54); no hidden asymptotic term is omitted.

## Open obligations

None.