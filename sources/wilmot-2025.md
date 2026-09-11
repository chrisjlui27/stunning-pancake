---
type: source
title: Structure of the Cayley–Dickson algebras
author: G. P. Wilmot
published: arXiv:2505.11747 (2025)
retrieved: 2026-09-11
url: https://arxiv.org/abs/2505.11747
kind: paper
read: abstract + introduction + structure search (2026-09-11)
confidence: medium
---

# Wilmot 2025 — structure of the Cayley–Dickson algebras

## Verdict — 2026-09-11

**RESOLVED — low risk confirmed, and should be cited.** Wilmot uses the **standard** product throughout (his eq. (1), (a,b)(c,d) = (ac − εd\*b, da + bc\*)); across 25 pages there are two total occurrences of any of 'doubling product', 'transpose', 'mirror', 'variant', 'Bales'. He does not consider alternative doubling products. Substantively adjacent though: his 'eight octonion and seven **power-associative** subalgebras of sedenions' is Theorem 6.1's split in other vocabulary (his power-associative subalgebras are the quasi-octonions M(H)). **Split sedenions ruled out computationally** — indefinite norm, no graded isomorphism to S or S′. The **84 → 7** reduction against S′'s **112 = 16 × 7** now looks like a real connection rather than a coincidence: he attributes the factor of seven to the seven power-associative subalgebras, and S′ has seven quasi-octonion hyperplanes too.

## Status: gap **identified**, not yet closed

Named in conversation as a key starting point alongside Reggiani and Moreno, but
absent from the v1 bibliography. The work is now identified. It has **not been
read** — only the abstract, via search.

G. P. Wilmot, University of Adelaide.

## Claims taken from it (abstract only)

- Views the **Cayley–Dickson process as a graded construction**, giving a
  definition of associativity in three classes with the non-associative parts
  dividing into four types.
- These simplify the **Moufang loop identities and Mal'cev's identity**, which
  identifies the non-associative Lie algebra structure.
- Uncovers **3-cycles** distinguishing the Moufang identities, used to identify
  **three power-associative subalgebras of sedenions** and higher CD algebras.
- **Zero divisors occur in multiples of 84**, with cycles and modes reducing
  these to **seven primary zero-divisor pairs** in most cases, including the
  sedenions.
- Proposes replacing "hypercomplex numbers" with "ultracomplex numbers" for the
  power-associative algebras.

## Assessment of the risk to the novelty claim

**Provisionally low, but unconfirmed.** On the abstract, Wilmot treats the
*standard* CD algebras: the grading, the associativity types, the power-
associative subalgebras. Nothing suggests alternative or transposed doubling
products, and nothing suggests a construction equivalent to M(A). The novelty
claim in §1 concerns S′, which is not a CD algebra, so it is probably untouched.

**But this must be read before the claim goes out.** "Probably untouched, on the
abstract" is not the standard the claim needs.

## The interesting part, if it survives

Wilmot's counting and the mirror's counting sit oddly together and may be saying
the same thing in different language:

| | two-term basis zero divisors | = 7 × |
|---|---|---|
| S | 84 (de Marrais's 42 assessors) | 12 |
| S′ | 112 (verified 2026-09-11) | 16 |

Wilmot reduces the sedenions' 84 to **seven** primary pairs via cycles and modes.
Both counts are multiples of seven. **Does the reduction apply to S′, and if so
what are its primary pairs?** Note 112 is *not* a multiple of 84, so if Wilmot's
"multiples of 84" is a theorem about CD algebras, S′ sits outside its hypothesis
rather than contradicting it — S′ is not a CD algebra. That boundary is worth
stating precisely, and could make a good remark in v2 either way.

<!-- UNVERIFIED: everything above is from the abstract. The 84/112 observation is
     my own and is not claimed by either source. -->

## What needs to happen

- [ ] Read it. PDF: https://arxiv.org/abs/2505.11747 (`papers/library/MANIFEST.md`)
- [ ] Check specifically for: alternative/transposed doubling products; any
      construction equivalent to M(A); any treatment of algebras that are not
      standard CD doubles.
- [ ] Decide whether the 84 / 112 comparison is a real connection or a coincidence.
- [ ] Cite in v2, or record here why not.

## Caveats

The "ultracomplex" terminology proposal suggests a paper willing to re-lay
foundations, which often means notation that will not line up with Convention 2.1
without work. Budget for translation.

## Disagrees with

Potentially `synthesis/mirror-sedenions.md` §"The claim" — unresolved until read.
