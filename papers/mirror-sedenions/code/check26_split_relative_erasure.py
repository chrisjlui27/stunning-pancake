"""check26 -- relative-erasure identities with split doublings (eps = -1), inner and/or outer."""
import numpy as np
from collections import Counter
from landscape import *
def hyperplane_basis(N, f):
    H = [g for g in range(N) if bin(f & g).count('1') % 2 == 0]
    basis = []; sp = {0}
    for g in H:
        if g not in sp: basis.append(g); sp |= {s ^ g for s in sp}
    return tuple(basis)
def lemma1_eps(w, f, eps):
    """identities of the doubling-unit criterion for CD_eps: (ii) n(mu)=(mn)u, (iii) (mu)n=(m nbar)u,
    (iv) (nu)(mu) = -eps mbar n, (v) u^2 = -eps, ubar=-u, u mbar = m u;  N = K + K(e_c e)."""
    N = w.shape[0]; W = dbl(w, False, eps); B = 2 * N; top = N; m = mul_fn(W)
    def E(i):
        v = np.zeros(B); v[i] = 1; return v
    def cj(x):
        y = -x.copy(); y[0] = x[0]; return y
    c = next(g for g in range(1, N) if bin(f & g).count('1') % 2 == 1)
    Nidx = [p for p in range(N) if bin(f & p).count('1') % 2 == 0]; Nidx = Nidx + [p ^ c ^ top for p in Nidx]
    u = E(top); ok = True
    ok &= np.allclose(m(u, u), -eps * E(0)) and np.allclose(cj(u), -u)
    for a in Nidx:
        ok &= np.allclose(m(u, cj(E(a))), m(E(a), u))
        for b in Nidx:
            n, mm = E(a), E(b)
            ok &= np.allclose(m(n, m(mm, u)), m(m(mm, n), u))
            ok &= np.allclose(m(m(mm, u), n), m(m(mm, cj(n)), u))
            ok &= np.allclose(m(m(n, u), m(mm, u)), -eps * m(cj(mm), n))
    return bool(ok)
O = cd_tower(3)
bases = {'S': dbl(O, False, 1), 'split S': dbl(O, False, -1), 'split M(O)': dbl(O, True, -1), 'split O = CD_-(H)': dbl(cd_tower(2), False, -1)}
for nm, w in bases.items():
    print(f'  inner {nm:18s} anticommutative {is_anticomm(w)!s:5s} diag(w): {dict(Counter(int(x) for x in np.diag(w)[1:]))}')
    for eps in (1, -1):
        res = Counter(lemma1_eps(w, f, eps) for f in range(1, w.shape[0]))
        print(f'      outer eps={eps:+d}: identities hold for {res[True]}/{sum(res.values())} hyperplanes K')
