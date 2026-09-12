"""Backtracking graded-isomorphism search on F_2^5 (|GL(5,2)| = 9999360, so enumerate with pruning)."""
import numpy as np, sys, itertools
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

def consistent(V, sig, wA, wB):
    """is  mu(p)+mu(q)+mu(p^q) = [wA(p,q)*wB(sig p,sig q) < 0]  solvable on subspace V?"""
    nz=[v for v in V if v]; idx={v:i for i,v in enumerate(nz)}; m=len(nz)
    rows=[]
    for a in range(m):
        for b in range(a+1,m):
            p,q=nz[a],nz[b]; r=p^q
            row=np.zeros(m+1,dtype=np.uint8)
            row[idx[p]]^=1; row[idx[q]]^=1; row[idx[r]]^=1
            row[m]= 1 if wA[p,q]*wB[sig[p],sig[q]]<0 else 0
            rows.append(row)
    if not rows: return True
    M=np.array(rows,dtype=np.uint8); piv=0
    for c in range(m):
        r=None
        for rr in range(piv,M.shape[0]):
            if M[rr,c]: r=rr; break
        if r is None: continue
        M[[piv,r]]=M[[r,piv]]
        mask=M[:,c].astype(bool).copy(); mask[piv]=False
        M[mask]^=M[piv]; piv+=1
    # inconsistent iff some row is all-zero in cols 0..m-1 but 1 in col m
    return not np.any((M[:,:m].sum(axis=1)==0) & (M[:,m]==1))

def search(wA,wB,n=5,limit=None):
    N=1<<n; gens=[1<<i for i in range(n)]; sols=[]
    def rec(k, sig, span):
        if limit and len(sols)>=limit: return
        if k==n:
            sols.append(dict(sig)); return
        for img in range(1,N):
            if img in span: continue
            newsig=dict(sig); newspan=list(span)
            for v in span:
                newsig[v^gens[k]] = sig[v]^img
                newspan.append(v^gens[k])
            if not consistent(newspan,newsig,wA,wB): continue
            rec(k+1,newsig,newspan)
            if limit and len(sols)>=limit: return
    rec(0,{0:0},[0])
    return sols

A={'T':CD(CD(mulO)),'CDSm':CD(MIR(mulO)),'MS':MIR(CD(mulO)),'MSm':MIR(MIR(mulO))}
W={k:omega(v,32) for k,v in A.items()}
print("graded isomorphism search on F_2^5 (dimension 32)")
for a,b,lab in (('T','T','Aut(T)  [sanity]'),('T','CDSm','T  ->  CD(S′)'),
                ('MS','MSm','M(S) -> M(S′)'),('T','MS','T  ->  M(S)')):
    s=search(W[a],W[b],limit=(1 if a!=b else None))
    if a==b: print(f"  {lab:22s} graded automorphisms (sigma count): {len(s)}")
    else:    print(f"  {lab:22s} {'ISOMORPHIC — found ' + str(len(s)) if s else 'NOT graded-isomorphic'}")
    sys.stdout.flush()
