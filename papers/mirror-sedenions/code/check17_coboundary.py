"""Is the mirror defect a coboundary one level up?

chi = the ratio of the two sign functions.  S vs S' on F_2^4: the paper proves chi
is not a 2-cocycle, so certainly not a coboundary -- that is why S != S'.
Question: is the corresponding ratio for CD(S) vs CD(S') a coboundary on F_2^5,
with NO relabelling (sigma = identity)?"""
import numpy as np
from cd import *
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
def is_coboundary(wA,wB,n):
    """solvable: mu(p)+mu(q)+mu(p^q) = [wA(p,q)wB(p,q) < 0] over F_2, sigma = identity"""
    nz=list(range(1,n)); idx={v:i for i,v in enumerate(nz)}; m=len(nz); rows=[]
    for a in range(m):
        for b in range(a+1,m):
            p,q=nz[a],nz[b]; r=p^q
            row=np.zeros(m+1,dtype=np.uint8)
            row[idx[p]]^=1; row[idx[q]]^=1; row[idx[r]]^=1
            row[m]=1 if wA[p,q]*wB[p,q]<0 else 0
            rows.append(row)
    M=np.array(rows,dtype=np.uint8); piv=0
    for c in range(m):
        r=None
        for rr in range(piv,M.shape[0]):
            if M[rr,c]: r=rr; break
        if r is None: continue
        M[[piv,r]]=M[[r,piv]]
        mask=M[:,c].astype(bool).copy(); mask[piv]=False
        M[mask]^=M[piv]; piv+=1
    return not np.any((M[:,:m].sum(axis=1)==0)&(M[:,m]==1))

pairs=[("S vs S′ (dim 16, F_2^4)", omega(CD(mulO),16), omega(MIR(mulO),16), 16),
       ("CD(S) vs CD(S′) (dim 32, F_2^5)", omega(CD(CD(mulO)),32), omega(CD(MIR(mulO)),32), 32),
       ("M(S) vs M(S′) (dim 32, F_2^5)", omega(MIR(CD(mulO)),32), omega(MIR(MIR(mulO)),32), 32),
       ("CD(splitS) vs CD(splitM) (dim 32)", omega(CD(CD(mulO,-1)),32), omega(CD(MIR(mulO,-1)),32), 32),
       ("splitS vs splitM (dim 16)", omega(CD(mulO,-1),16), omega(MIR(mulO,-1),16), 16)]
print("Is the ratio of the two sign functions a COBOUNDARY (sigma = identity, signs only)?\n")
for lab,wA,wB,n in pairs:
    print(f"  {lab:36s} {'YES — pure sign relabelling' if is_coboundary(wA,wB,n) else 'no'}")
