"""Fast graded-isomorphism test between sign-monomial algebras on F_2^4."""
import numpy as np
from itertools import product as iproduct
from cd import *

def gl42():
    mats = []
    for cols in iproduct(range(1, 16), repeat=4):
        span = {0}; okk = True
        for c in cols:
            if c in span: okk = False; break
            span |= {s ^ c for s in span}
        if okk: mats.append(cols)
    return mats
GL = gl42()
def apply(cols, g):
    r = 0
    for i in range(4):
        if (g >> i) & 1: r ^= cols[i]
    return r
SIG = np.array([[apply(cols, g) for g in range(16)] for cols in GL])   # 20160 x 16

# fixed coefficient matrix for the coboundary equations mu(g)+mu(h)+mu(g^h) = rhs(g,h), g<h, g,h != 0
PAIRS = [(g, h) for g in range(1, 16) for h in range(g + 1, 16)]
A = np.zeros((len(PAIRS), 15), dtype=np.uint8)
for r, (g, h) in enumerate(PAIRS):
    A[r, g - 1] ^= 1; A[r, h - 1] ^= 1; A[r, (g ^ h) - 1] ^= 1

def left_nullspace_f2(A):
    m, k = A.shape
    M = np.hstack([A.copy(), np.eye(m, dtype=np.uint8)])  # m x (k + m): each row = [A_row | e_row]
    piv = 0
    for c in range(k):
        pr = None
        for r in range(piv, m):
            if M[r, c]: pr = r; break
        if pr is None: continue
        M[[piv, pr]] = M[[pr, piv]]
        mask = M[:, c].astype(bool); mask[piv] = False
        M[mask] ^= M[piv]
        piv += 1
    N = M[piv:, k:]
    return N
N = left_nullspace_f2(A)   # consistency matrix: rhs consistent iff N rhs = 0 mod 2

def f2_rank(A):
    M = A.copy() % 2; m, k = M.shape; piv = 0
    for c in range(k):
        pr = None
        for r in range(piv, m):
            if M[r, c]: pr = r; break
        if pr is None: continue
        M[[piv, pr]] = M[[pr, piv]]
        mask = M[:, c].astype(bool); mask[piv] = False
        M[mask] ^= M[piv]; piv += 1
    return piv
A_RANK = f2_rank(A)

def graded_isos(signA, signB):
    """All sigma in GL(4,2) such that some lambda gives e_g -> lambda(g) e_{sigma g} an isomorphism A -> B."""
    fa = (signA < 0).astype(np.uint8); fb = (signB < 0).astype(np.uint8)
    if np.any(fa.diagonal() != fb.diagonal()) or np.any(fa[0] != fb[0]) or np.any(fa[:, 0] != fb[:, 0]):
        return []
    gs = np.array([g for g, h in PAIRS]); hs = np.array([h for g, h in PAIRS])
    rhs = (fa[gs, hs][None, :] ^ fb[SIG[:, gs], SIG[:, hs]]) & 1        # 20160 x 105
    test = (rhs.astype(np.int64) @ N.T.astype(np.int64)) % 2
    okk = np.where(~test.any(axis=1))[0]
    return [GL[i] for i in okk]

N_LAMBDA = 2 ** (15 - A_RANK)   # number of lambdas per working sigma
