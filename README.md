# Quantum Passive Field Sensing

**How precisely can a fixed array estimate field curvature in one exposure when its site phases are imperfectly calibrated?** Spatial finite differences cancel the unknown offset and gradient on the nominal array. A Fourier receiver estimates the curvature over a known physical interval and attains the optimal error scaling allowed by sensor count, entanglement depth and residual calibration.

| Setting | Guarantee |
|---|---|
| Fixed physical aperture | Worst-case coefficient mean-square error is $`\Theta_{d,I}((Nk)^{-1}+\epsilon^2)`$ for $`N`$ sensors, preparation depth at most $`k`$, and unknown deterministic site phase shifts with magnitude at most a sufficiently small $`\epsilon`$. |
| Curvature calibration floor | The optimal mean-square error for the quadratic coefficient is asymptotic to $`64\epsilon^2`$ when $`\epsilon\to0`$ and $`\epsilon^2Nk\to\infty`$. |
| Unknown positions | For degree $`d\ge2`$, bounded polynomial coefficients and an adjustable gradient, small maximum position error $`\eta`$ gives the matching order $`\Theta((Nk)^{-1}+\eta^2)`$, even with fixed aperture endpoints. |
| Ideal full phase circle | The exact cosine loss is $`1-\cos(\pi/(L+1))`$, where $`L`$ is the longest run of consecutive signal charges in a common lower-moment sector. For fixed $`d\ge1`$, $`L\sim N^{d+1}/(4^d d!)`$. |

The robust receiver uses groups of translated stencils. Neighboring Fourier levels differ on one stencil, so a small systematic phase bias remains small even when the probe coherently spans many sites. In the proof’s 1,024-sensor curvature example, depth 128 with site shifts up to 0.01 radians attains worst-case mean-square error below 0.04911. Ideal-phase separable probes with the same sensor count, arbitrary joint readout and unknown lower moments have error above 0.06364.

## Science

Read the [fixed-aperture calibration proof](science/calibration.md) for the robust receiver, the position-error converse, and the curvature benchmark. The [ideal model](science/model.md), [minimax proof](science/minimax.md) and [array construction](science/arithmetic.md) give the full-circle result. The [eight-qubit example](science/example.md) realizes three consecutive charges and a four-outcome readout with exact loss $`1-1/\sqrt2`$. The [phase and control analysis](science/robustness.md) gives the performance of the nominal-lattice decoder and discusses implementation costs. See the [primary-source comparison](references/RELATED_WORK.md) for the inherited phase and spatial sensing methods.

## Learning and verification

The [learning route](learning/README.md) pairs Tóth and Apellaniz’s metrology review with a project bridge and 30 milestones. The [verification guide](verification/README.md) explains the finite checks.

```sh
python3 verification/run_checks.py
python3 verification/check_calibration.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
