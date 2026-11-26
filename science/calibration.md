# Minimax precision with systematic site errors

[Science map](README.md) · [Ideal phase receiver](minimax.md) · [Full-circle phase errors](robustness.md)

A fixed-aperture array can retain its ideal precision despite small, unknown coherent shifts at individual sensors. The receiver uses a ladder with a fixed physical phase step chosen for the known coefficient interval. Consecutive ladder words differ at only a few sites.

## Model and precision law

One exposure rotates occupation one at nominal position $`x_j=j/(N-1)`$ by

```math
P(x_j)+e_j,\qquad
P(x)=\beta x^d+\sum_{a\lt d}\alpha_a x^a,\qquad |e_j|\le\epsilon.
```

The degree $`d\ge1`$ and nondegenerate closed bounded interval $`I`$ for $`\beta`$ are fixed. The lower coefficients are arbitrary. The phase errors are fixed during the exposure, unknown and allowed to vary arbitrarily across sites. Preparation is $`k`$-producible on the exposed sensors as in the [depth converse](minimax.md#entanglement-depth). Joint readout is allowed. All $`N`$ sites count, with one binary occupation and one simultaneous exposure per site.

For sufficiently large $`N`$ and sufficiently small $`\epsilon\ge0`$ the minimax mean-square error in $`\beta`$ is

```math
R^*_{N,k}(\epsilon)
  =\Theta_{d,I}\!\left(\frac{1}{Nk}+\epsilon^2\right),
  \qquad 1\le k\le N .
```

The constants are uniform in $`k`$ and $`\epsilon`$. Full-depth preparation retains $`N^{-2}`$ risk order when the systematic phase tolerance is of order $`1/N`$ or smaller.

## Equal-gap stencils and a finite receiver

Choose $`T=\lfloor\rho N\rfloor`$ with $`\rho>0`$ a sufficiently small constant, and set $`D=2^d`$. For $`0\le s\lt T`$ use the stencil at sites $`s+tT`$ with $`0\le t\lt D`$. Stencils are disjoint. The two occupation words use opposite subset parities, oriented as the $`d`$-fold forward difference. By the [finite-difference identity](arithmetic.md#blocks-with-prescribed-signal-gaps), their lower moments agree and the relative phase of one stencil is

```math
h\beta+\xi_s,\qquad
h=d!\,2^{d(d-1)/2}\left(\frac{T}{N-1}\right)^d,\qquad
|\xi_s|\le D\epsilon.
```

Choose $`\rho`$ so the stencils fit and $`hI`$ has length at most $`\pi`$. The step $`h`$ stays bounded away from zero as $`N`$ grows.

For $`k\ge D`$ put $`b=\min\{\lfloor k/D\rfloor,T\}`$ and use $`m=\lfloor T/b\rfloor`$ disjoint groups of $`b`$ stencils. A word $`|q\rangle_{\rm enc}`$ uses the one configuration in its first $`q`$ stencils and the zero configuration in the rest. Prepare the group in

```math
|\psi_b\rangle=\sum_{q=0}^b a_q|q\rangle_{\rm enc},\qquad
a_q=\sqrt{\frac{2}{b+2}}\sin\!\left(\frac{\pi(q+1)}{b+2}\right).
```

The exposure phase of that word relative to the zero word is $`qh\beta+\sum_{s=1}^q\xi_s`$ in the group's own indexing. Decode the charge address $`q`$ and use the [finite Fourier readout](minimax.md#finite-attaining-receiver) with $`M>b+1`$ points. If the reported angle is $`\alpha`$, Fourier orthogonality gives

```math
\begin{aligned}
Z&=e^{i\alpha}/c_b,\qquad c_b=\cos[\pi/(b+2)],\\
\mathbb E Z&=e^{ih\beta}\sum_{q=0}^{b-1}w_q e^{i\xi_{q+1}},
\qquad w_q=a_q a_{q+1}/c_b,\quad \sum_q w_q=1 .
\end{aligned}
```

The first harmonic only uses adjacent words. Its error phase $`\xi_{q+1}`$ depends on one stencil even when the cumulative phase of a word is large. The weights are positive, so the bias relative to $`e^{ih\beta}`$ has modulus at most $`D\epsilon`$. Expanding the squared modulus and using $`2(1-\cos u)\le u^2`$ gives a second moment about the ideal of at most $`\tan^2[\pi/(b+2)]+D^2\epsilon^2`$.

The group outcomes are independent at each fixed field and error vector. Their means may vary. Their normalized phasor average $`W`$ obeys

```math
\mathbb E|W-e^{ih\beta}|^2
\le \frac{\tan^2[\pi/(b+2)]+D^2\epsilon^2}{m}+D^2\epsilon^2 .
```

Project to the nearest point of the known arc and divide its lifted angle by $`h`$. The projected chord error is at most twice the raw error. Angular distance within the arc is at most $`\pi/2`$ times chord distance. Together with $`mb^2=\Theta_d(Nk)`$, this proves the upper bound.

For $`k\lt D`$, start every stencil in $`|+\rangle^{\otimes D}`$. After exposure project to the span of its two words. The probability $`p=2^{1-D}`$ is independent of the field and errors, and the conditional state is the exposed $`b=1`$ probe. Score a failed projection as zero and a Fourier success as $`e^{i\alpha}/(p c_1)`$. Each such score has the same expected phasor as the $`b=1`$ receiver and variance bounded in terms of $`d`$. Averaging over all $`T`$ stencils gives $`O_{d,I}(1/N+\epsilon^2)`$ throughout this bounded range of $`k`$. The strategy always charges every exposure and incorporates all failures.

## Matching lower bounds

At $`e=0`$, test two interior coefficients a small multiple of $`1/\sqrt{Nk}`$ apart, using the same lower coefficients. The sum of squared block generator diameters is bounded by $`k\sum_j x_j^{2d}\le Nk`$. Pure-state path length bounds the resulting trace distance away from one. The bound extends by convexity to mixtures with differing partitions. Nearest-target testing gives $`\Omega(1/(Nk))`$.

For the systematic contribution, choose $`\beta_\pm=\beta_0\pm\delta/2`$ in $`I`$ and take $`e_j^\pm=\mp(\delta/2)x_j^d`$, using the same lower coefficients. When $`\delta\le2\epsilon`$ both channels are admissible and identical. On their common outcome distribution, the mean of the two squared losses is at least $`\delta^2/4`$. Taking $`\delta`$ proportional to $`\epsilon`$ proves the floor. The maximum of the two lower bounds controls their sum up to a factor of two.

## Unknown coordinates with fixed aperture endpoints

Let the actual coordinates $`y_j\in[0,1]`$ be unsupplied with $`|y_j-x_j|\le\eta`$ and site phases $`P(y_j)`$. Assume fixed bounds on the nonconstant lower coefficients, with the gradient range containing a neighborhood of zero. The derivative bound on $`[0,1]`$ gives $`|P(y_j)-P(x_j)|\le C\eta`$, so the phase-error receiver gives $`O(1/(Nk)+\eta^2)`$.

For $`d\ge2`$, choose an interior $`\beta_0`$ and an interior nonzero gradient $`g`$ of the same sign (either sign at zero). Set $`P_0(x)=gx+\beta_0 x^d`$ and

```math
P_\pm(x)=P_0(x)\pm\frac{\delta}{2}(x^d-x),\qquad
y_j^\pm=P_\pm^{-1}(P_0(x_j)).
```

For sufficiently small $`\delta`$, the gradients are admissible and $`|P_\pm'|\ge |g|/2`$. The three polynomials have equal endpoint values. The arrays preserve order, fix both endpoints and have maximum displacement at most $`\delta/|g|`$. With $`\delta`$ proportional to $`\eta`$, the two channels are identical and the target coefficients differ by $`\delta`$. Combining this with the ideal statistical lower bound gives $`\Theta(1/(Nk)+\eta^2)`$. The [unbounded-gradient result](robustness.md#unbounded-gradient-on-a-perturbed-lattice) uses a different nuisance range.

## The exact systematic floor for curvature

For $`d=2`$ and a fixed $`I`$, along any sequence with $`\epsilon\to0`$ and $`A=\epsilon\sqrt{Nk}\to\infty`$ in the additive site-phase model,

```math
R^*_{N,k}(\epsilon)/\epsilon^2\longrightarrow64 .
```

For the lower bound, the monic quadratic $`p(x)=x^2-x+1/8`$ has modulus at most $`1/8`$ on $`[0,1]`$. Take two fields separated by $`16\epsilon p(x)`$ with coefficients centered inside $`I`$. Opposite site errors $`\mp8\epsilon p(x_j)`$ are admissible and make the channels identical. The separation in $`\beta`$ is $`16\epsilon`$.

For the upper bound, pack $`T_f=\lfloor N/A^{1/4}\rfloor`$ fine stencils with shifts $`u=\lfloor(N-2T_f)/2\rfloor`$ and $`v=u+T_f`$. The stencil at $`s`$ uses $`s,s+u,s+v,s+u+v`$ for $`0\le s\lt T_f`$. They are disjoint, occupying four ranges near 0, 1/2 and 1. Their common phase step is $`\gamma=2uv/(N-1)^2\to1/2`$. For $`k\ge4`$ use $`b_f=\min\{\lfloor k/4\rfloor,\lfloor T_f/A^{1/4}\rfloor\}`$ and $`m_f=\lfloor T_f/b_f\rfloor`$. Since $`A=o(N)`$ and $`k\le N`$,

```math
m_f\to\infty,\qquad
\epsilon^2 m_f b_f^2\ge c\min\{A^{7/4},A^{5/4}\}\to\infty
```

for some fixed $`c>0`$. Here $`m_f b_f^2\ge T_f b_f/2`$. At $`k\lt 4`$ use the product version on all $`T_f`$ single stencils and $`\epsilon^2 T_f\to\infty`$.

The expected fine phasor is $`e^{i\gamma\beta}`$ times a positive average of phase factors with shifts in $`[-4\epsilon,4\epsilon]`$. Its angular bias is at most $`4\epsilon`$ and its modulus is at least $`\cos(4\epsilon)`$ for small $`\epsilon`$. The sample mean variance is $`o(\epsilon^2)`$ by the size conditions.

To select a phase lift on any fixed $`I`$, use three disjoint macroscopic subarrays outside the fine ranges. The same bounded-interval receiver, with each subarray affinely rescaled, gives three independent estimates with MSE $`O(\epsilon^2)`$. Their median fails any fixed coarse tolerance with probability $`O(\epsilon^4)`$. Select the fine phase lift closest to the median and clip to $`I`$. When the median and sample phasor are within sufficiently small fixed neighborhoods of their intended values, the phase lift is unique and its noise about the expected phasor has root-mean-square size $`o(\epsilon)`$ by local Lipschitz continuity. The exceptional event has probability $`o(\epsilon^2)`$ and squared loss bounded by the diameter of $`I`$ squared. The bias contributes at most $`4\epsilon/\gamma`$ to coefficient error, giving the upper coefficient 64.

## Finite curvature comparison and endpoint controls

Take $`N=1024`$ and $`I=[-1,1]`$. Use 256 four-site stencils with spacing $`h=4(256)^2/(1023)^2`$ and eight groups of 32, at depth $`k=128`$. For $`\epsilon=0.01`$ the [finite check](../verification/README.md) certifies worst-case mean-square error below 0.049104. Clip the imaginary part of $`W`$ to the range of $`\sin(h\beta)`$ and use its inverse. The Lipschitz factor is $`1/(h\cos h)`$.

For an ideal-phase separable comparator, use the same aperture, exposure, coefficient interval and unknown lower moments, with arbitrary joint readout. Vary the lower coefficients along a subfamily where the phase at site $`j`$ is $`\beta r_j`$ and

```math
r_j=(x_j-1/2)^2-\frac1N\sum_{\ell=0}^{N-1}(x_\ell-1/2)^2.
```

The separable QFI bound is $`\sum_j r_j^2`$. The cosine-squared prior on $`[-1,1]`$ contributes Fisher information $`\pi^2`$ and vanishes at the endpoints. The van Trees inequality bounds worst-case error below by $`1/(\pi^2+\sum_j r_j^2)`$. The same finite check certifies this lower bound above 0.063649.

The unary sine amplitudes can be prepared by controlled rotations using successive ratios of remaining probability mass. Within each stencil, fixed bit flips and controlled-NOTs map one logical bit to the two occupation words. Invert these to recover the logical bits, then use a reversible count and threshold comparisons to convert the unary word to a clean binary address. The group uses $`O_d(b\,\mathrm{polylog}(b+1))`$ ideal one- and two-qubit gates including Fourier readout. The finite example uses a six-qubit Fourier address per group. Gate synthesis, routing across the aperture and imperfections in preparation and readout carry separate costs.
