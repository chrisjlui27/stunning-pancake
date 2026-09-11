---
type: source
title: Eigentheory of Cayley--Dickson algebras
author: D. K. Biss, J. D. Christensen, D. Dugger, D. C. Isaksen
published: Forum Math. 21 (2009), 833--851
retrieved: 2026-09-11
url: 
kind: paper
read: not-read (known only via mirror-sedenions v1)
confidence: high
ref: "[5] in papers/mirror-sedenions/mirror-sedenions-v1.pdf"
---

# BCDI 2009 --- eigentheory of CD algebras

## Why this source matters

Supplies the stretch operator L_xbar L_x (their M_a) and the S-side spectrum that Theorem 4.1 is compared against.

## Claims taken from it

- The **stretch operator** framework: x is a zero divisor exactly when L_xbar L_x has eigenvalue 0, and dim Ann(x) is its multiplicity.
- For **S** the spectrum has **three levels**: N +/- 2|Im a x Im b| and N, with multiplicities 4, 4, 8.
- Compare S': **five levels**, N +/- 2|Im a||b| (mult. 2 each), N +/- 2|Im a||b_parallel| (4 each), N (4).

## Caveats

The five-level/three-level contrast is the cleanest single discriminator between the two algebras and is machine-verified symbolically (sym_spectrum.py, check8_compare.py). Worth double-checking the normalisation --- the paper sometimes quotes the spectrum of L_xbar L_x and sometimes of the normalised L_xbar L_x / N(x).

## Disagrees with

Nothing.
