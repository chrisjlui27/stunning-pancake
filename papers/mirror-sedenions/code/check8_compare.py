import sympy as sp, numpy as np
from itertools import combinations, product as iproduct
from cd import *
rng = np.random.default_rng(8)

# symbolic spectrum for S in the same normal form
for name in ['S', 'Sm']:
    T = np.rint(struct(name)).astype(int)
    a0, a1, b0, b1, b2 = sp.symbols('a0 a1 b0 b1 b2', real=True)
    x = [0] * 16; x[0] = a0; x[1] = a1; x[8] = b0; x[9] = b1; x[10] = b2
    def Lmat(v):
        M = sp.zeros(16, 16)
        for i in range(16):
            if v[i] == 0: continue
            for j in range(16):
                for k in range(16):
                    if T[i, j, k]: M[k, j] += v[i] * T[i, j, k]
        return M
    xb = [x[0]] + [-x[i] for i in range(1, 16)]
    N = a0**2 + a1**2 + b0**2 + b1**2 + b2**2
    A = sp.expand(Lmat(xb) * Lmat(x) - N * sp.eye(16))
    lam = sp.symbols('lam')
    cp = sp.factor((A - lam * sp.eye(16)).det(method='berkowitz'))
    print(name, 'char poly of alt_x =', cp)

# two-term dead pairs  (e_i ± e_j)(e_k ± e_l) = 0 , i<j, k<l, all indices nonzero
def e(i): return basis(16, i)
for name in ['S', 'Sm']:
    cnt = 0; xs = set(); examples = []
    for i, j in combinations(range(1, 16), 2):
        for s in [1, -1]:
            x = e(i) + s * e(j)
            for k, l in combinations(range(1, 16), 2):
                for t in [1, -1]:
                    y = e(k) + t * e(l)
                    if np.allclose(mul(name, x, y), 0):
                        cnt += 1; xs.add((i, j, s))
                        if len(examples) < 4: examples.append(f'(e{i}{s:+d}e{j})(e{k}{t:+d}e{l})=0')
    print(f'{name}: ordered two-term dead pairs: {cnt}; distinct two-term dead lights: {len(xs)}; e.g. {examples}')
    # which index pairs {i,j} carry a dead light?
    pairs = sorted(set((i, j) for i, j, s in xs))
    print('   index pairs (i,j):', pairs)

# induced metric on P(S') in coordinates (u, n, q): is it a Riemannian product?  numeric check
def rand_im8():
    v = rng.standard_normal(8); v[0] = 0; return unit(v)
def point(u, n, q):
    b = q[0] * basis(8, 0) + q[1] * u + q[2] * n + q[3] * mulO(u, n)
    x = np.concatenate([u, b]) / np.sqrt(2); y = np.concatenate([mulO(n, u), mulO(b, n)]) / np.sqrt(2)
    return np.concatenate([x, y])
u = rand_im8(); n = rand_im8(); n = unit(n - (n @ u) * u); q = unit(rng.standard_normal(4))
assert np.allclose(mul('Sm', point(u, n, q)[:16], point(u, n, q)[16:]), 0, atol=1e-9)
h = 1e-6
# tangent vectors: vary q within S^3 (3 dirs), vary u within S^6 ⊥ ... (u,n) in V_2: 11 dirs
def tangent_dirs():
    dirs = []
    # q-directions
    for v in np.linalg.svd(q[None, :])[2][1:]:
        dirs.append(('q', (point(u, n, q + h * v) - point(u, n, q - h * v)) / (2 * h)))
    # u-directions with n fixed (u ⊥ n, u imaginary): 5 dirs ; and rotate (u,n) jointly in their plane: 1 dir; n-directions ⊥ u,n: 5 dirs
    basisIm = np.eye(8)[1:]
    for v in basisIm:
        w = v - (v @ u) * u - (v @ n) * n
        if np.linalg.norm(w) < 1e-9: continue
        w = unit(w)
        dirs.append(('u', (point(unit(u + h * w), n, q) - point(unit(u - h * w), n, q)) / (2 * h)))
        dirs.append(('n', (point(u, unit(n + h * w), q) - point(u, unit(n - h * w), q)) / (2 * h)))
    dirs.append(('rot', (point(unit(u + h * n), unit(n - h * u), q) - point(unit(u - h * n), unit(n + h * u), q)) / (2 * h)))
    return dirs
dirs = tangent_dirs()
labels = [d[0] for d in dirs]; V = np.array([d[1] for d in dirs])
G = V @ V.T
qidx = [i for i, l in enumerate(labels) if l == 'q']; oidx = [i for i, l in enumerate(labels) if l != 'q']
print('P(S\') induced metric: |cross terms between S^3-directions and V_2-directions| max =', np.abs(G[np.ix_(qidx, oidx)]).max())
print('   rank of full tangent frame:', np.linalg.matrix_rank(V, tol=1e-6))
# does the V_2 block depend on q ?
def block(q):
    global dirs
    globals()['q'] = q
    d = tangent_dirs(); V = np.array([x[1] for x in d]); lab = [x[0] for x in d]
    o = [i for i, l in enumerate(lab) if l != 'q']
    return (V @ V.T)[np.ix_(o, o)]
B1 = block(unit(rng.standard_normal(4))); B2 = block(unit(rng.standard_normal(4)))
print('   V_2-block of the metric changes with q? max diff =', np.abs(B1 - B2).max())
