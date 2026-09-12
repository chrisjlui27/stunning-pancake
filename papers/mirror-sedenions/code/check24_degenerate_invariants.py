"""
check24 -- Wilmot-style incidence of two-term zero divisors with the P4 hyperplanes, and the
structure of the 6-dimensional derivation algebra, for the degenerate 16-dim classes.
"""
import pickle, numpy as np
from collections import Counter
from landscape import *
reg = pickle.load(open('landscape_registry_n6.pkl', 'rb')); classes = reg['classes']
byk = {k: {c['label']: c['w'] for c in lst} for k, lst in classes.items()}
def classify8(w):
    A = assoc_pattern(w)
    for lab, rep in byk[3].items():
        if iso_search(assoc_pattern(rep), A) is not None: return lab
def zd_pairs(w):
    N = w.shape[0]; U = np.arange(N); pairs = {}
    for d in range(1, N):
        P = w * w[:, U ^ d]
        for i in range(1, N):
            j = i ^ d
            if j <= i or j == 0: continue
            k = int((P[i] == P[j]).sum()) // 2
            if k: pairs[(i, j)] = k
    return pairs
print('=== incidence of two-term zero-divisor index pairs with the 8-dim basis hyperplanes ===')
for lab in ['S', "S'", 'X16.2', 'X16.3']:
    w = byk[4][lab]; pairs = zd_pairs(w)
    mult = Counter(); per = Counter(); types = {}
    for f in range(1, 16):
        H = [g for g in range(16) if bin(f & g).count('1') % 2 == 0]
        basis = []; sp = {0}
        for g in H:
            if g not in sp: basis.append(g); sp |= {s ^ g for s in sp}
        t = classify8(restrict(w, tuple(basis))); types[f] = t
        # zero-divisor pairs OF THE SUBALGEBRA H itself (Wilmot's count), mapped back to ambient indices
        pos = {g: i for i, g in enumerate(span(tuple(basis)))}; inv = {i: g for g, i in pos.items()}
        sub = restrict(w, tuple(basis)); inH = [tuple(sorted((inv[a], inv[b]))) for (a, b) in zd_pairs(sub)]
        per[(t, len(inH))] += 1
        for p in inH: mult[p] += 1
    assert all(p in pairs for p in mult), 'a subalgebra zero divisor is a zero divisor of the whole algebra'
    prof = Counter(mult.get(p, 0) for p in pairs)
    by_ann = Counter((pairs[p], mult.get(p, 0)) for p in pairs)
    print(f'  {lab:6s}: {len(pairs)} ZD pairs; internal ZD pairs per 8-dim hyperplane by type {dict(per)}; incidence total {sum(mult.values())}; multiplicity profile {dict(sorted(prof.items()))}; (dim Ann, multiplicity) {dict(sorted(by_ann.items()))}')

print('\n=== derivation algebra: dimension, dimension of [Der,Der], centre ===')
def der_basis(w):
    N = w.shape[0]; T = struct_tensor(w); P = np.arange(N)
    rows = np.zeros((N, N, N, N, N))
    for i in range(N):
        for j in range(N):
            rows[i, j, :, :, i ^ j][P, P] += w[i, j]
            rows[i, j, :, :, i] -= T[:, j, :].T
            rows[i, j, :, :, j] -= T[i, :, :].T
    M = rows.reshape(N ** 3, N ** 2)
    u, s, vt = np.linalg.svd(M, full_matrices=True)
    null = vt[np.sum(s > 1e-9 * s[0]):]
    return [v.reshape(N, N) for v in null]
for lab in ['P4', 'X16.2', 'X16.3', 'S']:
    k = 3 if lab == 'P4' else 4
    D = der_basis(byk[k][lab]); d = len(D)
    comms = np.array([(A @ B - B @ A).ravel() for A in D for B in D])
    rk = np.linalg.matrix_rank(comms, tol=1e-8)
    # centre: X with [X, D_i] = 0 for all i
    Dm = np.array([x.ravel() for x in D])
    C = np.array([[np.linalg.norm(A @ B - B @ A) for B in D] for A in D])
    # Killing form signature to identify compact semisimple part
    ad = np.array([[np.linalg.lstsq(Dm.T, (A @ B - B @ A).ravel(), rcond=None)[0] for B in D] for A in D])  # ad_A in basis
    kill = np.array([[np.trace(ad[i] @ ad[j]) for j in range(d)] for i in range(d)])
    ev = np.linalg.eigvalsh((kill + kill.T) / 2)
    print(f'  {lab:6s}: dim Der = {d}, dim [Der,Der] = {rk}, Killing form eigenvalue signs: {"".join("+" if e > 1e-6 else ("-" if e < -1e-6 else "0") for e in ev)}')
    # orbit structure of Der on the 15 imaginary basis directions: rank of span{D e_i}
    for i in [1, len(D[0]) // 2, len(D[0]) - 1]:
        V = np.array([X[:, i] for X in D]); print(f'      dim (Der . e_{i}) = {np.linalg.matrix_rank(V, tol=1e-8)}', end='')
    print()
