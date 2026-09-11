---
type: note
date: 2026-09-11
topic: First literature pass — nine papers read
status: processed
---

# Literature pass — nine papers

Nine PDFs uploaded by hand (the container cannot reach any scholarly host).
All nine now in `papers/library/`. Headline: **both open threads close, the
novelty claim survives, and one citation erratum was found.**

## Verdicts

| Source | Prior risk | Verdict |
|---|---|---|
| Aryapoor–Bäck–Pautrel 2026 | **High** | **No threat.** Different axis entirely. |
| Bales 2011 catalog | Moderate | **No threat to novelty — but must be cited.** It is the source of the 32/24/8 census. |
| Bales 2017 doubling products | Low (editorial) | **Erratum found.** (2) is P₂ᵀ, not P₁ᵀ. |
| Bales 2016 alternate product | Low | **No threat.** "Equivalent" = isomorphic, as suspected. |
| Wilmot 2025 | Low | **No threat confirmed.** Uses the standard product throughout. |
| Cawagas et al. 2009 | Priority check | **Passes.** Explicit and decisive. |
| Moreno 2005 | Low | Not a threat; **should be cited** for Question 3. |
| Bales 2011 twisted / 2016 periodicity | Low | Background. Not read in depth. |

## 1. Cawagas priority check — PASSES

The decisive text is Table 6 and the sentence under it:

> "From this we find that the loops S_L, Sα_L, and Sβ_L differ in their maximal
> subloop compositions. Hence they are not isomorphic. **Note that the loop Sγ_L
> has the same subloop composition as S_L but analysis shows that they are not
> isomorphic.** Therefore all of these four subloops are distinct."

Their four isomorphy classes of the 31 sedenion-type subloops have sizes
**16, 7, 7, 1** — matching our own check6 run exactly. Sγ_L is the singleton,
with basis ±{0,…,7, 24,…,31} = O + O·e₂₄ = **O + O(ee′)**, exactly claim (A).
Their composition types: S_L and Sγ_L are both **[8 octonion + 7 quasi-octonion]**;
Sα is [2+13], Sβ is [0+15].

So: Sγ is recorded, its subloop composition is recorded, and its
non-isomorphism to S is asserted on the strength of a computer isomorphism test
("analysis shows"). **Nothing about zero divisors, annihilators, spectrum,
automorphisms, subalgebra geometry, or any construction.** "Noticed but not
studied" is accurate and can stand.

