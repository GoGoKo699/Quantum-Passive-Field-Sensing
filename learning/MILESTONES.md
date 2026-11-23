# Understanding map

The first 12 milestones establish the physical model and the tools for interpreting a global risk guarantee. The remaining 18 follow the proof, the explicit receiver, its optimal scaling and the limits imposed by sensor errors.

## Background and preliminaries

### M01 What phase does one qubit acquire?

Explain how the phase of an occupied level relative to an unoccupied level becomes observable when they are recombined.

Entry point. Ramsey interference gives an operational meaning to a local phase.

[Model](../science/model.md) · [Review bridge](ANCHOR.md)

### M02 How does one exposure combine phases across sites?

Compute the phase of a computational string as the sum of the local phases at occupied sites.

M01. Independent commuting evolutions produce a sum of one-body generators.

[Model](../science/model.md)

### M03 What resources define the sensing experiment?

Identify each sensor, the common exposure and the allowed pre-exposure preparation and post-exposure measurement.

M02. The timing boundary fixes which controls can affect the generator.

[Model](../science/model.md)

### M04 How does a spatial polynomial become a collection of generators?

Write the site phases in the binomial basis and identify the associated occupation-weighted moments.

M02. Known position weights turn each polynomial coefficient into a separate commuting generator.

[Model](../science/model.md)

### M05 Which phase can the array identify?

Relate the integer binomial basis to the identifiable phase circle and convert the leading monomial coefficient into the binomial coordinate.

M04. The coordinate determines both the period and the conversion back to physical units.

[Model](../science/model.md)

### M06 When can a nuisance field contribute only a common phase?

Show why strings sharing the same lower moments retain their relative phase for every value of those coefficients.

M02, M04. A common joint eigenspace supplies exact nuisance cancellation.

[Model](../science/model.md)

### M07 Why is the loss periodic?

Interpret one minus the cosine of the phase error and recover its local quadratic behavior and its value for an independent uniform guess.

M05. A circular loss makes the risk depend only on the physical difference between angles.

[Minimax proof](../science/minimax.md)

### M08 What can Fisher information establish?

Explain the connection between pure-state generator variance and local phase distinguishability, including the role of spectral width.

M02, M07. The local benchmark exposes why large generator spread is worth investigating.

[Minimax proof](../science/minimax.md) · [Review bridge](ANCHOR.md)

### M09 What changes when the phase is unknown on a full circle?

Explain how repeated likelihood peaks can leave two phases indistinguishable and why small local error can coexist with poor worst-case error.

M05, M07, M08. Global estimation requires examining the actual phases represented by the probe.

[Minimax proof](../science/minimax.md) · [Review bridge](ANCHOR.md)

### M10 How does symmetry simplify a worst-case calculation?

Use joint phase averaging to select nuisance sectors and explain how shift covariance makes phase risk independent of the true angle.

M06, M07. Group symmetry connects a uniform-average converse with a constant-risk strategy.

[Minimax proof](../science/minimax.md)

### M11 Why do consecutive levels matter for the cosine loss?

Expand the outcome error’s first Fourier component and identify the coherence between eigenvalues separated by one.

M07, M10. The loss translates a physical estimation problem into adjacency of integer charges.

[Minimax proof](../science/minimax.md)

### M12 How can entanglement depth constrain global estimation?

Relate the generator ranges of independent blocks to their total quantum Fisher information and explain how a two-alternative testing bound controls risk.

M03, M08, M09. A local speed bound can yield a global risk lower bound without an unbiasedness assumption.

[Minimax proof](../science/minimax.md) · [Review bridge](ANCHOR.md)

## Narrative and innovation

### M13 How do lower-moment sectors bound every strategy?

Explain why averaging nuisance phases removes inter-sector coherences and why a mixture of sectors cannot beat the best sector’s average risk.

M06, M10. This reduces the search for the worst-case optimum to ordinary spectra inside fixed sectors.

[Minimax proof](../science/minimax.md)

### M14 How does the longest consecutive run determine the exact optimum?

Use the path adjacency matrix on each consecutive component to identify the optimum cosine score and its sine-profile eigenvector.

M11, M13. The best sector must contain the longest useful run of signal charges.

[Minimax proof](../science/minimax.md)

### M15 How can finitely many outcomes attain the exact risk?

Trace the padded inverse Fourier readout and show why a grid larger than the chosen run preserves its first-harmonic score for every input angle.

M10, M14. The finite circuit realizes the continuous-parameter optimum.

[Minimax proof](../science/minimax.md)

### M16 Which eight-qubit strings can measure curvature?

Check the shared weight and first moment of the three example strings and compute their distinct consecutive quadratic charges.

