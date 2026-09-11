"""Symbolic spectrum of alt_x = L_{x*}L_x - N(x) I in the mirror sedenions,
for x = (a, b) with a = a0 + a1 e1,  b = b0 + b1 e1 + b2 e2  (general position up to G2)."""
import sympy as sp
import numpy as np
from cd import struct

T = struct('Sm')   # numeric structure constants (entries 0, ±1)
Ti = np.rint(T).astype(int)
a0, a1, b0, b1, b2 = sp.symbols('a0 a1 b0 b1 b2', real=True)
x = [0] * 16
x[0] = a0; x[1] = a1; x[8] = b0; x[9] = b1; x[10] = b2
def Lmat(v):
    M = sp.zeros(16, 16)
    for i in range(16):
        if v[i] == 0: continue
        for j in range(16):
            for k in range(16):
                if Ti[i, j, k]: M[k, j] += v[i] * Ti[i, j, k]
    return M
xb = [x[0]] + [-x[i] for i in range(1, 16)]
Lx = Lmat(x); Lxb = Lmat(xb)
N = a0**2 + a1**2 + b0**2 + b1**2 + b2**2
A = sp.simplify(Lxb * Lx - N * sp.eye(16))     # alt_x
print('alt_x symmetric:', sp.simplify(A - A.T) == sp.zeros(16, 16))
# block structure: find the coarsest partition of basis into invariant blocks
import itertools
nz = [(i, j) for i in range(16) for j in range(16) if A[i, j] != 0]
# characteristic polynomial via eigenvals of blocks
lam = sp.symbols('lam')
cp = sp.factor((A - lam * sp.eye(16)).det(method='berkowitz'))
print('char poly of alt_x :')
sp.pprint(cp)
print()
print('eigenvalues (as roots):')
for root, mult in sp.roots(sp.Poly(cp, lam)).items():
    print('  ', sp.factor(root), ' multiplicity', mult)
