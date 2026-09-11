import numpy as np
from cd import *
rng = np.random.default_rng(7)
def ok(label, cond): print(('PASS ' if cond else 'FAIL ') + label)
def rand_im8():
    v = rng.standard_normal(8); v[0] = 0; return unit(v)

# adjoint identity  <xy,z> = <y, xbar z>  i.e. L_{xbar} = L_x^T ; and R
for name in ['S', 'Sm']:
    x = rand(16, rng)
    ok(f'{name}: L_(x*) = L_x^T and R_(x*) = R_x^T', np.allclose(L(name, conj(x)), L(name, x).T) and np.allclose(R(name, conj(x)), R(name, x).T))
    y = rand(16, rng)
    A = np.column_stack([assoc(name, x, x, basis(16, i)) for i in range(16)])
    ok(f'{name}: L_(x*)L_x = N(x) I + alt_x', np.allclose(L(name, conj(x)) @ L(name, x), norm2(x) * np.eye(16) + A))

# spectrum closed form for Sm:  eigenvalues of L_{x*}L_x / N :  1 (x4), 1±sigma (x2), 1±tau (x4)
#   sigma = 2 |Im a| |b| / N,   tau = 2 |a| |b_par| / N  where b_par = projection of b on span{1, a}
print('=== spectrum fit for Sm ===')
worst = 0
for _ in range(200):
    a = rand(8, rng) * rng.random(); b = rand(8, rng) * rng.random()
    x = np.concatenate([a, b]); N = norm2(x)
    M = L('Sm', conj(x)) @ L('Sm', x) / N
    w = np.sort(np.linalg.eigvalsh((M + M.T) / 2))
    ima = a.copy(); ima[0] = 0
    sigma = 2 * np.sqrt(norm2(ima)) * np.sqrt(norm2(b)) / N
    # projection of b on span{1, a}
    e0 = basis(8, 0); e1 = unit(ima)
    bpar = (b @ e0) * e0 + (b @ e1) * e1
    tau = 2 * np.sqrt(norm2(a)) * np.sqrt(norm2(bpar)) / N
    pred = np.sort(np.array([1 - sigma] * 2 + [1 - tau] * 4 + [1] * 4 + [1 + tau] * 4 + [1 + sigma] * 2))
    worst = max(worst, np.max(np.abs(w - pred)))
print('  max deviation between computed spectrum and closed form over 200 random x:', worst)
# same for S (BCDI): 1 (x8), 1 ± s (x4) with s = 2|Im a x Im b + ...|? test BCDI form for imaginary a,b and general
worstS = 0
for _ in range(200):
    a = rand_im8() * rng.random(); b = rand_im8() * rng.random()
    x = np.concatenate([a, b]); N = norm2(x)
    M = L('S', conj(x)) @ L('S', x) / N
    w = np.sort(np.linalg.eigvalsh((M + M.T) / 2))
    cr = (mulO(a, b) - mulO(b, a)) / 2
    s = 2 * np.sqrt(norm2(cr)) / N
    pred = np.sort(np.array([1 - s] * 4 + [1] * 8 + [1 + s] * 4))
    worstS = max(worstS, np.max(np.abs(w - pred)))
print('  S (BCDI, imaginary a,b): max deviation', worstS)

# explicit basis zero divisors in Sm
print('=== explicit basis dead pairs in Sm (e_i e_j conventions of this model) ===')
def e(i): return basis(16, i)
sign, idx = sign_table('O')
print('  octonion table: e1 e2 = %+d e%d, e1 e4 = %+d e%d, e2 e4 = %+d e%d' % (sign[1, 2], idx[1, 2], sign[1, 4], idx[1, 4], sign[2, 4], idx[2, 4]))
cands = [(e(1) + e(9), e(3) - e(11)), (e(1) + e(8), -e(3) + e(10)), (e(1) + e(10), e(3) + e(8)), (e(1) + e(10), e(2) + e(9)),
         (e(1) + e(9), e(2) - e(10)), (e(1) + e(9), e(5) - e(13)), (e(1) + e(10), e(2) - e(9))]
for x, y in cands:
    xi = [i for i in range(16) if x[i]]; yi = [(i, int(y[i])) for i in range(16) if y[i]]
    print('   x = e%d + e%d,  y = %s :  xy = 0 in Sm? %s ; in S? %s' % (xi[0], xi[1], ' '.join('%+de%d' % (s, i) for i, s in yi), np.allclose(mulSm(x, y), 0), np.allclose(mulS(x, y), 0)))
# annihilator of e1 + e9 in Sm: basis description
x = e(1) + e(9); K = L('Sm', x); U, s, Vt = np.linalg.svd(K); ker = Vt[-nullity(K):]
print('  dim Ann(e1+e9) =', ker.shape[0])
# reduced-row-echelon-ish: find basis pairs
from itertools import combinations
found = []
for i, j in combinations(range(16), 2):
    for sgn in [1, -1]:
        y = e(i) + sgn * e(j)
        if np.allclose(mulSm(x, y), 0): found.append('e%d%+de%d' % (i, sgn, j))
