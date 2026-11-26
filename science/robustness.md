# Phase errors and lattice accuracy

The bounds below apply to the nominal-lattice encoder and decoder with one simultaneous exposure. They quantify diagonal phase errors separately from errors in preparation and decoding. A [separate receiver](calibration.md) attains the minimax error order on a bounded physical coefficient interval and gives the corresponding result under bounded, unsupplied position errors.

## Exact excess risk for diagonal phase errors

Let $`n(q)=(n_0(q),\ldots,n_{N-1}(q))`$ be the computational basis word of logical charge $`q=0,\ldots,L-1`$. All words have the same charges $`Q_a=\sum_j\binom{j}{a}n_j`$ for $`a<d`$, and $`Q_d(n(q))=Q_d(n(0))+q`$. The sine probe has amplitudes

```math
a_q=\sqrt{\frac{2}{L+1}}\sin\!\left(\frac{\pi(q+1)}{L+1}\right).
```

An additional phase $`e_j`$ at site $`j`$ adds $`g_q=\sum_j e_j n_j(q)`$ to word $`q`$. The model allows any real error vector in each exposure, including one that depends on the signal or nuisance fields. The formulas below hold for each such vector. Use the sign convention in which the signal adds $`q\phi`$ and apply the inverse Fourier transform to the decoded label. For $`M>L`$ bins $`\vartheta_k=2\pi k/M`$ the resulting probability is

```math
p_k=\frac{1}{M}\left|\sum_{q=0}^{L-1}a_q
 e^{i[q(\phi-\vartheta_k)+g_q]}\right|^2.
```

In $`\sum_k p_ke^{i(\vartheta_k-\phi)}`$, the Fourier grid retains exactly terms with $`q-q'=1`$. The test is modulo $`M`$, and $`q-q'-1\in[-L,L-2]`$ rules out any other multiple. Taking the real part gives the cosine-loss risk at the true phase:

```math
\begin{aligned}
R_0&=1-\cos\!\left(\frac{\pi}{L+1}\right),\\
R(\phi,e)-R_0
 &=\sum_{q=0}^{L-2}a_qa_{q+1}
       [1-\cos(g_{q+1}-g_q)].
\end{aligned}
```

In particular, the global phase of the probe drops out. Only differences between adjacent logical charges enter the error penalty. For $`\|e\|_\infty\le\epsilon`$, let $`D_q`$ be the Hamming distance between $`n(q)`$ and $`n(q+1)`$. Since $`|g_{q+1}-g_q|\le\epsilon D_q`$ and $`1-\cos t\le t^2/2`$,

```math
0\le R(\phi,e)-R_0
\le \frac{\epsilon^2}{L+1}\sum_{q=0}^{L-2} D_q^2.
```

## A uniform quadratic bound for the dyadic code

The code has a bank of disjoint binary blocks with gaps $`1,2,\ldots,2^K`$, so its labels span the integers from $`0`$ through $`S=2^{K+1}-1`$. Each bank block flip changes at most $`D_d`$ sensor occupations, where $`D_d`$ depends only on fixed degree $`d`$. Use bulk strings whose charges relative to the first are $`0=b_0<b_1<\cdots<b_m`$, and whose consecutive words differ on at most $`D_d`$ other sites. The equal-weight bulk construction has $`b_h=hW`$, and the quadratic mirror-pair construction also fits this statement by listing its monotone path of bulk words. In either case suppose $`\Delta_h=b_{h+1}-b_h\le S+1`$. The charge $`q`$ uses the last bulk word with $`b_h\le q`$ together with bank label $`r=q-b_h`$. This produces the $`L=b_m+S+1`$ consecutive labels.

Within a range of bank labels, advancing $`r`$ to $`r+1`$ flips exactly $`1+\nu_2(r+1)`$ bits, where $`\nu_2`$ counts factors of two. The sum of squared flip counts in the first $`T`$ such increments obeys

```math
\sum_{s=1}^T (1+\nu_2(s))^2
=\sum_{t\ge0}(2t+1)\left\lfloor\frac{T}{2^t}\right\rfloor
\le 6T.
```

