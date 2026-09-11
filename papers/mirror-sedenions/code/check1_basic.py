import numpy as np
from cd import *
rng = np.random.default_rng(1)

def check(label, ok):
    print(('PASS ' if ok else 'FAIL ') + label)

# --- octonions are a composition algebra, alternative
for _ in range(20):
    x, y = rand(8, rng), rand(8, rng)
    assert abs(norm2(mulO(x, y)) - norm2(x) * norm2(y)) < 1e-9
    assert np.allclose(assoc('O', x, x, y), 0) and np.allclose(assoc('O', y, x, x), 0)
check('O composition + alternative', True)

for name in ['S', 'Sm']:
    n = 16
    one = basis(n, 0)
    ok_id = all(np.allclose(mul(name, one, x), x) and np.allclose(mul(name, x, one), x) for x in [rand(n, rng) for _ in range(5)])
    ok_norm = True; ok_comp = True; ok_flex = True; ok_pa = True; ok_alt = True; ok_conj = True
    for _ in range(30):
        x, y, z = rand(n, rng), rand(n, rng), rand(n, rng)
        xc = conj(x)
        if not (np.allclose(mul(name, x, xc), norm2(x) * one) and np.allclose(mul(name, xc, x), norm2(x) * one)): ok_norm = False
        if abs(norm2(mul(name, x, y)) - norm2(x) * norm2(y)) < 1e-9: pass
        else: ok_comp = False
        if not np.allclose(mul(name, mul(name, x, y), x), mul(name, x, mul(name, y, x))): ok_flex = False
        x2 = mul(name, x, x)
        if not (np.allclose(mul(name, x2, x), mul(name, x, x2)) and np.allclose(mul(name, x2, x2), mul(name, x, mul(name, x, x2)))): ok_pa = False
        if not np.allclose(assoc(name, x, x, y), 0): ok_alt = False
        if not np.allclose(conj(mul(name, x, y)), mul(name, conj(y), conj(x))): ok_conj = False
    print(f'--- {name}: identity {ok_id}, x x* = N(x) {ok_norm}, composition {ok_comp}, flexible {ok_flex}, power-assoc(deg<=4) {ok_pa}, alternative {ok_alt}, (xy)*=y*x* {ok_conj}')
    sign, idx = sign_table(name)
    # anticommutativity & squares
    anti = all(sign[i, j] == -sign[j, i] for i in range(1, n) for j in range(1, n) if i != j)
    sq = all(sign[i, i] == -1 and idx[i, i] == 0 for i in range(1, n))
    xor = all(idx[i, j] == (i ^ j) for i in range(n) for j in range(n))
    print(f'    basis: e_i e_j = ± e_{{i xor j}} {xor}; anticommuting {anti}; squares -1 {sq}')

# the two algebras differ on the founding octave only, by reversal
S_sign, S_idx = sign_table('S'); M_sign, M_idx = sign_table('Sm')
diff = [(i, j) for i in range(16) for j in range(16) if S_sign[i, j] != M_sign[i, j]]
print('sign differences S vs Sm at (i,j):', len(diff), 'all with i,j<8 and i!=j, i,j!=0:', all(i < 8 and j < 8 and i != j and i and j for i, j in diff))
