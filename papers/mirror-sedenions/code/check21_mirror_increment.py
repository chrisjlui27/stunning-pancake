"""Prop 5.4 generalised?  At dimension 16 the first mirror adds exactly the 14 pairs
(i, i+8) and (i, 8).  In general that pattern would be
     {(i, i+n/2)} u {(i, n/2)},  1 <= i < n/2      -> (n/2-1)+(n/2-1) = n-2 pairs,
which is exactly the observed increment.  Test at n = 16, 32, 64, 128."""
import numpy as np
from collections import Counter
import sys
def dbl(w, mirror=False):
    n=w.shape[0]; N=2*n; W=np.zeros((N,N),dtype=np.int8)
    s=np.ones(n,dtype=np.int8); s[1:]=-1
    W[:n,:n]= w.T if mirror else w
    W[:n,n:]= w.T
    W[n:,:n]= w*s[None,:]
    for p in range(n):
        for q in range(n): W[n+p,n+q] = -s[q]*w[q,p]
    return W
def zd_pairs(w):
    n=w.shape[0]; U=np.arange(n); out=set()
    for d in range(1,n):
        P=w*w[:,U^d]
        for i in range(1,n):
            j=i^d
            if j<=i: continue
            if (P[i]==P[j]).sum(): out.add((i,j))
    return out
sys.path.insert(0,'.')
from cd import struct, register, mulO
register('O8',mulO,8); T=struct('O8')
wO=np.zeros((8,8),dtype=np.int8)
for p in range(8):
    for q in range(8):
        nz=np.nonzero(np.abs(T[p,q])>1e-9)[0]; wO[p,q]=int(np.sign(T[p,q][nz[0]]))
w=wO
for k in range(1,5):
    n=8*2**k; h=n//2
    wCD=dbl(w,False); wM=dbl(w,True)
    A=zd_pairs(wCD); B=zd_pairs(wM)
    new=B-A; lost=A-B
    predicted={(i,i+h) for i in range(1,h)} | {(i,h) for i in range(1,h)}
    print(f"dim {n:4d}:  CD pairs {len(A):5d}   M pairs {len(B):5d}   new {len(new):4d}  lost {len(lost):3d}")
    print(f"          predicted new = {{(i,i+{h})}} u {{(i,{h})}} : {len(predicted)} pairs   MATCH: {new==predicted}")
    w=wCD   # continue up the CD spine so the next level compares CD^k vs M.CD^(k-1)
