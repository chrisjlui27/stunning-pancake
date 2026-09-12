---
type: synthesis
title: Paper 1 / Paper 2 — scope, contents, and gap analysis
status: draft
updated: 2026-09-12
---

# Two papers: scope and gaps

## Correction first

I earlier reported, as a finding, that "no basis hyperplane of any 32-dimensional
node is a composition algebra (0/31), so the eight-octaves phenomenon is specific
to dimension 16." **That 0/31 is trivial.** By Hurwitz, unital composition
algebras over R have dimension 1, 2, 4 or 8, so a 16-dimensional hyperplane is
never one, for any algebra whatsoever. It was not evidence about the tower.

The meaningful dimension-32 statement is about **8-dimensional** subalgebras —
the 155 three-dimensional F₂-subspaces of F₂⁵, matching Cawagas's 155 subloops of
order 16. Recomputed properly:

| | octonion | quasi-octonion |
|---|---|---|
| **T = CD(CD(O))** | **50** | **105** |
| CD(S′) | 50 | 105 |
| **M(S)** | **64** | **91** |
| M(S′) | 64 | 91 |

The first row is **exactly Cawagas et al.'s published 50 / 105**, independently
reproduced — which validates the method. The 64 / 91 for the mirror nodes is new.
Like the associator census, this invariant sees only the outermost operation: it
does not separate M(S) from M(S′) (the zero-divisor count does).

---

## Paper 1 — *The mirror sedenions*

**Thesis.** There is a second G₂-symmetric doubling of the octonions, and its
structure can be determined completely.

**Scope boundary: dimension 16.** Everything in the paper is about M(O) = S′ and
its 8-dimensional relatives M(H). General statements about M appear only insofar
as they are needed to construct and place S′.

### Contents

| § | Content | Status |
|---|---|---|
| 1 | Introduction, results (A)–(H), relation to literature | revise per ERRATA |
| 2 | Conventions; octonion facts; quadratic algebras | + Bales proper-twist citation |
| 3 | The mirror double; **Thm 3.3** embedding; **Thm 3.6** the dichotomy | + erasure (see below) |
| 4 | **Thm 4.1** the five-level spectrum | done, verified |
| 5 | **Thms 5.1, 5.2, 5.5** zero divisors, annihilators, pair manifold | + incidence result |
| 6 | **Thm 6.1** octaves | done, verified |
| 7 | **Thm 7.1, Props 7.3–7.4** Aut, the orientation bit χ | done, verified |
| 8 | **Thm 8.1** the mirror octonions M(H) | done, verified |
| 9 | Questions | re-point Q2 at paper 2 |
| A | Verification | update for checks 13–20 |

### New material for paper 1

1. **The incidence decomposition** (§5, new proposition). Both S and S′ have seven
   quasi-octonion basis hyperplanes, each carrying exactly 12 zero-divisor index
   pairs, with incidence total 7 × 24 = 168 signed in both. They differ only in
   multiplicity: uniform 2 in S; in S′, the 42 pairs shared with S lie in one
   hyperplane and the 14 new ones lie in three. This places S′ inside Wilmot's
   "12 per quasi-octonion × 7" framework instead of merely contrasting 84 with 112.
2. **Prop 3.2 shortened** to a corollary of Bales's proper-twist theory.
3. **Errata E2–E6**: cite Bales's 2011 catalog for the 32-candidate enumeration,
   add Moreno 2005 and Wilmot 2025, fix the [9] citation details, keep Q2's
   quaternionic-line qualifier explicit.

### The placement decision: where does the erasure theorem go?

**Recommendation: paper 1, as a short subsection of §3 absorbing Remark 3.8.**

For: it is proved *from paper 1's own Theorem 3.3* with no new machinery; it is
about one page; Remark 3.8 already states its k = 2 case over H, so leaving the
general theorem out while keeping the special case as an aside reads oddly; and it
answers the question every reader will have after Theorem 3.3 — *what happens if
you keep going?*

Against: it is the backbone of paper 2, and giving it away weakens the sequel.

I think the "against" is wrong, because paper 2's contribution is the
**classification** (sharpness, invariants, the split interaction), not the
relation. Paper 2 opens by recalling it. **But this is the author's call.**

---

## Paper 2 — *The mirror tower*

**Thesis.** M and CD generate a monoid acting on ∗-algebras which collapses to a
single parameter, and the resulting one-parameter family can be classified.

**Scope boundary: all dimensions, one invariant at a time.** Paper 2 does not
attempt for M(S) what paper 1 does for S′ — there is no G₂-geometry to exploit
above dimension 16. It classifies and counts.

### Contents

| § | Content | Status |
|---|---|---|
| 1 | Two doubling operations; statement of results | — |
| 2 | **The erasure theorem** CD(M(A)) ≅ CD(CD(A)) | **PROVED** |
| 3 | **Normal form** M^b ∘ CD^a; at most k + 1 algebras at level k | **PROVED** (corollary) |
| 4 | **Sharpness**: the k + 1 are pairwise non-isomorphic | **GAP — main theorem** |
| 5 | Zero-divisor counts; the increment formula | **GAP — partially proved** |
| 6 | Invariants along the tower: Der, 8-dim subalgebra census, associator census | computational |
| 7 | The split parameter: permanence and independence | near-proved |
| 8 | Questions: Aut of higher nodes, higher mirrors, M(S) geometry | — |