At the boundary between bulk words $`h`$ and $`h+1`$, the bank label resets from $`\Delta_h-1`$ to zero. The bank flips at most $`\lceil\log_2\Delta_h\rceil`$ blocks and the bulk changes at most $`D_d`$ sites. Thus the Hamming distance squared at the boundary is at most $`D_d^2(1+\lceil\log_2\Delta_h\rceil)^2\le 8D_d^2\Delta_h`$ for every integer $`\Delta_h\ge 1`$. Summing the within-range and boundary bounds and using $`\sum_h\Delta_h=b_m`$ gives

```math
\sum_q D_q^2\le 14D_d^2(L-1),\qquad
R(\phi,e)\le R_0+14D_d^2\epsilon^2.
```

The constant is independent of array length. The quadratic error order is also necessary for a uniform bound on this receiver. Take independent signs for $`e_j=\pm\epsilon`$, with $`0\le\epsilon\le\pi/2`$. Each $`D_q\ge1`$, so the expected cosine at that edge is $`(\cos\epsilon)^{D_q}\le\cos\epsilon`$. The exact risk formula gives at least one deterministic error vector with excess at least $`(1-\cos\epsilon)\cos(\pi/(L+1))`$. This is a statement about this nominal decoder and the specified error class.

## Bounded field coefficients and position errors

At fixed physical aperture and exposure duration, use the known dimensionless coordinates $`x_j=j/(N-1)`$. Write the accumulated phase profile as $`P(x)=\sum_{a=0}^{d}\alpha_a x^a`$, with target coefficient $`\alpha_d=\beta`$. The ideal binomial phase is $`\phi=d!\beta/(N-1)^d`$ modulo $`2\pi`$, since $`j^d-d!\binom{j}{d}`$ has degree below $`d`$. Absorb these lower-order terms into the other binomial phases. If the physical model instead specifies a frequency profile in physical coordinates, convert its coefficient to $`\beta`$ by multiplying by the exposure duration and the aperture to power $`d`$, with any known coupling constant included. The raw angle precision and fixed-aperture precision use different units.

Suppose the actual dimensionless coordinates are $`y_j=x_j+\delta_j`$ with $`|\delta_j|\le\eta`$. The receiver still uses $`x_j`$ and sees $`e_j=P(x_j+\delta_j)-P(x_j)`$. If $`|\alpha_a|\le A_a`$ for $`1\le a\le d`$, define

```math
B_1=\sum_{a=1}^d aA_a,\qquad
B_2(\eta)=\sum_{a=2}^d a(a-1)A_a(1+\eta)^{a-2}.
```

Taylor's theorem gives $`e_j=P'(x_j)\delta_j+u_j`$ with $`|u_j|\le B_2(\eta)\eta^2/2`$. Hence one can take $`\epsilon=B_1\eta+B_2(\eta)\eta^2/2`$. The constant offset cancels exactly. For a worst-case uncalibrated geometry and a linear field $`P(x)=g x`$, signed displacements already realize the diagonal error patterns $`e_j=\pm g\eta`$ when shifts around both endpoints are allowed. Extra unmodeled profile terms can also be included by adding their maximum site phase to $`\epsilon`$.

The certified crossover for the receiver is $`\epsilon=O(N^{-d-1})`$ to retain the ideal risk order, or $`\epsilon=o(N^{-d-1})`$ to retain its leading constant. For curvature this means $`\epsilon=O(N^{-3})`$. This is the tolerance certified for the nominal-lattice receiver. The [fixed-aperture receiver](calibration.md) uses a bounded interval for the physical coefficient to attain a larger tolerance for the same physical precision order.

For a known bounded interval of $`\beta`$, project the phase estimate onto its image arc, of length at most $`\pi`$ for sufficiently large $`N`$. Projection onto this arc increases the circular distance to the true phase by at most a factor of two, by the triangle inequality. The projected and true phases lie on the same short arc, so convert their distance to the ordinary coefficient error by multiplying by $`(N-1)^d/d!`$. Since $`1-\cos t\ge 2t^2/\pi^2`$ for $`|t|\le\pi`$, the mean-square coefficient error is bounded by

```math
\min\!\left\{\mathrm{diam}(I)^2,\
  2\pi^2\left[\frac{(N-1)^d}{d!}\right]^2(R_0+14D_d^2\epsilon^2)\right\}
