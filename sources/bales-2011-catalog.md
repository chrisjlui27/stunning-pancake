---
type: source
title: A catalog of Cayley--Dickson-like products
author: J. W. Bales
published: arXiv:1107.1301 (2011)
retrieved: 2026-09-11
url: https://arxiv.org/abs/1107.1301
kind: paper
read: full (2026-09-11)
confidence: medium
status: READ — verdict below
---

# Bales 2011 --- a catalog of Cayley--Dickson-like products

## Verdict — 2026-09-11

**RESOLVED — no threat; a citation refinement, not a correction.**

*Correcting my own earlier note here:* I first wrote that the paper presents the
32/24/8 census as its own computation. **That was wrong.** §3.2 says "Bales [2]
shows that among thirty-two candidate doubling formulas … exactly eight produce …"
and Appendix A says "the thirty-two Bales candidates". The attribution is already
present and correct.

The refinement is *which* Bales paper. The 32 / 24 / 8 result is the explicit
subject of this one, which is uncited: "A catalog of all **32** … Only **eight**
of these are true Cayley-Dickson doubling products, since **24** of them do not
satisfy the quaternion properties." Suggest citing it alongside [2] at that
sentence; check whether AACA 2016 also carries the census.

Table 11 gives the eight in a third numbering: the standard product is **P31**,
the mirror is **P27** — verified bit-for-bit against our `S` and `Sm`. Classifying
all eight: S-class {P0, P7, P24, P31}, S′-class {P3, P4, P27, P28}, forming four
ac/ca partner pairs each split one to each class — Theorem 3.6's mechanism in a
third independent numbering. The catalog never applies a variant once on top of
standard O, nor observes that the eight give two non-isomorphic 16-dimensional
algebras, so the **construction** claim is untouched.

## Why this source matters

Sets out to enumerate **all** variants of the doubling product. The mirror double is a variant of the doubling product. Those two sentences need to be reconciled.

## Claims taken from it (abstract only)

- Purpose stated as: **catalog all possible variants of the Cayley--Dickson doubling product**, and suggest an alternate numbering of the basis vectors.

## Risk to the paper

**Moderate.** §1 claims 'no prior formulation of the mirror double as a construction'. A catalog of product variants is the most likely place for that to be wrong. Mitigating: the v1 paper already engages with Bales [2] and makes the sharp point that Bales considers only **uniform towers** --- one product used at every level --- whereas the mirror applies a variant **once**, on top of standard O. If the catalog inherits that restriction, the claim stands. If it catalogs products applied at a single level, it does not.

## What needs to happen

- [ ] Read; check whether the catalog is of uniform towers or of single-level variants.
- [ ] Check whether the mirror product (Bales P1^T) appears applied on top of standard O.
- [ ] Reword the §1 novelty sentence to whatever survives.

## Disagrees with

Potentially `synthesis/mirror-sedenions.md` §'The claim', item (iii).