### The key theorem to aim for

Computed (`check21`, all levels 16 → 128):

> **M(A) has exactly the two-term basis zero divisors of CD(A), plus the pairs
> {(i, i+h)} ∪ {(i, h)} for 1 ≤ i < h, where h = dim A. It loses none.**
> That is **n − 2** additional index pairs, n = 2h = dim M(A).

**Prop. 5.4 of paper 1 is the case A = O** (h = 8, giving the 14 pairs (i, i+8)
and (i, 8)). Verified at dimensions 16, 32, 64, 128 — the new set matches the
prediction exactly and nothing is lost, at every level.

If this is proved, and its analogue for the higher increments
(the b-th mirror adds n − 2^(b+1) pairs), then:

- the closed form **Z(k,b) = Z(k,0) + 2nb − 4(2^b − 1)** follows, and
- **sharpness follows immediately**, since Z is then strictly increasing in b.

So §4 and §5 are one target, not two. **This is where paper 2's effort should go.**

---

## Gap analysis

Difficulty is my estimate; priority is for getting each paper submittable.

### Paper 1

| # | Gap | Difficulty | Priority |
|---|---|---|---|
| ~~1.1~~ | **CLOSED 2026-09-12.** Proved by a count in F₂³: the quasi-octonion hyperplanes of S′ are H_f with f ∈ {1..7} and of S are H_{8+f'}; the multiplicity of a pair (i, q+8) is the number of nonzero f' with f'·i = 0 and f'·q = 0 (resp. = 1), giving 3 or 1 (resp. 0 or 2) according as q ∈ {0,i} or not, and 3×4 = 12 per hyperplane either way. `check24`. | — | done |
| 1.2 | Prop 3.2 as a corollary of Bales's proper twists: need M(A) proper whenever A is, in general (verified case-by-case only) | **Easy** | Medium |
| 1.3 | Erasure placement | decision, not work | — |
| 1.4 | Q1 (metric on P(S′)) stays open | — | — |
| 1.5 | Q2 rephrasing given paper 2 | **Easy** | Medium |
| 1.6 | Appendix A must list checks 13–20 and the two script fixes | **Easy** | High |

**Paper 1 is essentially submittable now.** Every v1 theorem is verified and no
error was found. Gap 1.1 is the only one that could delay it, and it can be
dodged by presenting the incidence result as a computational observation.

### Paper 2

| # | Gap | Difficulty | Priority |
|---|---|---|---|
| ~~2.1~~ | **CLOSED 2026-09-12.** Sharpness follows from Corollary 3 of the increment theorem: Z is an isomorphism invariant and is strictly increasing in b, so the k+1 normal forms are pairwise non-isomorphic and the class count at level k is **exactly** k+1. | — | done |
| ~~2.2~~ | **CLOSED 2026-09-12.** The increment theorem is proved: dim Ann_M = (h−2) − dim Ann_CD on mixed pairs, every mixed pair is a zero divisor of M(A), and Z(M(A)) = 2Z(A) + h(h−1). `papers/mirror-sedenions/INCREMENT-THEOREM.md`, `check23`. | — | done |
| 2.3 | Der = g₂ at every node — computational; Schafer covers the CD spine only | **Medium** | High |
| 2.4 | split S ≇ split mirror — computational (GL(4,2) search). The χ non-cocycle argument should port verbatim to ε = −1 | **Easy** | Medium |
| 2.5 | Split permanence — signature is an isomorphism invariant and is inherited; essentially proved, needs writing | **Easy** | High |
| 2.6 | 8-dim subalgebra census (50/105 vs 64/91) and its dependence on the outermost operation only — computational | **Medium** | Medium |
| 2.7 | ~~Content risk: all counts.~~ **Substantially addressed.** The increment theorem is a structural result about annihilators, not a count: it gives an exact duality dim Ann_M = (h−2) − dim Ann_CD valid at every level, recovers Prop. 5.4 and the 2/6 stratification of Thm 5.2 as the case A = O, and exposes an asymmetry (M is uniform, CD is not). A zero-divisor *manifold* for M(S) is still absent, but is no longer needed to carry the paper. | Medium | Medium |
| 2.8 | Aut of higher nodes unknown (Aut(T): 80 graded σ's computed, full Aut not) | **Hard** | Low |

**Paper 2 is now ready to draft.** The increment theorem went through, so both
blocking gaps are closed and the content risk is substantially answered. The
decision is therefore **two papers**, not one.

---

## Status 2026-09-12

Steps 1 and 2 are **done**: the increment theorem is proved in full, with every
lemma machine-verified on six bases, and sharpness follows as a corollary. The
remaining work is step 3 (the incidence decomposition, optional for paper 1) and
the drafting itself.

**Decision: two papers.**
