# Consecutive spectra on the fixed lattice

Take sites $`j=0,\ldots,N-1`$ with occupation $`n_j\in\{0,1\}`$ and charges $`Q_a(n)=\sum_j\binom{j}{a}n_j`$. Fix the degree $`d\ge 1`$ as $`N`$ grows. A sector fixes $`Q_0,\ldots,Q_{d-1}`$. Let $`L_N^{(d)}`$ be the length, including both endpoints, of a longest interval of consecutive $`Q_d`$ values in any one sector. Then

```math
L_N^{(d)}=\frac{N^{d+1}}{4^d d!}+O_d\!\left(N^{d+1-1/(d+1)}\right).
```

The upper bound follows from a polynomial envelope. The construction first balances the lower moments on a sequence of configurations, then fills gaps in the signal along that sequence. It uses only the specified lattice sites and binary occupations.

## Blocks with prescribed signal gaps

An order-$`a`$ block, for $`a\ge1`$, is determined by a position $`s`$ and positive shifts $`h_1,\ldots,h_a`$ with distinct subset sums. Its sites are $`s+\sum_{i\in S}h_i`$ for all $`S\subseteq\{1,\ldots,a\}`$. The two configurations occupy opposite parities of $`|S|`$. Orient the change so its signed moment difference is the forward difference

```math
\Delta Q_k
  = (\Delta_{h_1}\cdots\Delta_{h_a})\binom{s}{k}
  = \sum_{0\le t_i<h_i}\binom{s+t_1+\cdots+t_a}{k-a},
```

