import numpy as np
from cd import *
rng = np.random.default_rng(6)
def ok(label, cond): print(('PASS ' if cond else 'FAIL ') + label)

# ---------------------------------------------------------------- embedding S' -> T = A_5
# T = S ⊕ S e' ; S = O ⊕ O e.  index: g in 0..31, bit3 = e, bit4 = e'.
def emb(x):
    a, b = x[:8], x[8:]
    y = np.zeros(32)
    y[:8] = conj(a)               # abar
    y[24:32] = b                  # (b e) e'  : indices 8+16 .. = bits 3,4 set
    return y
good = all(np.allclose(emb(mulSm(x, y)), mulT(emb(x), emb(y))) for x, y in [(rand(16, rng), rand(16, rng)) for _ in range(20)])
ok("Phi(a,b) = abar + (b e)e' is an algebra isomorphism S' -> O ⊕ (O e)e'  ⊂ T", good)
# and (be)e' = bbar (ee') :
j = mulT(basis(32, 8), basis(32, 16))
print('  e e\' = e_%d' % np.argmax(np.abs(j)))
chk = True
for b in [rand(8, rng) for _ in range(5)]:
    B = np.zeros(32); B[:8] = conj(b)
    lhs = mulT(B, j)              # conj(b) (ee')
    rhs = np.zeros(32); rhs[24:] = b   # (b e) e'
    chk &= np.allclose(lhs, rhs)
ok("(b e) e' = bbar (e e') in T", chk)

# the same lemma one level down: quasi-octonions  H ⊕ (H l) e ⊂ S  vs mirror double of H
def emb8(x):
    a, b = x[:4], x[4:]
    y = np.zeros(16); y[:4] = conj(a); y[12:16] = b
    return y
good = all(np.allclose(emb8(mulOm(x, y)), mulS(emb8(x), emb8(y))) for x, y in [(rand(8, rng), rand(8, rng)) for _ in range(20)])
ok("Phi(a,b) = abar + (b l)e is an isomorphism  M(H) -> H ⊕ (H l)e ⊂ S  (quasi-octonions)", good)

# ---------------------------------------------------------------- the 31 hyperplane subalgebras of T
print('=== the 31 basis hyperplanes of F_2^5 in T: type by (number of octonion 8-subalgebras among their 15 planes, ann dims) ===')
def hyper_type(H):
    idx = np.array(H)
    def sub(x):
        y = np.zeros(32); y[idx] = x; return y
    def mul16(x, y):
        return mulT(sub(x), sub(y))[idx]
    tag = 'tmpH'; register(tag, mul16, 16)
    struct.cache_clear()
    # octaves: hyperplanes of the 16-dim algebra (in its own index set 0..15 via position)
    noct = 0
    for f in range(1, 16):
        Hs = [g for g in range(16) if bin(f & g).count('1') % 2 == 0]
        comp = True
        for _ in range(6):
            x = np.zeros(16); y = np.zeros(16); x[Hs] = rng.standard_normal(8); y[Hs] = rng.standard_normal(8)
            z = mul16(x, y)
            if abs(norm2(z) - norm2(x) * norm2(y)) > 1e-8: comp = False
        noct += comp
    # zero divisor stats: sample dead dims
    dims = set()
    for _ in range(40):
        x = rand(16, rng)
        # project to candidate dead loci in the intrinsic coordinates is not available; use random + Moreno-type
        dims.add(nullity(L(tag, x)))
    # generic annihilator dims over the two 'loci' expressed in the hyperplane's first 8 / last 8 split
    ann = set()
    for _ in range(40):
        a = rng.standard_normal(8); a[0] = 0; a = unit(a); b = rng.standard_normal(8); b[0] = 0; b = unit(b - (b @ a) * a)
        ann.add(nullity(L(tag, np.concatenate([a, b]))))
        b2 = unit(rng.standard_normal(8)); ann.add(nullity(L(tag, np.concatenate([a, b2]))))
    return noct, tuple(sorted(ann))
types = {}
for f in range(1, 32):
    H = [g for g in range(32) if bin(f & g).count('1') % 2 == 0]
    t = hyper_type(H)
    types.setdefault(t, []).append(f)
for t, fs in types.items():
    print(f'  octaves={t[0]}, ann dims on test loci={t[1]}: functionals {fs}  (count {len(fs)})')
struct.cache_clear()

# ---------------------------------------------------------------- stretch spectrum of M_x = L_{xbar} L_x / N(x)
print('=== spectrum of L_{x*}L_x / N(x) ===')
def spec(name, x):
    M = L(name, conj(x)) @ L(name, x) / norm2(x)
    w = np.linalg.eigvalsh((M + M.T) / 2)
    return np.round(w, 6)
def rand_im8():
    v = rng.standard_normal(8); v[0] = 0; return unit(v)
def cross(a, b):
    return (mulO(a, b) - mulO(b, a)) / 2
for name in ['S', 'Sm']:
    print(name)
    # (1) a,b imaginary
    a = rand_im8(); b = rand_im8(); x = np.concatenate([a, b])
    s = 2 * np.sqrt(norm2(cross(a, b))) / (norm2(a) + norm2(b))
    print('   a,b imaginary units: s=2|a×b|/(|a|^2+|b|^2)=%.4f  spectrum' % s, sorted(set(spec(name, x))), 'mults', [int(np.sum(spec(name, x) == v)) for v in sorted(set(spec(name, x)))])
    # (2) a imaginary, b general
    a = rand_im8(); b = unit(rand(8, rng)); x = np.concatenate([a, b])
    sp = spec(name, x); vals = sorted(set(sp))
    print('   a imaginary, b general: |b0|=%.3f, <b,a>=%.3f, |b_perp|=%.3f' % (b[0], b @ a, np.sqrt(1 - b[0] ** 2 - (b @ a) ** 2)), 'spectrum', vals, 'mults', [int(np.sum(sp == v)) for v in vals])
    # (3) general
    a = unit(rand(8, rng)); b = unit(rand(8, rng)); x = np.concatenate([a, b])
    sp = spec(name, x); vals = sorted(set(sp))
    print('   a,b general: a0=%.3f b0=%.3f' % (a[0], b[0]), 'spectrum', vals, 'mults', [int(np.sum(sp == v)) for v in vals])
