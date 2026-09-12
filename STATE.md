# State

> The handoff file. Every session reads this first and updates it before ending.
> Keep it short — if a section is growing past a screen, the detail belongs in
> `synthesis/` and this file should link to it instead.

**Last updated:** 2026-09-12 (second session) — **relative erasure theorem** proved; the
basis-subalgebra landscape of the CD tower classified through dimension 128; the degenerate
subalgebras identified as relative mirrors. `synthesis/degenerate-subalgebras.md`.

## Subject

**Hypercomplex algebras** — Cayley–Dickson constructions, octonions and beyond,
zero-divisor geometry, automorphism and derivation theory.

## Current focus

`papers/mirror-sedenions/` — *The mirror sedenions*, working draft v1. Result summary in
`synthesis/mirror-sedenions.md`; the {CD,M} tower in `synthesis/mirror-tower.md`; the
subalgebra landscape and the degenerate classes in `synthesis/degenerate-subalgebras.md`.

The mathematics of v1 is machine-verified (`papers/mirror-sedenions/VERIFICATION.md`,
2026-09-11 and 2026-09-12 runs). The literature position holds on ten papers read.

## Open threads

| Thread | Status | Next step |
|---|---|---|
| ~~64-dim landscape count~~ | **done** | \|L_5\| = 16: 15 hyperplane orbits of A_6, 15 distinct relative mirrors. `check25`, under a minute. |
| **32-dim stability in A_7** | running at session end | `check21_landscape.py 7 5`, 2667 subgroups, ~1 h. First 1000 gave only the 8 known classes. Fill the A_7 row. |
| **Conjecture \|L_k\| = 2^{k−2}** | new | 1, 2, 4, 8, 16 at dims 4–64. Equivalent to: Aut(A_k) has 2^{k−2} − 1 orbits on hyperplanes with pairwise non-isomorphic relative mirrors. A proof needs the orbit structure of the graded automorphism group on hyperplanes. |
| **Apply the v2 additions** | ready | `ERRATA.md`, plus: replace the erasure theorem by relative erasure; name the [2+13] / [0+15] hyperplanes (X16.2 = R_S(O_L), X16.3 = M²(H)); the dim Ann = 2 × (#quasi-octonions) rule; Wilmot's P12/P14 ≅ P4 remark. |
| **Own notes not in vault** | open | Import JS-1–41 and JS-LANDSCAPE-II. Reference [16] is load-bearing and unreachable. |
| Read Bales twisted + periodicity | open, low | Background for §7. Proper-twist framing already used. |
| **Bibliography is second-hand** | open, ongoing | Twenty of 23 `sources/` files still `read: not-read`. |
| Open Question 1 (metric on P(S′)) | open | Reggiani's treatment of P(S) is the template. |
| ~~Open Question 2 (orientation tree)~~ | **answered, strengthened** | Normal form M^b CD^a (erasure) and now the full landscape: at dimension 16 the four words give S, S′, X16.3; the fourth class X16.2 is reachable only as a relative mirror. |

## Decisions made

- **2026-09-10** — Vault in git, not assistant memory.
- **2026-09-11** — `sources/` files carry `read:`; nothing promoted without a reading.
- **2026-09-11** — Computed claims get **run**; output committed with date and environment.
- **2026-09-12** — Graded isomorphism is decided by the **associator pattern**
  (`code/landscape.py`), not by enumerating GL(n,2): it is a proved complete invariant for
  anticommutative sign-monomial algebras and it reaches dimension 64. Class labels live in
  `code/landscape_registry.pkl`; regenerate with `check21_landscape.py 4; 5; 6` (~2 min).

## New results (2026-09-12, second session)

- **Relative erasure:** CD(K + K(e_c e)) ≅ CD(A) for every basis hyperplane K of every
  anticommutative sign-monomial A. `RELATIVE-ERASURE-PROOF.md`. Uses only anticommutativity.
- **Absorption:** CD(B) ≅ A_k for every 2^{k−1}-dim basis subalgebra B of any A_n.
- **Stability + generation:** the 2^k-dim basis subalgebras of A_n (n ≥ k+1) are exactly the
  hyperplanes of A_{k+1} = {A_k} ∪ {relative mirrors of A_k}. Classes: **1, 2, 4, 8, 16** at
  dims 4–64; conjecture |L_k| = 2^{k−2}.
- Cawagas's [2+13] hyperplane is R_S(O_L) — not any Bales double of any hyperplane; his
  [0+15] is M(M(H)). Both have Der = so(4), 24 graded automorphisms, 148 / 160 zero divisors.
- Bales's 24 rejected products fail the quaternion property on every base; never subalgebras.
- Wilmot's P12 and P14 generating triads span algebras ≅ P4. His Theorem 8 counts reproduced.
- dim Ann(e_i ± e_j) = 2 × (number of quasi-octonion hyperplanes it is a zero divisor of),
  in all four 16-dim classes.

## Known gaps

- Reference [16] (own working notes) is outside the vault.
- The 64-dim class count and the A_7 32-dim census were still running at session end.
- |L_k| = 2^{k−2} is a conjecture from five data points (dims 4–64).

## Environment constraint

Claude Code sessions here **cannot reach scholarly hosts** — arxiv, semanticscholar,
crossref, doi.org, mdpi, openalex are blocked. Only WebSearch gets out. PDFs must be
uploaded by hand. `pip install numpy sympy pymupdf` at session start.
