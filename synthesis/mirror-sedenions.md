---
type: synthesis
title: The mirror sedenions S' = M(O)
status: working
updated: 2026-09-11
author: Lui
artifact: papers/mirror-sedenions/mirror-sedenions-v1.pdf
sources: [sources/bales-2016.md, sources/moreno-1998.md, sources/reggiani-2024.md, sources/biss-christensen-dugger-isaksen-2009.md, sources/biss-dugger-isaksen-2008.md, sources/cawagas-2004.md, sources/cawagas-et-al-2009.md, sources/chan-dokovic-2006.md, sources/brown-1967.md, sources/schafer-1954.md, sources/albuquerque-majid-1999.md, sources/de-marrais-2000.md]
---

# The mirror sedenions S' = M(O)

## The claim

The Cayley–Dickson double of O can be formed with the product of the founding
copy written **backwards**:

    (a, b)(c, d) = (ca - d̄b, da + bc̄)          [the mirror double M(A)]
    (a, b)(c, d) = (ac - d̄b, da + bc̄)          [standard CD(A)]

Over a commutative base the two coincide. Over **H** they already diverge —
M(H) is the quasi-octonion algebra, not O. Over **O** the single transposed
letter yields a 16-dimensional real algebra **S′ = M(O)**, the *mirror
sedenions*, which is flexible, quadratic, carries the diagonal action of G2,
and is **not isomorphic to the sedenions S**.

This is not a new algebra in the sense of never having been seen: it is the
subalgebra Sγ = O + O(ee′) of the trigintaduonions, which Cawagas et al.
recorded in a subalgebra census and did not study. What is new here is (i) the
mirror double as a *construction*, (ii) the observation that Bales's eight
doubling products applied once to O yield exactly two algebras — S and S′ — and
(iii) a complete structural determination of S′.

Confidence: **high on the computed structure** (every numerical claim is
machine-verified, see `papers/mirror-sedenions/VERIFICATION.md`); **medium on
novelty**, which rests on a literature search that has a known gap (see below).

## The structural result

