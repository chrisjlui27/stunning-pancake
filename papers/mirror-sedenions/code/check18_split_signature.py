"""Does CD erase a split the way it erases a mirror?"""
import numpy as np, itertools, sys
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
            v=mulf(ep,eq); nz=np.nonzero(np.abs(v)>1e-9)[0]
            if len(nz)!=1 or nz[0]!=(p^q): return None
            w[p,q]=int(np.sign(v[nz[0]]))
    return w
def signature(w,n):
    """N(x) = x x-bar = sum_g (-w[g,g]) x_g^2 for g != 0, plus x_0^2"""
    pos=1; neg=0
    for g in range(1,n):
        if -w[g,g] > 0: pos+=1
        else: neg+=1
    return pos,neg
def zd_count(w,n):
    c=0
    for i in range(1,n):
        for j in range(i+1,n):
            d=i^j; seen=np.zeros(n,bool); k=0
            for u in range(n):
                if seen[u]: continue
                v=u^d; seen[u]=seen[v]=True
                if w[i,u]*w[i,v]==w[j,u]*w[j,v]: k+=1
            if k>0: c+=2
    return c

# build: O -> {CD, M, CD-, M-} at level 1, then {CD, M} at level 2
L1={'CD(O)=S':CD(mulO),"M(O)=S′":MIR(mulO),'CD₋(O)=split S':CD(mulO,-1),'M₋(O)=split mirror':MIR(mulO,-1)}
print(f"{'algebra':26s} {'dim':>4} {'signature':>12} {'2-term ZD':>10}")
for nm,m in L1.items():
    w=omega(m,16); print(f"{nm:26s} {16:4d} {str(signature(w,16)):>12} {zd_count(w,16):10d}")
print()
L2={}
for nm,m in L1.items():
    L2[f'CD({nm.split("=")[-1]})']=CD(m); L2[f'M({nm.split("=")[-1]})']=MIR(m)
for nm,m in L2.items():
    w=omega(m,32); print(f"{nm:26s} {32:4d} {str(signature(w,32)):>12} {zd_count(w,32):10d}")
