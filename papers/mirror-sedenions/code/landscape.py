"""
landscape.py -- the basis-subalgebra landscape of the Cayley-Dickson tower.

Everything here is about SIGN-MONOMIAL algebras on F_2^n:  e_p e_q = w(p,q) e_{p^q},
w(p,q) in {+1,-1}, given as an (N,N) int8 array with N = 2^n.  Every basis subalgebra
(span of a subgroup of F_2^n) of a Cayley-Dickson algebra is again such an algebra.

Key fact used throughout (proved in synthesis/degenerate-subalgebras.md, "The
associator pattern"): for anti-commutative sign tables with e_p^2 = -1, two tables
are graded-isomorphic  (e_p -> lambda(p) e_{sigma p}, sigma in GL(n,2))  iff some
sigma carries the ASSOCIATOR PATTERN

    assoc(p,q,r) = w(p,q) w(p^q,r) w(q,r) w(p,q^r)          ( = +1 iff (e_p e_q) e_r = e_p (e_q e_r) )

of one onto the other.  So graded isomorphism is an orbit problem of GL(n,2) on
associator patterns, and can be decided by a pruned backtracking search rather than
by enumerating GL(n,2).
"""
import numpy as np
from collections import Counter
from itertools import combinations

# --------------------------------------------------------------------------- doubling
def dbl(w, mirror=False, eps=1):
    """Sign table of CD(A) (mirror=False) or M(A) (mirror=True) from that of A.
    Index p < n is A, p + n is A e.   (a,b)(c,d) = (ac - eps d* b, da + b c*),
    mirror replaces ac by ca."""
    n = w.shape[0]; N = 2 * n
    W = np.zeros((N, N), dtype=np.int8)
    s = np.ones(n, dtype=np.int8); s[1:] = -1                # conjugation sign
    W[:n, :n] = w.T if mirror else w
    W[:n, n:] = w.T                                          # e_p (e_q e) = (e_q e_p) e
    W[n:, :n] = w * s[None, :]                               # (e_p e) e_q = (e_p e_q*) e
    W[n:, n:] = -eps * (s[None, :] * w.T)                    # (e_p e)(e_q e) = -eps e_q* e_p
    return W

def cd_tower(n, eps=1):
    w = np.ones((1, 1), dtype=np.int8)
    for _ in range(n):
        w = dbl(w, False, eps)
    return w

def word(wd, base=None):
    """Apply a word in {'C','M'} (outermost letter FIRST, as in 'CM' = CD(M(base)))."""
    w = cd_tower(3) if base is None else base
    for ch in reversed(wd):
        w = dbl(w, ch == 'M')
    return w

# --------------------------------------------------------------------------- subgroups of F_2^n
def subspaces(n, k):
    """All k-dim subspaces of F_2^n, each as a tuple of k basis vectors in reduced echelon
    form (pivot = lowest set bit)."""
    out = []
    for piv in combinations(range(n), k):
        free = [[j for j in range(n) if j not in piv and j > p] for p in piv]
        nfree = [len(f) for f in free]
        for bits in range(1 << sum(nfree)):
            rows = []; off = 0
            for i, p in enumerate(piv):
                v = 1 << p
                for t, j in enumerate(free[i]):
                    if (bits >> (off + t)) & 1: v |= 1 << j
                off += nfree[i]
                rows.append(v)
            out.append(tuple(rows))
    return out

def span(basis):
    k = len(basis); g = np.zeros(1 << k, dtype=np.int64)
    for x in range(1 << k):
        v = 0
        for i in range(k):
            if (x >> i) & 1: v ^= basis[i]
        g[x] = v
    return g

def restrict(w, basis):
    g = span(basis)
    return np.ascontiguousarray(w[np.ix_(g, g)])

# --------------------------------------------------------------------------- basic checks
def is_anticomm(w):
    N = w.shape[0]
    return bool(np.all(w[0] == 1) and np.all(w[:, 0] == 1) and np.all(np.diag(w)[1:] == -1)
                and np.all((w + w.T)[1:, 1:][~np.eye(N - 1, dtype=bool)] == 0))

def quaternion_property(w):
    """Bales's quaternion property: e_p e_q = e_r  =>  e_q e_p = -e_r  and  e_q e_r = e_p.
    Equivalently every 2-dim subspace spans an associative (quaternion) subalgebra."""
    N = w.shape[0]; P = np.arange(N)
    ok = True
    for p in range(1, N):
        q = P[1:]; q = q[q != p]
        ok &= bool(np.all(w[p, q] == -w[q, p]) and np.all(w[q, p ^ q] == w[p, q]))
    return ok

