---
type: proof
title: Relative erasure — every basis hyperplane, not just the founding copy, is erased by a standard doubling
date: 2026-09-12
status: complete — hand derivation on basis elements, machine-verified for A = O, P4, S, S′, X16.2, X16.3, T, X32.7 and a Bales-rejected base
verification: papers/mirror-sedenions/code/check23_relative_mirror.py (§2), check22_classes.py (absorption)
generalises: papers/mirror-sedenions/ERASURE-PROOF.md
---

# CD(K + K(e_c e)) ≅ CD(A) for every basis hyperplane K of A

## Setting

A **sign-monomial algebra** on G = F₂ⁿ is the real algebra with basis {e_p : p ∈ G} and
e_p e_q = w(p,q) e_{p⊕q}, w(p,q) ∈ {±1}. It is **anticommutative** if

    w(0,p) = w(p,0) = 1,    w(p,p) = −1 (p ≠ 0),    w(p,q) = −w(q,p) (p ≠ q, both ≠ 0).

With ē_p = s_p e_p (s₀ = 1, s_p = −1 otherwise) every such algebra is a ∗-algebra with
(xy)‾ = ȳx̄ and xx̄ = x̄x = |x|²; this is a two-line check on basis pairs and uses nothing but
the three sign rules. **Every basis subalgebra of every Cayley–Dickson algebra is of this
kind**, because the three rules are statements about pairs of basis elements and pass to
any subgroup of G. (These are exactly Bales's "Cayley–Dickson-like" algebras in his twisted-
group-algebra language; associativity, alternativity, the quaternion property and the
composition property are *not* assumed anywhere below.)

Fix an anticommutative sign-monomial A on G, a hyperplane K = ker f ⊂ G (f ≠ 0 a linear
functional) and a point c ∉ K. Then A = K ⊕ Ke_c as vector spaces, Ke_c = span{e_x : x ∈ c⊕K}.
Inside B = CD(A) = A ⊕ Ae, with (p + qe)(r + se) = (pr − s̄q) + (sp + q r̄)e, define the
**relative mirror of A with respect to K**:

    R_A(K) := K ⊕ (Ke_c)e  =  span{ e_p : p ∈ K } ⊕ span{ e_x e : x ∈ c ⊕ K }.

As a set of indices this is the graph subgroup {p + f(p)·top : p ∈ G} of G ⊕ F₂, so R_A(K)
is a basis subalgebra of CD(A) of the same dimension as A, and it does not depend on the
choice of c. It is the hyperplane of CD(A) *avoiding* the doubling unit e whose intersection
with A is K. The basis hyperplanes of CD(A) are exactly: A itself, the CD(K) = K ⊕ Ke for K a
hyperplane of A (these contain e), and the R_A(K) (these avoid e) — 1 + (2ⁿ−1) + (2ⁿ−1) in all.

## Theorem

> **Theorem (relative erasure).** For every anticommutative sign-monomial algebra A and
> every basis hyperplane K ⊂ A,
>
>     CD( R_A(K) ) ≅ CD(A)        as ∗-algebras,
>
> by the explicit map Ψ(n, m) = n + m e, n, m ∈ R_A(K).

The erasure theorem of `ERASURE-PROOF.md` is the case A = CD(A₀), K = A₀, c = e₀: then
R_A(K) = A₀ + A₀(e₀e) ≅ M(A₀) by Theorem 3.3, and the statement reads CD(M(A₀)) ≅ CD²(A₀).
**The proof below never uses that A is itself a double.** That is the whole point: the
argument in `ERASURE-PROOF.md` looked as if it needed the inner Cayley–Dickson formulas,
but every step survives when those are replaced by the three sign rules.

## Proof

Apply Lemma 1 of `ERASURE-PROOF.md` (the doubling-unit criterion) with B = CD(A),
N = R_A(K), u = e. Its hypotheses are: (i) N is a ∗-subalgebra with B = N ⊕ Nu, and for all
n, m, m₁, m₂ ∈ N: (ii) n(mu) = (mn)u; (iii) (mu)n = (mn̄)u; (iv) (m₁u)(m₂u) = −m̄₂m₁;
(v) u² = −1, ū = −u, and u m̄ = m u.

