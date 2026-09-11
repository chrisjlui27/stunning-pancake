---
type: source
title: The Cayley--Dickson doubling products / The eight Cayley--Dickson doubling products
author: J. W. Bales
published: arXiv:1707.07318 (2017); cf. Adv. Appl. Clifford Algebras 26 (2016), 529--551
retrieved: 2026-09-11
url: https://arxiv.org/abs/1707.07318
kind: paper
read: full, v3 and v4 (2026-09-11)
confidence: high
status: READ — verdict below
---

# Bales --- the eight doubling products (arXiv version)

## Verdict — 2026-09-11

**No erratum. The paper's §3.2 transcription of Bales is correct.**

I twice claimed otherwise and was twice wrong. Bales prints all eight products
explicitly on p. 8 (identically in v3 and v4):

    P0ᵀ = (ca − bd*, ad + c*b)     P1ᵀ = (ca − d*b, da + bc*)   ← eq. (2), mirror
    P2ᵀ = (ac − bd*, ad + c*b)     P3ᵀ = (ac − d*b, da + bc*)   ← eq. (1), standard

§3.2 matches **label for label**, and §1's "formula (2) is Bales's product P₁ᵀ" is
correct. Verified: Bales's P1ᵀ is identical to our `Sm`, his P3ᵀ to our `S`.

My error: a grep requiring the formula on one line missed the four transposes
(PDF extraction splits the label as `P ⊤` / `1 :`), and I reconstructed them by
argument-swap. Bales's ᵀ does **not** mean argument-swap — it marks a second set
of four whose *product matrices of unit vectors* are transposes. Under
argument-swap the pairing is Pᵢᵀ = swap(P₍₃₋ᵢ₎), which is the "reversal" I
mistook for the paper's error. Full retraction in
`papers/mirror-sedenions/ERRATA.md` §E1.

**Both v3 and v4 are in `papers/library/`.** v3 (`bales-2017-doubling-v3.pdf`) is
the version whose title matches the AACA 26 (2016) citation in [2].

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
