---
type: source
title: The basic subalgebra structure of the Cayley--Dickson algebra of dimension 32 (trigintaduonions)
author: R. E. Cawagas, A. S. Carrascal, L. A. Bautista, J. P. Sta. Maria, J. D. Urrutia, B. Nobles
published: arXiv:0907.2047 (2009)
retrieved: 2026-09-11
url: arXiv:0907.2047
kind: paper
read: not-read (abstract + search summary only — arxiv.org is egress-blocked in the container)
confidence: high
ref: "[9] in papers/mirror-sedenions/mirror-sedenions-v1.pdf"
---

# Cawagas et al. 2009 --- subalgebras of the trigintaduonions

## Why this source matters

**The priority question lives here.** S' already appears in this census as S_gamma. This source decides how much of the paper is genuinely new.

## Claims taken from it

- In a loop-theoretic census of T = CD(S), records **S_gamma = O + O(ee')** as the **unique basis hyperplane of T with eight octonion subalgebras that is not isomorphic to S**.
- Records that it has **eight octonion and seven quasi-octonion subloops**.
- **Proves nothing further** about it --- per the mirror paper's own assessment (Sec. 1, Relation to the literature).

## Priority check — 2026-09-11, partially resolved

The characterisation to verify was: S′ ≅ Sγ is **noticed but not studied**, and is
**the unique** basis hyperplane of T with eight octonion subalgebras not isomorphic
to S.

**What the search turned up.** A summary of this paper states that T's loop has
373 non-trivial subloops, all normal, generating subalgebras of dimensions 16, 8,
4, 2, 1; and that **three of the 31 sedenion-type loops of order 32 have been
identified as distinct (non-isomorphic)**.

**What our own computation says** (check6, run 2026-09-11). The 31 basis
hyperplanes of T fall into exactly four type-classes:

| octaves | ann dims on test loci | functionals | count |
|---|---|---|---|
| 8 | (0, 4) | 1–8, 16 | 9 |
| 8 | (0,) | 9–15 | 7 |
| 8 | **(2,)** | **24** | **1** |
| 2 | (2,) | 17–23 | 7 |
| 0 | (2,) | 25–31 | 7 |

The first two rows are S (16 hyperplanes, matching Table 1's "S: 16 basis
hyperplanes"), leaving **three** non-S classes of sizes 7, 1, 7 — consistent with
"three of the 31 sedenion-type loops are distinct". And among those three, exactly
**one** has eight octonion subalgebras: functional 24, which is Sγ.

**So the uniqueness half of the claim is independently corroborated.** The
"noticed but not studied" half is not — that is a statement about what the paper
does and does not prove, and it can only be settled by reading it.

**Verdict: partially resolved. Read before the novelty claim ships.**

## Caveats

'Noticed but not studied' is the paper's characterisation and is load-bearing for the novelty claim. The uniqueness is now corroborated by independent computation; the "not studied" part still rests on trust --- it is the one citation where being wrong is expensive.

Loop-theoretic vocabulary: the source counts *subloops*, we count *subalgebras*. The translation is standard but should be stated when citing specific numbers.

## Disagrees with

Nothing --- but this is the nearest prior art, and the closest thing to a competing claim.
