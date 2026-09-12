"""
check13 -- Wilmot's "12 zero divisors per quasi-octonion, seven copies" decomposition,
tested in both S and S'.

Wilmot (arXiv:2505.11747) accounts for the sedenions' 84 two-term zero divisors as
12 per quasi-octonion subalgebra x 7 quasi-octonion subalgebras.  S' has 112.  This
script asks where the difference comes from.

Answer: the "12 per quasi-octonion" holds verbatim in BOTH algebras, and so does the
incidence total 7 x 24 = 168 signed.  The difference is purely the multiplicity with
which the seven quasi-octonion hyperplanes overlap.
"""
import numpy as np
from collections import Counter
from cd import *
rng = np.random.default_rng(13)

HP = {f: [g for g in range(16) if bin(f & g).count('1') % 2 == 0] for f in range(1, 16)}

def is_composition(name, H):
    for _ in range(25):
        u = np.zeros(16); v = np.zeros(16)
        u[H] = rng.standard_normal(8); v[H] = rng.standard_normal(8)
        if abs(norm2(mul(name, u, v)) - norm2(u) * norm2(v)) > 1e-8:
            return False
    return True

def two_term_zds(name):
    return [(i, j, s) for i in range(1, 16) for j in range(i + 1, 16) for s in (1, -1)
            if nullity(L(name, basis(16, i) + s * basis(16, j))) > 0]

def ok(label, cond): print(('PASS ' if cond else 'FAIL ') + label)

report = {}
for name, lab in (('S', 'S'), ('Sm', "S'")):
    Z  = two_term_zds(name)
    qo = [f for f in HP if not is_composition(name, HP[f])]
    pairs_per = [len(set((i, j) for i, j, s in Z if i in HP[f] and j in HP[f])) for f in qo]
    mult = Counter(sum(1 for f in qo if i in HP[f] and j in HP[f]) for (i, j, s) in Z)
    report[name] = (Z, qo, mult)
    print(f"\n=== {lab} ===")
    print(f"  two-term zero divisors: {len(Z)} signed, {len(set((i,j) for i,j,_ in Z))} index pairs")
    ok(f"{lab}: exactly 7 quasi-octonion basis hyperplanes", len(qo) == 7)
    ok(f"{lab}: exactly 12 zero-divisor index pairs in EVERY quasi-octonion hyperplane"
       f"  (Wilmot's 12)", pairs_per == [12] * 7)
    ok(f"{lab}: incidence total = 7 x 24 = 168 signed",
       sum(k * v for k, v in mult.items()) == 168)
    print(f"  multiplicity profile (how many of the 7 contain each zero divisor):")
    for k in sorted(mult): print(f"      in {k}: {mult[k]:4d} signed zero divisors")
    ok(f"{lab}: every zero divisor lies in at least one quasi-octonion hyperplane",
       0 not in mult)

# the structural statement
ZS = set((i, j) for i, j, _ in report['S'][0])
Zm, qo_m, _ = report['Sm']
m1 = sorted(set((i, j) for (i, j, s) in Zm if sum(1 for f in qo_m if i in HP[f] and j in HP[f]) == 1))
m3 = sorted(set((i, j) for (i, j, s) in Zm if sum(1 for f in qo_m if i in HP[f] and j in HP[f]) == 3))
print("\n=== the split of S' ===")
ok("S: uniform multiplicity 2, so 168/2 = 84", set(report['S'][2]) == {2})
ok("S': multiplicities are exactly {1, 3}", set(report['Sm'][2]) == {1, 3})
ok("S': the multiplicity-1 pairs are EXACTLY de Marrais's 42 assessors (the S-shared ones)",
   set(m1) == ZS and len(m1) == 42)
ok("S': the multiplicity-3 pairs are EXACTLY the 14 new to S', i.e. (i, i+8) and (i, 8)",
   len(m3) == 14 and all(j == i + 8 or j == 8 for i, j in m3))
print(f"  84*1 + 28*3 = {84*1 + 28*3} = 168; union = 84 + 28 = {84+28} signed = 56 pairs")
