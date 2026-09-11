import numpy as np
from cd import *
rng = np.random.default_rng(2)

def ann_dim(name, x):
    return nullity(L(name, x))

def pair_from(a, b):
    return np.concatenate([a, b])

def rand_im8():
    v = rng.standard_normal(8); v[0] = 0; return unit(v)

print('=== annihilator dimension statistics ===')
for name in ['S', 'Sm']:
    # generic elements: never zero divisors
    gen = [ann_dim(name, rand(16, rng)) for _ in range(50)]
    # a,b imaginary, orthogonal, equal norm (Moreno's locus for S)
    mor = []
    for _ in range(50):
        a = rand_im8(); b = rand_im8(); b = unit(b - (b @ a) * a)
        mor.append(ann_dim(name, pair_from(a, b)))
    # a imaginary unit, b arbitrary unit (the conjectured locus for Sm)
    conj_locus = [ann_dim(name, pair_from(rand_im8(), unit(rand(8, rng)))) for _ in range(50)]
    # a arbitrary unit with Re a != 0, b arbitrary unit, |a|=|b|
    off = [ann_dim(name, pair_from(unit(rand(8, rng)), unit(rand(8, rng)))) for _ in range(50)]
    # a imaginary, b imaginary, not orthogonal
    imim = [ann_dim(name, pair_from(rand_im8(), rand_im8())) for _ in range(50)]
    # special: (u,u), (u,1), (u, cos t + sin t u)
    u = rand_im8()
    sp = [ann_dim(name, pair_from(u, u)), ann_dim(name, pair_from(u, basis(8, 0))),
          ann_dim(name, pair_from(u, np.cos(.7) * basis(8, 0) + np.sin(.7) * u))]
    print(f'{name}: generic {set(gen)}; Moreno locus (a⊥b imaginary) {set(mor)}; a imaginary/b any {set(conj_locus)}; Re a≠0 {set(off)}; a,b imaginary non-orthogonal {set(imim)}; (u,u),(u,1),(u,cos+sin u) {sp}')

print()
print('=== Sm: annihilator dimension as a function of (Re b, <Im b, a>) for a imaginary unit ===')
# parametrize b = b0 * 1 + b1 * a + b2 * n, n ⊥ a imaginary, b0^2+b1^2+b2^2 = 1
u = rand_im8(); n = rand_im8(); n = unit(n - (n @ u) * u)
seen = {}
for b0 in np.linspace(-1, 1, 21):
    for b1 in np.linspace(-1, 1, 21):
        r = 1 - b0 ** 2 - b1 ** 2
        if r < -1e-12: continue
        b2 = np.sqrt(max(r, 0))
        b = b0 * basis(8, 0) + b1 * u + b2 * n
        k = ann_dim('Sm', pair_from(u, b))
        seen.setdefault(k, []).append((round(b0, 2), round(b1, 2), round(b2, 3)))
for k in sorted(seen):
    pts = seen[k]
    print(f'  ann dim {k}: {len(pts)} sample points; e.g. {pts[:6]}')
    if k > 2:
        print('     all with b2 = 0 (b in span{1,a})?', all(p[2] < 1e-6 for p in pts))

print()
print('=== dimension of the pair variety P = {(x,y): xy = 0, |x|=|y|=1} at sample points ===')
def pair_variety_tangent_dim(name, x, y):
    # differential of mu(x,y) = xy at (x,y): (xi, eta) -> xi*y + x*eta  ;  matrix 16 x 32
    J = np.hstack([R(name, y), L(name, x)])
    # add the two sphere constraints
    C = np.zeros((2, 32)); C[0, :16] = x; C[1, 16:] = y
    return 32 - rank(np.vstack([J, C]))

for name in ['S', 'Sm']:
    dims = []
    for _ in range(20):
        a = rand_im8()
        if name == 'S':
            b = rand_im8(); b = unit(b - (b @ a) * a)
        else:
            b = unit(rand(8, rng))
        x = pair_from(a, b) / np.sqrt(2)
        K = L(name, x); U, s, Vt = np.linalg.svd(K)
        ker = Vt[-ann_dim(name, x):]           # basis of annihilator
        y = unit(ker.T @ rng.standard_normal(ker.shape[0]))
        assert np.allclose(mul(name, x, y), 0, atol=1e-9)
        dims.append(pair_variety_tangent_dim(name, x, y))
    print(f'{name}: tangent-space dimension of P at generic points: {set(dims)}')
# special stratum in Sm
u = rand_im8(); x = pair_from(u, u) / np.sqrt(2)
K = L('Sm', x); U, s, Vt = np.linalg.svd(K); ker = Vt[-6:]
y = unit(ker.T @ rng.standard_normal(6))
print('Sm: at the special point (u,u): ann dim', ann_dim('Sm', x), ', tangent dim of P', pair_variety_tangent_dim('Sm', x, y))

print()
print('=== dimension of the zero-divisor set Z (unit sphere) via tangent cone of {det-drop} ===')
# Z = {x : L_x singular}. Near a point x with dim ker L_x = k, the locus where nullity >= k
# has tangent space = { xi : P_coker (dL(xi)) ker = 0 } where dL(xi) = L_xi restricted to ker, projected to coker.
def Z_tangent_dim(name, x, k):
    K = L(name, x); U, s, Vt = np.linalg.svd(K)
    ker = Vt[-k:].T           # 16 x k
    cok = U[:, -k:]           # 16 x k   (left null vectors)
    # linear map xi -> cok^T L_xi ker  (k x k), as a 32? no: xi in R^16
    A = np.zeros((k * k, 16))
    for i in range(16):
        A[:, i] = (cok.T @ L(name, basis(16, i)) @ ker).ravel()
    A = np.vstack([A, x[None, :]])   # unit sphere constraint
    return 16 - rank(A)

for name, mk in [('S', 'moreno'), ('Sm', 'conj')]:
    ds = []
    for _ in range(20):
        a = rand_im8()
        if mk == 'moreno':
            b = rand_im8(); b = unit(b - (b @ a) * a)
        else:
            b = unit(rand(8, rng))
        x = pair_from(a, b) / np.sqrt(2)
        k = ann_dim(name, x)
        ds.append(Z_tangent_dim(name, x, k))
    print(f'{name}: dim of unit zero-divisor set at generic dead points: {set(ds)}')
