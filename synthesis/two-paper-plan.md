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
| **1.1** | The incidence decomposition is **computational only**. Needs proof of: 12 pairs per quasi-octonion hyperplane in both; multiplicity 2 in S; multiplicity {1, 3} split in S′. | **Medium** — likely follows from Thm 8.1(2) plus Thm 6.1's hyperplane description and Prop 5.4 | High if included; or drop to a remark with "verified computationally" |
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
| **2.1** | **Sharpness unproved** — that M^b CD^a, b = 0…k, are pairwise non-isomorphic. Verified to k = 4 on counts; k = 2 by explicit search. | **Hard alone, easy via 2.2** | **Blocking** |
| **2.2** | **The increment theorem unproved.** First mirror: verified exactly to n = 128, with the explicit new-pair set. Higher b: 14 data points, no structural statement yet. | **Medium (b=0→1), Hard (general b)** | **Blocking — do this first** |
| 2.3 | Der = g₂ at every node — computational; Schafer covers the CD spine only | **Medium** | High |
| 2.4 | split S ≇ split mirror — computational (GL(4,2) search). The χ non-cocycle argument should port verbatim to ε = −1 | **Easy** | Medium |
| 2.5 | Split permanence — signature is an isomorphism invariant and is inherited; essentially proved, needs writing | **Easy** | High |
| 2.6 | 8-dim subalgebra census (50/105 vs 64/91) and its dependence on the outermost operation only — computational | **Medium** | Medium |
| **2.7** | **Content risk: paper 2 is all counts.** There is no structural result about M(S) analogous to Thm 5.1/5.5 — no zero-divisor manifold, no Aut, no annihilator description. | **Hard** | **High — this is what makes it a paper rather than a table** |
| 2.8 | Aut of higher nodes unknown (Aut(T): 80 graded σ's computed, full Aut not) | **Hard** | Low |

**Paper 2 is not ready.** Two blocking gaps (2.1/2.2, which are one problem) and
one content risk (2.7). The honest position: paper 2 is a good paper *if* the
increment theorem goes through, and a table *if* it does not.

---

## Recommended order of work

1. **Prove the increment theorem for b = 0 → 1** — M(A) = CD(A)'s zero divisors
   plus {(i, i+h)} ∪ {(i, h)}. The set is explicit and the pattern is exact at
   four dimensions; this is the most likely thing to fall.
2. **Try to extend to general b.** If it works, 2.1, 2.2 and most of §5 close at
   once and paper 2 has a spine.
3. **Prove the incidence decomposition (1.1)** — needed by paper 1 and probably
   reusable in paper 2's §6.
4. Write **paper 1** (it is ready modulo 1.1 and 1.6).
5. Attack **2.7** — find one structural statement about M(S), or accept that
   paper 2 is a classification paper and frame it that way honestly.
6. Write **paper 2**.

## What would change my mind about the split

If the increment theorem does **not** generalise, paper 2 as scoped is thin, and
the better move is a single longer paper: paper 1 plus a final section giving the
erasure theorem, the normal form, and the tower counts as a coda, with sharpness
stated as verified-to-k=4. That is an honest and still-substantial paper, and
avoids publishing a classification whose main theorem is empirical.