M04, M06, M14. The example turns the abstract conditions into three explicit configurations.

[Eight-qubit example](../science/example.md)

### M17 How do two address qubits implement the eight-qubit receiver?

Follow the sine-state preparation, reversible basis mapping, one exposure, inverse mapping and Fourier readout. Identify the only parameter-dependent step.

M03, M15, M16. This separates sensing from decoding in a circuit that can be simulated directly.

[Eight-qubit example](../science/example.md)

### M18 Why can a wide cubic spectrum have chance-level loss?

Read the finite enumeration for cubic sensing and explain how a sector can contain widely separated charges without any usable adjacent pair.

M08, M09, M14. The finite counterexample motivates a construction that guarantees adjacency.

[Finite enumeration](../verification/README.md) · [Minimax proof](../science/minimax.md)

### M19 How does a finite-difference stencil eliminate lower moments?

Derive moment cancellation from a zero of order equal to the polynomial degree and obtain the product-of-shifts target gap.

M04, M06, M18. One stencil is a binary, exactly protected encoding with a tunable signal gap.

[Arithmetic construction](../science/arithmetic.md)

### M20 How can stencils produce a bank of consecutive charges?

Explain the need for a unit-gap seed, how coprime gaps supply one, and how disjoint binary stencils implement the powers of two.

M19. A sum of selectable gaps supplies all possible remainders up to the bank’s range.

[Arithmetic construction](../science/arithmetic.md)

### M21 How does the array reach the optimal power of its length?

Combine the consecutive remainder from the bank with independently selectable large equal gaps and compare the contiguous run with the generator’s total range.

M14, M20. Quotient and remainder turn a single protected gap into a long native spectrum.

[Arithmetic construction](../science/arithmetic.md)

### M22 What fixes the sharp coefficient of the longest run?

Use a degree-matched Chebyshev residual and subtract any lower polynomial within a common sector to recover the upper coefficient.

M06, M14, M21. The continuum bound gives a target for the discrete receiver construction.

[Arithmetic construction](../science/arithmetic.md)

### M23 How are approximate moment constraints made exact?

Explain how the ordered changes between configurations keep lower-moment deviations bounded and how correction stencils remove each deviation without disturbing earlier moments.

M19, M21, M22. The ordering and corrections transfer the continuum extremum to one exact moment sector.

[Arithmetic construction](../science/arithmetic.md)

### M24 How are the remaining gaps filled near the sharp bound?

Compare the largest charge change along the corrected path with the range of the separate fine bank and show that its intervals overlap.

M20, M23. Overlap lets the nearly extremal configurations support one consecutive run.

[Arithmetic construction](../science/arithmetic.md)

### M25 Why does curvature admit a direct sharp construction?

Use mirror pairs to fix the first moment, then follow adjacent radial exchanges from the innermost to the outermost occupied pairs and apply a fine bank.

M16, M20, M22. The symmetric construction gives a second way to see the curvature coefficient.

[Arithmetic construction](../science/arithmetic.md)

### M26 How does the same exposure constrain separable probes?

Explain the block variance bound and the two-point comparison that give the separable-input risk lower bound, even when the nuisance values are supplied.

M12, M14, M21. Charging the same number of sensors and exposure time makes the entangled-input comparison meaningful.

[Minimax proof](../science/minimax.md)

### M27 What scales at a fixed physical aperture?

Translate the raw lattice angle and circular risk into the error for a bounded physical coefficient. Identify where the normalized generator and the physical bandwidth enter.

M03, M05, M21, M26. The comparison gives Heisenberg-order physical mean-square error for the entangled receiver.

[Model](../science/model.md)

### M28 Which calibration errors reduce the Fourier score?

Derive the role of phase differences between neighboring codewords and distinguish a common phase from a site-dependent residual.

M15, M19, M24. The same adjacency that governs ideal risk identifies which errors matter.

[Robustness](../science/robustness.md)

### M29 Why does the nuisance range matter under geometry error?

Relate bounded smooth-field derivatives to a site-phase error budget and explain how a generic perturbation with unbounded slope can destroy the shared moment sectors.

M06, M13, M27, M28. Exact lattice cancellation and robustness under calibrated placement errors have different assumptions.

[Robustness](../science/robustness.md)

### M30 What does one passive exposure establish?

Connect exact lower-moment cancellation, the sharp consecutive spectrum, finite readout, separable comparison and geometric accuracy. State which assumptions each conclusion uses.

M15, M17, M24–M29. This assembles the precision guarantee and its implementation limits into one argument.

[Model](../science/model.md) · [Minimax proof](../science/minimax.md) · [Arithmetic construction](../science/arithmetic.md) · [Robustness](../science/robustness.md) · [Eight-qubit example](../science/example.md)