Write every element of N as n = a + αe, m = b + βe with a, b ∈ K and α, β ∈ Ke_c. Two facts
about the coset part are used over and over:

    (F1)  α ∈ Ke_c  ⇒  ᾱ = −α                    (x ∈ c⊕K is never 0, so s_x = −1)
    (F2)  a ∈ K, α ∈ Ke_c  ⇒  aα = αā  and  āα = αa   (anticommutativity: p ∈ K and
          x ∈ c⊕K are distinct and, for p ≠ 0, both nonzero; the p = 0 case is trivial)

and the standard Cayley–Dickson identities for elements of A, read off from the doubling
formula: for p, r ∈ A, p(re) = (rp)e, (re)p = (rp̄)e, (pe)(re) = −r̄p, e p̄ = pe, (re)e = −r.

**(i) N is a ∗-subalgebra with B = N ⊕ Ne.** Closure: e_p e_q ∈ K; e_p(e_x e) = (e_x e_p)e and
(e_x e)e_p = (e_x ē_p)e lie in (Ke_c)e; (e_x e)(e_y e) = −ē_y e_x ∈ K since x⊕y ∈ K.
Involution: (αe)‾ = ē ᾱ = −eᾱ = −αe ∈ N. Decomposition: Ne = Ke ⊕ (Ke_c)e·e = Ke ⊕ Ke_c, so
N ⊕ Ne = K ⊕ Ke_c ⊕ Ke ⊕ (Ke_c)e = A ⊕ Ae = B.

**(ii) n(me) = (mn)e.** Since me = (b + βe)e = −β + be,

    n(me) = (a + αe)(−β + be) = (−aβ − b̄α) + (ba − αβ̄)e.

On the other side mn = (b + βe)(a + αe) = (ba − ᾱβ) + (αb + βā)e, and (X + Ye)e = −Y + Xe,
so (mn)e = −(αb + βā) + (ba − ᾱβ)e. The two agree iff

    aβ + b̄α = αb + βā        and        αβ̄ = ᾱβ.

The second is (F1) twice. The first splits into aβ = βā and b̄α = αb, both (F2). ✔

**(iii) (me)n = (mn̄)e.** (me)n = (−β + be)(a + αe) = (−βa − ᾱb) + (−αβ + bā)e. Since
n̄ = ā − αe, mn̄ = (b + βe)(ā − αe) = (bā + ᾱβ) + (−αb + βa)e and
(mn̄)e = (αb − βa) + (bā + ᾱβ)e. Agreement iff −ᾱb = αb and −αβ = ᾱβ, i.e. ᾱ = −α. (F1). ✔

**(iv) (ne)(me) = −m̄n.** ne = −α + ae, me = −β + be, so
(ne)(me) = (αβ − b̄a) + (−bα − aβ̄)e. And m̄n = (b̄ − βe)(a + αe) = (b̄a + ᾱβ) + (αb̄ − βā)e,
so −m̄n = (−b̄a − ᾱβ) + (−αb̄ + βā)e. Agreement iff αβ = −ᾱβ [F1], bα = αb̄ [F2], and
aβ̄ = −βā, i.e. −aβ = −βā [F1 then F2]. ✔

**(v)** e² = −1 and ē = −e are the doubling formula. e m̄ = e(b̄ − βe) = β̄ + be = −β + be = me. ✔

Lemma 1 now gives Ψ: CD(N) → B, Ψ(n, m) = n + me, an isomorphism of ∗-algebras. ∎

