"""
check23 -- every lemma of the Increment Theorem (papers/mirror-sedenions/INCREMENT-THEOREM.md).

Setup: A is a *-algebra with sign-monomial basis indexed by F_2^m, h = 2^m, twist w.
Index CD(A) and M(A) by F_2^(m+1): g < h is A, g+h is Ae.
A pair (i,j), d = i^j, is alpha (both < h), beta (both >= h) or mixed (i < h <= j).
"""
import numpy as np, sys
from collections import Counter
sys.path.insert(0,'.')
from cd import struct, register, mulO, mulH

def dbl(w, mirror=False):
    h=w.shape[0]; N=2*h; W=np.zeros((N,N),dtype=np.int8); s=np.ones(h,dtype=np.int8); s[1:]=-1
    W[:h,:h] = w.T if mirror else w
    W[:h,h:] = w.T
    W[h:,:h] = w*s[None,:]
    for p in range(h):
        for q in range(h): W[h+p,h+q] = -s[q]*w[q,p]
    return W
def sigma(p,q): return 1 if (p==q or p==0 or q==0) else -1
def contrib(W,i,j,u):
    v=u^(i^j); return W[i,u]*W[i,v]==W[j,u]*W[j,v]
def anndim(W,i,j):
    n=W.shape[0]; d=i^j; seen=np.zeros(n,bool); k=0
    for u in range(n):
        if seen[u]: continue
        v=u^d; seen[u]=seen[v]=True
        if W[i,u]*W[i,v]==W[j,u]*W[j,v]: k+=1
    return k
def zpairs(W):
    n=W.shape[0]; U=np.arange(n); out=set()
    for d in range(1,n):
        P=W*W[:,U^d]
        for i in range(1,n):
            j=i^d
            if j>i and (P[i]==P[j]).sum(): out.add((i,j))
    return out
def proper(w):
    h=w.shape[0]
    return all(w[p,q]*w[q,q]==w[p^q,q] and w[p,p]*w[p,q]==w[p,p^q]
               for p in range(h) for q in range(h))
def ok(lab,c): print(('PASS ' if c else 'FAIL ')+lab)

def run(w,label):
    h=w.shape[0]; n=2*h; A=dbl(w,False); B=dbl(w,True)
    print(f"\n=== {label}   (h={h}, dim {n}) ===")
    ok("base twist is proper (Bales Def 4.1)", proper(w))
    ok("L1  W_M = W_CD * sigma on A x A, and W_M = W_CD elsewhere",
       all(B[p,q]==A[p,q]*sigma(p,q) for p in range(h) for q in range(h)) and
       all(B[i,j]==A[i,j] for i in range(n) for j in range(n) if not (i<h and j<h)))
    ok("L2  alpha and beta pairs: dim Ann identical in CD(A) and M(A)",
       all(anndim(A,i,j)==anndim(B,i,j) for i in range(1,n) for j in range(i+1,n)
           if (i<h and j<h) or (i>=h and j>=h)))
    ok("L3  mixed pairs: cosets u in {0, p, q, t} never contribute in CD(A)",
       all(not contrib(A,p,q+h,u) for p in range(1,h) for q in range(h) for u in (0,p,q,p^q)))
    ok("L3' same four cosets never contribute in M(A) for u in {0,p} (sigma=+1 there)",
       all(not contrib(B,p,q+h,u) for p in range(1,h) for q in range(h) for u in (0,p)))
    ok("L4  mixed duality  dim Ann_M = (h-2) - dim Ann_CD",
       all(anndim(B,p,q+h)==(h-2)-anndim(A,p,q+h) for p in range(1,h) for q in range(h)))
    ok("L4  degenerate families have dim Ann_CD = 0  (j = i+h and j = h)",
       all(anndim(A,p,p+h)==0 for p in range(1,h)) and
       all(anndim(A,p,h)==0   for p in range(1,h)))
    ok("L3c dim Ann_CD(mixed) <= h - |{0,p,q,t}|",
       all(anndim(A,p,q+h) <= h-len({0,p,q,p^q}) for p in range(1,h) for q in range(h)))
    ok("T1  EVERY mixed pair is a two-term zero divisor of M(A)",
       all(anndim(B,p,q+h)>0 for p in range(1,h) for q in range(h)))
    ok("L5  alpha/beta: dim Ann of the double = 2 * dim Ann_A",
       all(anndim(A,i,j)==2*anndim(w,i,j) and anndim(B,i,j)==2*anndim(w,i,j) and
           anndim(A,i+h,j+h)==2*anndim(w,i,j) and anndim(B,i+h,j+h)==2*anndim(w,i,j)
           for i in range(1,h) for j in range(i+1,h)))
    ZA=zpairs(w); ZB=zpairs(B); ZC=zpairs(A)
    al=lambda P:sum(1 for i,j in P if i<h and j<h); be=lambda P:sum(1 for i,j in P if i>=h and j>=h)
    ok(f"T2  alpha count = beta count = Z(A) = {len(ZA)}  (in both CD and M)",
       al(ZB)==be(ZB)==al(ZC)==be(ZC)==len(ZA))
    ok(f"T3  Z(M(A)) = 2 Z(A) + h(h-1) = {2*len(ZA)+h*(h-1)}   [got {len(ZB)}]",
       len(ZB)==2*len(ZA)+h*(h-1))
    exc=sorted({(i,j) for i in range(1,h) for j in range(h,n)} - ZC)
    pred=sorted({(p,p+h) for p in range(1,h)} | {(p,h) for p in range(1,h)})
    print(f"     (CD exceptions: {len(exc)}; equal to the two degenerate families: {exc==pred})")

def bo(name,mulf,n):
    register(name,mulf,n); T=struct(name); w=np.zeros((n,n),dtype=np.int8)
    for p in range(n):
        for q in range(n):
            nz=np.nonzero(np.abs(T[p,q])>1e-9)[0]; w[p,q]=int(np.sign(T[p,q][nz[0]]))
    return w
wH=bo('H4',mulH,4); wO=bo('O8',mulO,8)
run(wH,"A = H"); run(wO,"A = O"); run(dbl(wO,False),"A = S"); run(dbl(wO,True),"A = S'")
run(dbl(dbl(wO,False),False),"A = T"); run(dbl(dbl(wO,False),True),"A = M(S)")
