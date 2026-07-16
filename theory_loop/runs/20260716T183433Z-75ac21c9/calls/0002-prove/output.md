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