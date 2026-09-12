---
type: note
date: 2026-09-12
topic: degenerate basis subalgebras of the CD tower — relative mirrors, absorption, the landscape
status: processed into synthesis/degenerate-subalgebras.md
---

# Session log — the "messed-up" subalgebras

Prompt: the mirror construction keeps turning up *inside* the CD construction as subalgebras;
Wilmot and Bales mapped the subalgebra landscape; what about the degenerate constructions
that give genuinely messed-up subalgebras, and what do they teach?

## What was done

1. Built `code/landscape.py`: sign-table doubling, subgroup enumeration, and a graded
   isomorphism test via the **associator pattern** (proved a complete invariant for
   anticommutative sign-monomial algebras; validated against `f2iso.py`).
2. `check21`: census of every basis subalgebra of A_4 … A_7 by graded isomorphism.
3. `check22`: invariants per class; absorption test; Wilmot's P12 / P14 triads.
4. `check23`: relative-mirror table; Lemma-1 identities for the general relative mirror;
   {CD,M}-words; all 32 Bales products on every class.
5. `check24`: Wilmot incidence and Der structure for the degenerate classes.
6. `check25`: the 64-dimensional landscape by fingerprint + associator search.
7. Wrote `RELATIVE-ERASURE-PROOF.md` and `synthesis/degenerate-subalgebras.md`.

## Findings, in the order they arrived

- 8-dim landscape: only O and P4 = M(H), at every level. Wilmot's P12, P14 triads ≅ P4.
- 16-dim: S 16, S′ 1, X16.2 ×7, X16.3 ×7 in T (Cawagas's 16/1/7/7); same four classes in A_6
  and A_7. X16.3 = M(M(H)). X16.2 is not any Bales double of any of its hyperplanes.
- 32-dim in A_6: T ×32, M(S), M(S′), X32.4 (×1), X32.3/5/6/7 (×7). All 31 hyperplanes
  through the top unit are T — CD(X16.2) ≅ CD(X16.3) ≅ T. That was the moment the general
  theorem became visible: CD absorbs everything.
- Relative-mirror table: every non-T 32-dim class is R_T(K) for one Aut-orbit of hyperplanes K.
- Lemma-1 identities hold for N = K + K(e_c e), all K, all A tested, including a
  Bales-rejected base. Hand derivation: only anticommutativity between K and its coset.
- Der(X16.2) = Der(X16.3) = so(4); 24 graded automorphisms; ZD 148 / 160; the rule
  dim Ann = 2 × (#P4 hyperplanes containing the pair) holds in all four 16-dim classes.
- Bales's 24 rejected products fail the quaternion property on every base; never subalgebras.

## Loose ends

- ~~|L_5|~~ = 16, done once the pruned search landed (15 orbits of hyperplanes of A_6).
- ~~Stability at 32-dim inside A_7~~ — confirmed (8 classes over 2667 subgroups), and the 64-dim census of A_7 reproduces |L_5| = 16 directly.
- Conjecture |L_k| = 2^{k−2}.
- Closed forms for the counts of each class in A_n beyond dimension 16.
