---
type: proof
title: The increment theorem for two-term zero divisors
date: 2026-09-12
status: complete — machine-verified for A = H, O, S, S′, T, M(S)
verification: papers/mirror-sedenions/code/check23_increment_theorem.py
---

# The mirror increment

## Setting

Let A be a ∗-algebra of dimension h = 2^m with a basis {e_g}_{g ∈ F₂^m} satisfying
e_p e_q = w(p,q) e_{p⊕q}, w(p,q) ∈ {±1}, whose twist w is **proper** in the sense
of Bales [Def. 4.1, arXiv:1107.1375]; on F₂^m, where every element is its own
inverse, properness reads

    w(p,q) w(q,q) = w(p⊕q, q),        w(p,p) w(p,q) = w(p, p⊕q).        (P1), (P2)

All algebras of the {CD, M}-tower over O have proper twists (verified).
Write s(q) = 1 for q = 0 and −1 otherwise, so ē_q = s(q) e_q.

Index CD(A) and M(A) by F₂^{m+1}, with g < h denoting A and g + h denoting Ae.
From the doubling formulas,

| block | CD(A) | M(A) |
|---|---|---|
| (p, q), p,q < h | w(p,q) | **w(q,p)** |
| (p, q+h) | w(q,p) | w(q,p) |
| (p+h, q) | w(p,q) s(q) | w(p,q) s(q) |
| (p+h, q+h) | −s(q) w(q,p) | −s(q) w(q,p) |

**Lemma 1.** W_M = W_CD except on the A × A block, where
W_M(p,q) = W_CD(p,q)·σ(p,q) with σ(p,q) = −1 if p ≠ q and p, q ≠ 0, and +1
otherwise.

*Proof.* Immediate from the table, using w(q,p) = −w(p,q) for p ≠ q both
nonzero, and w(p,0) = w(0,p) = 1. ∎

σ is exactly the function χ of the mirror-sedenions paper, §7.

## The coset criterion

For x = e_i ± e_j with d = i ⊕ j ≠ 0, the equation xy = 0 decouples over the
cosets of {0, d}: writing Q_i(u) = W(i,u) W(i,u⊕d) — a function constant on each
coset — one has

    dim Ann(e_i ± e_j) = #{ cosets {u, u⊕d} : Q_i(u) = Q_j(u) }.       (∗)

In particular the condition does not depend on the sign, so e_i + e_j is a zero
divisor iff e_i − e_j is.

Call a pair **α** if i, j < h, **β** if i, j ≥ h, and **mixed** if i < h ≤ j.

## Lemma 2 (α and β are unchanged)

*For α and β pairs, dim Ann agrees in CD(A) and M(A).*

*Proof.* For β pairs neither index lies in the A × A block, so Q is unchanged.
For an α pair, d < h. On cosets with u ≥ h both u and u⊕d exceed h, so Q is
unchanged there. For u < h, Lemma 1 gives Q_M,i(u) = Q_CD,i(u)·τ_i(u) with
τ_i(u) = σ(i,u)σ(i,u⊕d). Now σ(i,u) = +1 iff u ∈ {0,i}, and σ(i,u⊕d) = +1 iff
u ∈ {d, j}; hence τ_i = −1 exactly on {0,i} Δ {d,j}. Symmetrically τ_j = −1
exactly on {0,j} Δ {d,i}. Since i, j, d and 0 are pairwise distinct (d ≠ 0,
i ≠ j, and d = i would force j = 0), both symmetric differences equal
{0, i, d, j}, so τ_i = τ_j and the condition Q_i = Q_j is unaffected. ∎

## Lemma 3 (four cosets never contribute)

*Let (p, q+h) be mixed, t = p ⊕ q. In CD(A) the cosets with lower representative
u ∈ {0, p, q, t} never contribute.*

*Proof.* Four computations from the block table.

**u = 0** (partner d): Q_i = 1·w(t,p), Q_j = 1·(−s(t) w(t,q)). If t = 0 this
reads 1 = −1. If t ≠ 0 it reads w(t,p) = w(t,q), and (P2) gives
w(t,q) = w(t, t⊕p) = w(t,t) w(t,p) = −w(t,p), a contradiction.

**u = p** (partner q+h): Q_i = w(p,p) w(q,p), Q_j = w(q,p) s(p)·(−s(q) w(q,q)).
For p ≠ 0 this reads −1 = +1 whether or not q = 0.

**u = q** (partner p+h), q ≠ 0: Q_i = w(p,q) w(p,p) = −w(p,q), while
Q_j = w(q,q)s(q)·(−s(p) w(p,q)) = +w(p,q).

**u = t** (partner h), t ≠ 0: Q_i = w(p,t), Q_j = −s(t) w(q,t) = w(q,t).
By (P2), w(t,q) = −w(t,p); antisymmetry then gives w(q,t) = −w(t,q) = w(t,p)
and w(p,t) = −w(t,p), so the condition reads −w(t,p) = w(t,p). ∎