| | S = CD(O) | S′ = M(O) |
|---|---|---|
| norm-one zero divisors Z | V₂(R⁷), dim 11 | S⁶ × S⁷, dim 13 |
| zero-divisor condition on x = a + bℓ | a, b ∈ Im O, a ⊥ b, \|a\| = \|b\| | a ∈ Im O, \|a\| = \|b\| |
| dim Ann(x) | 4 | 2; **6** when b ∈ C_a |
| pair manifold P | G2 (a G2-torsor) | V₂(R⁷) × S³ (stabilizers SU(2)) |
| P → G2/SO(4), fibre | SO(4) | SO(3) × S³ |
| stretch spectrum (multiplicities) | 1 ± s (4, 4), 1 (8) | 1 ± σ (2, 2), 1 ± τ (4, 4), 1 (4) |
| dim ker alt_x, generic x | 8 (an octonion subalgebra) | 4 (a quaternion subalgebra) |
| octonion basis hyperplanes | O and the 7 **through** ℓ | the 8 **avoiding** ℓ |
| quasi-octonion basis hyperplanes | the 7 avoiding ℓ except O | the 7 through ℓ |
| two-term basis zero divisors | 84 (de Marrais's assessors) | 112 |
| Der | g₂ | g₂ |
| Aut | G2 × S³ (Brown) | G2 × Z/2 |
| graded automorphisms | order 2688 = 168·16 | order 2688 |
| inside T = CD(S) | S (16 basis hyperplanes) | Sγ = O + O(ee′) (1 hyperplane) |

where s = 2\|a′ × b′\|/N, σ = 2\|a′\|\|b\|/N, τ = 2\|a′\|\|b∥\|/N.

## The argument, in one paragraph

Both algebras have derivation algebra g₂, both have eight octonion and seven
quasi-octonion subalgebras among their basis hyperplanes, and both have a
14-dimensional manifold of zero-divisor pairs fibring over V₂(R⁷) with fibre S³.
The difference is **where the frame lives**. In S the frame (u, v) ∈ V₂(R⁷) is
carried by the zero divisor x = u + vℓ itself and the S³ by its annihilator, so
P(S) is the principal bundle G2 → G2/SU(2). In S′ the frame (u, n) is *split*
between x = u + bℓ and its partner y = nu + (bn)ℓ, the S³ is the quaternion
coordinate of b in the chart H(u, n), and the bundle is **trivial**.

The consequence for the literature is the interesting part:

> Moreno's theorem that the zero-divisor pairs of S form a G2-torsor is, in this
> light, a statement about the **alignment of the orientation of the founding
> octave with the doubling twist** — not about G2 alone. S′ has the same G2 and
> no torsor.

Formally, the two algebras differ as twisted group algebras of F₂⁴ by a single
sign function χ on F₂⁴ × F₂⁴, equal to −1 on pairs of distinct nonzero points of
the founding F₂³ and +1 elsewhere. **χ is not a 2-cocycle**, and no signed
relabelling of the sixteen basis units carries S to S′ (exhaustive search over
GL(4,2)). This is the "orientation bit" of the fourth doubling.

## What would change my mind

Ranked by how much damage each would do.

1. **A prior description of S′'s zero divisors, spectrum, or automorphisms.**
   This would not make the mathematics wrong but would remove the novelty claim,
   which is the paper's main contribution. The literature search is the weakest
   link — see the Wilmot gap below.
2. **A signed relabelling carrying S → S′.** Would collapse the whole thing.
   Ruled out by exhaustive search over GL(4,2); the search is machine-verified,
   so this would require a bug in `f2iso.py`, not a mathematical surprise.
3. **An error in Lemma 2.2** (kernel of n ↦ [b, n, u] is the quaternion
   subalgebra H(u, b)). Theorems 5.2 and 5.5 both route through it — the
   annihilator description and the trivialization of the pair bundle would fall
   together.
4. **A different convention making the comparison table apples-to-oranges.**
   The paper fixes Convention 2.1 explicitly and notes that inside S′ the
   founding copy of O carries the *opposite* product (e₁e₂ = −e₃), which is
   exactly the kind of detail that silently breaks cross-paper comparisons.

## Open questions (from §9)

1. **Riemannian geometry.** Z(S′) is a product of round spheres. What is the
   induced metric on P(S′) ⊂ S¹⁵ × S¹⁵ in coordinates (u, n, q)? It is
   G2-invariant of cohomogeneity three and *not* a Riemannian product — the
   cross terms do not vanish (verified numerically). Is it Einstein for some
   rescaling, as Reggiani's deformations of P(S) are? → `sources/reggiani-2024.md`
2. **The orientation tree.** Each word in {CD, M} applied to O gives an algebra
   with diagonal G2; at dimension 16 the three are S, S′, M(M(H)). Which of the
   2^(n−3) words give non-isomorphic algebras at dimension 2ⁿ, and which have
   Der = g₂? Numerical census suggests S and S′ are the only two with eight
   octaves and 14-dimensional Der. **A proof is wanted.**
3. **Higher mirrors.** M(S) and M(S′) sit inside the 64-dimensional CD algebra.
   Do the Biss–Dugger–Isaksen large-annihilator results have mirror analogues?
   Is dim Ann ≡ 0 (mod 2), rather than (mod 4), the general pattern?
4. **A conceptual proof of Theorem 5.5.** Moreno realizes a zero-divisor pair of
   S as a Cayley frame. Is there a similarly intrinsic description of the
   trivialization P(S′) ≅ V₂(R⁷) × S³ — e.g. via the fibration over G2/SO(4)?

## Known gap in the literature search

<!-- UNVERIFIED: Wilmot is named as a key starting point but appears nowhere in
     the bibliography of v1. Either the search missed him, or he was considered
     and dropped without a note. Resolve before any novelty claim goes out. -->

**Wilmot is not in the v1 bibliography.** He is cited in conversation as one of
the three good starting points alongside Reggiani and Moreno, and the latter two
are references [19] and [18]. This is the single most likely place for a prior
description of S′ to be hiding, and the novelty claim in §1 ("We found no prior
description of the zero divisors, annihilators, spectrum, automorphisms, or
subalgebra geometry of S′") is exposed until it is closed.

See `sources/wilmot-GAP.md`.
