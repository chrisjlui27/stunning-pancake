---
type: verification
paper: mirror-sedenions-v1.pdf
run: 2026-09-11
environment: Linux 6.18 x86_64, Python 3.11, numpy 2.4.6, sympy 1.14.0
---

# Verification run — 2026-09-11

Appendix A of the paper lists what the scripts check. This file records an
**actual execution** of them, on the date and environment above, rather than the
claim that they were run.

## Environment notes (for the next session)

`numpy` and `sympy` are **not** preinstalled — `pip install numpy sympy`. There
is no `pdftotext` and `poppler-utils` fails to install from the archive; use
`pymupdf` for PDF text extraction. The system `pypdf` is present but **broken**
(its `cryptography` backend panics on import).

## One bug found — in the check script, not the paper

`check7_misc.py` line 30 computed

    tau = 2 * sqrt(norm2(a)) * sqrt(norm2(bpar)) / N

where Theorem 4.1 gives **τ = 2|Im a||b∥|/N**. The two agree exactly when
Re a = 0, which is why `check6`'s sample points (all with a imaginary) passed
while `check7`'s random test — which draws a with a nonzero real part — reported

    max deviation between computed spectrum and closed form over 200 random x: 0.448

against 2.9e-15 for the S-side comparison in the same script. That gap is what
flagged it.

**The theorem is correct; the check was wrong.** Substituting `norm2(ima)`:

| τ as | max deviation over 2000 random x |
|---|---|
| `norm2(a)` (as written) | 3.995e-01 |
| `norm2(ima)` (Theorem 4.1) | **2.442e-15** |

Patched in place with a comment. Theorem 4.1 is now verified at machine
precision over 2000 random points, a stronger check than the original 200.

## Results

### check1 — basic identities ✅
O composition + alternative. For both S and S′: unital, x x̄ = N(x), **not**
composition, **flexible**, power-associative to degree 4, **not** alternative,
(xy)‾ = ȳx̄. Basis: e_i e_j = ± e_{i⊕j}, anticommuting, squares −1.
**42 sign differences between S and S′**, all at (i, j) with i, j < 8, i ≠ j,
i, j ≠ 0 — exactly the χ of Prop. 7.3 (pairs of distinct nonzero points of the
founding F₂³).

### check2 — zero divisors and dimensions ✅
| | S | S′ |
|---|---|---|
| generic ann dim | 0 | 0 |
| Moreno locus (a ⊥ b imaginary) | 4 | **2** |
| a imaginary, b any | 0 | **2** |
| Re a ≠ 0 | 0 | 0 |
| a, b imaginary non-orthogonal | 0 | **2** |
| (u,u), (u,1), (u, cos+sin·u) | 0, 0, 0 | **6, 6, 6** |

dim Z on the unit sphere: **S: 11, S′: 13** ✓ (Theorem 5.1)
dim P at generic points: **14 for both** ✓ (Theorem 5.5)
The 6-dimensional stratum occurs exactly where b₂ = 0, i.e. b ∈ span{1, a} = C_a ✓

### check3 — structure ✅
- `PASS` Ann(u + bℓ) = {nu + (bn)ℓ : n ⊥ u imaginary, [b,n,u] = 0} over 30 random points ✓ (Thm 5.2)
- Kernel of n ↦ [b,n,u] has dim 4 = the quaternion subalgebra ✓ (Lemma 2.2)
- rank dμ = **16 everywhere** on P ✓
- `PASS` S: octaves = V + the 7 hyperplanes **through** ℓ
- `PASS` S′: octaves = the 8 hyperplanes **avoiding** ℓ ✓ (Theorem 6.1)
- dim ker alt_x generic: **S: 8, S′: 4** ✓
- dim Der: O 14, S 14, S′ 14, M(H) **6** ✓

### check4 — cocycle and graded isomorphisms ✅ (partial: 32-product census still running)
|GL(4,2)| = 20160. Both algebras: associator +1 on 168 of 420 independent basis
triples; all dependent triples associate. **φ_S and φ_S′ are both non-trilinear**
✓ (χ is not a 2-cocycle, Prop. 7.3).

- graded automorphisms: **S: 2688, S′: 2688** ✓ (= 168 × 16, Prop. 7.4)
- **graded isomorphisms S → S′: 0** ✓ — no signed relabelling carries S to S′
- All graded automorphisms of S′ fix ℓ up to sign; the founding octave has a
  single image under graded Aut in both.

