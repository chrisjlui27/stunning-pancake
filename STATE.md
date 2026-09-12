# State

> The handoff file. Every session reads this first and updates it before ending.
> Keep it short — if a section is growing past a screen, the detail belongs in
> `synthesis/` and this file should link to it instead.

**Last updated:** 2026-09-12 — increment theorem PROVED; all gaps closed; two papers drafted.

## Subject

**Hypercomplex algebras** — Cayley–Dickson constructions, octonions and beyond,
zero-divisor geometry, automorphism and derivation theory.

## Current focus

`papers/mirror-sedenions/` — *The mirror sedenions: a second G2-symmetric
doubling of the octonions and the geometry of its zero divisors*, working draft
v1 (September 2026). Result summary and comparison table in
`synthesis/mirror-sedenions.md`.

The mathematics is machine-verified — all twelve checks re-executed 2026-09-11,
every claim reproduced, **no mathematical error found**
(`papers/mirror-sedenions/VERIFICATION.md`). Two check-script bugs found and
fixed; the scripts now run clean.

**The literature position is not verified.** That asymmetry is the thing to fix
next: the contribution depends on it, though the mathematics does not.

## Open threads

| Thread | Status | Next step |
|---|---|---|
| **Apply the v2 additions** | ready | `papers/mirror-sedenions/ERRATA.md`. **No corrections to the paper** — E1 was retracted after reading Bales v3, which prints all eight products and matches §3.2 label for label. Four citation additions plus one qualifier to keep explicit. |
| ~~Aryapoor–Bäck–Pautrel~~ | **closed** | Read. No threat — they vary the scalar µ, not the product, and their isomorphisms extend the identity where Theorem 3.6's extend conjugation. |
| ~~Bales 2011 catalog~~ | **closed, with an action** | Read. No threat to novelty, but it *is* the source of the 32/24/8 census the paper presents as its own. Must cite. |
| ~~Wilmot gap~~ | **closed** | Read. Uses the standard product throughout. Split sedenions also ruled out computationally. Cite for the 8+7 subalgebra split and the 84→7 reduction. |
| **Own notes not in vault** | open | Import JS-1–41 and JS-LANDSCAPE-II, plus the sign-function census code. Reference [16] is load-bearing and currently unreachable. `sources/lui-js-notes.md` |
| ~~Cawagas priority check~~ | **PASSES** | Read. Their Table 6 records Sγ's existence, its [8+7] composition, and its non-isomorphism to S from a computer test — and nothing else. "Noticed but not studied" is accurate. Class sizes 16/7/7/1 match our check6 run exactly. |
| **84 / 112 remark** | new, promising | Wilmot reduces S's 84 zero divisors to 7 primary pairs via the seven power-associative subalgebras. S′ has 112 = 16×7 and seven quasi-octonion hyperplanes. Mechanism should carry over with 16 modes. Checkable. |
| Read Bales twisted + periodicity | open, low | In `papers/library/`, not yet opened. Background for §7. |
| **Bibliography is second-hand** | open, ongoing | All 23 `sources/` files are `read: not-read` — claims are what the paper cites them for, not what the sources say. Promote as read. |
| **v2 fix: Q2 qualifier** | ready to apply | Eight octaves + dim Der = 14 does *not* characterise S and S′ — four other Bales products share both. The quaternionic-line qualifier is load-bearing and must stay explicit when Q2 is restated. Verified. |
| Open Question 2 (orientation tree) | open | Most tractable of the four: a finite classification, not a geometry problem. Needs the census code from [16]. |
| Open Question 1 (metric on P(S′)) | open | Reggiani's treatment of P(S) is the template. |

## Decisions made

- **2026-09-10** — Vault lives in git rather than in assistant memory, so it is
  readable from Claude Code, Cowork, and chat alike, and is versioned.
- **2026-09-11** — `sources/` files carry a **`read:`** field. A claim recorded
  from a citation is not a claim from the source. Nothing gets promoted to
  settled without an actual reading.
- **2026-09-11** — Computed claims get **run**, not trusted. Verification output
  is committed with the date and environment. This paid for itself immediately:
  both discrepancies found were script bugs that a reading pass would have missed,
  and one of them (`check7`'s τ) was invisible at every sample point check6 used.

## Papers

- **Paper 1** `papers/mirror-sedenions/` — v1 plus `REVISION-v2.md` (six revisions
  R1–R6) and `v2-insertions.tex` (the erasure theorem and the incidence
  proposition, LaTeX-ready). No theorem of v1 changes.
- **Paper 2** `papers/mirror-tower/mirror-tower.tex` — complete draft.
  Erasure, normal form, increment theorem, sharpness, split permanence,
  invariants, three questions.

## New results this session (2026-09-12)

- **Theorem (erasure): CD(M(A)) ≅ CD(CD(A)) for every ∗-algebra A.** Proved from
  Theorem 3.3; `papers/mirror-sedenions/ERASURE-PROOF.md`, machine-verified
  step by step. Corollary: every {CD, M} word reduces to M^b ∘ CD^a, so at most
  k + 1 algebras at level k. Generalises Theorem 3.6 (k=1) and Remark 3.8 (k=2).
- **Wilmot's 12-per-quasi-octonion count holds verbatim in S′**; the 84 vs 112
  difference is purely incidence multiplicity (uniform 2 vs {1: 84, 3: 28}), and
  the split is canonical — the 42 assessors versus the 14 new pairs.
- **Split is permanent**: the norm signature is inherited by every descendant, so
  no doubling repairs ε = −1. The two parameters are independent.
- **Theorem (increment): for A of dimension h with proper twist,
  dim Ann_{M(A)} = (h−2) − dim Ann_{CD(A)} on mixed basis pairs and agrees with
  CD(A) elsewhere; every mixed pair is a zero divisor of M(A); and
  Z(M(A)) = 2Z(A) + h(h−1).** Recovers Prop. 5.4 and the 2/6 stratification of
  Thm 5.2 as the case A = O. `INCREMENT-THEOREM.md`, `check23`.
- **Sharpness (corollary): the class count at level k is exactly k+1**, since Z
  is strictly increasing in the number of leading mirrors.
- **The incidence decomposition is proved** by a count in F₂³ (`check24`), closing
  the last paper-1 gap.
- **Asymmetry:** Z(M(A)) = 2Z(A) + h(h−1) holds universally; the CD analogue
  Z(CD(A)) = 2Z(A) + (h−1)(h−2) holds on the CD spine but fails for mirror bases
  (58 exceptions rather than 30 for A = S′).

## Known gaps

- **The novelty claim now holds**, on ten papers read (2026-09-11). Both threads
  closed; no prior description of S′'s structure found. **No errors have been
  found in the paper.** The one claimed erratum was retracted — it came from my
  own bad PDF extraction, not from the paper.
- Reference [16] (own working notes) is outside the vault.
- **Twenty of the 23 original bibliography entries remain `read: not-read`** —
  they record what the paper says about the literature, not what the literature
  says. The nine newly-read papers carry dated `read:` fields and verdicts.

## Environment constraint

Claude Code sessions here **cannot reach scholarly hosts** — arxiv.org,
semanticscholar, crossref, doi.org, mdpi, openalex are all blocked by the egress
policy, for WebFetch and curl alike. Only WebSearch gets out, and it returns
search summaries rather than documents. **PDFs must be uploaded by hand.** Plan
literature work around that: this environment can search, verify computations,
and organise, but it cannot fetch papers.
