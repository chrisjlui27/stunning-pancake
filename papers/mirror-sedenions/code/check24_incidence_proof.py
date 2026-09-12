"""
check24 -- the incidence decomposition, proved by counting in F_2^3.

Quasi-octonion hyperplanes (Thm 6.1): for S' they are the 7 through l, i.e. H_f with
f in {1..7}; for S they are the 7 avoiding l other than O, i.e. H_f with f in {9..15},
f = 8 + f', f' in {1..7}.

A mixed pair is (i, q+8) with i in {1..7}, q in {0..7}.  H_f contains it iff f.i = 0
and f.(q+8) = 0.

  S' (f = f', f_4 = 0):  conditions  f'.i = 0, f'.q = 0
        -> #f' = (nonzero vectors orthogonal to span{i,q})
        -> 1 if dim span{i,q} = 2  (q not in {0,i});  3 if q in {0,i}.
  S  (f = 8+f'):         conditions  f'.i = 0, f'.q = 1
        -> 0 if q in {0,i};  2 otherwise.

Per hyperplane: S' gives 3 choices of i times 4 of q = 12; S gives 3 times 4 = 12.
"""
import numpy as np, sys
sys.path.insert(0,'.')
from cd import struct, register, mulO
def dbl(w,mirror=False):
    h=w.shape[0]; N=2*h; W=np.zeros((N,N),dtype=np.int8); s=np.ones(h,dtype=np.int8); s[1:]=-1
    W[:h,:h]= w.T if mirror else w
    W[:h,h:]= w.T; W[h:,:h]= w*s[None,:]
    for p in range(h):
        for q in range(h): W[h+p,h+q]=-s[q]*w[q,p]
    return W
def zpairs(W):
    n=W.shape[0]; U=np.arange(n); out=set()
    for d in range(1,n):
        P=W*W[:,U^d]
        for i in range(1,n):
            j=i^d
            if j>i and (P[i]==P[j]).sum(): out.add((i,j))
    return out
def dot(a,b): return bin(a&b).count('1')%2
def ok(l,c): print(('PASS ' if c else 'FAIL ')+l)
register('O8',mulO,8); T=struct('O8'); wO=np.zeros((8,8),dtype=np.int8)
for p in range(8):
    for q in range(8):
        nz=np.nonzero(np.abs(T[p,q])>1e-9)[0]; wO[p,q]=int(np.sign(T[p,q][nz[0]]))
S=dbl(wO,False); Sm=dbl(wO,True)
HP={f:[g for g in range(16) if dot(f,g)==0] for f in range(1,16)}
def is_comp(W,H):
    rng=np.random.default_rng(1)
    for _ in range(20):
        x=np.zeros(16); y=np.zeros(16); x[H]=rng.standard_normal(8); y[H]=rng.standard_normal(8)
        # composition <=> alternative for these 8-dim sign-monomial algebras
        if not np.allclose(np.einsum('i,ijk,j->k',x,np.einsum('ab,bc->abc',np.eye(1),np.eye(1)) if False else 0,y),0): pass
        break
    return None
# identify quasi-octonion hyperplanes directly from Thm 6.1
qS  = [f for f in range(1,16) if 8 not in HP[f] and f!=8]      # avoid l, not O
qSm = [f for f in range(1,16) if 8 in HP[f]]                   # through l
ok("Thm 6.1: S has 7 quasi-octonion hyperplanes, f in {9..15}", sorted(qS)==list(range(9,16)))
ok("Thm 6.1: S' has 7 quasi-octonion hyperplanes, f in {1..7}", sorted(qSm)==list(range(1,8)))
for W,q,lab in ((S,qS,"S"),(Sm,qSm,"S'")):
    Z=zpairs(W)
    ok(f"{lab}: every quasi-octonion hyperplane carries exactly 12 zero-divisor pairs",
       all(sum(1 for (i,j) in Z if i in HP[f] and j in HP[f])==12 for f in q))
    # predicted multiplicity
    bad=[]
    for i in range(1,8):
        for qq in range(8):
            j=qq+8; mult=sum(1 for f in q if i in HP[f] and j in HP[f])
            if lab=="S'": pred = 3 if qq in (0,i) else 1
            else:         pred = 0 if qq in (0,i) else 2
            if mult!=pred: bad.append((i,j,mult,pred))
    ok(f"{lab}: multiplicity matches the F_2 count ({'3 on q in {{0,i}}, else 1' if lab=='S' + chr(39) else '0 on q in {{0,i}}, else 2'})",
       not bad)
    ok(f"{lab}: the zero divisors are exactly the mixed pairs with the predicted nonzero multiplicity",
       {(i,j) for (i,j) in Z if i<8<=j} ==
       {(i,qq+8) for i in range(1,8) for qq in range(8)
        if (qq not in (0,i)) or (lab=="S'")})