print('  two-term annihilators of e1+e9:', found)

# Brown/Dray S_3 in S:  q -> cos t q + sin t (q l), q l -> -sin t q + cos t (q l) for imaginary q ; 1,l fixed
def dray(t, name):
    def phi(x):
        a, b = x[:8].copy(), x[8:].copy()
        a0 = a[0]; b0 = b[0]; a[0] = 0; b[0] = 0
        na = np.cos(t) * a - np.sin(t) * b; nb = np.sin(t) * a + np.cos(t) * b
        na[0] = a0; nb[0] = b0
        return np.concatenate([na, nb])
    good = all(np.allclose(phi(mul(name, x, y)), mul(name, phi(x), phi(y))) for x, y in [(rand(16, rng), rand(16, rng)) for _ in range(5)])
    return good
for name in ['S', 'Sm']:
    print(f'  {name}: Dray rotation by 2pi/3 is an automorphism? {dray(2*np.pi/3, name)};  by pi (l -> -l with q -> -q): {dray(np.pi, name)}; by a generic angle: {dray(0.4, name)}')
# other discrete candidates for Sm: (a,b) -> (a,-b) ; (a,b) -> (abar, ...)?
for name in ['S', 'Sm']:
    eps = lambda x: np.concatenate([x[:8], -x[8:]])
    print(f'  {name}: (a,b)->(a,-b) automorphism? ', all(np.allclose(eps(mul(name, x, y)), mul(name, eps(x), eps(y))) for x, y in [(rand(16, rng), rand(16, rng)) for _ in range(5)]))

# ---- toy: mirror double of H (quasi-octonions)
print('=== mirror double of H ===')
def rand_im4():
    v = rng.standard_normal(4); v[0] = 0; return unit(v)
ann_generic = set(); ann_dead = set(); ann_off = set()
for _ in range(50):
    ann_generic.add(nullity(L('Om', rand(8, rng))))
    ann_dead.add(nullity(L('Om', np.concatenate([rand_im4(), unit(rand(4, rng))]))))
    ann_off.add(nullity(L('Om', np.concatenate([unit(rand(4, rng)), unit(rand(4, rng))]))))
u = rand_im4(); print('  ann dims: generic', ann_generic, '; (u, b) u imaginary |u|=|b|:', ann_dead, '; Re a != 0:', ann_off, '; (u,u):', nullity(L('Om', np.concatenate([u, u]))), '(u,1):', nullity(L('Om', np.concatenate([u, basis(4, 0)]))))
# pair manifold dimension and rank of dmu
ranks = set(); dims = set()
for _ in range(50):
    u = rand_im4(); b = unit(rand(4, rng)); x = np.concatenate([u, b]) / np.sqrt(2)
    K = L('Om', x); U, s, Vt = np.linalg.svd(K); ker = Vt[-2:]; y = unit(ker.T @ rng.standard_normal(2))
    J = np.hstack([R('Om', y), L('Om', x)]); ranks.add(rank(J))
    C = np.zeros((2, 16)); C[0, :8] = x; C[1, 8:] = y; dims.add(16 - rank(np.vstack([J, C])))
print('  rank d(mu) on P:', ranks, '; dim P:', dims, '(expect 8, 6)')
# Der(Om) structure: compute basis and brackets
def der_basis(name):
    T = struct(name); n = T.shape[0]; rows = []
    for i in range(n):
        for j in range(n):
            eq = np.zeros((n, n, n))
            for m in range(n): eq[:, :, m][np.arange(n), np.arange(n)] += T[i, j, m]
            for p in range(n): eq[:, p, i] -= T[p, j, :]; eq[:, p, j] -= T[i, p, :]
            rows.append(eq.reshape(n, n * n))
    A = np.vstack(rows); U, s, Vt = np.linalg.svd(A); k = nullity(A)
    return [Vt[-i - 1].reshape(n, n) for i in range(k)]
D = der_basis('Om')
# Killing form signature / derived algebra dim
k = len(D); br = []
for i in range(k):
    for j in range(k):
        br.append((D[i] @ D[j] - D[j] @ D[i]).ravel())
derived = np.linalg.matrix_rank(np.array(br), tol=1e-8)
print('  Der(Om): dim', k, ', dim [Der,Der] =', derived)
# does Der(Om) preserve the first factor H? check D(H) ⊂ H for all D
pres = all(np.allclose(Dm[4:, :4], 0) for Dm in D)
print('  every derivation preserves the founding H:', pres)
# split: derivations vanishing on H
sub = [Dm for Dm in D]
A = np.array([Dm[:, :4].ravel() for Dm in D])
print('  dim of derivations that vanish on the founding H:', k - np.linalg.matrix_rank(A, tol=1e-8))
