# State

> The handoff file. Every session reads this first and updates it before ending.
> Keep it short — if a section is growing past a screen, the detail belongs in
> `synthesis/` and this file should link to it instead.

**Last updated:** 2026-09-11 — nine papers read; both literature threads closed; five errata logged.

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
| **Apply the v2 errata** | **open, highest priority** | Five items in `synthesis/mirror-sedenions.md` §Errata: the P₁ᵀ→P₂ᵀ fix, citing Bales's 2011 catalog for the 32/24/8 census, adding Moreno 2005 and Wilmot, and keeping Question 2's quaternionic-line qualifier. |
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

## Known gaps

- **The novelty claim now holds**, on nine papers read (2026-09-11). Both threads
  closed; no prior description of S′'s structure found. Five errata to apply —
  the largest being that the 32/24/8 doubling-product census is **Bales's**, not
  the paper's own.
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