**What was used.** Only (F1), (F2) and the outer doubling formula. (F2) is anticommutativity
between K and its complementary coset; (F1) says the coset carries no real part. Neither the
quaternion property (associativity of 2-generated subalgebras) nor any identity inside K
enters. So the theorem holds verbatim for Bales's 24 rejected products used as the base A
(machine-checked for P(1,3) on H), and for the split Cayley–Dickson algebras (ε = −1), since
the three sign rules hold there too. <!-- UNVERIFIED: the eps=-1 case is asserted from the
proof, which is indifferent to eps; it has not been run separately. -->

## Corollaries

Write A_n = CDⁿ(R) (dim 2ⁿ) and **L_k(n)** for the set of graded-isomorphism classes of
2^k-dimensional basis subalgebras of A_n.

**Corollary 1 (absorption).** For every basis subalgebra B of A_n of dimension 2^{k−1},
CD(B) ≅ A_k. In particular every basis hyperplane of A_{k+1} *through* the top unit is
isomorphic to A_k.

*Proof.* Induction on n. If B ⊂ A_{n−1}, use induction. If B ∋ top, B = CD(B′) with
B′ ⊂ A_{n−1} of dimension 2^{k−2}, and CD(B) = CD(CD(B′)) ≅ CD(A_{k−1}) = A_k by induction on
B′. Otherwise B is the graph of a nonzero functional on a 2^{k−1}-dimensional B̃ ⊂ A_{n−1},
i.e. B = R_{B̃}(K) for a hyperplane K of B̃; by the theorem CD(B) ≅ CD(B̃) ≅ A_k, the last by
induction on B̃. ∎

**Corollary 2 (stability of the landscape).** L_k(n) = L_k(k+1) for all n ≥ k+1: the
2^k-dimensional basis subalgebras of every Cayley–Dickson algebra of dimension ≥ 2^{k+1}
realise exactly the classes of the basis hyperplanes of A_{k+1}, no more.

*Proof.* A 2^k-dimensional basis subalgebra of A_{n+1} either lies in A_n (induction), or
contains the top unit and is CD(B′) ≅ A_k by Corollary 1, or is R_{B̃}(K) ⊂ CD(B̃) ≅ A_{k+1}
(Corollary 1 again) and hence is a hyperplane of A_{k+1}. ∎

**Corollary 3 (generation by relative mirrors).**

    L_k = { A_k } ∪ { R_{A_k}(K) : K a basis hyperplane of A_k },

and the classes R_{A_k}(K) depend only on the Aut-orbit of K. Hence
|L_k| ≤ 1 + #(orbits of graded automorphisms of A_k on its hyperplanes). The relative mirror is
the **only** mechanism that produces new isomorphism types; the standard doubling produces
none (Corollary 1).

**Corollary 4 (the mirror tower lives inside the standard tower).** For every B ∈ L_{k−1},
M(B) ∈ L_k: indeed M(B) ≅ R_{CD(B)}(B) by Theorem 3.3 of the paper, and CD(B) ≅ A_k. In
particular every normal-form algebra M^b CD^a(O) of the {CD,M} tower is a basis hyperplane of
CD^{a+b+1}(O) — the sedenion fact S′ = Sγ ⊂ T is the first instance.

## Machine verification (2026-09-12)

`check23_relative_mirror.py` §2 checks (ii)–(v) on all pairs of basis elements of
N = R_A(K), for **every** hyperplane K, with A = O, P4 = M(H), S, S′, X16.2, X16.3 (all 15
hyperplanes), T (all 31), X32.7 (all 63), and the Bales-rejected P(1,3)(H), which is
anticommutative but lacks the quaternion property. All pass.

`check22_classes.py` checks Corollary 1 directly: of the 31 hyperplanes of A_5, the 15
through the top unit are all ≅ S; of the 63 of A_6, the 31 through the top are all ≅ T —
including the doubles of the degenerate classes X16.2 and X16.3.

`check21_landscape.py` checks Corollary 2: the 16-dimensional census is {S, S′, X16.2, X16.3}
in A_5, A_6 and A_7 (31, 651 and 11811 subgroups respectively), and the 8-dimensional census is
{O, P4} in A_4 … A_7.
