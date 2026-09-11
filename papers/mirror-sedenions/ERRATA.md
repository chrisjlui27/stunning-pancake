---
type: errata
paper: mirror-sedenions-v1.pdf
compiled: 2026-09-11
basis: nine sources read (papers/library/), plus re-running the products
---

# Errata and additions for v2

No LaTeX source in the vault, so this is a change list against the v1 PDF, keyed
by section. Each item states the current text, the replacement, and why.

**Nothing here affects a theorem.** Every mathematical statement checked so far
reproduces. The items are citation accuracy, attribution, and one qualifier.

---

## E1 — §3.2: the four transposed products carry reversed subscripts

**Severity: real, and the one a referee would catch.**

### Current text (§3.2)

    P0 = (ca − b̄d, dā + bc),      P0ᵀ = (ca − bd̄, ad + c̄b),
    P1 = (ca − db̄, ād + cb),      P1ᵀ = (ca − d̄b, da + bc̄),
    P2 = (ac − b̄d, dā + bc),      P2ᵀ = (ac − bd̄, ad + c̄b),
    P3 = (ac − db̄, ād + cb),      P3ᵀ = (ac − d̄b, da + bc̄).

### What is wrong

The unprimed P0–P3 **match Bales exactly** — verified formula by formula against
arXiv:1707.07318. The eight as a set also match Bales's eight exactly.

But the **transposes are subscript-reversed**: the paper's Pᵢᵀ is Bales's P₍₃₋ᵢ₎ᵀ.

| paper | is actually Bales's | |
|---|---|---|
| P0ᵀ | **P3ᵀ** | |
| P1ᵀ | **P2ᵀ** | = formula (2), the mirror |
| P2ᵀ | **P1ᵀ** | |
| P3ᵀ | **P0ᵀ** | = formula (1), the standard |

Bales defines the transpose by Pᵀ(x, y) = P(y, x). Under that definition the
paper's "P0ᵀ" is the transpose of **P3**, not of P0 — so the superscript does not
mean what the notation says, and a reader going to [2] to look up P1ᵀ will find a
different formula from the one the paper calls P1ᵀ.

### Consequences, and what survives

**Theorem 3.6 is correct under either labelling**, by a lucky symmetry: the
subscript reversal maps {0,3} → {3,0} and {1,2} → {2,1}, so the *sets*
{P0ᵀ, P3ᵀ} and {P1ᵀ, P2ᵀ} are preserved. The class statement — S for
(P0, P3, P0ᵀ, P3ᵀ), S′ for (P1, P2, P1ᵀ, P2ᵀ) — reproduces exactly under both.
Verified computationally in both labellings. **No change needed to Theorem 3.6.**

What does not survive is the identification in §1.

### Fix

Preferred — relabel §3.2 to match [2], swapping the two transpose pairs:

    P0ᵀ = (ac − d̄b, da + bc̄),     P1ᵀ = (ac − bd̄, ad + c̄b),
    P2ᵀ = (ca − d̄b, da + bc̄),     P3ᵀ = (ca − bd̄, ad + c̄b).

Then in §1 "Relation to the literature":

> **current:** The formula (2) is Bales's product P₁ᵀ [2]
> **replace with:** The formula (2) is Bales's product P₂ᵀ [2]

and in Remark 3.8, "For P₁ᵀ this is not the mirror sedenions" → "For P₂ᵀ …",
and likewise "the uniform P₁ᵀ tower" → "the uniform P₂ᵀ tower" (two occurrences
in §1 and Remark 3.8).

Alternative — keep the current subscripts but stop attributing them to Bales:
state the eight formulas as the paper's own enumeration, and in §1 identify (2)
by its formula rather than by a Bales label. Less good: it loses the link to [2].

<!-- UNVERIFIED: this comparison is against arXiv:1707.07318v4 (2023), titled
     "The Cayley-Dickson doubling products". Reference [2] cites Adv. Appl.
     Clifford Algebras 26 (2016) 529-551, "The eight Cayley-Dickson doubling
     products" — the title of arXiv v3. The numbering is assumed stable across
     versions. CONFIRM AGAINST THE AACA TEXT before publishing this correction;
     if AACA numbers the transposes as the paper does, the erratum is void and
     the right fix is a footnote naming which version's numbering is in use. -->

---

## E2 — Add Bales's 2011 catalog for the thirty-two candidates

**Severity: an addition, not a correction.**

I earlier characterised this as the paper claiming the census as its own. **That
was wrong** — §3.2 says "Bales [2] shows that among thirty-two candidate doubling
formulas … exactly eight produce …", and Appendix A says "the thirty-two Bales
candidates". The attribution is already there and is correct.

The refinement is *which* Bales paper. The 32 / 24 / 8 result is the explicit
subject of a different, uncited paper:

> J. W. Bales, *A catalog of Cayley–Dickson-like products*, arXiv:1107.1301.
> "A catalog of all **32** Cayley-Dickson-like doubling products on ordered pairs
> (a,b)·(c,d) for which (1,0) is the left and right identity and for which
> x·x\* = x\*·x = ‖x‖² … Only **eight** of these are true Cayley-Dickson doubling
> products, since **24** of them do not satisfy the **quaternion properties**."

That is exactly the paper's §3.2 setup, including the quaternion-triple condition
and the count of rejects behind Appendix A's "twenty-four rejected formulas".

