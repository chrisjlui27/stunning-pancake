"""The real dimension-32 analogue of Theorem 6.1: count 8-DIMENSIONAL subalgebras,
not 16-dimensional hyperplanes.  (A 16-dim subalgebra is never a composition algebra
by Hurwitz, so the 'composition hyperplane' count at dim 32 is trivially zero.)

8-dim coordinate subalgebras <-> 3-dimensional F_2 subspaces of F_2^5.
There are [5 choose 3]_2 = 155 of them -- matching Cawagas's 155 subloops of order 16.
Cawagas et al. report for T: 50 octonion + 105 quasi-octonion."""
import numpy as np, itertools, sys
from cd import struct, register, mulO, split, join, conj, norm2, mul

def CD(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y); return join(b(a,c)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
def MIR(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y); return join(b(c,a)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
def omega(mulf,n):
    w=np.zeros((n,n),dtype=np.int8)
    for p in range(n):
        ep=np.zeros(n); ep[p]=1
        for q in range(n):
            eq=np.zeros(n); eq[q]=1
            v=mulf(ep,eq); nz=np.nonzero(np.abs(v)>1e-9)[0]; w[p,q]=int(np.sign(v[nz[0]]))
    return w
def subspaces3(nbits):
    """all 3-dimensional subspaces of F_2^nbits, as sorted 8-element index sets"""
    N=1<<nbits; out=set()
    for a in range(1,N):
        for b in range(a+1,N):
            if b==a: continue
            for c in range(b+1,N):
                span={0,a,b,c,a^b,a^c,b^c,a^b^c}
                if len(span)==8: out.add(tuple(sorted(span)))
    return sorted(out)
def is_octonion(w,H):
    """the span of H is a composition algebra iff every 'line' associates in the
       octonion pattern; equivalently the 8-dim sign-monomial algebra is alternative."""
    idx={g:i for i,g in enumerate(H)}
    # alternative <=> (x x) y = x (x y) for basis elements: check associator [p,p,q]=0
    # for sign-monomial algebras: e_p(e_p e_q) = w(p,p)w(p,q)... use associator on triples
    for p in H:
        for q in H:
            for r in H:
                if p==0 or q==0 or r==0: continue
                s=w[p,q]*w[p^q,r]*w[q,r]*w[p,r^q]
                # associative triple test is only valid for dependent triples in O;
                # instead use: octonion <=> every independent triple has [p,q,r] != 0 ... 
                pass
    return None
# simpler and decisive: an 8-dim sign-monomial algebra on F_2^3 is either O (alternative,
# composition) or M(H) (not alternative).  Test alternativity numerically.
def classify(name, H, n):
    idx=np.array(H)
    rng=np.random.default_rng(abs(hash((name,H)))%(2**31))
    alt=True
    for _ in range(12):
        x=np.zeros(n); y=np.zeros(n); x[idx]=rng.standard_normal(8); y[idx]=rng.standard_normal(8)
        if not np.allclose(mul(name,mul(name,x,x),y), mul(name,x,mul(name,x,y)), atol=1e-9): alt=False; break
    return 'octonion' if alt else 'quasi-octonion'

W={'T = CD(CD(O))':CD(CD(mulO)),'M(S)':MIR(CD(mulO)),"CD(S′)":CD(MIR(mulO)),"M(S′)":MIR(MIR(mulO))}
for nm,m in W.items(): register(nm,m,32)
S3=subspaces3(5)
print(f"3-dimensional subspaces of F_2^5: {len(S3)}  (Cawagas: 155 subloops of order 16)\n")
print(f"{'algebra':18s} {'octonion':>9} {'quasi-oct':>10}   (Cawagas for T: 50 / 105)")
for nm in W:
    c=[classify(nm,H,32) for H in S3]
    print(f"  {nm:16s} {c.count('octonion'):9d} {c.count('quasi-octonion'):10d}")
    sys.stdout.flush()
