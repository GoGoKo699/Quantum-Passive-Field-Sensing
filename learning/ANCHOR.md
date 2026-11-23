# Educational anchor

**Géza Tóth and Iagoba Apellaniz, _Quantum metrology from a quantum information science perspective_, Journal of Physics A 47, 424006 (2014).** Use [arXiv:1405.4878v4](https://arxiv.org/abs/1405.4878v4), dated 21 October 2014. [Read the review](https://arxiv.org/html/1405.4878v4).

| Review sections | Bridge to this project |
|---|---|
| §§2.1–2.3, Ramsey, GHZ and Dicke probes | Ramsey interference illustrates phase-to-probability conversion. Replace the review’s collective spin generator with a sum of site occupancies weighted by the known field profile. A GHZ-type pair illustrates spectral width. A fixed-weight family illustrates the first nuisance constraint. [Model](../science/model.md) |
| §§4.1–4.4, Fisher information and multiparameter estimation | The review analyzes distinguishability near an operating point. This project asks for a single estimate on the whole identifiable phase circle, with lower field coefficients unknown. Its loss is periodic and its receiver has a continuous input parameter and finitely many outputs. [Minimax proof](../science/minimax.md) |
| §§3.1 and 5.1–5.4, entanglement, Fisher information and evolution speed | Replace the common spin weight by the actual site-dependent generator range. Add the information over independent blocks, then use the distinguishability of two nearby alternatives to obtain a worst-case risk bound. [Minimax proof](../science/minimax.md) |
| §6, metrology in noise | Separate exactly canceled lower-order fields from residual site-dependent phase errors, which change the relative phases inside the sensing subspace. [Robustness](../science/robustness.md) |

With the convention $`Z|0\rangle=|0\rangle`$, the occupancy is $`n_j=(I-Z_j)/2`$. This convention makes the generator eigenvalues visible as sums over occupied sites. The review’s spin normalization and its unitary sign convention can differ by an overall scale or sign. Keep the array’s written convention when converting a Fourier outcome into a phase estimate.

Work through the [eight-qubit receiver](../science/example.md) after the Ramsey sections. Its three basis configurations have the same two lower moments and three adjacent target moments. The shared lower moments bridge familiar interference and the project’s main problem of creating a long sequence of adjacent phases within one nuisance sector.

The project develops the phase-covariant minimax argument, the exact finite Fourier readout, and the arithmetic construction in its own [science account](../science/README.md). The review supplies the metrology background and the entangled-input comparison.
