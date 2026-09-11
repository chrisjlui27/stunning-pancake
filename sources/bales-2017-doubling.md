---
type: source
title: The Cayley--Dickson doubling products / The eight Cayley--Dickson doubling products
author: J. W. Bales
published: arXiv:1707.07318 (2017); cf. Adv. Appl. Clifford Algebras 26 (2016), 529--551
retrieved: 2026-09-11
url: https://arxiv.org/abs/1707.07318
kind: paper
read: full (2026-09-11)
confidence: high
status: READ — verdict below
---

# Bales --- the eight doubling products (arXiv version)

## Verdict — 2026-09-11

**ERRATUM FOUND — but narrower than I first stated.**

*Correcting my own earlier note:* I first said "formula (2) is P₂ᵀ, not P₁ᵀ,"
implying §1 was simply wrong. It is more subtle. The paper's §3.2 prints its own
list of the eight, and **in that list P₁ᵀ is indeed formula (2)** — so §1 is
internally consistent with §3.2. I had not read §3.2 when I made the claim.

The actual defect: the paper's §3.2 **unprimed P0–P3 match Bales exactly**, and
the eight match **as a set**, but the **transposes are subscript-reversed** —
the paper's Pᵢᵀ is Bales's P₍₃₋ᵢ₎ᵀ:

| paper | Bales |
|---|---|
| P0ᵀ | P3ᵀ |
| P1ᵀ | **P2ᵀ** (= formula (2), mirror) |
| P2ᵀ | P1ᵀ |
| P3ᵀ | **P0ᵀ** (= formula (1), standard) |

Since Bales defines Pᵀ(x,y) = P(y,x), the paper's "P0ᵀ" is the transpose of **P3**,
so the superscript does not mean what the notation says, and a reader consulting
[2] for P₁ᵀ finds a different formula.

**Theorem 3.6 survives under either labelling** — the reversal maps {0,3}→{3,0}
and {1,2}→{2,1}, preserving the sets {P0ᵀ,P3ᵀ} and {P1ᵀ,P2ᵀ}. Verified in both.
Only §1's identification and Remark 3.8's references to "P₁ᵀ" need changing.
Full fix in `papers/mirror-sedenions/ERRATA.md` §E1.

<!-- UNVERIFIED: compared against arXiv:1707.07318v4 (2023). Ref [2] cites AACA 26
     (2016), whose title matches arXiv v3. Numbering assumed stable across
     versions — confirm against the AACA text; if AACA numbers the transposes as
     the paper does, the erratum is void. -->

## Why this source matters

Housekeeping with teeth: reference [2] is cited as the AACA 2016 paper, and there is an arXiv item with a near-identical title whose v3 is titled 'The eight Cayley--Dickson doubling products'. Theorem 3.6 depends on Bales's **numbering** of the eight products, so citing the wrong version could misalign every P_i label in the paper.

## Claims taken from it (abstract only)

- There are eight and only eight distinct CD doubling products, in paired groups: P0--P3 and transposes P0^T--P3^T.
- The most commonly used is **P3^T**; P3 has also been used. (Consistent with Convention 2.1, which uses (1) = P3^T.)

## Risk to the paper

**Low mathematically, real editorially.** Confirm which version the P_i numbering in Theorem 3.6 matches, and cite that one.

## What needs to happen

- [ ] Compare the arXiv versions against the AACA paper's numbering.
- [ ] Confirm S-class {{P0, P3, P0^T, P3^T}} and S′-class {{P1, P2, P1^T, P2^T}} against the cited version.

## Disagrees with

Nothing.
