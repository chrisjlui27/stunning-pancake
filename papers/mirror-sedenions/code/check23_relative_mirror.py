"""
check23 -- the relative mirror  R_A(K) = K + K(e_c e)  inside CD(A), the relative-erasure
identities, the {CD,M}-word and Bales-product identification of the degenerate classes.
"""
import pickle, sys, time
import numpy as np
from collections import Counter
from landscape import *
import cd as CDLIB
reg = pickle.load(open('landscape_registry_n6.pkl', 'rb')); classes = reg['classes']
byk = {k: {c['label']: c['w'] for c in lst} for k, lst in classes.items()}
def classify(w):
    k = w.shape[0].bit_length() - 1
    if k not in byk: return '?'
    A = assoc_pattern(w)
    for lab, rep in byk[k].items():
        if iso_search(assoc_pattern(rep), A) is not None: return lab
    return '?'
def hyperplane_basis(N, f):
    H = [g for g in range(N) if bin(f & g).count('1') % 2 == 0]
    basis = []; sp = {0}
    for g in H:
        if g not in sp: basis.append(g); sp |= {s ^ g for s in sp}
    return tuple(basis)

# ------------------------------------------------------------------ 1. relative mirrors
def relative_mirror(w, f):
    """R_A(K) for K = ker f: the span of {e_p : p in K} u {e_p e_c e : p in K} inside CD(A),
    i.e. the graph subgroup {p + f(p) top} of F_2^{n+1}."""
    N = w.shape[0]; W = dbl(w); top = N
    c = next(g for g in range(1, N) if bin(f & g).count('1') % 2 == 1)
    basis = list(hyperplane_basis(N, f)) + [c ^ top]     # K-basis and (e_c e)
    return restrict(W, tuple(basis))

print('=== relative mirrors R_A(K), K running over the basis hyperplanes of A ===')
for lab, w in list(byk[3].items()) + list(byk[4].items()) + [('T', byk[5]['T'])]:
    N = w.shape[0]; tab = Counter()
    for f in range(1, N):
        K = classify(restrict(w, hyperplane_basis(N, f)))
        # distinguish the founding-copy hyperplanes: f a power of two means K = {p : bit i of p = 0}
        pos = 'founding' if f == N // 2 else ('through-top' if f < N // 2 else 'avoiding-top')
        tab[(K, pos, classify(relative_mirror(w, f)))] += 1
    print(f'  A = {lab:6s}:')
    for (K, pos, R), v in sorted(tab.items()): print(f'      K = {K:6s} ({pos:12s}) x{v:2d}  ->  R_A(K) = {R}')
    sys.stdout.flush()

# ------------------------------------------------------------------ 2. relative-erasure identities
print('\n=== Lemma-1 identities for N = R_A(K), u = e (outer unit) in B = CD(A), on basis elements ===')
def lemma1_check(w, f):
    N = w.shape[0]; W = dbl(w); B = 2 * N; top = N
    m = mul_fn(W)
    def E(i):
        v = np.zeros(B); v[i] = 1; return v
    def cj(x): return CDLIB.conj(x)
    c = next(g for g in range(1, N) if bin(f & g).count('1') % 2 == 1)
    Nidx = [p for p in range(N) if bin(f & p).count('1') % 2 == 0]
    Nidx = Nidx + [p ^ c ^ top for p in Nidx]
    u = E(top); ok = {'ii': True, 'iii': True, 'iv': True, 'v': True, 'umbar': True}
    ok['v'] = np.allclose(m(u, u), -E(0)) and np.allclose(cj(u), -u)
    for a in Nidx:
        for b in Nidx:
            n, mm = E(a), E(b)
            ok['ii'] &= np.allclose(m(n, m(mm, u)), m(m(mm, n), u))
            ok['iii'] &= np.allclose(m(m(mm, u), n), m(m(mm, cj(n)), u))
            ok['iv'] &= np.allclose(m(m(n, u), m(mm, u)), -m(cj(mm), n))
        ok['umbar'] &= np.allclose(m(u, cj(E(a))), m(E(a), u))
    return ok
tests = [('O', byk[3]['O']), ('P4', byk[3]['P4']), ('S', byk[4]['S']), ("S'", byk[4]["S'"]), ('X16.2', byk[4]['X16.2']), ('X16.3', byk[4]['X16.3']), ('T', byk[5]['T']), ('X32.7', byk[5]['X32.7'])]
for lab, w in tests:
    N = w.shape[0]; allok = Counter()
    for f in range(1, N):
        r = lemma1_check(w, f); allok[tuple(sorted(r.items()))] += 1
    print(f'  A = {lab:6s}: {dict(allok)}')
# and for a Bales-rejected (non-quaternion-property) base, to see what the identities need
wrej = table_from_fn(CDLIB.double(CDLIB.mulH, 1, 3), 8)   # P(1,3) applied to H
print('  Bales P(f=1,g=3) on H: quaternion property', quaternion_property(wrej), ' anticommutative', is_anticomm(wrej))
allok = Counter()
for f in range(1, 8): allok[tuple(sorted(lemma1_check(wrej, f).items()))] += 1
print(f'  A = P13(H): {dict(allok)}')

# ------------------------------------------------------------------ 3. {CD,M} words and Bales products
print('\n=== {CD,M}-words (outermost letter first) ===')
wH = cd_tower(2); wR = np.ones((1, 1), dtype=np.int8)
for base_name, base in [('H', wH), ('O', cd_tower(3)), ('R', wR)]:
    L = {'H': 2, 'O': 1, 'R': 4}[base_name]
    for wd in [''.join(t) for t in __import__('itertools').product('CM', repeat=L)]:
        print(f'  {wd}({base_name}) = {classify(word(wd, base))}', end=';')
    print()

print('\n=== the 32 Bales products applied once to each class (cd.py numbering (f,g); standard = (7,3), mirror = (5,3)) ===')
def bales(w, f, g):
    return table_from_fn(CDLIB.double(mul_fn(w), f, g), 2 * w.shape[0])
for lab, w in [('H', wH), ('O', byk[3]['O']), ('P4', byk[3]['P4']), ('S', byk[4]['S']), ("S'", byk[4]["S'"]), ('X16.2', byk[4]['X16.2']), ('X16.3', byk[4]['X16.3'])]:
    out = Counter(); qp = Counter(); anti = Counter()
    t0 = time.time()
    for f in range(8):
        for g in range(4):
            try: W = bales(w, f, g)
            except AssertionError: out['non-monomial'] += 1; continue
            q = quaternion_property(W); a = is_anticomm(W)
            lab2 = classify(W) if (q and a) else ('no-QP' if a else 'not-anticomm')
            out[lab2] += 1; qp[(f, g)] = lab2
    print(f'  base {lab:6s}: {dict(out)}   [{time.time()-t0:.0f}s]')
    if lab in ('O', 'P4'):
        print('      by (f,g):', {k: v for k, v in qp.items() if v not in ('no-QP',)})
    sys.stdout.flush()
