import numpy as np
from cd import *
rng = np.random.default_rng(12)
def quaternionic_lines(name):
    s, idx = sign_table(name); n = s.shape[0]; bad = []
    for p in range(1, n):
        for q in range(1, n):
            if p == q: continue
            r = idx[p, q]
            # e_p e_q = s e_r  =>  need e_q e_r = s e_p
            if not (idx[q, r] == p and s[q, r] == s[p, q]): bad.append((p, q))
    return bad
res = {}
for f in range(8):
    for g in range(4):
        tag = f'Q{f}{g}'; register(tag, double(mulO, f, g), 16)
        bad = quaternionic_lines(tag)
        res[(f, g)] = len(bad)
print('number of failing ordered basis pairs (p,q) per product:')
for k, v in res.items(): print(' ', k, v)
# ker alt_x in S for generic x: subalgebra? composition?
x = rand(16, rng)
A = np.column_stack([assoc('S', x, x, basis(16, i)) for i in range(16)])
U, s, Vt = np.linalg.svd(A); K = Vt[-8:].T
closed = True; comp = True
for _ in range(10):
    p = K @ rng.standard_normal(8); q = K @ rng.standard_normal(8); z = mulS(p, q)
    closed &= np.allclose(K @ np.linalg.lstsq(K, z, rcond=None)[0], z)
    comp &= abs(norm2(z) - norm2(p) * norm2(q)) < 1e-8
print('S: ker alt_x (dim 8) is a subalgebra:', closed, '; composition:', comp)
