# One-exposure model and results

[Science map](README.md) · [Minimax proof](minimax.md) · [Spectrum construction](arithmetic.md)

## Exposure and loss

Place one qubit per site $`j=0,\ldots,N-1`$. Its occupation is $`n_j=|1\rangle\langle1|_j`$ and the binomial moment is $`Q_a=\sum_j\binom ja n_j`$. One passive exposure applies the unitary

```math
U_{\lambda,\phi}=\exp\!\left[i\left(\sum_{a=0}^{d-1}\lambda_a Q_a+\phi Q_d\right)\right].
```

The target $` \phi `$ and each nuisance $` \lambda_a `$ can be any angles. A strategy prepares a parameter-independent state on the array and an optional unexposed ancilla, applies the evolution once, and measures. Joint preparation and readout are available. All sites have the same exposure duration, with no intermediate control or supplied calibration. Unused sites may stay in occupation zero.

At sites $`0,\ldots,d`$ the binomial evaluation matrix is triangular with unit diagonal. For $`N\ge d+1`$, equality of all site phases modulo $`2\pi`$ is equivalent to equality of all binomial coefficients modulo $`2\pi`$. A monomial phase $`\theta j^d`$ has $`\phi=d!\theta`$ after absorbing lower-degree terms. Its identifiable period is $`2\pi/d!`$.

Risk is the supremum of the expected loss $`1-\cos(\widehat\phi-\phi)`$ over all nuisance and signal angles. An independent uniform guess has risk one.

## Exact results

Let $`L_N^{(d)}`$ be the maximum run length of consecutive occupied eigenvalues of $`Q_d`$ over the common eigenspaces of $`Q_0,\ldots,Q_{d-1}`$. An occupied charge requires one computational string in that sector.

```math
R^*=1-\cos\left(\frac{\pi}{L_N^{(d)}+1}\right),
\qquad L_N^{(d)}\sim\frac{N^{d+1}}{4^d d!}\quad(d\ge 1\text{ fixed}).
```

The [receiver](minimax.md) uses one string per charge. The [construction](arithmetic.md) proves the leading constant and supplies strings. A simpler dyadic construction attains the same scaling with structured encoding. For curvature, the minimax constant is $`512\pi^2`$ for risk scaled by $`N^6`$. For $`N=16,d=3`$, the maximum sector diameter is 140 and the longest run is one, giving global minimax loss one.

## Fixed-aperture interpretation

With physical coordinates $`x_j=j/(N-1)`$ and a target term $`\beta x_j^d`$, the lattice angle is $`\phi=d!\beta/(N-1)^d`$. Fix a bounded interval for $`\beta`$ of positive length. For large $`N`$, its phase arc is shorter than $`\pi`$. Project the estimate to the arc and rescale. The circular triangle inequality gives at most twice the distance error on the arc, where circular and ordinary angular distance agree. Squared circular distance is bounded by a constant times cosine loss. This gives physical mean-square risk $`O_d(N^{-2})`$. The total physical generator diameter $`O_d(N)`$ gives a matching two-point lower bound. The [same test for separable inputs](minimax.md) gives $`\Omega_d(N^{-1})`$ even with joint readout and known nuisance.

The comparison charges $`N`$ parallel sensor uses of a fixed duration. Joint preparation and readout are separate control resources. The [imperfection analysis](robustness.md) treats phase deviations and gate costs.

A [separate fixed-aperture result](calibration.md) gives a matching depth-dependent risk under bounded systematic site shifts. It uses a fixed interval for the physical coefficient and scores ordinary squared error.
