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
reproduces. After E1's retraction there is **no correction to the paper at all** —
what remains is four suggested additions and one qualifier to keep explicit.

---

## E1 — RETRACTED. The paper is correct; the error was mine.

**Status: withdrawn 2026-09-11, same day, after reading arXiv:1707.07318v3.**

I claimed §3.2's four transposed products carried reversed subscripts, and that
§1's "formula (2) is Bales's product P₁ᵀ" named the wrong member. **Both claims
were false.** Bales prints all eight explicitly on p. 8 of v3 (and identically in
v4):

    P0ᵀ : (a,b)(c,d) = (ca − bd*, ad + c*b)
    P1ᵀ : (a,b)(c,d) = (ca − d*b, da + bc*)      ← formula (2), the mirror
    P2ᵀ : (a,b)(c,d) = (ac − bd*, ad + c*b)
    P3ᵀ : (a,b)(c,d) = (ac − d*b, da + bc*)      ← formula (1), the standard

This matches §3.2 **label for label**, and confirms §1: formula (2) **is** Bales's
P₁ᵀ. Verified computationally against the printed formulas — Bales's P1ᵀ is
identical to our `Sm`, his P3ᵀ identical to our `S`.

### How I got it wrong

Two compounding mistakes, both mine:

1. **I derived what was printed.** My grep for the product list required
   `(a, b)(c, d)` on a single line. PDF extraction splits the transpose labels
   across lines as `P ⊤` / `0 :`, so the pattern matched P0–P3 and silently
   missed all four transposes. I did not notice the list was half-length.
2. **I then reconstructed them from an assumption.** I took Pᵢᵀ to mean the
   argument-swap P(y, x). It does not. Bales writes: *"The 'transpose' symbol is
   used for the second set of four doubling products since … the corresponding
   product matrices of unit vectors are transposes of each other."* Under
   argument-swap the pairing is actually Pᵢᵀ = swap(P₍₃₋ᵢ₎) — which is precisely
   the "reversal" I mistook for the paper's error.

So the discrepancy was between the paper and **my reconstruction**, never between
the paper and Bales.

### Lesson recorded

A missing-data failure that looked like a finding. The check that would have
caught it immediately: **the extracted list had four entries where the text says
eight.** Any enumeration taken from a PDF should be counted against its stated
size before anything is built on it. Added to `CLAUDE.md`.

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
