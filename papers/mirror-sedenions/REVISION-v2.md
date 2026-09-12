---
type: revision-spec
paper: mirror-sedenions-v1.pdf
target: v2
date: 2026-09-12
---

# Paper 1, v2 — revision specification

No theorem of v1 changes. Every statement was re-verified and no mathematical
error was found; two bugs were located and fixed in the *verification scripts*
(`check7_misc.py`, `check9_final.py`), not in the mathematics. The revisions are
one new proposition, one new theorem, and citation corrections.

New LaTeX for the insertions is in `v2-insertions.tex`.

---

## R1 — §1, "Relation to the literature": four citation changes

**Current text is correct** on the identification of formula (2) as Bales's
$P_1^{\top}$; this was checked against arXiv:1707.07318 v3 (the version whose
title matches the AACA citation) and v4, which print all eight products and agree
with §3.2 label for label.

Changes:

1. **Add Bales, *A catalog of Cayley–Dickson-like products*, arXiv:1107.1301**
   at the §3.2 sentence attributing the thirty-two candidates. That paper states
   the 32 / 24 / 8 enumeration outright, and is the natural citation for it;
   confirm whether the AACA paper also contains it and adjust to "see also"
   if so.
2. **Add Moreno, *Constructing zero divisors in the higher dimensional
   Cayley–Dickson algebras*, arXiv:math/0512517.** A sequel to [18] relating
   zero-divisor sets to Stiefel manifolds; cite in §1 and in Question 3.
3. **Add Wilmot, *Structure of the Cayley–Dickson algebras*, arXiv:2505.11747.**
   His "eight octonion and seven power-associative subalgebras of sedenions" is
   the content of Theorem 6.1 in other terminology, and his reduction of the
   sedenions' 84 zero divisors to twelve per quasi-octonion subalgebra is the
   subject of the new Proposition R3 below.
4. **[9] Cawagas et al.**: cite the algebra as $\Sed_\gamma$ (their bullet list
   types it as $\Sed_\delta$ while their Table 6 and isomorphy classes use
   $\gamma$), and add a clause noting that their classification is of *subloops*
   whereas claim (A) is about subalgebras.

**Supporting quotation**, should a referee press on "prove nothing further" —
from beneath their Table 6: *"Note that the loop $\Sed^\gamma_L$ has the same
subloop composition as $\Sed_L$ but analysis shows that they are not isomorphic."*
Their four isomorphy classes have sizes 16, 7, 7, 1, which our own hyperplane
census reproduces exactly.

## R2 — §3, new subsection: the erasure theorem

**Replace Remark 3.8 with the general statement.** Remark 3.8 currently records
that $\CD(\MM(\HH))\cong\Sed$ and that the four words in $\{\CD,\MM\}$ at
dimension 16 give three algebras. Both are instances of:

> **Theorem.** $\CD(\MM(A))\cong\CD(\CD(A))$ as $*$-algebras, for every
> $*$-algebra $A$.

