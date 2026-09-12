---
type: proof
title: The erasure relation, proved from Theorem 3.3
date: 2026-09-12
status: complete — hand derivation, machine-verified for A = H, O, S, S′
verification: papers/mirror-sedenions/code/check19_erasure_proof.py
---

# CD(M(A)) ≅ CD(CD(A))

Notation is the paper's. A ∗-algebra is a unital real algebra with a linear
involution x ↦ x̄ satisfying (xy)‾ = ȳx̄ and 1̄ = 1. Write

    CD(A) = A ⊕ Ae,     (a,b)(c,d) = (ac − d̄b,  da + bc̄),     (a,b)‾ = (ā, −b),

and CD²(A) = CD(A) ⊕ CD(A)e′, whose elements are pairs (p,q) = p + qe′ with
p, q ∈ CD(A) and

    (p,q)(r,s) = (pr − s̄q,  sp + q r̄).                                    (∗)

**No associativity, alternativity or composition property of A is used anywhere
below.** Everything is formal manipulation of (∗) and the involution axioms.

---

## 1. A doubling-unit criterion

**Lemma 1.** Let B be a ∗-algebra, N ⊆ B a ∗-subalgebra, and u ∈ B with
B = N ⊕ Nu as vector spaces. Suppose for all n, m, m₁, m₂ ∈ N

&nbsp;&nbsp;(i) N is closed under the product and the involution;
&nbsp;&nbsp;(ii) n(mu) = (mn)u;
&nbsp;&nbsp;(iii) (mu)n = (mn̄)u;
&nbsp;&nbsp;(iv) (m₁u)(m₂u) = −m̄₂m₁;
&nbsp;&nbsp;(v) u² = −1 and ū = −u.

Then Ψ: CD(N) → B, Ψ(n, m) = n + mu, is an isomorphism of ∗-algebras.

*Proof.* Ψ is a linear bijection by B = N ⊕ Nu. Expanding and applying
(ii)–(iv),

    (n₁ + m₁u)(n₂ + m₂u)
      = n₁n₂ + n₁(m₂u) + (m₁u)n₂ + (m₁u)(m₂u)
      = (n₁n₂ − m̄₂m₁) + (m₂n₁ + m₁n̄₂)u,

which is exactly the CD product of (n₁, m₁) and (n₂, m₂). For the involution,
(mu)‾ = ū m̄ = −u m̄, and u m̄ = m u (shown in §2 for our case), so
(n + mu)‾ = n̄ − mu, the CD involution. ∎

---

## 2. M(A) is a doubling factor of CD²(A)

Inside CD²(A) write, for a, b ∈ A,

    ⟨a, b⟩ := ((a,0), (0,b))   =   a + (be)e′.

By **Theorem 3.3**, Φ(a + bℓ) = ā + (be)e′ = ⟨ā, b⟩ is a ∗-isomorphism of M(A)
onto N := {⟨a,b⟩ : a, b ∈ A} = A + A(ee′), which is therefore a ∗-subalgebra.

Two computations from (∗) that we use repeatedly:

    ⟨a₁,b₁⟩⟨a₂,b₂⟩ = ⟨ a₁a₂ − b̄₁b₂ ,  b₂ā₁ + b₁a₂ ⟩                        (2.1)
    ⟨a,b⟩‾ = ⟨ā, −b⟩                                                        (2.2)

*(Check of (2.1): with p=(a₁,0), q=(0,b₁), r=(a₂,0), s=(0,b₂), (∗) gives
pr = (a₁a₂,0), s̄q = (0,−b₂)(0,b₁) = (b̄₁b₂, 0), sp = (0, b₂ā₁),
q r̄ = (0,b₁)(ā₂,0) = (0, b₁a₂).)*

As a sanity check (2.1) reproduces Theorem 3.3's j-coordinate formula: putting
⟨a,b⟩ = a + b̄ j with j = ee′ = ⟨0,1⟩ gives
(a + bj)(c + dj) = (ac − bd̄) + (ad + c̄b)j, as stated there.

### 2.1 Set u := e′. Then CD²(A) = N ⊕ Nu

From (∗) with p=(a,0), q=(0,b), r=(0,0), s=(1,0):

    ⟨a,b⟩·e′ = ((0,−b), (a,0)).                                             (2.3)

Write [c,d] := ⟨c,d⟩e′ = ((0,−d),(c,0)). Then N occupies the slots
A ⊕ (Ae)e′ and Nu occupies Ae ⊕ Ae′, so

    N ⊕ Nu = A ⊕ Ae ⊕ Ae′ ⊕ (Ae)e′ = CD²(A).                               ✔

Note in particular **(ee′)e′ = −e**: the composite unit, doubled again, returns
the original doubling unit. This is the whole mechanism in one line.

### 2.2 The four identities

Throughout n = ⟨a,b⟩, m = ⟨c,d⟩, mᵢ = ⟨cᵢ,dᵢ⟩.

