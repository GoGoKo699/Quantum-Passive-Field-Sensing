# Quantum Passive Field Sensing

**Can a fixed array estimate field curvature in one exposure while rejecting an unknown offset and linear gradient?** An entangled probe of equally spaced qubits cancels lower spatial coefficients exactly, while a finite Fourier measurement estimates the highest coefficient over its full identifiable phase circle.

| Result | Guarantee |
|---|---|
| Global single-shot risk | $`R^*=1-\cos(\pi/(L+1))`$, where $`L`$ is the longest run of consecutive signal charges in a common lower-moment sector. |
| Fixed-degree asymptotic | $`L\sim N^{d+1}/(4^d d!)`$ for fixed degree $`d\ge 1`$. For curvature, $`R^*\sim 512\pi^2/N^6`$ in the lattice angle. |
| Physical error at fixed aperture | $`\Theta_d(N^{-2})`$ worst-case mean-square error on a fixed bounded interval of the physical coefficient. Separable inputs have risk $`\Omega_d(N^{-1})`$ even with joint readout. |
| Eight-qubit curvature receiver | Three consecutive charges and a four-outcome readout give exact worst-case loss $`1-1/\sqrt 2`$. |

The site array and exposure are fixed. Preparation and readout can use parameter-independent entangling gates. The protocol needs no nuisance calibration or control during exposure. The scaling in lattice angle includes the growth of the unnormalized site couplings. The fixed-aperture result accounts for that growth.

## Science

Start with the [model and exact results](science/model.md). The [minimax proof](science/minimax.md) explains why a wide spectrum can still fail to yield a global estimate. The [array construction](science/arithmetic.md) supplies the consecutive charges and sharp leading constant. The [eight-qubit receiver](science/example.md) gives an explicit circuit. The [imperfection analysis](science/robustness.md) treats extra diagonal phases, position errors and control costs. See the [prior-work comparison](references/RELATED_WORK.md) for the linear-gradient antecedent and related weighted spatial sensing.

## Learning and verification

The [learning route](learning/README.md) pairs Tóth and Apellaniz’s metrology review with a project bridge and 30 milestones. The [verification guide](verification/README.md) explains the finite checks.

```bash
python3 verification/run_checks.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
