---
type: note
date: 2026-09-12
topic: Wilmot incidence result, the {CD,M} tree, and what the paper contributes
status: processed
---

# Two computations and a framing question

## 1. The 84 / 112 question — resolved, and it is a real result

**Wilmot's mechanism holds verbatim in S′. Only the incidence multiplicity changes.**

Wilmot accounts for the sedenions' 84 two-term zero divisors as *12 per
quasi-octonion subalgebra × 7 quasi-octonion subalgebras*. Tested in both
(`check13_wilmot_incidence.py`, all PASS):

| | S | S′ |
|---|---|---|
| quasi-octonion basis hyperplanes | 7 | 7 |
| zero-divisor index pairs in **each** | **12** | **12** |
| incidence total (signed) | **7 × 24 = 168** | **7 × 24 = 168** |
| multiplicity profile | **uniform 2** | **{1: 84, 3: 28}** |
| union | 168 / 2 = **84** | 84 + 28 = **112** |

So the "12 per quasi-octonion, seven copies" count is **identical** in the two
algebras, as is the incidence total. The 84 vs 112 difference is entirely in how
the seven quasi-octonion hyperplanes overlap: in S every two-term zero divisor
lies in exactly **two** of them; in S′ the set splits.

### And the split is canonical

| S′'s 56 index pairs | multiplicity | what they are |
|---|---|---|
| **42** | **1** | exactly de Marrais's assessors — the pairs that are *also* zero divisors in S |
| **14** | **3** | exactly (i, i+8) and (i, 8) for i = 1…7 — the pairs new to S′ |

The 14 are precisely Prop. 5.4's "a hue with its own ultraviolet, or with the
bare ultraviolet ℓ". So the colour vocabulary and Wilmot's incidence count are
picking out the same set from two directions.

**This is a v2 remark worth writing.** It ties S′'s 112 to an existing framework
instead of leaving it as a bare comparison against de Marrais's 84, and it says
something sharper than either count alone: *the local structure is identical and
the global incidence is not*.

## 2. The {CD, M} tree

`check15_tree_invariants.py`, `check14_tree_hyperplanes.py`.

### Dimension 16

| | Der | composition hyperplanes | 2-term ZD | pos. def. |
|---|---|---|---|---|
| CD(O) = S | 14 | 8/15 | 84 | yes |
| M(O) = S′ | 14 | 8/15 | **112** | yes |
| CD₋(O) = split S | 14 | **1/15** | 112 | **no** |
| M₋(O) = split mirror | 14 | **1/15** | 112 | **no** |

The split algebras also have 112 two-term zero divisors — but they are separated
from S′ on two invariants that need no convention-matching: **one** composition
hyperplane instead of eight, and an **indefinite** norm.

### Dimension 32 — the basis-hyperplane census

Each of the 31 basis hyperplanes is 16-dimensional; classify by graded isomorphism:

| | S | S′ | other |
|---|---|---|---|
| **T = CD(CD(O))** | **16** | **1** | 14 |
| M(S) = M(CD(O)) | 16 | 8 | 7 |
| CD(S′) = CD(M(O)) | 16 | 1 | 14 |
| **M(S′) = M(M(O))** | **0** | **24** | 7 |

**The first row independently reproduces claim (A) and Cawagas et al.** — inside
T, S occupies 16 basis hyperplanes and S′ = Sγ exactly one. That was previously
verified via the composition-hyperplane census; this is an independent route,
by graded isomorphism against S and S′ directly.

**The last row is its exact mirror image.** M(S′) contains *no copy of S at all*
and 24 copies of S′. The asymmetry that makes S′ a lone hyperplane of T is
reversed one level up.

All four length-2 words give **pairwise non-isomorphic** algebras: T and CD(S′)
share the hyperplane profile (16, 1, 14) and the two-term count (588) but are
separated by annihilator dimension on the S-locus (4 vs 0). M(S) has 648 and
M(S′) has 704.

### What does not vary

**Der = g₂ (dimension 14) at every node, including the split ones.** The
derivation algebra is blind to the whole tree — which is why the zero-divisor
geometry and Aut have to do all the separating work, exactly as in Table 1.

**No basis hyperplane of any 32-dimensional node is a composition algebra
(0/31).** The "eight octaves" phenomenon is specific to dimension 16. Whatever
the M-tower does higher up, it is not more of Theorem 6.1.

## 3. The framing question — what is the paper contributing?

Recorded in `synthesis/mirror-sedenions.md` §"What the contribution is".
