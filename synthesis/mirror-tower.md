---
type: synthesis
title: The {CD, M} tower — what the mirror construction actually contributes
status: draft
updated: 2026-09-12
sources: [sources/wilmot-2025.md, sources/bales-2011-catalog.md, sources/cawagas-et-al-2009.md]
evidence: papers/mirror-sedenions/code/check13_wilmot_incidence.py, check14_tree_hyperplanes.py, check15_tree_invariants.py
---

# The {CD, M} tower

## The claim

**The mirror double is erased by a subsequent standard doubling:**

> **The erasure relation.** For every ∗-algebra A in the tower,
> CD(M(A)) ≅ CD(CD(A)).

**Status: verified at level 2 by explicit isomorphism; conjectural in general.**

| case | status |
|---|---|
| CD(M(H)) ≅ CD(CD(H)) = S | **proved in the paper** — Remark 3.8's signed relabelling |
| CD(M(O)) ≅ CD(CD(O)) = T | **verified 2026-09-12** — explicit graded isomorphism found by backtracking search over GL(5,2) |
| level 3 (dimension 64) | invariants only — count and full annihilator profile |
| general A | **conjecture** |

The level-2 search also settles the negative direction, which matters just as much:

    T  ->  CD(S′)     GRADED-ISOMORPHIC          (erasure holds)
    T  ->  M(S)       not graded-isomorphic
    M(S) -> M(S′)     not graded-isomorphic      (M does NOT erase)
    Aut(T)            80 graded automorphism sigmas

**M does not erase.** M(S) ≇ M(S′), so the tree is genuinely non-trivial: it is
specifically the *outer* CD that destroys the mirror bit, and the normal form
M^b ∘ CD^a is not a collapse to a single algebra per level.