**(ii) n(mu) = (mn)u.** By (∗) with p=(a,0), q=(0,b), r=(0,−d), s=(c,0):

    pr = (0, −da),  s̄q = (c̄,0)(0,b) = (0, bc̄),  sp = (ca, 0),  q r̄ = (0,b)(0,d) = (−d̄b, 0)

so n(mu) = ((0, −da − bc̄), (ca − d̄b, 0)) = [ ca − d̄b , da + bc̄ ].
By (2.1), mn = ⟨ca − d̄b, bc̄ + da⟩, hence (mn)u = [ca − d̄b, bc̄ + da]. Equal. ✔

**(iii) (mu)n = (mn̄)u.** With p=(0,−d), q=(c,0), r=(a,0), s=(0,b):

    pr = (0,−dā),  s̄q = (0,−b)(c,0) = (0,−bc̄),  sp = (d̄b, 0),  q r̄ = (cā, 0)

so (mu)n = ((0, bc̄ − dā), (cā + d̄b, 0)) = [ cā + d̄b , dā − bc̄ ].
By (2.2), n̄ = ⟨ā,−b⟩; by (2.1), mn̄ = ⟨cā + d̄b, −bc̄ + dā⟩, so
(mn̄)u = [cā + d̄b, dā − bc̄]. Equal. ✔

**(iv) (m₁u)(m₂u) = −m̄₂m₁.** With p=(0,−d₁), q=(c₁,0), r=(0,−d₂), s=(c₂,0):

    pr = (−d̄₂d₁, 0),  s̄q = (c̄₂c₁, 0),  sp = (0, −d₁c₂),  q r̄ = (c₁,0)(0,d₂) = (0, d₂c₁)

so (m₁u)(m₂u) = ⟨ −c̄₂c₁ − d̄₂d₁ , d₂c₁ − d₁c₂ ⟩.
By (2.2) and (2.1), m̄₂m₁ = ⟨c̄₂,−d₂⟩⟨c₁,d₁⟩ = ⟨c̄₂c₁ + d̄₂d₁, d₁c₂ − d₂c₁⟩, whose
negative is the same. Equal. ✔

**(v)** e′² = −1 and ē′ = −e′ are immediate from (∗).

**Also u m̄ = m u**, needed for the involution in Lemma 1: with p=(0,0), q=(1,0),
r=(c̄,0), s=(0,−d), (∗) gives u m̄ = ((0,−d),(c,0)) = mu. ✔

---

## 3. The theorem

**Theorem (erasure).** For every ∗-algebra A,

> **CD(M(A)) ≅ CD(CD(A))** as ∗-algebras.

*Proof.* Lemma 1 applies to B = CD²(A), N = A + A(ee′), u = e′: hypothesis (i) is
Theorem 3.3, (ii)–(v) are §2.2, and B = N ⊕ Nu is §2.1. So CD(N) ≅ CD²(A). By
Theorem 3.3, N ≅ M(A), hence CD(M(A)) ≅ CD(N) ≅ CD²(A) = CD(CD(A)). ∎

The isomorphism is explicit: Ψ(n, m) = Φ(n) + Φ(m)e′. In particular it fixes A
and e′ pointwise and sends the **inner doubling unit ℓ ↦ ee′** — which is exactly
the σ found by the independent machine search at dimension 32
(e₁,e₂,e₄ ↦ themselves, e₈ ↦ e₂₄ = e₈ ⊕ e₁₆, e₁₆ ↦ e₁₆).

**Corollary (normal form).** Every word w in {CD, M} of length k applied to A
satisfies w(A) ≅ M^b(CD^{k−b}(A)), where b is the length of the maximal leading
(outermost) run of M's in w. Hence at level k there are at most **k + 1**
algebras rather than 2^k.

*Proof.* If w contains CD immediately outside an M, that occurrence is
CD(M(Y)) for some Y in the tower, which the Theorem replaces by CD(CD(Y)). This
strictly decreases the number of M's outside the leading run and leaves the
leading run untouched (nothing stands outside it). Iterate. ∎

---

## 4. Remarks

**Why it is not surprising, in hindsight.** M(A) is not a competitor to CD(A) but
a *second copy of the same kind of object inside the same ambient algebra*:
CD²(A) contains both A + Ae and A + A(ee′), and the two differ only in which unit
is called the doubling unit. Doubling again produces an algebra containing both
choices, and (ee′)e′ = −e converts one into the other. The mirror bit is genuine
exactly at the level where only one of the two units is present.

**What is *not* absorbed.** M itself does not erase: M(S) ≇ M(S′), machine-checked
at dimension 32. Lemma 1 needs u to be a doubling unit for N *in the standard
sense*; the mirror product is not of that form, so the argument gives nothing
for M(M(A)) — correctly.

**The split parameter is untouched by all of this.** The norm signature is an
isomorphism invariant and is inherited by every descendant, so no amount of
doubling repairs ε = −1. The proof above is indifferent to ε: it goes through
verbatim for the split CD, which is why CD(split S) ≅ CD(split mirror) was found
computationally.

**Scope.** The proof uses only (∗) and the involution axioms. A need not be
associative, alternative, or a composition algebra, and no positivity is used.