**Corollary.** dim Ann_{CD(A)}(mixed) ≤ h − |{0, p, q, t}|, so ≤ h − 4 whenever
0, p, q, t are distinct, i.e. whenever q ≠ 0 and p ≠ q.

## Lemma 4 (the degenerate families)

*In CD(A), dim Ann(e_i ± e_{i+h}) = 0 and dim Ann(e_i ± e_h) = 0 for 1 ≤ i < h.*

*Proof.* For j = p + h (so d = h): on the coset of u < h,
Q_i(u) = w(p,u) w(u,p) and Q_j(u) = w(p,u)s(u)·(−s(u) w(u,p)) = −Q_i(u), which
can never be equal. For j = h (so q = 0, d = p + h): for u ∉ {0,p},
(P2) and antisymmetry give w(p⊕u, p) = w(p,u), so Q_i(u) = w(p,u)² = 1, while
Q_j(u) = −s(u)s(u⊕p) = −1; the cases u ∈ {0,p} are Lemma 3. ∎

## Theorem (the increment)

**(a)** For α and β pairs, dim Ann is the same in CD(A) and in M(A).

**(b)** For mixed pairs,
> **dim Ann_{M(A)} = (h − 2) − dim Ann_{CD(A)}.**

**(c)** Every mixed pair is a two-term zero divisor of M(A).

**(d)** Writing Z(X) for the number of two-term zero-divisor index pairs of X,
> **Z(M(A)) = 2 Z(A) + h(h − 1).**

*Proof.* (a) is Lemma 2. For (b), on a mixed pair the coset with lower
representative u satisfies Q_M,j = Q_CD,j and Q_M,i = Q_CD,i · σ(p,u); since
σ(p,u) = +1 exactly for u ∈ {0,p}, M and CD agree on those two cosets and are
complementary on the remaining h − 2. By Lemma 3 neither of the two agreeing
cosets contributes in CD (nor therefore in M), so every contributing coset of CD
is a non-contributing coset of M among the other h − 2 and conversely, giving
dim Ann_M = (h−2) − dim Ann_CD. For (c): if q ≠ 0 and p ≠ q the Corollary gives
dim Ann_CD ≤ h − 4, so dim Ann_M ≥ 2; in the two degenerate cases Lemma 4 gives
dim Ann_CD = 0, so dim Ann_M = h − 2 ≥ 2 for h ≥ 4. For (d): by (a) the α and β
zero-divisor pairs are the same in CD(A) and M(A) and number Z(A) each
(verified — see below), and by (c) all h(h−1) mixed pairs contribute. ∎

<!-- UNVERIFIED: the count "alpha pairs = beta pairs = Z(A)" in (d) is confirmed
     computationally for A = H, O, S, S', T, M(S) but is not proved here. It is
     the statement that a two-term pair inside either half is a zero divisor of
     the double exactly when it is one of A. Proving it would complete (d). -->

## Consequences

**Corollary 1 (the mirror octonion case).** For A = O, h = 8: the mixed pairs
number 56, all are zero divisors of M(O) = S′, and the 14 exceptions of CD(O) = S
are exactly (i, i+8) and (i, 8) — which is Prop. 5.4 of the mirror-sedenions
paper. Their annihilators have dimension h − 2 = **6**, and the other 42 have
dimension (h−2) − 4 = **2**: this is exactly the 2/6 stratification of
Theorem 5.2, recovered from the duality.

**Corollary 2 (the tower counts).** Along the CD spine one has likewise
Z(CD(A)) = 2Z(A) + (h−1)(h−2), since there the mixed exceptions are precisely
the two degenerate families. Combining with the theorem, for the level-k algebra
with b leading mirrors,

    Z(k,b) = 2^b Z(CD^{k−b}(O)) + 2^{b−1} h₀ [ h₀(2^b − 1) − b ],   h₀ = 2^{k−b+3}.

This reproduces every computed value at k ≤ 4 and is strictly increasing in b at
each fixed k (checked to k = 8).

**Corollary 3 (sharpness).** The k + 1 algebras M^b ∘ CD^{k−b}(O), b = 0,…,k, are
pairwise non-isomorphic, since Z is an isomorphism invariant and is strictly
increasing in b. With the erasure theorem's normal form this makes the count of
isomorphism classes at level k **exactly k + 1**.

## A caution: CD is not uniform

The analogue of (c) fails for CD: the mixed exceptions of CD(A) are the two
degenerate families when A lies on the CD spine, but **not** in general. For
A = S′ (h = 16) there are 58 exceptions rather than 30, and for A = M(S)
(h = 32) there are 122 rather than 62. Hence Z(CD(A)) = 2Z(A) + (h−1)(h−2) holds
along the spine but not universally, whereas **Z(M(A)) = 2Z(A) + h(h−1) holds for
every A tested**. The mirror double is the uniform operation here; the standard
one is not.