The proof is short and uses only Theorem 3.3: inside $\CD^2(A)$ take
$N=A+A(ee')$ and $u=e'$; then $(ee')e'=-e$ gives $\CD^2(A)=N\oplus Nu$, and the
four Cayley–Dickson component identities hold by direct computation. Full text
in `ERASURE-PROOF.md`; LaTeX in `v2-insertions.tex`.

Keep the existing observation about uniform towers as a remark following it.

**This is a judgment call.** The theorem is also the opening of the companion
paper. Arguments for keeping it here: it follows from this paper's own
Theorem 3.3 with no new machinery; it is roughly one page; it makes Remark 3.8 a
special case rather than an aside; and it answers the question a reader has
immediately after Theorem 3.3. If it is moved to the companion, Remark 3.8 should
at least be cross-referenced to it.

## R3 — §5, new proposition: the incidence decomposition

> **Proposition.** In both $\Sed$ and $\Sed'$ each of the seven quasi-octonion
> basis hyperplanes contains exactly twelve two-term zero-divisor index pairs, so
> the incidence total is $7\times12=84$ pairs counted with multiplicity in both.
> The multiplicities differ: in $\Sed$ every two-term zero divisor lies in
> exactly two of the seven; in $\Sed'$ the forty-two pairs shared with $\Sed$ lie
> in one and the fourteen pairs $(i,i+8)$, $(i,8)$ lie in three.

The proof is a count in $\FF_2^3$ and is given in `v2-insertions.tex`. This
places $\Sed'$ inside Wilmot's "twelve per quasi-octonion subalgebra, seven
copies" accounting rather than merely contrasting 84 with 112: the local data are
identical and only the incidence differs.

## R4 — §2.4 and §3, Proposition 3.2: shorten

Proposition 3.2 (unit, $x\bar x=N(x)$, involution an anti-automorphism,
quadraticity) is currently proved by direct substitution. All of it, together
with the adjoint identity used throughout §2.2 and §2.4, follows from Bales's
theory of *proper twists* [arXiv:1107.1375, Def. 4.1, Thms. 4.3–4.5, Cor. 4.11].
On $\FF_2^n$, where every element is its own inverse, properness reads
\[
  w(p,q)w(q,q)=w(p\oplus q,q),\qquad w(p,p)w(p,q)=w(p,p\oplus q),
\]
and holds for every algebra of the tower, split nodes included. Cite and
compress; note explicitly that none of these properties distinguishes $\Sed'$
from $\Sed$.

## R5 — §9, Question 2: keep the qualifier, and re-point

The claim is **false** without the quaternionic-line restriction: four further
Bales candidates — in the $(f,g)$ indexing of the scripts, $(1,3)$, $(2,2)$,
$(5,1)$, $(6,0)$ — have eight octaves *and* $\dim\Der=14$ without being $\Sed$ or
$\Sed'$. They are excluded precisely by the quaternionic-line condition, with 28
failing ordered basis pairs each; exactly 8 of the 32 have none, which is what
makes Appendix A's "twenty-four rejected formulas". Add a parenthetical saying so.

Questions 2 and 3 are now largely answered in the companion paper (the normal
form, sharpness, and the increment theorem). Re-point them rather than deleting:
Question 2 becomes the finite-classification statement proved there, and
Question 3's higher-mirror part is answered for two-term zero divisors and
remains open for the geometry.

## R6 — Appendix A: extend

Add to the list of verified assertions:

- the Wilmot incidence decomposition of R3 (`check13`, `check24`);
- the $8$-dimensional subalgebra census of $\Trig$, reproducing Cawagas et al.'s
  $50/105$ (`check22`);
- the erasure theorem and each intermediate identity (`check19`);
- the corrections to `check7_misc.py` and `check9_final.py`;
- `check26`, an assertion gate covering every numerical claim of both papers.
  Thirteen of the original scripts print data without asserting anything, so
  running them cannot detect a regression; `check26` is the script that can.

**The two script corrections should be stated**, since Appendix A asserts the
scripts verify the paper:

1. `check7_misc.py` computed $\tau$ with $\lvert a\rvert$ in place of
   $\lvert\operatorname{Im}a\rvert$. The two agree when $\operatorname{Re}a=0$,
   so the sample points elsewhere passed while a random test reported a deviation
   of $0.45$. Theorem 4.1 is correct; with the fix the agreement is $2.4\times
   10^{-15}$ over 2000 random points.
2. `check9_final.py` asserted that $\ell$ is alternative in $\Sed'$ but not in
   $\Sed$. Both are true: $\ell\in\RR+\OO\ell$, which Table 1 lists as alternative
   for both. The element separating them is $u+u\ell$. Table 1 is confirmed.

## Checklist

| | |
|---|---|
| R1 citations | ready |
| R2 erasure theorem | ready (`v2-insertions.tex`) |
| R3 incidence proposition | ready, proof included |
| R4 proper twists | ready |
| R5 Question 2 qualifier | ready |
| R6 Appendix A | ready |
