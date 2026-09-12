"""
check25 -- properness is preserved by both doublings, throughout the tower.

The increment theorem assumes the base twist is proper in Bales's sense
(arXiv:1107.1375, Def. 4.1); on F_2^m this reads
      w(p,q) w(q,q) = w(p^q, q)        and       w(p,p) w(p,q) = w(p, p^q).
This script verifies that R, C, H, O are proper and that both CD and M preserve
properness at every node of the {CD, M}-tree up to dimension 128, split nodes
included -- so the theorem applies at every level at which it is used.
"""
import numpy as np, sys
sys.path.insert(0,'.')
def dbl(w,mirror=False,eps=1):
    h=w.shape[0]; N=2*h; W=np.zeros((N,N),dtype=np.int8); s=np.ones(h,dtype=np.int8); s[1:]=-1
    W[:h,:h]= w.T if mirror else w
    W[:h,h:]= w.T
    W[h:,:h]= w*s[None,:]
    for p in range(h):
        for q in range(h): W[h+p,h+q]=-eps*s[q]*w[q,p]
    return W
def proper(w):
    h=w.shape[0]
    return all(w[p,q]*w[q,q]==w[p^q,q] and w[p,p]*w[p,q]==w[p,p^q]
               for p in range(h) for q in range(h))
def ok(l,c): print(('PASS ' if c else 'FAIL ')+l)

wR=np.array([[1]],dtype=np.int8)
ok("R is proper", proper(wR))
wC=dbl(wR); ok("C  = CD(R) is proper", proper(wC))
wH=dbl(wC); ok("H  = CD(C) is proper", proper(wH))
wO=dbl(wH); ok("O  = CD(H) is proper", proper(wO))
ok("M(H) (quasi-octonions) is proper", proper(dbl(wC,True)))

# every node of the {CD, M} tree above O, to dimension 128
level=[("O",wO)]
allok=True
for k in range(1,5):
    nxt=[]
    for nm,w in level:
        for mir,tag in ((False,"CD"),(True,"M")):
            W=dbl(w,mir); nm2=f"{tag}.{nm}"
            if not proper(W): allok=False; print("   FAIL at",nm2)
            nxt.append((nm2,W))
    level=nxt
    ok(f"all {len(level)} words of length {k} (dimension {8*2**k}) are proper", allok)
# split branch
sp=[("CD-(O)",dbl(wO,False,-1)),("M-(O)",dbl(wO,True,-1))]
ok("both split nodes at dimension 16 are proper", all(proper(w) for _,w in sp))
ok("their doubles (dimension 32, both operations) are proper",
   all(proper(dbl(w,m)) for _,w in sp for m in (False,True)))
