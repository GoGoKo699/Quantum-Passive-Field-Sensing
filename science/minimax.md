# Exact minimax probe and receiver

[Model](model.md) · [Spectrum construction](arithmetic.md) · [Eight-qubit receiver](example.md)

## Converse

Use independent uniform priors on all nuisance and signal angles. Averaging the nuisance dephases the probe into sectors of $`(Q_0,\ldots,Q_{d-1})`$ even with an unexposed ancilla. Worst-case risk dominates Bayes risk. Revealing the sector can only improve the score, so bound each sector separately.

In a pure sector probe write the component at signal charge $`q`$ as $`a_q|v_q\rangle`$, with $`a_q\ge0`$ and orthogonal normalized vectors that can include the ancilla. Mixtures cannot outperform the bound for pure states. Group-averaging a receiver preserves the uniform-prior score and gives a covariant POVM. On the charge span its seed $`T`$ is positive and has diagonal one. Thus $`|T_{q,q+1}|\le1`$. Integration against the first phase harmonic retains adjacent terms only. Its score is bounded by

```math
\sum_q a_q a_{q+1},\qquad \sum_q a_q^2=1.
```

Set the amplitudes at missing charges to zero. The form splits into one half of the adjacency matrix on each consecutive path. On a path of length $`L`$ its top eigenvalue is $`\cos(\pi/(L+1))`$ with the positive sine eigenvector. Maximizing over sectors proves the bound for any input and measurement.

## Finite attaining receiver

Choose one string $`|x_r\rangle`$ for each charge in a longest run, with $`r=0,\ldots,L-1`$ counting from the first charge. Prepare

```math
|\psi\rangle=\sum_{r=0}^{L-1} a_r|x_r\rangle,\qquad
a_r=\sqrt{\frac2{L+1}}\sin\left(\frac{(r+1)\pi}{L+1}\right).
```

The nuisance and first charge give a common phase. Reversibly decode to the address register with dimension $`M>L`$. Take the inverse Fourier transform and report $` \alpha_m=2\pi m/M `$ for outcome $`m`$. Its probability is

```math
p_m=\frac1M\left|\sum_{r=0}^{L-1}a_r e^{ir(\phi-\alpha_m)}\right|^2.
```

In the first moment of $`e^{i(\alpha_m-\phi)}`$, the discrete Fourier sum keeps $`r-s=1\bmod M`$. Since $`|r-s|<L<M`$ and $`M>L`$, the surviving terms have $`r-s=1`$. The score is exactly the adjacent sum for all target and nuisance values, attaining the converse. A power of two for $`M`$ permits a qubit Fourier transform.

## Entanglement depth

A $`k`$-producible probe is a mixture of product states across blocks of at most $`k`$ sensors, possibly with local unexposed ancillas. Supply the nuisance values for the lower bound. For each pure block product, the quantum Fisher information is at most the sum of squared block generator diameters. With $`g_j=\binom jd`$, Cauchy–Schwarz bounds it by

```math
\sum_B\left(\sum_{j\in B}g_j\right)^2
\le k\sum_jg_j^2=O_d(kN^{2d+1}).
```

For any two signals at distance $`\delta`$ the pure-state path length bounds their output trace distance by half of $`\delta`$ times the square root of this information bound. Convexity applies to mixtures. With $`\delta=c_d/(\sqrt kN^{d+1/2})`$ and small fixed $`c_d`$, distinguishing the two signals from any measurement has error at least one quarter under equal priors. The nearest-point test built from an estimator errs only if that estimate is at least $`\delta/2`$ from the true point. Its worst-case circular risk is therefore $`\Omega_d((kN^{2d+1})^{-1})`$.

In fixed-aperture units, the same reasoning uses weights $`x_j^d`$ and squared loss, giving $`\Omega_d((kN)^{-1})`$. The unrestricted lower bound uses $`k=N`$, and the separable lower bound uses $`k=1`$. Joint readout is permitted in both cases.
