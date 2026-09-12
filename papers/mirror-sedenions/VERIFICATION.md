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

### check4 — cocycle and graded isomorphisms ✅
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
the question is restated. **Confirmed by check12 below:** those four products have
28 failing quaternionic-line pairs each, so they are among the 24 rejected.

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

### check9 — final structural checks ✅ (after one fix — see below)
- `PASS` alt_x on M(Q) and on M(Q)^⊥, the two block formulas (5), (6) ✓
- `PASS` L_x preserves the splitting M(Q) + M(Q)^⊥
- `PASS` ker alt_x = C_a + (b C_a)ℓ, 4-dimensional for generic x, and **is a
  composition subalgebra (= H)** ✓
- `PASS` S′: xy = 0 ⟹ yx = 0 — annihilation is two-sided ✓ (Remark 5.3)
- `PASS` M(H): (a,b) ↦ (a, qb) is an automorphism; in S′ it is **not** ✓ (Thm 8.1(3))
- dim nucleus = 1 and dim centre = 1 for both
- Uniform P1^T tower: dimension-8 stage is **not** a composition algebra, Der = 6
  at both dimensions 8 and 16 (against 14 for S′) ✓ (Remark 3.8)
- For x ∈ Z(S): dim Ann_S = 4, dim Ann_S′ = 2, **intersection 0**

#### Second bug found — again in the check, not the paper

    FAIL  Sm: l is alternative; S: l is not

The assertion is wrong. ℓ = 0 + 1·ℓ lies in **R + Oℓ**, which Table 1 lists as
alternative for **both** algebras — so ℓ is alternative in both, as direct
computation confirms. The element that actually separates them is a, b ∈ C_u with
Im a ≠ 0 and b ≠ 0: it lies in S's larger alternative set ⋃_u(C_u + C_uℓ) but
outside S′'s O ∪ (R + Oℓ). Verified:

| element | alternative in S | alternative in S′ |
|---|---|---|
| ℓ | True | True |
| R + Oℓ, generic b | True | True |
| O, generic a | True | True |
| **u + uℓ** (u an imaginary unit) | **True** | **False** |
| a imaginary, b generic | False | False |

Replaced with the two correct assertions; both pass. **Table 1's alternative-element
rows are confirmed** — the original check simply tested the wrong element.

### check10 — the orientation tree ✅
Reproduces the 32-product census independently, in agreement with check5.

### check11 — tree isomorphism ✅
- **CD(M(H))** (standard double of the quasi-octonions) is graded-isomorphic to **S**
- **M(M(H))** (mirror double of them) is graded-isomorphic to **neither S nor S′**

This is the third dimension-16 algebra of Open Question 2, confirmed distinct.

### check12 — the quaternionic-line condition ✅
Failing ordered basis pairs per product. **Exactly 8 of the 32 have zero
failures**, and they are precisely the S-class and the S′-class:

    zero failures:  (0,0) (3,1) (4,2) (7,3)   = S
                    (1,1) (2,0) (5,3) (6,2)   = S′
    the four 8-octave, Der-14 "neither" products:
                    (1,3) (2,2) (5,1) (6,0)   = 28 failing pairs each

So 32 − 8 = **24 rejected formulas** ✓, matching Appendix A, and the precision
point raised under check5 is settled: the four extra products with eight octaves
and dim Der = 14 are excluded precisely by the quaternionic-line condition.

Also: `S: ker alt_x (dim 8) is a subalgebra: True; composition: True` ✓

### sym_spectrum — symbolic eigenvalues ✅
alt_x is symmetric. Characteristic polynomial

    λ⁴ (4a₁²b₀² + 4a₁²b₁² − λ²)⁴ (4a₁²b₀² + 4a₁²b₁² + 4a₁²b₂² − λ²)²

with roots

| eigenvalue | multiplicity | Theorem 4.1 |
|---|---|---|
| ±2\|a₁\|√(b₀²+b₁²+b₂²) | 2 each | ±2\|Im a\|\|b\| |
| ±2\|a₁\|√(b₀²+b₁²) | 4 each | ±2\|Im a\|\|b∥\| |
| 0 | 4 | N(x) |

**Exactly Theorem 4.1**, symbolically. ✓

## Summary

**Every check reproduces the paper's claim. No mathematical error was found.**

Two discrepancies surfaced, and both were errors in the verification scripts
rather than in the mathematics:

1. `check7_misc.py` computed τ with \|a\| instead of \|Im a\| — masked at
   check6's sample points because they all have Re a = 0. Fixed; Theorem 4.1
   now verifies at 2.4e-15 over 2000 random points.
2. `check9_final.py` asserted that ℓ is alternative in S′ but not in S. ℓ is
   alternative in **both**; the discriminating element is u + uℓ. Fixed; Table 1
   is confirmed.

Both fixes are marked in the source with a dated comment. The scripts now run
clean — no `FAIL` lines anywhere.

One substantive note for v2, under check5/check12: eight octaves together with
dim Der = 14 does **not** characterise S and S′ among the Bales products; four
others share both invariants. The quaternionic-line condition is what excludes
them, and Open Question 2's phrasing should keep that qualifier explicit.

---

# Verification run — 2026-09-12 (degenerate subalgebras)