where $`\Delta_h f(x)=f(x+h)-f(x)`$. The second identity holds for $`k\ge a`$ by telescoping the unit-step binomial identity. Thus all $`Q_k`$ with $`k<a`$ are unchanged, and $`\Delta Q_a=\prod_i h_i`$. For $`k>a`$, the absolute change is at most $`C_d N^{k-a}\Delta Q_a`$ on the full length-$`N`$ lattice. Reversing the orientation reverses the sign. For $`a=0`$ a single site is the analogous unit block. The equal-lower-power-sum identity is an instance of the [Prouhet–Tarry–Escott construction](https://arxiv.org/abs/2609.05061). The arrangement of many such blocks for a consecutive same-sector spectrum is the step needed here.

### Small gaps and the dyadic sequence

Write $`b_a=a(a-1)/2`$. For any integer $`k\ge b_a`$, write $`k-b_a=aq+r`$ with $`0\le r<a`$. Start with the $`a`$ exponents $`q,q+1,\ldots,q+a-1`$, then increase the largest $`r`$ by one. Taking $`h_i`$ as powers of two with these exponents gives distinct subset sums, gap $`2^k`$, and a span of $`O_a(2^{k/a})`$ sites. The spans needed through $`2^K`$ have sum $`O_a(2^{K/a})`$.

To cover the finitely many missing low gaps, take one block with shifts $`1,2,\ldots,2^{a-1}`$ and another with shifts $`1,3,\ldots,3^{a-1}`$. Their respective gaps $`2^{b_a}`$ and $`3^{b_a}`$ are coprime. A fixed Bézout combination, realized by disjoint translated copies and the appropriate orientations, is one composite block of gap one. Flip its constituent blocks together. Group disjoint copies of this composite into binary blocks of sizes $`1,2,\ldots,2^{b_a-1}`$ to supply all residual gaps below $`2^{b_a}`$. For $`a=1`$ the dyadic sequence already starts at one.

### A full interval on a short stretch of sites

Let $`T`$ be a power of two. Use the shifts $`h_i=2^{i-1}T`$ in a block and translate it by each $`t=0,\ldots,T-1`$. The blocks are disjoint because the original sites differ by multiples of $`T`$, and they all fit in $`2^a T`$ consecutive sites. Each block has the same gap

```math
G=2^{b_a}T^a.
```

On a separate stretch, combine the low-gap blocks with the dyadic blocks below $`G`$ to supply every offset in $`[0,G-1]`$. This stretch takes $`O_a(T)`$ sites, since $`G`$ is a power of two. Choosing any number of the $`T`$ identical-gap blocks gives all multiples $`0,G,\ldots,TG`$. The full collection therefore supplies every offset in $`[0,(T+1)G-1]`$ in one lower-charge sector. On a stretch of $`M`$ sites choose the largest power of two below a sufficiently small constant times $`M`$. The collection supplies an interval of length $`\Omega_a(M^{a+1})`$. With just an order-$`d`$ collection, this already proves the scaling $`L_N^{(d)}=\Theta_d(N^{d+1})`$.

The net higher-charge bound remains valid for a chosen offset $`u`$. For an increasing collection use only positive-orientation changes from a fixed baseline and for a decreasing collection reverse all orientations. Summing the individual bounds gives $`|\Delta Q_k|\le C_d N^{k-a}|u|`$ for $`k>a`$. In a composite block the absolute constituent gaps sum to a constant depending only on $`a`$, which changes just $`C_d`$. These bounds also hold for the single-site collection at order zero.

## Upper bound from a polynomial envelope

Let $`U_d`$ be the Chebyshev polynomial of the second kind and $`x_j=2j/N-1`$. Its leading coefficient is $`2^d`$, so the polynomial

```math
\binom{j}{d}-\frac{N^d}{4^d d!}U_d(x_j)
```

has degree at most $`d-1`$ in $`j`$. For two configurations in the same sector, this polynomial cancels in their difference. Each occupation difference has absolute value at most one, hence the signal diameter is at most

```math
\frac{N^d}{4^d d!}\sum_{j=0}^{N-1}|U_d(x_j)|
=\frac{N^{d+1}}{4^d d!}+O_d(N^d).
```

The Riemann sum uses $`\int_{-1}^1|U_d(x)|\,dx=\int_0^\pi|\sin((d+1)t)|\,dt=2`$. Any consecutive run has length at most the signal diameter plus one.

## Matching construction for every fixed degree

### Reserve sites without creating a leading moment error

Put $`\sigma(x)=\operatorname{sgn}U_d(x)`$. Its lower moments vanish

```math
\int_{-1}^1 \sigma(x)x^a\,dx=0,\qquad 0\le a<d.
```

With $`x=\cos t`$, the integrand becomes $`\operatorname{sgn}\sin((d+1)t)\cos^a(t)\sin(t)`$. The second factor is a combination of sine harmonics of order at most $`a+1`$. The first has only odd multiples of harmonic $`d+1`$ in its sine expansion on $`[0,\pi]`$.

Take $`M=\lceil A_dN^{d/(d+1)}\rceil`$ with a fixed large constant $`A_d`$. Reserve the leftmost $`M`$ sites, and let $`B=N-M`$. On the remaining interval, use the rescaled points $`z_j=2(j-M)/B-1`$ and signs $`\sigma(z_j)`$. The signed sums of each lower charge are $`O_d(N^a)`$. Indeed, $`N^{-a}\binom{M+B(z+1)/2}{a}`$ has degree $`a<d`$ and uniformly bounded coefficients and derivative. Its signed continuum integral vanishes by orthogonality. A Riemann sum has error $`O_d(1)`$ before normalization by the number of sites, because the degree and number of sign boundaries are fixed. At a root, either choice of sign changes the estimate by only finitely many terms.

### Make the lower charges exact

Outside the reserved sites, start with a configuration occupying all negative-sign sites and finish with the one occupying all positive-sign sites. The individual changes are single-site toggles. The vectors of their lower-charge changes, with component $`a`$ divided by $`N^a`$, are uniformly bounded and have bounded total sum. Add one dummy vector equal to the negative of the sum and apply the [Steinitz rearrangement lemma](https://fanchung.ucsd.edu/ron/papers/96_02_primitive_partition.pdf) (Lemma 2), then remove the dummy. Every prefix now differs from the starting configuration by only $`O_d(N^a)`$ in $`Q_a`$ for $`a<d`$.

In the reserved stretch place two disjoint collections of each order $`a=0,\ldots,d-1`$, one increasing and one decreasing, and a separate increasing order-$`d`$ collection. Each collection can use a constant fraction of $`M`$ sites. Start every prefix's reserved part in the same baseline. Repair each prefix to the starting sector by visiting the lower charges in increasing order. At stage $`a`$ the residual is $`O_d(N^a)`$: the initial error has this bound, and a previous correction of order $`h<a`$ contributes at most $`O_d(N^{a-h}N^h)`$. The order-$`a`$ capacity $`\Omega_d(M^{a+1})`$ grows faster than $`N^a`$ for $`a<d`$, so the correction can hit the residual exactly with the appropriate orientation. Its lower charges stay fixed. Every prefix is now in the same lower-charge sector. The total change to $`Q_d`$ from the repairs is at most $`O_d(N^d)`$ per prefix.

### Fill every gap before and after the repairs

Consider the signal values of the repaired prefixes with the order-$`d`$ collection still fixed at its baseline. Successive values differ by at most $`C_d N^d`$, because one unreserved-site toggle costs $`O_d(N^d)`$ and each repair costs $`O_d(N^d)`$. The repair constants depend only on the fixed degree and the bounded Riemann-sum and rearrangement errors. The final order-$`d`$ collection supplies $`\Omega_d(M^{d+1})`$ consecutive offsets without changing any nuisance charge. Taking $`A_d`$ sufficiently large makes the interval from each repaired prefix overlap the next one. Monotonicity of the sequence is unnecessary for its union to be a single interval.

The difference between the last and first signal values is obtained by pairing the bulk envelope $`B^d U_d(z_j)/(4^d d!)`$ with its sign. The discarded lower-degree polynomial contributes only $`O_d(N^d)`$ before repairs, because its coefficient at degree $`a`$ in the binomial basis is $`O_d(N^{d-a})`$ and the lower moment discrepancies are $`O_d(N^a)`$. The envelope contributes $`B^{d+1}/(4^d d!)+O_d(N^d)`$. Replacing $`B`$ by the full length costs at most $`O_d(MN^d)`$. Repairs cost another $`O_d(N^d)`$. Consequently the single interval has length at least

```math
\frac{N^{d+1}}{4^d d!}-O_d(MN^d),
```

which matches the upper bound to leading order. The argument fixes $`d`$ before increasing $`N`$ and does not assert a uniform bound when $`d`$ grows.

## Quadratic construction with mirror pairs

For $`d=2`$ the binomial charge gives a leading width of $`N^3/32`$. A separate elementary construction achieves error $`O(N^{5/2})`$. Reserve a central stretch of $`O(\sqrt N)`$ sites, invariant under reflection about $`c=(N-1)/2`$. Within it place the low-gap and dyadic order-two blocks giving an interval of offsets $`[0,B-1]`$ for power-of-two $`B\ge 2N`$. These blocks need only $`O(\sqrt B)`$ sites. Choose $`B<4N`$.

Use only fully occupied or fully empty mirror pairs outside that stretch, occupying exactly half of the available pairs rounded down. Both lower charges are then fixed. A pair at radius $`r`$ has charge $`\binom{c+r}{2}+\binom{c-r}{2}=c^2-c+r^2`$. Move from the innermost possible occupied set to the outermost by successive swaps of an occupied radius with its next, empty radial shell. All available radii form a consecutive sequence with step one, so each swap changes the signal by at most $`N`$. The offset interval covers the intervening integers. Without the reservation the endpoint difference is $`N^3/32+O(N^2)`$, by summing the outer and inner squared radii. The reservation changes at most $`O(\sqrt N)`$ terms at $`O(N^2)`$ each, which proves the claimed quadratic error bound.

## Finite calculation

For fixed $`d`$, a subset-sum dynamic program can compute the exact optimum and produce the occupation representatives. For each site, carry the reachable charge vectors forward once with and once without the site's vector $`(1,j,\binom{j}{2},\ldots,\binom{j}{d})`$. Select a longest consecutive run after grouping by the first $`d`$ charges. Backpointers supply one configuration per signal charge. Each charge $`Q_a`$ is at most $`\binom{N}{a+1}`$, so this procedure takes polynomial time in $`N`$ at fixed degree, with a degree-dependent exponent.
