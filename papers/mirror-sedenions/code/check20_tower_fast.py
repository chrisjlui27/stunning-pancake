"""Fast tower: build the sign table of a double directly from the base's, O(n^2),
and count two-term zero divisors by the coset closed form, vectorised."""
import numpy as np, sys
from collections import Counter

def dbl(w, mirror=False, eps=1):
    """sign table of CD(A) (or M(A)) from that of A.  Index g<n is A, g+n is (A e)."""
    n = w.shape[0]; N = 2*n
    W = np.zeros((N,N), dtype=np.int8)
    s = np.ones(n, dtype=np.int8); s[1:] = -1          # sign of conjugation on e_q
    # A x A
    W[:n,:n] = w.T if mirror else w
    # A x Ae :  e_p (e_q e) = (e_q e_p) e
    W[:n, n:] = w.T
    # Ae x A :  (e_p e) e_q = (e_p ebar_q) e
    W[n:, :n] = w * s[None, :]
    # Ae x Ae : (e_p e)(e_q e) = -eps * ebar_q e_p
    W[n:, n:] = -eps * (w.T * s[:, None]).T * 0 + (-eps) * (s[None,:].T * w.T).T
    # (rewritten explicitly below to avoid ambiguity)
    for p in range(n):
        for q in range(n):
            W[n+p, n+q] = -eps * s[q] * w[q, p]
    return W

def zd(w):
    """(signed count, Counter of annihilator dims) for two-term basis zero divisors"""
    n = w.shape[0]; U = np.arange(n); cnt = 0; dims = Counter()
    for d in range(1, n):
        P = w * w[:, U ^ d]                      # P[i] = w(i,u) w(i,u^d) over u
        for i in range(1, n):
            j = i ^ d
            if j <= i or j == 0: continue
            k = int((P[i] == P[j]).sum()) // 2   # cosets {u, u^d}
            if k: cnt += 2; dims[k] += 1
    return cnt, dims

wO = np.array([[0]*8]*8, dtype=np.int8)
# seed from cd.py's octonions
sys.path.insert(0,'.')
from cd import struct, register, mulO
register('O8', mulO, 8); T = struct('O8')
for p in range(8):
    for q in range(8):
        nz = np.nonzero(np.abs(T[p,q])>1e-9)[0]; wO[p,q] = int(np.sign(T[p,q][nz[0]]))

levels = {0: [("O", wO)]}
for k in range(1,5):
    cur = []
    for nm,w in levels[k-1]:
        cur.append((("CD·"+nm) if nm!="O" else "CD(O)", dbl(w, False)))
        cur.append((("M·"+nm)  if nm!="O" else "M(O)",  dbl(w, True)))
    levels[k] = cur
for k in (1,2,3,4):
    print("="*76); print(f"U{k}  —  dimension {8*2**k}   ({len(levels[k])} words)"); print("="*76)
    seen = {}
    for nm,w in levels[k]:
        c,dims = zd(w)
        lead = 0
        for ch in nm.replace("(O)","").split("·"):
            if ch.startswith("M"): lead += 1
            else: break
        seen.setdefault(c, []).append((nm, lead))
        print(f"  {nm:22s} leading-M={lead}  2-term ZD {c:6d}")
        sys.stdout.flush()
    print(f"  --> {len(seen)} distinct counts (theorem predicts at most {k+1})")
    for c,ws in sorted(seen.items()):
        leads = sorted(set(l for _,l in ws))
        print(f"      {c:6d}: {len(ws)} words, leading-M values {leads}")