# --------------------------------------------------------------------------- associator pattern
def assoc_pattern(w):
    """A[p,q,r] = +1 iff (e_p e_q) e_r = e_p (e_q e_r)."""
    N = w.shape[0]; P = np.arange(N)
    pq = P[:, None] ^ P[None, :]
    A = (w[:, :, None] * w[pq, :][:, :, :]                     # w(p,q) w(p^q, r)
         * w[None, :, :] * w[:, pq][:, :, :])                  # w(q,r) w(p, q^r)  -- w[:, pq] gives w[p, q^r] indexed [p,q,r]
    return A.astype(np.int8)

def _check_assoc_impl():
    rng = np.random.default_rng(0)
    w = cd_tower(4); A = assoc_pattern(w); N = 16
    for _ in range(200):
        p, q, r = rng.integers(0, N, 3)
        lhs = w[p, q] * w[p ^ q, r]; rhs = w[q, r] * w[p, q ^ r]
        assert A[p, q, r] == lhs * rhs
_check_assoc_impl()

def nonassoc_triads(w):
    """Unordered independent triples {p,q,r} (nonzero, r != p^q) on which the algebra is
    NOT associative; also returns whether non-associativity is ordering-independent."""
    N = w.shape[0]; A = assoc_pattern(w)
    bad = set(); consistent = True
    for p in range(1, N):
        for q in range(p + 1, N):
            for r in range(q + 1, N):
                if r == p ^ q: continue
                vals = {A[p, q, r], A[p, r, q], A[q, p, r], A[q, r, p], A[r, p, q], A[r, q, p]}
                if len(vals) > 1: consistent = False
                if -1 in vals: bad.add(frozenset((p, q, r)))
    return len(bad), consistent

# --------------------------------------------------------------------------- graded isomorphism
def iso_search(A1, A2, count=False, limit=None):
    """Find sigma in GL(n,2) with A2[sigma p, sigma q, sigma r] = A1[p,q,r].
    Returns the first sigma found (as basis images) or None; with count=True returns the
    number of such sigma (the graded automorphism group mod the lambda's when A1 == A2)."""
    N = A1.shape[0]; n = N.bit_length() - 1
    found = [0]; first = [None]
    def rec(sig, imgs):
        m = len(sig)
        if m == N:
            found[0] += 1
            if first[0] is None: first[0] = list(imgs)
            return not count or (limit is not None and found[0] >= limit)
        used = set(sig.tolist())
        sub1 = A1[:2 * m, :2 * m, :2 * m]
        for v in range(1, N):
            if v in used: continue
            new = np.concatenate([sig, sig ^ v])
            if np.array_equal(A2[np.ix_(new, new, new)], sub1):
                if rec(new, imgs + [v]): return True
        return False
    rec(np.array([0], dtype=np.int64), [])
    return found[0] if count else first[0]

def graded_iso(w1, w2):
    """True iff w1 and w2 are graded-isomorphic (anticommutative tables assumed)."""
    if w1.shape != w2.shape: return False
    return iso_search_pruned(assoc_pattern(w1), assoc_pattern(w2)) is not None

def sigma_count(w):
    A = assoc_pattern(w)
    return iso_search_pruned(A, A, count=True)

# --------------------------------------------------------------------------- invariants
def zd(w):
    """Two-term basis zero divisors e_i +- e_j: (signed count, Counter of dim Ann)."""
    N = w.shape[0]; U = np.arange(N); cnt = 0; dims = Counter()
    for d in range(1, N):
        P = w * w[:, U ^ d]
        for i in range(1, N):
            j = i ^ d
            if j <= i or j == 0: continue
            k = int((P[i] == P[j]).sum()) // 2
            if k: cnt += 2; dims[k] += 1
    return cnt, dict(sorted(dims.items()))

def struct_tensor(w):
    N = w.shape[0]; T = np.zeros((N, N, N))
    P = np.arange(N); pq = P[:, None] ^ P[None, :]
    T[P[:, None], P[None, :], pq] = w
    return T

def der_dim(w):
    """dim of the derivation algebra, by linear algebra on D(e_i e_j) = D(e_i) e_j + e_i D(e_j)."""
    N = w.shape[0]; T = struct_tensor(w)
    # unknown D as N x N matrix (D e_i = sum_k D[k,i] e_k).  Equation for each (i,j), output k.
    # LHS: D(e_i e_j) = w(i,j) D e_{i^j}  -> coefficient of D[k, i^j] is w(i,j)
    # RHS: (D e_i) e_j = sum_a D[a,i] e_a e_j = sum_a D[a,i] T[a,j,k] ; e_i (D e_j) = sum_a D[a,j] T[i,a,k]
    P = np.arange(N)
    rows = np.zeros((N, N, N, N, N))          # [i,j,k, a,b] coefficient of D[a,b]
    ij = P[:, None] ^ P[None, :]
    for i in range(N):
        for j in range(N):
            rows[i, j, :, :, i ^ j][P, P] += w[i, j]        # D[k, i^j]
            rows[i, j, :, :, i] -= T[:, j, :].T               # -D[a,i] T[a,j,k]  -> [k,a]
            rows[i, j, :, :, j] -= T[i, :, :].T               # -D[a,j] T[i,a,k]
    M = rows.reshape(N ** 3, N ** 2)
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-9 * s[0]))

