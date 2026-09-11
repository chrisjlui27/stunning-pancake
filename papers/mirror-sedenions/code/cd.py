"""
cd.py -- Cayley-Dickson algebras, the sedenions S and the mirror sedenions S'.

Elements of a 2^n-dimensional algebra are numpy vectors of length 2^n.
Basis e_0 = 1, e_g for g in {0,...,2^n-1} (bits = coordinates in F_2^n).
"""
import numpy as np
from itertools import product as iproduct
from functools import lru_cache

# ----------------------------------------------------------------------------
# Generic doubling.  A "product" is a function mul(a, b) on vectors of length m.
# The doubled product on vectors of length 2m is one of the 32 Bales products,
# specified by a first-component word f in {0..7} and a second-component word
# g in {0..3}.  We only use:
#   standard : (a,b)(c,d) = (ac - d*b, da + bc*)      [Bales P3^T]
#   mirror   : (a,b)(c,d) = (ca - d*b, da + bc*)      [Bales P1^T]
# but the general list is kept for the census.
# ----------------------------------------------------------------------------

def conj(x):
    y = -x.copy()
    y[0] = x[0]
    return y

def split(x):
    m = len(x) // 2
    return x[:m], x[m:]

def join(a, b):
    return np.concatenate([a, b])

# first components (Bales f_0..f_7)
FIRST = {
    0: lambda mul, a, b, c, d: mul(c, a) - mul(conj(b), d),
    1: lambda mul, a, b, c, d: mul(c, a) - mul(d, conj(b)),
    2: lambda mul, a, b, c, d: mul(a, c) - mul(conj(b), d),
    3: lambda mul, a, b, c, d: mul(a, c) - mul(d, conj(b)),
    4: lambda mul, a, b, c, d: mul(c, a) - mul(b, conj(d)),
    5: lambda mul, a, b, c, d: mul(c, a) - mul(conj(d), b),
    6: lambda mul, a, b, c, d: mul(a, c) - mul(b, conj(d)),
    7: lambda mul, a, b, c, d: mul(a, c) - mul(conj(d), b),
}
# second components (Bales g_0..g_3)
SECOND = {
    0: lambda mul, a, b, c, d: mul(d, conj(a)) + mul(b, c),
    1: lambda mul, a, b, c, d: mul(conj(a), d) + mul(c, b),
    2: lambda mul, a, b, c, d: mul(a, d) + mul(conj(c), b),
    3: lambda mul, a, b, c, d: mul(d, a) + mul(b, conj(c)),
}

def double(mul, f=7, g=3):
    """Return the doubled product built from base product `mul`."""
    F, G = FIRST[f], SECOND[g]
    def mul2(x, y):
        a, b = split(x); c, d = split(y)
        return join(F(mul, a, b, c, d), G(mul, a, b, c, d))
    return mul2

def real_mul(x, y):
    return x * y

# standard tower
def standard_tower(n):
    mul = real_mul
    for _ in range(n):
        mul = double(mul, 7, 3)
    return mul

mulR = real_mul
mulC = standard_tower(1)
mulH = standard_tower(2)
mulO = standard_tower(3)
mulS = standard_tower(4)          # sedenions S = A_4
mulT = standard_tower(5)          # trigintaduonions T = A_5

# the mirror sedenions S' : mirror-double the standard octonions
mulSm = double(mulO, 5, 3)        # (ca - d*b, da + bc*)
# mirror double of the quaternions ("mirror octonions" / quasi-octonions)
mulOm = double(mulH, 5, 3)

# ----------------------------------------------------------------------------
# Structure constants and multiplication matrices
# ----------------------------------------------------------------------------

def basis(n_dim, i):
    e = np.zeros(n_dim); e[i] = 1.0; return e

@lru_cache(maxsize=None)
def struct(mul_name):
    mul, n = ALG[mul_name]
    T = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            T[i, j] = mul(basis(n, i), basis(n, j))
    return T

ALG = {}
def register(name, mul, n):
    ALG[name] = (mul, n)

register('R', mulR, 1); register('C', mulC, 2); register('H', mulH, 4)
register('O', mulO, 8); register('S', mulS, 16); register('T', mulT, 32)
register('Sm', mulSm, 16); register('Om', mulOm, 8)

def L(name, x):
    """Left multiplication matrix of x."""
    T = struct(name)
    return np.einsum('i,ijk->kj', x, T)   # (L_x y)_k = sum_ij x_i y_j T[i,j,k]

def R(name, x):
    T = struct(name)
    return np.einsum('j,ijk->ki', x, T)   # (R_x y)_k = sum_ij y_i x_j T[i,j,k]

def mul(name, x, y):
    return ALG[name][0](x, y)

def norm2(x):
    return float(x @ x)

def rand(n, rng=None):
    rng = rng or np.random.default_rng()
    return rng.standard_normal(n)

def unit(x):
    return x / np.sqrt(norm2(x))

def nullity(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < tol * max(1.0, s[0])))

def rank(M, tol=1e-9):
    return M.shape[1] - nullity(M, tol) if M.shape[0] >= M.shape[1] else np.linalg.matrix_rank(M, tol=tol)

def sign_table(name):
    """Return (sign, index) tables: e_i e_j = sign[i,j] e_{index[i,j]}; check monomiality."""
    T = struct(name); n = T.shape[0]
    sign = np.zeros((n, n), dtype=int); idx = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            v = T[i, j]
            nz = np.nonzero(np.abs(v) > 1e-12)[0]
            assert len(nz) == 1, (name, i, j, v)
            idx[i, j] = nz[0]; sign[i, j] = int(np.sign(v[nz[0]]))
    return sign, idx

def assoc(name, x, y, z):
    return mul(name, mul(name, x, y), z) - mul(name, x, mul(name, y, z))