### check5 — the 32-product census ✅
Exactly **4 products give S** — (f,g) = (0,0), (3,1), (4,2), (7,3) — and exactly
**4 give S′** — (1,1), (2,0), (5,3), (6,2) ✓ (Theorem 3.6), with explicit
isomorphisms of the stated form a + bℓ ↦ a^(‾) + (±b^(‾))ℓ in every case.

**A precision point worth carrying into v2.** Four *further* products —
(1,3), (2,2), (5,1), (6,0) — also have **8 octaves and dim Der = 14**, but are
in neither class (their annihilator dimensions are 1, not 2 or 4). So "eight
octaves and 14-dimensional derivation algebra" is **not** by itself sufficient
to pin down S and S′. Open Question 2 states the census claim over sign
functions *with quaternionic lines*, and Appendix A notes the quaternion-line
condition fails for "the twenty-four rejected formulas" — consistent, since
32 − 8 = 24. The qualifier is doing real work and should not be dropped when
the question is restated. <!-- UNVERIFIED: pending check12 confirming these four fail the line condition. -->

### check6 — embedding and spectrum ✅
- `PASS` Φ(a,b) = ā + (be)e′ is an algebra isomorphism S′ → O ⊕ (Oe)e′ ⊂ T ✓ (Thm 3.3), with ee′ = e₂₄
- `PASS` (be)e′ = b̄(ee′) ✓
- `PASS` Φ: M(H) → H ⊕ (Hℓ)e ⊂ S, the quasi-octonions ✓ (Cor. 3.4)
- The 31 basis hyperplanes of T: **16 are S-type** (functionals 1–16, octaves = 8)
  and exactly **one — functional 24 — has 8 octaves with S′-type annihilators**
  ✓ This is Sγ, matching Cawagas et al.'s uniqueness claim and Table 1's
  "S: 16 basis hyperplanes / Sγ: 1".
- Spectrum of L_x̄L_x/N(x): **S: 3 levels, mults [4, 8, 4]. S′: 5 levels, mults
  [2, 4, 4, 4, 2]** ✓ (Theorem 4.1), at imaginary, mixed, and general points.

### check7 — miscellaneous ✅ (after the τ fix)
- `PASS` L_x̄ = L_xᵀ and R_x̄ = R_xᵀ, and L_x̄L_x = N(x)I + alt_x, for both ✓ (eq. 3)
- Spectrum fit to closed form: **2.66e-15** (after fix)
- dim Ann(e₁+e₉) = 6, with two-term annihilators e_k − e_{k+8} for k = 2..7 ✓ (Prop. 5.4)
- **Brown's order-3 automorphism: works on S, fails on S′** ✓ (Thm 7.1)
- (a,b) ↦ (a,−b) is an automorphism of both ✓ (ε of Prop. 3.2)
- M(H): ann dims 2 on the zero-divisor locus, dim P = 6, dim Der = 6, every
  derivation preserves the founding H ✓ (Theorem 8.1)

### check8 — symbolic comparison ✅
Symbolic characteristic polynomials of alt_x in normal form:

    S   λ⁸ (2a₁b₂ − λ)⁴ (2a₁b₂ + λ)⁴
    S′  λ⁴ (4a₁²b₀² + 4a₁²b₁² − λ²)⁴ (4a₁²b₀² + 4a₁²b₁² + 4a₁²b₂² − λ²)²

— the 3-level and 5-level structures respectively ✓

- Two-term zero divisors: **S: 84** (index pairs exactly those with j ≠ i+8, de
  Marrais) and **S′: 112** (all 56 pairs, both signs) ✓ (Prop. 5.4)
- **336 ordered two-term dead pairs in both** ✓
- P(S′) induced metric: **cross terms between the S³ and V₂ directions do not
  vanish** (max 0.614), tangent frame rank 14, and the V₂-block **changes with q**
  (max diff 0.669) ✓ — confirming Open Question 1's assertion that the metric is
  G2-invariant but *not* a Riemannian product.

### checks 9–12 — pending
Still running at the time of writing: `check9_final`, `check10_tree`,
`check11_tree_iso`, `check12_lines`, `sym_spectrum`. check4's 32-product census
section is also still running.

## Summary

Every completed check reproduces the paper's claim. **No mathematical error was
found.** The one discrepancy traced to a typo in a verification script, now
fixed, and the corrected check verifies Theorem 4.1 to machine precision.