=O_d(N^{-2}+N^{2d}\epsilon^2),
```

where $`I`$ is the coefficient interval. This yields risk of order $`N^{-2}`$ under fixed-aperture normalization at the stated crossover. The bound concerns coefficient error after projection, irrespective of the fact that the unprojected readout measures a circle.

## Unbounded gradient on a perturbed lattice

Consider any fixed set of positions $`y_j`$ with the property that distinct binary occupation words of the same Hamming weight have different sums $`\sum_j y_j n_j`$. This holds for almost every position vector in any open neighborhood of the nominal array. Each excluded equality is a proper hyperplane, and there are finitely many equal-weight pairs.

Let the uniform offset and the gradient be unknown and unbounded, and fix all other nuisance coefficients to zero. To lower bound worst-case risk, average the offset uniformly over one period and the gradient uniformly over $`[-T,T]`$. In the computational basis, averaging the offset removes all off-diagonals between different Hamming weights. Each remaining off-diagonal has a factor $`\sin(Ts)/(Ts)`$, where $`s`$ is the difference of position sums, and $`s\ne0`$. As $`T\to\infty`$, the averaged state therefore converges to complete dephasing in the occupation basis, uniformly in the true signal. Every matrix element of the signal action has modulus one. The conclusion also holds with an arbitrary reference ancilla, since an off-diagonal sensor block is multiplied by the same scalar and the finite sum of trace norms tends to zero. The dephased sensor–ancilla state is independent of the signal.

For the full nominal curvature-phase circle, average the true target uniformly on a fixed fundamental interval. This choice of admissible target values gives limiting average cosine loss one for any receiver, even if the perturbed physical channel has a different periodicity. An independent uniform estimate attains loss one for every target and nuisance. The perturbed model's full-circle minimax risk is therefore exactly one. For a bounded physical coefficient interval $`I`$ with squared error, the same argument on the two endpoints gives minimax risk $`\mathrm{diam}(I)^2/4`$, attained by the midpoint. The conclusion holds even when the perturbed positions are supplied to the receiver. The positions are held fixed as the available nuisance magnitude grows without bound.

## Control and synthesis accounting

The sensing resource is one fixed-duration exposure per site. Before exposure, the dyadic construction can use an address register of $`O_d(\log N)`$ qubits. For the ideal sine preparation, take a uniform register over a power-of-two grid $`L<M\le 2L`$. An ancilla rotation conditional on $`q<L`$ gives a selected amplitude $`\sin[\pi(q+1)/(L+1)]`$. The selection probability is $`(L+1)/(2M)\ge1/4`$. This is a preparation step that finishes before applying the field. The rotation angle is affine in the binary address and can be generated by bit-controlled rotations after checking $`q<L`$.

For the dyadic code, reversible arithmetic splits the address into the bank residual and the equal-weight bulk count. The bank bits select block flips and a threshold comparison for each bulk block selects its word. To erase the address before sensing, compute $`Q_d`$ from the physical word and subtract its known baseline to recover $`q`$ reversibly. A serial implementation with ideal nonlocal gates uses $`O_d(N\mathrm{polylog}N)`$ elementary gates for the encoder and its inverse, using $`O_d(\log N)`$ scratch qubits with workspace reuse. The final address-register Fourier transform uses $`O_d(\log^2 N)`$ ideal one- and two-qubit gates. Routing, spatial communication, and fault tolerance incur separate costs. Codes extracted by exhaustive search also admit the finite Fourier readout. Their encoding cost depends on how the resulting list of codewords is compiled.

For compiled controls, let $`\delta_{\mathrm{ctrl}}`$ be a uniform total variation bound on the final outcome distribution compared with ideal control at the same actual phase profile. The circular loss lies in $`[0,2]`$, so compilation increases risk by at most $`2\delta_{\mathrm{ctrl}}`$. To keep the leading ideal constant it is sufficient that $`\delta_{\mathrm{ctrl}}=o(N^{-2d-2})`$. A conservative way to certify this is a sum of normalized diamond-distance bounds for the operations, including the prepared state's trace-distance discrepancy after conditioning on successful preparation. Phase accumulation during control, entanglement generation across distant sensors, and noncommuting exposure noise require separate error models.
