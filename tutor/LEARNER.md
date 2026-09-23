# Learner

> Who the tutor is teaching and how they like to be taught. Read at the start
> of every session; edited whenever the learner says they want something
> done differently. Keep it short.

## Person

- Name: Chris
- Pronouns: they/them unless told otherwise
- 39, teaches 9th-grade English in East Texas, raising three children. Time
  is the scarce resource: assume three sessions a week of about 45 minutes,
  and plan each session to be complete on its own.

## Background

- Formal mathematics to Calculus 2. Brushing up calculus this year.
  **No linear algebra course.** This is the main technical gap.
- Read to completion: Lawvere & Schanuel, *Conceptual Mathematics*; Fong &
  Spivak, *Seven Sketches*. Conceptual vocabulary is well ahead of technical
  foundation. Expect fluent use of words like functor, adjoint, universal
  property, alongside gaps in things like determinants and eigenvalues.
- Self-described intellectual trespasser (Ellerman's phrase). Came in through
  Spencer-Brown's *Laws of Form*, Furey and Baez on octonions, applied
  category theory, and working with Claude.
- Doing research-level work on the mirror sedenions. The paper and its
  verification code are the research vault in this same repo (`papers/`,
  `sources/`, `synthesis/`, `notes/`, `STATE.md`), which the tutor reads for
  context but **does not edit** — the tutor writes only inside `tutor/`.
  The computations there are machine-verified; the goal is for the learner
  to be able to prove what they currently compute.
- Planning to start Aluffi, *Algebra: Chapter 0*, later this year. Good fit
  for the category-theory reading; phase 2 below supports it.

## Goals

- Six months: **prove Lemma 2.2 of the mirror-sedenions paper unaided** (the
  kernel of n ↦ [b, n, u] is the quaternion subalgebra H(u, b)) and defend
  it. Everything in the plan points at this.
- Longer: expand understanding broadly, and take structure from mathematics
  into thinking about other things. The tutor serves the first; the second
  is the learner's own business and the tutor should not editorialise on it.
- Parked, not abandoned: Laws of Form, Girard's logic program, octonionic
  physics, and the learner's own "Categorical Laws of Form" draft. Connect
  to them only when an example lands naturally; revisit the draft after
  phase 2, when the learner can sort its theorems from its metaphors.

## Plan (set 2026-09-12)

1. **Linear algebra** (6–8 weeks). Axler as the text. Vectors, inner
   products, orthogonality, linear maps as matrices, determinants,
   eigenvalues, orthogonal groups. Destination: the cross product on R³, and
   why R⁷ has one and R⁵ does not.
2. **Groups, concretely** (6–8 weeks), alongside Aluffi ch. I–II. Symmetry
   groups, homomorphisms, actions, orbit–stabilizer. Hook: the 168 in the
   paper's automorphism table is the symmetry group of the Fano plane.
3. **Quaternions and octonions from scratch** (8–10 weeks). Build H, prove
   associativity. Build O by Cayley–Dickson, prove alternativity and the
   multiplicative norm, derive the Fano plane. Then Lemma 2.2.

Every session ends with one proof written by the learner and marked.

## How they learn

- Understands something when they can decompose with the concept and
  rebuild the other way. The tutor's job is to add the third mode: write the
  rebuild down as a proof someone else can check.
- Strong at computing; the tutor pushes proving and explaining.
- Hints before answers, unless they ask for the solution outright.
- Plain-text notation in the terminal.
- Verify computations by running them. A checked result beats a plausible one.
- Concept-first learner: give the idea behind a procedure before the
  procedure. Connect new material to the octonions whenever it is honest to.
