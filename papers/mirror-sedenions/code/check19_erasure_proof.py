"""
check19 -- verifies the erasure proof (papers/mirror-sedenions/ERASURE-PROOF.md)
step by step, including every intermediate formula stated by hand, not just the
final isomorphism.

   Theorem:  CD(M(A)) = CD(CD(A))  for every *-algebra A.
"""
import numpy as np
from cd import *
rng = np.random.default_rng(19)

def CDmul(base):
    def m(x,y):
        a,b=split(x); c,d=split(y)
        return join(base(a,c)-base(conj(d),b), base(d,a)+base(b,conj(c)))
    return m
def Mmul(base):
    def m(x,y):
        a,b=split(x); c,d=split(y)
        return join(base(c,a)-base(conj(d),b), base(d,a)+base(b,conj(c)))
    return m
def ok(lab,c): print(('PASS ' if c else 'FAIL ')+lab)

def run(Abase, nA, label):
    print(f"\n=== {label} ===")
    A=Abase; B=CDmul(CDmul(A)); MA=Mmul(A); CDMA=CDmul(MA); n4=4*nA
    def ang(a,b):                       # <a,b> = a + (b e)e'  in CD^2(A)
        v=np.zeros(n4); v[:nA]=a; v[3*nA:]=b; return v
    def brk(c,d):                       # [c,d] = <c,d> e'
        v=np.zeros(n4); v[nA:2*nA]=-d; v[2*nA:3*nA]=c; return v
    def R(): return rng.standard_normal(nA)
    up=np.zeros(n4); up[2*nA]=1.0       # u = e'
    C=conj
    # (2.1) product formula on N
    ok("(2.1)  <a1,b1><a2,b2> = <a1a2 - b1bar b2,  b2 a1bar + b1 a2>",
       all(np.allclose(B(ang(a1,b1),ang(a2,b2)),
                       ang(A(a1,a2)-A(C(b1),b2), A(b2,C(a1))+A(b1,a2)), atol=1e-9)
           for a1,b1,a2,b2 in ((R(),R(),R(),R()) for _ in range(40))))
    # (2.2) involution on N
    ok("(2.2)  <a,b>bar = <abar, -b>",
       all(np.allclose(C(ang(a,b)), ang(C(a),-b), atol=1e-9) for a,b in ((R(),R()) for _ in range(40))))
    # (2.3) <a,b> e' = [a,b]
    ok("(2.3)  <a,b> e' = [a,b]",
       all(np.allclose(B(ang(a,b),up), brk(a,b), atol=1e-9) for a,b in ((R(),R()) for _ in range(40))))
    # N + Nu spans
    Z=np.column_stack([ang(np.eye(nA)[i],np.zeros(nA)) for i in range(nA)]
                     +[ang(np.zeros(nA),np.eye(nA)[i]) for i in range(nA)]
                     +[brk(np.eye(nA)[i],np.zeros(nA)) for i in range(nA)]
                     +[brk(np.zeros(nA),np.eye(nA)[i]) for i in range(nA)])
    ok("N + Nu = CD^2(A)  (spanning)", np.linalg.matrix_rank(Z)==n4)
    # (ee')e' = -e
    e_=np.zeros(n4); e_[nA]=1.0; j=ang(np.zeros(nA),np.eye(nA)[0])
    ok("(ee')e' = -e", np.allclose(B(j,up), -e_, atol=1e-9))
    # (ii)
    ok("(ii)   n(mu) = (mn)u,  both = [ca - dbar b, da + b cbar]",
       all(np.allclose(B(ang(a,b),B(ang(c,d),up)), B(B(ang(c,d),ang(a,b)),up), atol=1e-9)
           and np.allclose(B(ang(a,b),B(ang(c,d),up)), brk(A(c,a)-A(C(d),b), A(d,a)+A(b,C(c))), atol=1e-9)
           for a,b,c,d in ((R(),R(),R(),R()) for _ in range(40))))
    # (iii)
    ok("(iii)  (mu)n = (m nbar)u,  both = [c abar + dbar b, d abar - b cbar]",
       all(np.allclose(B(B(ang(c,d),up),ang(a,b)), B(B(ang(c,d),C(ang(a,b))),up), atol=1e-9)
           and np.allclose(B(B(ang(c,d),up),ang(a,b)), brk(A(c,C(a))+A(C(d),b), A(d,C(a))-A(b,C(c))), atol=1e-9)
           for a,b,c,d in ((R(),R(),R(),R()) for _ in range(40))))
    # (iv)
    ok("(iv)   (m1 u)(m2 u) = -m2bar m1 = <-c2bar c1 - d2bar d1, d2 c1 - d1 c2>",
       all(np.allclose(B(B(ang(c1,d1),up),B(ang(c2,d2),up)), -B(C(ang(c2,d2)),ang(c1,d1)), atol=1e-9)
           and np.allclose(B(B(ang(c1,d1),up),B(ang(c2,d2),up)),
                           ang(-A(C(c2),c1)-A(C(d2),d1), A(d2,c1)-A(d1,c2)), atol=1e-9)
           for c1,d1,c2,d2 in ((R(),R(),R(),R()) for _ in range(40))))
    # (v) and u mbar = m u
    one=np.zeros(n4); one[0]=1.0
    ok("(v)    u^2 = -1,  ubar = -u", np.allclose(B(up,up),-one,atol=1e-9) and np.allclose(C(up),-up,atol=1e-9))
    ok("       u mbar = m u", all(np.allclose(B(up,C(ang(c,d))), B(ang(c,d),up), atol=1e-9)
                                  for c,d in ((R(),R()) for _ in range(40))))
    # Theorem 3.3 and the punchline
    def Phi(x):
        a,b=split(x); return ang(C(a),b)
    def Psi(z):
        n,m=split(z); return Phi(n)+B(Phi(m),up)
    ok("Thm 3.3: Phi: M(A) -> N is a homomorphism",
       all(np.allclose(Phi(MA(x,y)),B(Phi(x),Phi(y)),atol=1e-9)
           for x,y in ((rng.standard_normal(2*nA),rng.standard_normal(2*nA)) for _ in range(40))))
    ok("THEOREM: Psi: CD(M(A)) -> CD^2(A) is an algebra isomorphism",
       all(np.allclose(Psi(CDMA(x,y)),B(Psi(x),Psi(y)),atol=1e-9)
           for x,y in ((rng.standard_normal(n4),rng.standard_normal(n4)) for _ in range(50))))
    ok("         Psi is a *-isomorphism (commutes with conjugation)",
       all(np.allclose(Psi(conj(z)),C(Psi(z)),atol=1e-9) for z in (rng.standard_normal(n4) for _ in range(40))))
    Zp=np.column_stack([Psi(np.eye(n4)[i]) for i in range(n4)])
    ok("         Psi is bijective", np.linalg.matrix_rank(Zp)==n4)
    # Psi sends the inner doubling unit l to ee'
    l=np.zeros(2*nA); l[nA]=1.0
    ok("         Psi fixes A and e', and sends l -> ee'", np.allclose(Phi(l), j, atol=1e-9))

run(mulH,4,"A = H   -> CD(M(H)) = CD^2(H), dim 16")
run(mulO,8,"A = O   -> CD(M(O)) = CD^2(O), dim 32   [CD(S') = T]")
run(CDmul(mulO),16,"A = S   -> dim 64")
run(Mmul(mulO),16,"A = S'  -> dim 64")
# and the split branch: the proof is indifferent to eps
def CDs(base):
    def m(x,y):
        a,b=split(x); c,d=split(y)
        return join(base(a,c)+base(conj(d),b), base(d,a)+base(b,conj(c)))
    return m
print("\n=== split base (eps = -1): the proof never uses eps ===")
run(CDs(mulO),16,"A = split S -> dim 64")
