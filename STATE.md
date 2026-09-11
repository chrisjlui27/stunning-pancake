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

The mathematics is machine-verified (`papers/mirror-sedenions/VERIFICATION.md`).
**The literature position is not.** That asymmetry is the thing to fix next.

## Open threads

| Thread | Status | Next step |
|---|---|---|
| **Wilmot gap** | open, highest priority | Identify the work; check for prior treatment of alternative doubling products or M(A). Either cite in v2 or record why not. `sources/wilmot-GAP.md` |
| **Own notes not in vault** | open | Import JS-1–41 and JS-LANDSCAPE-II, plus the sign-function census code. Reference [16] is load-bearing and currently unreachable. `sources/lui-js-notes.md` |
| **Cawagas et al. 2009 priority check** | open | Read it; confirm S′ ≅ Sγ is genuinely "noticed but not studied". Nearest prior art. |
| **Bibliography is second-hand** | open, ongoing | All 23 `sources/` files are `read: not-read` — claims are what the paper cites them for, not what the sources say. Promote as read. |
| Open Question 2 (orientation tree) | open | Most tractable of the four: a finite classification, not a geometry problem. Needs the census code first. |
| Open Question 1 (metric on P(S′)) | open | Reggiani's treatment of P(S) is the template. |

## Decisions made

- **2026-09-10** — Vault lives in git rather than in assistant memory, so it is
  readable from Claude Code, Cowork, and chat alike, and is versioned.
- **2026-09-11** — `sources/` files carry a **`read:`** field. A claim recorded
  from a citation is not a claim from the source. Nothing gets promoted to
  settled without an actual reading.
- **2026-09-11** — Computed claims get **run**, not trusted. Verification output
  is committed with the date and environment.

## Known gaps

- The novelty claim in §1 of the paper is **unverified** until the Wilmot gap and
  the Cawagas priority check are closed. The mathematics does not depend on this;
  the contribution does.
- Reference [16] (own working notes) is outside the vault.