**Suggested:** cite arXiv:1107.1301 alongside [2] at the §3.2 sentence, as the
source of the 32-candidate enumeration specifically. Worth checking whether the
AACA paper also contains the census; if it does, a "see also" is enough.

Its Table 11 also gives the eight in a third numbering, in which the standard
product is **P31** and the mirror is **P27** — verified bit-for-bit against our
`S` and `Sm`. Classifying all eight by graded isomorphism gives S-class
{P0, P7, P24, P31} and S′-class {P3, P4, P27, P28}, falling into four `ac`/`ca`
partner pairs each split one to each class — Theorem 3.6's stated mechanism,
confirmed in a third independent numbering. Could be a one-line remark.

---

## E3 — §9 Question 2: keep the quaternionic-line qualifier explicit

**Severity: the statement is currently correct; the risk is in restatement.**

Question 2 currently reads that the census "over all sign functions on F₂⁴ **with
quaternionic lines**" indicates S and S′ are the only two with eight octaves and
14-dimensional derivation algebra.

**The qualifier is load-bearing and the claim is false without it.** Four further
Bales candidates — in our (f,g) indexing (1,3), (2,2), (5,1), (6,0) — have eight
octaves **and** dim Der = 14, and are neither S nor S′ (their annihilator
dimensions are 1). They are excluded precisely by the quaternionic-line
condition, with 28 failing ordered basis pairs each. Exactly 8 of the 32 have
zero failures, which is what makes Appendix A's "twenty-four rejected".

**Suggested:** add a parenthetical making the necessity visible, e.g. "(the
quaternionic-line condition is essential here: four further candidates have eight
octaves and dim Der = 14 without being S or S′)".

---

## E4 — Add Moreno 2005

G. Moreno, *Constructing zero divisors in the higher dimensional Cayley–Dickson
algebras*, arXiv:math/0512517 (2005). Explicitly a sequel to [18]; gives methods
to construct zero divisors in Aₙ for n > 4 and **relates the zero-divisor set to
Stiefel manifolds** — the apparatus Theorem 5.5 uses.

Citing [18] but not this is a conspicuous gap, and it is the natural entry point
for **Open Question 3** (higher mirrors, M(S) and M(S′) in the 64-dimensional
algebra). Suggested placement: §1 "Relation to the literature" and Question 3.

---

## E5 — Add Wilmot 2025

G. P. Wilmot, *Structure of the Cayley–Dickson algebras*, arXiv:2505.11747.

Not a priority threat — he uses the standard product throughout and does not
consider doubling variants — but squarely adjacent, and two points connect:

- His "**eight octonion and seven power-associative subalgebras of sedenions**,
  uniquely derived up to representation" is **Theorem 6.1's split** in different
  vocabulary; his power-associative subalgebras are the quasi-octonions M(H).
- He reduces the sedenions' zero divisors **84 → 7 primary pairs**, attributing
  the factor of seven to those seven subalgebras. S′ has **112 = 16 × 7** against
  S's **84 = 12 × 7**, and seven quasi-octonion hyperplanes of its own, so the
  mechanism should carry over with 16 modes rather than 12.

**Optional remark for v2**, if it checks out: it would tie the 112 count to an
existing framework instead of leaving it as a bare comparison against de Marrais.
Worth doing the computation before committing to a sentence.

Also worth one line: **split sedenions are not the mirror**. Wilmot analyses
them, and they are the obvious neighbouring variant, so a reader may wonder.
Verified: no graded isomorphism to S or S′, and their norm is indefinite where
S′'s is positive definite.

---

## E6 — Citation details for [9] (Cawagas et al.)

The priority check **passes** — see `sources/cawagas-et-al-2009.md`. Two details:

1. Their bullet list labels the algebra **Sδ_L(#4)** while their isomorphy
   classes and Table 6 call it **Sγ_L(#4)**. A typo in their paper; cite the γ
   form, which is what the mirror paper already uses.
2. Their uniqueness is at the level of **loops**; the mirror paper's claim (A) is
   at the level of **algebras**. One clause acknowledging the translation would
   pre-empt the question.

Supporting quote for the "prove nothing further" characterisation, if a referee
presses — from under their Table 6:

> "Note that the loop Sγ_L has the same subloop composition as S_L but analysis
> shows that they are not isomorphic."

That, plus the [8 + 7] composition type, is the whole of what they establish
about it.

---

## Not errata — checked and clean

- **Theorem 3.6's class assignment** — reproduces in three independent numberings
  (the paper's, Bales arXiv:1707.07318's, Bales catalog's).
- **Theorem 4.1** — symbolic characteristic polynomial matches exactly; machine
  precision over 2000 random points after fixing a τ typo in `check7_misc.py`.
- **Table 1's alternative-element rows** — confirmed after fixing a wrong
  assertion in `check9_final.py` (ℓ is alternative in *both* algebras; the
  separating element is u + uℓ).
- **Claim (A), the Sγ identification** — our own hyperplane census of T gives
  class sizes 16 / 7 / 7 / 1 matching Cawagas exactly, with the singleton on
  basis O + O(ee′).
- **Aryapoor–Bäck–Pautrel 2026** does not pre-empt Theorem 3.6: they vary the
  scalar µ with the product fixed, and their isomorphisms extend the identity
  where Theorem 3.6's extend conjugation.
