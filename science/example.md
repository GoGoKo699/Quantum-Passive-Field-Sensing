# An eight-qubit curvature receiver

[Model](model.md) · [Minimax theorem](minimax.md) · [Verification](../verification/README.md)

The sites are $`0,\ldots,7`$. Use the following computational states.

| Address | Occupied sites | Count | First moment | Quadratic charge |
|---|---|---:|---:|---:|
| 00 | 0, 3, 4, 6 | 4 | 13 | 24 |
| 01 | 1, 2, 3, 7 | 4 | 13 | 25 |
| 10 | 0, 2, 5, 6 | 4 | 13 | 26 |

The two nuisance terms give a common phase. After removing the first signal charge, the three curvature phases are $`0,\phi,2\phi`$.

## Circuit

Use sites 5 and 7 as address bits $`a,b`$. Prepare the address in

```math
\frac12|00\rangle+\frac{1}{\sqrt2}|01\rangle+\frac12|10\rangle.
```

From zero, apply $`R_y(\pi/3)`$ to $`a`$. Conditional on $`a=0`$, apply $`R_y(2\arccos(1/\sqrt3))`$ to $`b`$. The other six sensors start at zero. Set them with reversible XORs.

```math
x_0=x_6=1\oplus b,\quad x_1=b,\quad x_2=a\oplus b,\quad
x_3=1\oplus a,\quad x_4=1\oplus a\oplus b.
```

The encoder uses eight CNOTs and four X gates. The fourth address has zero amplitude. Expose all eight sites once, reverse the encoder, then apply a four-point inverse Fourier transform on the address qubits. For measured label $`m\in\{0,1,2,3\}`$, report $`m\pi/2`$.

The first Fourier moment of the estimation error is $`1/\sqrt{2}`$, the sum of two adjacent products of the sine amplitudes. The expected cosine loss is $`1-1/\sqrt2`$ for every curvature, offset and slope. Eight sites have no length-four run, so this is optimal under the ideal model.

To test the outcome law, sweep the full curvature circle and vary offset and slope independently. Repeated trials at each setting assess the prediction for a single shot. The [verification program](../verification/run_checks.py) checks the encoding, nuisance moments and angle-invariant risk.
