import numpy as np
from itertools import product as iproduct, combinations
from cd import *
rng = np.random.default_rng(4)

def bits(g, n=4): return [(g >> i) & 1 for i in range(n)]

# ---------------------------------------------------------------- GL(4,2)
def gl42():
    mats = []
    for cols in iproduct(range(1, 16), repeat=4):
        # check invertibility over F2 : columns independent
        span = {0}
        okk = True
        for c in cols:
            if c in span: okk = False; break
            span |= {s ^ c for s in span}
        if okk: mats.append(cols)
    return mats
def apply(cols, g):
    r = 0
    for i in range(4):
        if (g >> i) & 1: r ^= cols[i]
    return r
GL = gl42()
print('|GL(4,2)| =', len(GL))

# ---------------------------------------------------------------- sign functions and associators
def signfun(name):
    sign, idx = sign_table(name)
    n = sign.shape[0]
    assert all(idx[i, j] == i ^ j for i in range(n) for j in range(n))
    return sign
def assoc_fun(sign):
    n = sign.shape[0]
    phi = np.zeros((n, n, n), dtype=int)
    for g in range(n):
        for h in range(n):
            for k in range(n):
                phi[g, h, k] = sign[g, h] * sign[g ^ h, k] * sign[h, k] * sign[g, h ^ k]
    return phi

def graded_iso(signA, signB):
    """Find (sigma, lambda) with  signB(sigma g, sigma h) lambda(g+h) = signA(g,h) lambda(g) lambda(h).
    Returns list of sigmas that work (and the count of lambdas each)."""
    n = signA.shape[0]
    fa = (signA < 0).astype(int)
    res = []
    for cols in GL:
        sg = [apply(cols, g) for g in range(n)]
        fb = np.array([[(signB[sg[g], sg[h]] < 0) for h in range(n)] for g in range(n)], dtype=int)
        # unknown mu(g), g=1..15 ; equations mu(g)+mu(h)+mu(g^h) = fa(g,h)+fb(g,h)  mod 2
        rows = []; rhs = []
        for g in range(1, n):
            for h in range(1, n):
                if g == h: continue
                r = np.zeros(n - 1, dtype=int); r[g - 1] ^= 1; r[h - 1] ^= 1; r[(g ^ h) - 1] ^= 1
                rows.append(r); rhs.append((fa[g, h] + fb[g, h]) % 2)
        # also g=h and g or h = 0 constraints: mu(0)=0 automatically; g==h : 2mu(g)+mu(0) = fa+fb -> need fa==fb there
        if any((fa[g, g] != fb[g, g]) for g in range(n)) or any(fa[0, g] != fb[0, g] or fa[g, 0] != fb[g, 0] for g in range(n)):
            continue
        A = np.array(rows, dtype=int); b = np.array(rhs, dtype=int)
        # solve over F2 by elimination
        M = np.hstack([A, b[:, None]]) % 2
        m, k = A.shape; piv = 0; pivcols = []
        for c in range(k):
            pr = None
            for r in range(piv, m):
                if M[r, c]: pr = r; break
            if pr is None: continue
            M[[piv, pr]] = M[[pr, piv]]
            for r in range(m):
                if r != piv and M[r, c]: M[r] ^= M[piv]
            pivcols.append(c); piv += 1
        consistent = not any(M[r, :k].sum() == 0 and M[r, k] for r in range(m))
        if consistent:
            res.append((cols, 2 ** (k - len(pivcols))))
    return res

sS = signfun('S'); sM = signfun('Sm')
phiS = assoc_fun(sS); phiM = assoc_fun(sM)

def indep(g, h, k):
    return len({0, g, h, k, g ^ h, g ^ k, h ^ k, g ^ h ^ k}) == 8
def count_assoc_indep(phi):
    c = 0; tot = 0
    for g, h, k in combinations(range(1, 16), 3):
        if indep(g, h, k):
            tot += 1
            if phi[g, h, k] == 1: c += 1
    return c, tot
def dependent_all_assoc(phi):
    return all(phi[g, h, k] == 1 for g in range(16) for h in range(16) for k in range(16) if not indep(g, h, k))
for nm, phi in [('S', phiS), ('Sm', phiM)]:
    c, tot = count_assoc_indep(phi)
    print(f'{nm}: associator +1 on {c} of {tot} independent basis triples (unordered); all dependent triples associate: {dependent_all_assoc(phi)}')
# trilinearity test
def is_trilinear(phi):
    f = (phi < 0).astype(int)
    for g, h, k, l in iproduct(range(16), repeat=4):
        if (f[g ^ l, h, k] != (f[g, h, k] ^ f[l, h, k])): return False
    return True
print('phi_S trilinear?', is_trilinear(phiS), '  phi_Sm trilinear?', is_trilinear(phiM))

# ---------------------------------------------------------------- graded automorphisms and graded isomorphism S vs Sm
autS = graded_iso(sS, sS); autM = graded_iso(sM, sM)
print(f'graded automorphisms: S: {len(autS)} sigmas x {autS[0][1]} sign choices = {len(autS)*autS[0][1]};  Sm: {len(autM)} sigmas x {autM[0][1]} = {len(autM)*autM[0][1]}')
iso = graded_iso(sS, sM)
print('graded isomorphisms S -> Sm:', len(iso))
# what do the sigmas of Aut(Sm) do to the founding octave V = {0..7}?
V = set(range(8))
images = set()
for cols, _ in autM:
    images.add(frozenset(apply(cols, g) for g in V))
print('number of distinct images of the founding octave under graded Aut(Sm):', len(images))
imagesS = set(frozenset(apply(cols, g) for g in V) for cols, _ in autS)
print('number of distinct images of the founding octave under graded Aut(S):', len(imagesS))
fix8 = all(apply(cols, 8) == 8 for cols, _ in autM)
print('all graded automorphisms of Sm fix l = e_8 (up to sign)?', fix8)

# ---------------------------------------------------------------- census of the 32 Bales products on top of the standard octonions
print('=== the 32 doubling products applied to the standard octonions ===')
def invariants(mul16, tag):
    register(tag, mul16, 16)
    try:
        sign = signfun(tag)
    except AssertionError:
        return None
    n = 16
    anti = all(sign[i, j] == -sign[j, i] for i in range(1, n) for j in range(1, n) if i != j)
    sq = all(sign[i, i] == -1 for i in range(1, n))
    one = basis(16, 0)
    unital = all(np.allclose(mul16(one, x), x) and np.allclose(mul16(x, one), x) for x in [rand(16, rng)])
    # x x* = N
    xxs = all(np.allclose(mul16(x, conj(x)), norm2(x) * one) for x in [rand(16, rng) for _ in range(3)])
    phi = assoc_fun(sign)
    c, tot = count_assoc_indep(phi)
    return dict(unital=unital, anti=anti, sq=sq, xxstar=xxs, assoc_indep=c, sign=sign)
classes = {}
rows = []
for f in range(8):
    for g in range(4):
        mul16 = double(mulO, f, g)
        inv = invariants(mul16, f'P{f}{g}')
        if inv is None:
            rows.append((f, g, 'not monomial')); continue
        key = None
        for kname, ksign in [('S', sS), ('Sm', sM)]:
            if len(graded_iso(ksign, inv['sign'])) > 0: key = kname
        rows.append((f, g, inv['unital'], inv['anti'], inv['sq'], inv['xxstar'], inv['assoc_indep'], key))
for r in rows:
    print('  f=%d g=%d' % r[:2], r[2:])
