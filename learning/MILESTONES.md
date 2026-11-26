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

### M26 How does preparation depth constrain physical precision?

Use the block variance bound to construct a two-point lower bound on mean-square error at fixed aperture. State what the bound gives for separable preparation and for one array-wide block.

M12, M14, M21. The comparison charges the same sensors and one exposure for both probes.

[Minimax proof](../science/minimax.md)

### M27 Why does a bounded coefficient interval allow wider phase steps?

Compare the size of one integer step on the full phase circle with the fixed physical phase step of a translated stencil. Show how a known interval allows that wider step to encode the coefficient without aliases.

M05, M19, M26. The physical coefficient interval sets the useful phase step for the new receiver.

[Model](../science/model.md) · [Fixed-aperture calibration](../science/calibration.md)

### M28 Which site errors affect the Fourier score?

Compute the Fourier first moment when neighboring codewords differ by one stencil. Bound the bias of the normalized Fourier outcome and explain how averaging groups reduces its variance.

M15, M19, M24, M27. Large codewords can accumulate phases while adjacent differences remain small.

[Phase and control errors](../science/robustness.md) · [Fixed-aperture calibration](../science/calibration.md)

### M29 Why can position knowledge limit the coefficient estimate?

Construct two coefficient values that give the same site phases with opposite residual shifts. For unknown positions, use a monotone coordinate warp to obtain the same ambiguity with both endpoints fixed. Identify where the bounded slope enters the receiver guarantee.

M06, M13, M27, M28. Matching the actual phase profiles gives a lower bound for every preparation and readout.

[Fixed-aperture calibration](../science/calibration.md) · [Phase and control errors](../science/robustness.md)

### M30 Why does the curvature floor have coefficient 64?

Use the maximum deviation of the monic quadratic residual on the aperture to derive the lower constant. Explain how the high-gap four-site stencils approach it and how coarse estimates select the correct phase branch. State when the constant applies.

M15, M19, M22, M27–M29. This connects the calibration-dominated asymptotic to explicit sensing resources and the global parameter range.

[Fixed-aperture calibration](../science/calibration.md)