Two details for citation accuracy:
- Their bullet list labels it **Sδ_L(#4)** while the isomorphy classes and Table 6
  call it **Sγ_L(#4)** — a typo in their paper. Cite the γ form.
- Their uniqueness is at the level of **loops**; ours is at the level of
  **algebras**. Worth one sentence when citing.

## 2. Wilmot — low risk confirmed

**G. P. Wilmot, arXiv:2505.11747v3 (Feb 2026), University of Adelaide.**

He uses the **standard** product throughout — his equation (1) is
(a,b)(c,d) = (ac − εd\*b, da + bc\*). In 25 pages there are two occurrences total
of any of "doubling product", "transpose", "mirror", "variant", "Bales". He does
not consider alternative doubling products, so the novelty claim is untouched.

But he is very much on the same territory and **should be cited**:

- "The graded notation allows **the eight octonion and seven power-associative
  subalgebras of sedenions** to be uniquely derived, up to representation."
  That is Theorem 6.1's split, in different vocabulary — his "power-associative
  subalgebras" are the quasi-octonions M(H).
- "Zero divisors occur in **multiples of 84** … reduced to **factors of seven
  primary zero divisor pairs** … due to the power-associative subalgebras being
  embedded into ultracomplex numbers **in multiples of seven**."
- He analyses **split sedenions** and gives mappings between three of them.

### The split-sedenion question, settled

Split sedenions are the neighbouring variant axis (ε = −1 rather than reversing
ac ↔ ca), so it was worth ruling out. Done computationally:

| algebra | graded-iso to S | to S′ | x·x̄ |
|---|---|---|---|
| split S | no | no | **indefinite** |
| mirror split | no | no | **indefinite** |
| S, S′ | — | — | positive definite |

S′ has a positive-definite norm; the split algebras have isotropic vectors. Not
isomorphic, on an invariant that needs no convention-matching.

### The 84 / 112 question, sharpened

Wilmot's reduction is **84 → 7** for the sedenions. S′ has **112 = 16 × 7**
two-term zero divisors, against S's **84 = 12 × 7**. Both multiples of seven, and
Wilmot attributes the factor of seven to the **seven** power-associative
subalgebras — which S′ also has (Theorem 6.1: seven quasi-octonion hyperplanes).
So the mechanism he identifies looks like it should apply to S′ too, with 16
rather than 12 modes. **This is a concrete, checkable v2 remark**, and it would
connect the mirror to his framework rather than leaving the two counts unrelated.

## 3. Aryapoor–Bäck–Pautrel — no threat, and the reason is clean

Their Cayley double has a **fixed** product,

    (u,v)(x,y) = (ux + µy*v, vx* + yu)

parametrised by the scalar µ. Theorem 2 classifies A-isomorphisms
**Cay(A,µ₁) → Cay(A,µ₂)** — same formula, different µ — and finds they are
exactly ϕ(x,y) = (x + cy\*, dy) with c ∈ N(A) a skew ∗-element, d ∈ N_l(A).

Two independent reasons this does not touch Theorem 3.6:

1. **They vary µ; the mirror varies the product itself.** S′ is not Cay(O,µ) for
   any µ — it is a different formula, not a rescaled one.
2. **Their isomorphisms extend the identity on A.** Theorem 3.6's isomorphisms
   have the form a + bℓ ↦ ā + (±b̄)ℓ, extending **conjugation**. Excluded from
   their scope by hypothesis.

For A = O the classification is nearly vacuous anyway: N(O) = R, whose only skew
element is 0, so c = 0; d ∈ N_l(O) = R; and condition (19) reduces to µ₁ = µ₂d².
Cite as adjacent work if at all; it does not need defending against.

## 4. Bales's catalog — the real find

**arXiv:1107.1301v5, *A catalog of Cayley–Dickson-like products*.** Abstract:

> "A catalog of all **32** Cayley-Dickson-like doubling products on ordered pairs
> (a,b)·(c,d) for which (1,0) is the left and right identity and for which
> x·x\* = x\*·x = ‖x‖² … Only **eight** of these are true Cayley-Dickson doubling
> products, since **24** of them do not satisfy the **quaternion properties**."

That is precisely the census the paper's Appendix A and our check5/check12
reproduce — the 32 candidates, the 24 rejected by the quaternion-line condition,
the 8 survivors. **This paper is not cited and probably should be.**

*Correction to my first pass:* I initially wrote that the paper presents the
census as its own computation. **Wrong** — §3.2 attributes it ("Bales [2] shows
that among thirty-two candidate doubling formulas…") and Appendix A says "the
thirty-two Bales candidates". The attribution is there. The open question is only
whether [2] (AACA 2016) carries the census, or whether this 2011 catalog is the
right citation for it.

Bales's Table 11 lists the eight explicitly, and two of them are the paper's own
formulas verbatim:

    P31 : (a,b)(c,d) = (ac − d*b, da + bc*)     = the paper's (1), standard
    P27 : (a,b)(c,d) = (ca − d*b, da + bc*)     = the paper's (2), MIRROR

Verified: our `S` is bit-for-bit `P31`, our `Sm` is bit-for-bit `P27`.

Classifying all eight by graded isomorphism:

| class | Bales catalog numbering |
|---|---|
| **S** | P0, P7, P24, P31 |
| **S′** | P3, P4, P27, P28 |

and the eight fall into four `ac`/`ca` partner pairs — (P31,P27), (P28,P24),
(P4,P0), (P7,P3) — **each pair split one to each class**. That is exactly
Theorem 3.6's mechanism ("the two classes are exchanged by reversing the first
product ac ↔ ca"), now confirmed in Bales's own numbering.

**Does the catalog pre-empt the mirror double?** No. It catalogs *products* and
their Fano-plane twist structure; it does not apply one variant once on top of
standard O, and it does not observe that the eight yield two non-isomorphic
16-dimensional algebras. The construction claim survives. But §1's wording should
acknowledge that the product itself is catalogued there.

## 5. ERRATUM — the wrong Bales product is named

*Correction to my first pass:* I claimed "formula (2) is P₂ᵀ, not P₁ᵀ" before
reading §3.2. The paper prints **its own list** of the eight there, and in that
list P₁ᵀ **is** formula (2) — so §1 is internally consistent. The defect is real
but different.

Comparing the paper's §3.2 list with Bales arXiv:1707.07318 formula by formula:
the **unprimed P0–P3 match exactly**, and the eight match **as a set**, but the
**transposes are subscript-reversed** — the paper's Pᵢᵀ is Bales's P₍₃₋ᵢ₎ᵀ.

| paper | Bales | |
|---|---|---|
| P0ᵀ | P3ᵀ | |
| P1ᵀ | **P2ᵀ** | = formula (2), mirror |
| P2ᵀ | P1ᵀ | |
| P3ᵀ | **P0ᵀ** | = formula (1), standard |

Bales defines Pᵀ(x,y) = P(y,x), so the paper's "P0ᵀ" is the transpose of **P3** —
the superscript does not mean what the notation says, and a reader consulting [2]
for P₁ᵀ finds a different formula.

**Theorem 3.6 survives under either labelling**, by a symmetry: the reversal maps
{0,3} → {3,0} and {1,2} → {2,1}, preserving the sets {P0ᵀ,P3ᵀ} and {P1ᵀ,P2ᵀ}.
Verified computationally in both. Only §1's identifying sentence and Remark 3.8's
two references to "P₁ᵀ" need changing.

<!-- UNVERIFIED: ref [2] is cited as AACA 26 (2016). arXiv:1707.07318v4 is titled
     "The Cayley-Dickson doubling products" (2023); v3 was titled "The eight
     Cayley-Dickson doubling products", matching the AACA title. Numbering is
     assumed stable across versions. Confirm against the AACA text before
     publishing the correction. -->

## 6. Moreno 2005 — should be cited

*Constructing zero divisors in the higher dimensional Cayley–Dickson algebras.*
Gives methods to construct zero divisors in A_n for n > 4 and **relates the set
of zero divisors to Stiefel manifolds** — the same apparatus Theorem 5.5 uses.
Explicitly a sequel to [18]. Citing [18] but not this one is an odd gap, and it
is the natural starting point for Open Question 3 (higher mirrors).

## To follow up

- [ ] Apply the P₁ᵀ → P₂ᵀ erratum, after checking the AACA text.
- [ ] Cite Bales 2011 catalog for the 32/24/8 census; reword §1 to acknowledge
      that the mirror product is catalogued as P27 there.
- [ ] Cite Wilmot; consider the 84 → 7 / 112 = 16 × 7 remark.
- [ ] Cite Moreno 2005 in Question 3.
- [ ] Read Bales 2011 twisted + 2016 periodicity properly for §7.
