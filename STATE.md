# State

> The handoff file. Every session reads this first and updates it before ending.
> Keep it short — if a section is growing past a screen, the detail belongs in
> `synthesis/` and this file should link to it instead.

**Last updated:** 2026-09-11 — vault seeded with the mirror sedenions work.

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
| **Read Aryapoor–Bäck–Pautrel 2026** | **open, highest priority** | Classifies algebra isomorphisms between Cayley doubles extending the identity — Theorem 3.6's exact question, published this year. Read before anything else. `sources/aryapoor-back-pautrel-2026.md` |
| **Read Bales's 2011 catalog** | open, high | "Catalog all possible variants of the CD doubling product." Most likely place for the "no prior formulation of M(A)" claim to be wrong. `sources/bales-2011-catalog.md` |
| **Wilmot gap** | identified, not closed | G. P. Wilmot, arXiv:2505.11747. Abstract read: treats standard CD algebras, so risk looks low — but unconfirmed. `sources/wilmot-2025.md` |
| **Own notes not in vault** | open | Import JS-1–41 and JS-LANDSCAPE-II, plus the sign-function census code. Reference [16] is load-bearing and currently unreachable. `sources/lui-js-notes.md` |
| **Cawagas et al. 2009 priority check** | half resolved | Uniqueness **independently corroborated** by our own check6 run (31 hyperplanes → 16 are S, plus three non-S classes of sizes 7, 1, 7; only functional 24 = Sγ has eight octaves). "Noticed but not studied" still needs the text. `sources/cawagas-et-al-2009.md` |
| **Library is empty** | open | `papers/library/MANIFEST.md` has the ranked download list. Nothing could be fetched in-container — every scholarly host is egress-blocked. Needs manual upload. |
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

- The novelty claim in §1 is **unverified**, and the literature search now looks
  thinner than it did: **seven references turned up in a single search pass that
  are not in the v1 bibliography**, two of them squarely on the paper's own
  territory. The mathematics does not depend on this; the contribution does.
- Reference [16] (own working notes) is outside the vault.
- **No source in `sources/` has been read.** All 30 are `read: not-read`. The
  vault currently records what the paper says about the literature, not what the
  literature says.

## Environment constraint

Claude Code sessions here **cannot reach scholarly hosts** — arxiv.org,
semanticscholar, crossref, doi.org, mdpi, openalex are all blocked by the egress
policy, for WebFetch and curl alike. Only WebSearch gets out, and it returns
search summaries rather than documents. **PDFs must be uploaded by hand.** Plan
literature work around that: this environment can search, verify computations,
and organise, but it cannot fetch papers.
