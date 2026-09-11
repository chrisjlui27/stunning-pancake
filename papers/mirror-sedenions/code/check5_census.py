import numpy as np
from itertools import combinations
from cd import *
from f2iso import graded_isos, N_LAMBDA, GL, apply
rng = np.random.default_rng(5)

def signfun(name):
    sign, idx = sign_table(name)
    assert all(idx[i, j] == i ^ j for i in range(sign.shape[0]) for j in range(sign.shape[0]))
    return sign
sS = signfun('S'); sM = signfun('Sm')
print('sanity: Aut sigmas S', len(graded_isos(sS, sS)), 'Sm', len(graded_isos(sM, sM)), 'S->Sm', len(graded_isos(sS, sM)), '; lambdas per sigma', N_LAMBDA)

def rand_im8():
    v = rng.standard_normal(8); v[0] = 0; return unit(v)

def hyperplane_octaves(mul16):
    res = []
    for f in range(1, 16):
        H = [g for g in range(16) if bin(f & g).count('1') % 2 == 0]
        idx = np.array(H); comp = True; closed = True
        for _ in range(8):
            x = np.zeros(16); y = np.zeros(16); x[idx] = rng.standard_normal(8); y[idx] = rng.standard_normal(8)
            z = mul16(x, y)
            if not np.allclose(z[[i for i in range(16) if i not in H]], 0): closed = False
            if abs(norm2(z) - norm2(x) * norm2(y)) > 1e-8: comp = False
        res.append((f, closed, comp))
    return res

print('=== census of the 32 Bales products on top of the standard octonions ===')
print(' f g | unital anti sq xx* | #octaves (which) | ann dims on {a im ⊥ b im}, {a im, b any} | Der | class')
def der_dim_fast(name):
    T = struct(name); n = T.shape[0]
    rows = []
    for i in range(n):
        for j in range(n):
            eq = np.zeros((n, n, n))
            for m in range(n):
                eq[:, :, m][np.arange(n), np.arange(n)] += T[i, j, m]
            for p in range(n):
                eq[:, p, i] -= T[p, j, :]; eq[:, p, j] -= T[i, p, :]
            rows.append(eq.reshape(n, n * n))
    return nullity(np.vstack(rows))
summary = {}
for f in range(8):
    for g in range(4):
        tag = f'P{f}{g}'; mul16 = double(mulO, f, g); register(tag, mul16, 16)
        try:
            sign = signfun(tag)
        except AssertionError:
            print(f' {f} {g} | not monomial'); continue
        one = basis(16, 0)
        unital = all(np.allclose(mul16(one, x), x) and np.allclose(mul16(x, one), x) for x in [rand(16, rng)])
        anti = all(sign[i, j] == -sign[j, i] for i in range(1, 16) for j in range(1, 16) if i != j)
        sq = all(sign[i, i] == -1 for i in range(1, 16))
        xxs = all(np.allclose(mul16(x, conj(x)), norm2(x) * one) and np.allclose(mul16(conj(x), x), norm2(x) * one) for x in [rand(16, rng) for _ in range(3)])
        octs = hyperplane_octaves(mul16)
        noct = [ff for ff, cl, co in octs if co]
        ann1 = set(); ann2 = set()
        for _ in range(6):
            a = rand_im8(); b = rand_im8(); b = unit(b - (b @ a) * a)
            ann1.add(nullity(L(tag, np.concatenate([a, b]))))
            ann2.add(nullity(L(tag, np.concatenate([rand_im8(), unit(rand(8, rng))]))))
        cls = []
        if graded_isos(sS, sign): cls.append('S')
        if graded_isos(sM, sign): cls.append("S'")
        dd = der_dim_fast(tag)
        print(f' {f} {g} | {unital!s:5} {anti!s:5} {sq!s:5} {xxs!s:5} | {len(noct)} {noct} | {sorted(ann1)} {sorted(ann2)} | {dd} | {cls}')
        summary[(f, g)] = (cls, len(noct), dd)
print('S-class:', [k for k, v in summary.items() if v[0] == ['S']])
print("S'-class:", [k for k, v in summary.items() if v[0] == ["S'"]])
print('neither:', [k for k, v in summary.items() if not v[0]])

# --- explicit simple isomorphisms between the four S'-type products (maps (a,b) -> (s1 a, s2 b), s in {id, conj, -id, -conj})
print("=== explicit isomorphisms of the form (a,b) -> (s1(a), s2(b)) between S'-type products and Sm ===")
ops = {'id': lambda a: a, 'conj': conj, '-id': lambda a: -a, '-conj': lambda a: -conj(a)}
for (f, g), v in summary.items():
    if v[0] != ["S'"]: continue
    mul16 = double(mulO, f, g)
    found = []
    for n1, s1 in ops.items():
        for n2, s2 in ops.items():
            phi = lambda x: np.concatenate([s1(x[:8]), s2(x[8:])])
            good = all(np.allclose(phi(mulSm(x, y)), mul16(phi(x), phi(y))) for x, y in [(rand(16, rng), rand(16, rng)) for _ in range(4)])
            if good: found.append((n1, n2))
    print(f'  P{f}{g}: Sm -> P{f}{g} via (a,b) -> ({found})')
for (f, g), v in summary.items():
    if v[0] != ['S']: continue
    mul16 = double(mulO, f, g)
    found = []
    for n1, s1 in ops.items():
        for n2, s2 in ops.items():
            phi = lambda x: np.concatenate([s1(x[:8]), s2(x[8:])])
            good = all(np.allclose(phi(mulS(x, y)), mul16(phi(x), phi(y))) for x, y in [(rand(16, rng), rand(16, rng)) for _ in range(4)])
            if good: found.append((n1, n2))
    print(f'  P{f}{g}: S -> P{f}{g} via (a,b) -> ({found})')