If it holds, the free monoid {CD, M}\* collapses: any word can be rewritten by
pushing M's outward, and every word reduces to a normal form

    M^b ∘ CD^a    (all M's outermost)

so that at level k — dimension 2^(3+k) above O — there are **at most k + 1**
algebras rather than 2^k.

This is not a new observation so much as the general form of one the paper
already makes. **Remark 3.8 is the k = 2 case based at H**: "the standard double
CD(M(H)) of the quasi-octonions is again S … at dimension 16 the four words in
{CD, M} give exactly three algebras: S (twice), S′, and M(M(H))." *S twice* is
exactly CD∘CD ≅ CD∘M. The paper states it as an aside about one pair; the
relation says it always happens.

## Evidence

Two-term zero divisors and their annihilator-dimension profiles, computed via a
closed form for dim Ann(eᵢ ± eⱼ) (`check15`, and the tower script):

### Level 1 — dimension 16

| word | 2-term ZD | annihilator dims |
|---|---|---|
| CD(O) = S | 84 | {4: 42} |
| M(O) = S′ | **112** | {2: 42, **6: 14**} |

Two classes = k + 1. **This is Theorem 3.6.**

Note the annihilator split: the 14 pairs with 6-dimensional annihilators are
exactly the 14 new to S′, matching Theorem 5.2's "dim 6 when b ∈ C_a" and the
multiplicity-3 set of the incidence result below.

### Level 2 — dimension 32

| word | 2-term ZD | class |
|---|---|---|
| CD·CD(O) = T | 3036→ **588** | CD² |
| CD·M(O) = CD(S′) | **588** | **= CD², as predicted** |
| M·CD(O) = M(S) *(mirror trigintaduonions)* | **648** | M·CD |
| M·M(O) = M(S′) | **704** | M² |

Three distinct values = k + 1. CD(S′) matches T on **every** invariant computed:
588 zero divisors, identical annihilator profile {4: 84, 8: 84, 12: 126},
identical basis-hyperplane census (16 S, 1 S′, 14 other), identical associator
census (2184 / 2156 of 4340 independent triples), Der = g₂.

### Level 3 — dimension 64 — all eight words, complete

| leading M's (b) | words | 2-term ZD |
|---|---|---|
| **0** | CD·CD·CD, CD·M·CD, CD·CD·M, CD·M·M | **3036** |
| **1** | M·CD·CD, M·CD·M | **3160** |
| **2** | M·M·CD | **3280** |
| **3** | M·M·M | **3392** |

**Eight words, exactly four classes** — k + 1 = 4, as predicted. Every collapse
agreed on the full annihilator-dimension profile, not merely the count.

And the invariant has a clean description: **the class is determined by the
length of the leading (outermost) run of M's**, which is exactly what the normal
form M^b ∘ CD^a says. The word counts per class — 4, 2, 1, 1 — are the numbers of
length-3 words with exactly b leading M's.

The same pattern at the lower levels:

| level | classes | counts |
|---|---|---|
| k = 1 (dim 16) | 2 | 84, 112 |
| k = 2 (dim 32) | 3 | 588, 648, 704 |
| k = 3 (dim 64) | 4 | 3036, 3160, 3280, 3392 |

Successive differences within a level: 28 at k = 1; 60, 56 at k = 2;
124, 120, 112 at k = 3.

## Bales's proper twists

Every algebra in the tower — O, H, M(H), S, S′, T, M(S), M(S′), **and both split
nodes** — has a **proper twist** in the sense of Bales's Definition 4.1
(arXiv:1107.1375): on F₂ⁿ, where every element is its own inverse,

    w(p,q) w(q,q) = w(p⊕q, q)        and        w(p,p) w(p,q) = w(p, p⊕q).

Verified for all of them. By Bales's Theorems 4.3–4.5 and Corollary 4.11 a proper
twist already gives the unit, positivity, (xy)\* = y\*x\*, and the adjoint identity
⟨xy, z⟩ = ⟨x, z y\*⟩ = ⟨x\* z, y⟩.

**So Proposition 3.2 is a corollary of existing general theory**, not something
needing direct substitution — and the same for the adjoint identity used
throughout §2.2 and §2.4. Worth a citation and a shortened proof; it also makes
clear that none of those properties is where S′ differs from S.

## What does *not* vary

- **Der = g₂ (dimension 14) at every node**, at every dimension, including the
  split nodes. The derivation algebra is blind to the entire tree. The title's
  "G₂-symmetric" is accurate but is not what distinguishes S′ — it is automatic.
- **No basis hyperplane of any 32-dimensional node is a composition algebra
  (0 / 31).** Theorem 6.1's eight octaves are a **dimension-16 phenomenon**. The
  tower does not generalise them.

These two facts matter for the framing question below: the *sharp* results about
S′ are exactly the ones that do not survive going up.

## The dimension-32 hyperplane census

Classifying the 31 basis hyperplanes (each 16-dimensional) by graded isomorphism:

| | S | S′ | other |
|---|---|---|---|
| **T = CD(CD(O))** | **16** | **1** | 14 |
| M(S) | 16 | 8 | 7 |
| CD(S′) | 16 | 1 | 14 |
| **M(S′)** | **0** | **24** | 7 |

The first row independently reproduces **claim (A)** and Cawagas et al. — S
occupies 16 basis hyperplanes of T, S′ = Sγ exactly one — by a different route
(graded isomorphism rather than the composition census).

The last row is its exact mirror: **M(S′) contains no copy of S at all.** The
asymmetry that makes S′ a lone hyperplane of T is inverted one level up.

## The Wilmot incidence result

`check13_wilmot_incidence.py`, all PASS. Wilmot accounts for the sedenions' 84
two-term zero divisors as *12 per quasi-octonion × 7 quasi-octonions*.

**The mechanism holds verbatim in S′.** Both algebras have seven quasi-octonion
basis hyperplanes; each carries exactly **12** zero-divisor index pairs; the
incidence total is **7 × 24 = 168 signed** in both. The counts differ only in
overlap multiplicity:

| | multiplicity profile | union |
|---|---|---|
| S | uniform **2** | 168 / 2 = **84** |
| S′ | **{1: 84, 3: 28}** | 84 + 28 = **112** |

And the split is canonical: the multiplicity-1 pairs are **exactly de Marrais's
42 assessors** (those S′ shares with S); the multiplicity-3 pairs are **exactly
the 14 new to S′** — (i, i+8) and (i, 8) — which is Prop. 5.4's "a hue with its
own ultraviolet, or with the bare ultraviolet ℓ", reached from the other side.

**The local structure is identical; only the global incidence differs.** That is
a sharper statement than 84 vs 112, and it puts S′ inside Wilmot's framework
rather than alongside it.

<!-- UNVERIFIED: Wilmot's "zero divisors occur in multiples of 84" holds for
     T (588 = 7 x 84) but our 64-dimensional count is 3036, which is not a
     multiple of 84 (3036 = 12 x 11 x 23). Our count is of two-term basis
     elements e_i +- e_j that are zero divisors. Wilmot may be counting zero
     divisor *pairs* or restricting to particular silos. Resolve his exact
     definition before asserting any tension. -->

## What the paper is contributing

The paper presents three things:

1. **The mirror double M(A) as a construction**, with the embedding theorem
   M(A) ≅ A + A(ee′) ⊂ CD²(A) — valid for *every* ∗-algebra A (Theorem 3.3).
2. **The dichotomy**: Bales's eight products applied once to O give exactly two
   algebras (Theorem 3.6).
3. **A complete structural determination of S′ = M(O)** — the five-level
   spectrum, S⁶ × S⁷, V₂(R⁷) × S³, Aut = G₂ × Z/2, the non-cocycle χ.

The title and abstract foreground (3). **(1) is the engine** — everything else
is one instance of it — and (2) is the k = 1 case of the erasure relation.

### On following it all the way up

Half right, and the computation says which half. Going up buys a **structure
theorem for the construction**: the erasure relation, the normal form M^b ∘ CD^a,
at most k + 1 algebras per level. That is a genuinely good theorem, it subsumes
Theorem 3.6 and Remark 3.8, and it answers Open Question 2 in a stronger form
than the question asks.

But it will be **coarse**. Der is constant, no composition subalgebras survive
past dimension 16, and there is no exceptional symmetry to exploit above S′. The
higher algebras will be characterised by counts and isomorphism classes, not by
sphere products and Stiefel manifolds. The sharp results are sharp *because* they
live where G₂ and the octonions do.

**Recommendation: two papers.** Keep v1's depth on S′ — a complete determination
of one object is a stronger paper than a partial survey of a family. Add the
erasure relation to v1 as a theorem (it is cheap given Theorem 3.3 and Remark
3.8's proof technique, and it upgrades Remark 3.8 from an aside to a structural
principle), and let the tower be the sequel. The split construction belongs with
the sequel too: split algebras are separated from S′ on invariants that need no
convention-matching (one composition hyperplane instead of eight; indefinite
norm), so they are a parallel branch rather than a complication.

## What would change my mind

- **The erasure relation failing at some level.** It is now confirmed by explicit
  graded isomorphism at k = 2 (over O) and proved in the paper at k = 2 (over H),
  but k = 3 rests on invariants alone — a word that collapses on counts and
  annihilator profiles while being genuinely non-isomorphic would break the normal
  form. The k = 3 search needs GL(6,2), which the current backtracking code will
  not reach without better pruning.
- **A composition subalgebra appearing somewhere above dimension 16.** That would
  mean Theorem 6.1 does generalise and the tower is richer than the counts
  suggest.