def mul_fn(w):
    """numpy product function from a sign table (for feeding cd.double)."""
    N = w.shape[0]; T = struct_tensor(w)
    def m(x, y): return np.einsum('i,j,ijk->k', x, y, T)
    return m

def table_from_fn(m, N):
    w = np.zeros((N, N), dtype=np.int8)
    for i in range(N):
        ei = np.zeros(N); ei[i] = 1
        for j in range(N):
            ej = np.zeros(N); ej[j] = 1
            v = m(ei, ej); nz = np.nonzero(np.abs(v) > 1e-9)[0]
            assert len(nz) == 1 and nz[0] == (i ^ j), (i, j, v)
            w[i, j] = int(np.sign(v[nz[0]]))
    return w

def is_composition(w, trials=6, rng=None):
    rng = rng or np.random.default_rng(1)
    m = mul_fn(w); N = w.shape[0]
    for _ in range(trials):
        x = rng.standard_normal(N); y = rng.standard_normal(N); z = m(x, y)
        if abs(z @ z - (x @ x) * (y @ y)) > 1e-8: return False
    return True

def is_alternative(w, trials=6, rng=None):
    rng = rng or np.random.default_rng(2)
    m = mul_fn(w); N = w.shape[0]
    for _ in range(trials):
        x = rng.standard_normal(N); y = rng.standard_normal(N)
        if not (np.allclose(m(m(x, x), y), m(x, m(x, y))) and np.allclose(m(m(y, x), x), m(y, m(x, x)))):
            return False
    return True

def hyperplane_types(w, classify):
    """types (via `classify(subtable)`) of the codim-1 basis subalgebras."""
    N = w.shape[0]; n = N.bit_length() - 1
    out = []
    for f in range(1, N):
        H = [g for g in range(N) if bin(f & g).count('1') % 2 == 0]
        # H is a subgroup; pick an echelon basis
        basis = []; sp = {0}
        for g in H:
            if g not in sp:
                basis.append(g); sp |= {s ^ g for s in sp}
        out.append(classify(restrict(w, tuple(basis))))
    return Counter(out)

# --------------------------------------------------------------------------- pruned search (2026-09-12)
def _invariants(A):
    """vertex and pair statistics of an associator pattern, invariant under sigma."""
    neg = (A < 0)
    V = np.stack([neg.sum(axis=(1, 2)), neg.sum(axis=(0, 2)), neg.sum(axis=(0, 1))], axis=1)          # (N,3)
    P = np.stack([neg.sum(axis=2), neg.sum(axis=1), neg.sum(axis=0)], axis=2)                          # (N,N,3)
    return V, P

def _reorder_source(A1):
    """choose a basis of F_2^n for the source so that rare vertices come first; return (A1', tau)."""
    N = A1.shape[0]; n = N.bit_length() - 1
    V, P = _invariants(A1)
    keys = [tuple(V[p]) for p in range(N)]
    from collections import Counter as _C
    freq = _C(keys[1:])
    basis = []; sp = {0}
    while len(basis) < n:
        cands = [p for p in range(1, N) if p not in sp]
        # rarest vertex class, tie-break by rarest pair profile against chosen basis
        def score(p):
            return (freq[keys[p]], tuple(sorted(_C(tuple(P[b, p]) for b in basis).items())), p)
        b = min(cands, key=score)
        basis.append(b); sp |= {s ^ b for s in sp}
    tau = span(tuple(basis))
    return np.ascontiguousarray(A1[np.ix_(tau, tau, tau)]), basis

def iso_search_pruned(A1, A2, count=False):
    """Same contract as iso_search, with vertex/pair-invariant pruning and rarest-first source order."""
    N = A1.shape[0]; n = N.bit_length() - 1
    A1r, _ = _reorder_source(A1)
    V1, P1 = _invariants(A1r); V2, P2 = _invariants(A2)
    if sorted(map(tuple, V1)) != sorted(map(tuple, V2)): return 0 if count else None
    found = [0]; first = [None]
    def rec(sig, imgs):
        m = len(sig)
        if m == N:
            found[0] += 1
            if first[0] is None: first[0] = list(imgs)
            return not count
        i = len(imgs); b = 1 << i                      # source basis vector for this level
        used = set(sig.tolist())
        sub1 = A1r[:2 * m, :2 * m, :2 * m]
        for v in range(1, N):
            if v in used or not np.array_equal(V2[v], V1[b]): continue
            # pair invariants against everything already mapped
            if not np.array_equal(P2[sig, v], P1[:m, b]): continue
            new = np.concatenate([sig, sig ^ v])
            if np.array_equal(A2[np.ix_(new, new, new)], sub1):
                if rec(new, imgs + [v]): return True
        return False
    rec(np.array([0], dtype=np.int64), [])
    return found[0] if count else first[0]
