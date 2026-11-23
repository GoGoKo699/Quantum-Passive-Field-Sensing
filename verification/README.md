# Reproduce the finite checks

From the repository root, run with Python 3.9 or later and its standard library.

```sh
python3 verification/run_checks.py
```

The script enumerates binomial charges exactly with integer bitsets. A bit at position $`q`$ records that a signal charge $`q`$ occurs in the given vector of lower-moment charges. Adding a site shifts the bitset for the occupied branch by its signal charge and adjusts its sector by the site's lower moments. The unoccupied branch retains the old sector and bitset. The script compares the recurrence with direct basis enumeration on seven sites.

| Polynomial degree | Sensors | Maximum sector diameter | Longest consecutive run |
| --- | ---: | ---: | ---: |
| 2 | 8 | 16 | 3 |
| 2 | 12 | 54 | 29 |
| 2 | 16 | 128 | 87 |
| 2 | 24 | 432 | 361 |
| 2 | 32 | 1024 | 919 |
| 3 | 16 | 140 | 1 |
| 3 | 20 | 384 | 2 |

The columns maximize over sectors independently. For 16 sensors at degree three, the diameter reaches 140, while every sector lacks a pair of adjacent charges. The analytic minimax formula then gives circular risk 1, the risk of a uniform phase guess under $`1-\cos`$ loss.

For the eight-sensor receiver, the script checks the encoded bitstrings, their shared lower moments, their three consecutive signal charges, and the exact discrete Fourier frequency-selection rule. A floating-point simulation independently sweeps 257 triples of signal, offset and slope angles. The received distribution gives risk $`1-1/\sqrt{2}`$ to machine precision on that sweep.

Further integer checks verify translated finite-difference stencils for degrees two through seven, disjoint packed examples with 1,024 and 2,048 consecutive charges, and the lower-moment conservation and exact signal span of the quadratic mirror moves. The [arithmetic construction](../science/arithmetic.md) gives the analytical guarantees beyond these finite cases.
