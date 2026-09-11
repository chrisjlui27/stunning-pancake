---
type: note
date: 2026-09-11
topic: Seeding the vault with the mirror sedenions work
status: processed
---

# Seeding the vault — 2026-09-11

## Capture

The vault's subject is settled: **hypercomplex algebras**. Named starting points
were Wilmot, Reggiani, Moreno.

Dropped in: `mirror_sedenions_1.pdf` (15pp, "working draft v1", dated September
2026, author Lui, Quitman, Texas) and `mirror_sedenions_code.zip` (cd.py,
f2iso.py, sym_spectrum.py, check1–check12).

The paper is original work, not a literature review. Its result: applying one of
Bales's eight doubling products *once* on top of standard O yields exactly two
algebras — S and a second one, S′ = M(O), the "mirror sedenions" — and S′ is
determined completely.

## Immediate observations

**Reggiani and Moreno are references [19] and [18]. Wilmot is nowhere in the
bibliography.** Since all three were named in the same breath as good starting
points, that asymmetry needs an explanation. It is also precisely where a prior
description of S′ would hide, and §1 makes an explicit no-prior-work claim.
Logged as `sources/wilmot-GAP.md` rather than left as a loose end.

**Reference [16] is self-citation to working notes** (JS-1–41, JS-LANDSCAPE-II)
that are **not in the vault**. The paper leans on them twice in load-bearing
ways: the colour vocabulary (hues / ultraviolets) used to state Prop. 5.4, and
the numerical census behind Open Question 2. A referee cannot be answered from
anything committed here. Logged as `sources/lui-js-notes.md`.

## Verification run

Ran the accompanying scripts rather than taking Appendix A on trust. Environment
notes for next time: `numpy` and `sympy` are **not** preinstalled; there is no
`pdftotext` (use `pymupdf`); `pypdf` is present but broken (its `cryptography`
backend panics on import). Results in
`papers/mirror-sedenions/VERIFICATION.md`.

## Questions this raised

- Is S′ ≅ Sγ genuinely "noticed but not studied" by Cawagas et al.? That is the
  nearest prior art and the whole novelty claim rests on the characterisation.
  It is the one citation where being wrong is expensive.
- Open Question 2 (the orientation tree) has numerical evidence in notes that
  aren't here and no proof. It looks like the most tractable of the four — it is
  a finite classification statement, not a geometry problem.
- What is the actual Riemannian metric on P(S′)? Question 1 is the one with a
  ready-made template in Reggiani's treatment of P(S).

## To follow up

- [ ] Resolve the Wilmot gap — identify the work, then cite it or record why not.
- [ ] Import JS-1–41 and JS-LANDSCAPE-II into `notes/`, with the census code.
- [ ] Read Cawagas et al. 2009 properly and confirm the priority characterisation.
- [ ] Promote source files from `read: not-read` as they actually get read.
