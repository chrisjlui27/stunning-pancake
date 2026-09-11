---
type: source-index
title: "J. W. Bales — corpus index"
author: John W. Bales (Tuskegee University)
retrieved: 2026-09-11
kind: index
---

# Bales's corpus — the reference frame for doubling products

**Six of the ten papers in `papers/library/` are his.** Anything about *which*
Cayley–Dickson doubling product is in use, how the eight relate, or how the twist
behaves, runs through his work. Treat him as the standard reference for the
product-variation axis, the way Moreno and Biss–Dugger–Isaksen are for zero
divisors and Schafer for derivations.

| Year | Work | In library | Role here |
|---|---|---|---|
| 2011 | *A catalog of Cayley–Dickson-like products* (arXiv:1107.1301) | ✅ | The **32 / 24 / 8** census. Table 11 lists the eight; standard = **P31**, mirror = **P27**. Uncited in v1. |
| 2011 | *Cayley–Dickson and Clifford algebras as twisted group algebras* (arXiv:1107.1375) | ✅ | Twisted-group-algebra framework, as in §7. Not yet read. |
| 2016 | *An alternate Cayley–Dickson product* (Missouri J. Math. Sci. 28; arXiv:1602.02317) | ✅ | Shuffle basis, closed-form twist. "Different from yet **equivalent to**" — isomorphic, no new algebra. |
| 2016 | *Periodicity of the Cayley–Dickson twists* (arXiv:1602.02843) | ✅ | Twist periodicity. Not yet read. |
| 2016 | *The eight Cayley–Dickson doubling products* (AACA 26, 529–551) = **ref [2]** | ✅ (arXiv v3) | The eight products and their numbering. **v3's title matches the AACA citation.** |
| 2017/2023 | *The Cayley–Dickson doubling products* (arXiv:1707.07318v4) | ✅ | Retitled later version of the above; product list identical to v3. |

Also cited by him and not yet chased: *Properly twisted groups and their algebras*
(arXiv:1107.1297), *A tree for computing the Cayley–Dickson twist* (Missouri J.
Math. Sci. 21, 2009).

## The numbering, settled

Three numbering schemes are in play across his papers and ours. They agree on the
mathematics and disagree on labels, which is how a day was lost to a false
erratum. **Verified computationally, 2026-09-11:**

| | standard, eq. (1) | mirror, eq. (2) |
|---|---|---|
| **Bales [2] / arXiv:1707.07318** (v3 and v4 identical) | **P3ᵀ** | **P1ᵀ** |
| **Bales 2011 catalog**, Table 11 | **P31** | **P27** |
| **mirror-sedenions v1** §3.2 | P3ᵀ | P1ᵀ — matches [2] ✓ |

His ᵀ marks a **second set of four whose product matrices of unit vectors are
transposes** — it is *not* the argument-swap P(y,x). Under argument-swap the
pairing is Pᵢᵀ = swap(P₍₃₋ᵢ₎). Assuming otherwise is what generated the retracted
erratum; see `papers/mirror-sedenions/ERRATA.md` §E1.

**Always state which numbering is in use when citing a specific Pᵢ.**

## Class assignment, in all three numberings

| numbering | S-class | S′-class |
|---|---|---|
| Bales [2] / paper §3.2 | P0, P3, P0ᵀ, P3ᵀ | P1, P2, P1ᵀ, P2ᵀ |
| Bales 2011 catalog | P0, P7, P24, P31 | P3, P4, P27, P28 |

In the catalog numbering the eight form four `ac`/`ca` partner pairs —
(P31,P27), (P28,P24), (P4,P0), (P7,P3) — **each split one to each class**, which
is Theorem 3.6's stated mechanism confirmed in an independent numbering.

## Still to read

`bales-2011-twisted.pdf` and `bales-2016-periodicity.pdf` — both background for
§7's sign-function analysis.