Environment: Linux 6.18 x86_64, Python 3.11, numpy 2.4.6. All scripts in `code/`,
run from that directory. New library `landscape.py`; new scripts `check21`–`check25`.
Full logs of the long runs are in the session scratchpad and summarised here.

### landscape.py — self-tests ✅
`dbl` reproduces the sign tables of S, T, S′ and M(H) from `cd.py` bit for bit. The
associator-pattern isomorphism search agrees with `f2iso.py`: graded automorphism σ-counts
168 (S), 168 (S′), 0 (S → S′); 60/60 random pairs of Bales products on O agree.
Quaternion property holds for S, S′, T.

### check21 — basis-subalgebra census by graded isomorphism ✅
| A_n | dim 4 | dim 8 | dim 16 | dim 32 |
|---|---|---|---|---|
| A_4 | H 35 | O 8, P4 7 | | |
| A_5 | H 155 | O 50, P4 105 | S 16, S′ 1, X16.2 7, X16.3 7 | |
| A_6 | H 651 | O 310, P4 1085 | S 186, S′ 31, X16.2 217, X16.3 217 | T 32, M(S) 1, M(S′) 1, X32.4 1, X32.3 7, X32.5 7, X32.6 7, X32.7 7 |
| A_7 | | | S 2046, S′ 651, X16.2 4557, X16.3 4557 (11 811 subgroups, 442 s) | T 714, M(S) 63, M(S′) 63, X32.4 63, X32.3/5/6/7 441 each (2667 subgroups, 11 s with the pruned search); dim 64: 16 classes, multiplicities 64, 1⁷, 7⁸ (127 subgroups, 2 s; X64.0 = A_6) |

Cawagas et al.'s 16/7/7/1 for T reproduced; Wilmot's Theorem 8 counts (105 = 7·15,
1085 = 7·155) reproduced.

### check22 — class invariants, absorption, Wilmot triads ✅
Invariant table as in `synthesis/degenerate-subalgebras.md` (nonassociative ordered
triples, two-term zero divisors with annihilator profile, Der, σ-count, alternative /
composition flags, codim-1 census). Absorption: A_5 — 15 hyperplanes through the top unit
all ≅ S; A_6 — 31 through the top all ≅ T. Wilmot's triads (e₁,e₁₀,e₂₈) ⊂ A_5 and
(e₉,e₁₈,e₃₆) ⊂ A_6 both classify as P4, with explicit σ.

### check23 — relative mirrors, Lemma-1 identities, words, Bales products ✅
Relative-mirror table as in the synthesis. Lemma-1 identities (ii)–(v) hold on all basis
pairs of N = K + K(e_c e), for every hyperplane K, with A = O, P4, S, S′, X16.2, X16.3, T,
X32.7 and the Bales-rejected P(1,3)(H) (anticommutative, no quaternion property).
Words: CC(H) = CM(H) = S, MC(H) = S′, MM(H) = X16.3; all 16 length-4 words on R give
S / S′ / X16.3 by leading-M count 0 / 1 / ≥ 2. Bales's 32 products: on every base tested
(H, O, P4, S, S′, X16.2, X16.3) 24 fail the quaternion property and the 8 others give
4 × standard + 4 × mirror: H → O, P4; O → S, S′; P4 → S, X16.3; S → T, M(S);
S′ → T, M(S′); X16.2 → T, X32.6; X16.3 → T, X32.7.

### check24 — incidence and Der structure ✅
Every P4 hyperplane of S, S′, X16.2, X16.3 carries 12 internal zero-divisor pairs;
(dim Ann, multiplicity) ∈ {(2,1), (4,2), (6,3)} throughout. Der(P4), Der(X16.2),
Der(X16.3): dimension 6, perfect, negative-definite Killing form — compact semisimple, so(4).

### check25 — the 64-dimensional landscape ✅
The 63 relative mirrors R_{A_6}(K) fall into 15 fingerprint groups (sizes 1,1,1,1,1,1,1 and
7,7,7,7,7,7,7,7), each a single graded-isomorphism class by the associator search at k = 6;
|L_5| = 16. The fingerprints (nonassociative ordered triples, two-term ZD count):
K = T founding (138840, 3160) = M(T); K = M(S) (149592, 3280) = M²(S); K = M(S′) (149592,
3392) = M³(O); K = T f=8,16,24 (118680; 3276, 3220, 3332); K = T 7-orbits (118680; 3420,
3468, 3476, 3524); K = X32.3 / X32.5 / X32.4 (117336; 3480, 3528, 3336); K = X32.6
(112728, 3536); K = X32.7 (100440, 3584). Run time under a minute with the pruned search.

### check26 — split relative erasure ✅
Lemma-1 identities for N = K + K(e_c e) hold for all hyperplanes K with inner algebra S,
split S, split M(O), split O and outer ε = ±1 (all 15/15 resp. 7/7). Neither e_p² = −1 nor
positivity is needed.

### Tool note
`iso_search_pruned` (vertex/pair invariants of the associator pattern, rarest-first source
basis) replaced the plain backtracking midway; it agrees with the plain search and with
`f2iso.py` on every test (168 / 168 / 0; T: 168) and is 100–500× faster at dimension 32.
`graded_iso` and `sigma_count` now use it.
