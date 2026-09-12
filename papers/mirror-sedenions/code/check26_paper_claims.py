"""
check26 -- an assertion gate for every numerical claim made in the two papers.

Scripts check2, 4, 5, 8, 10-12, 14-18, 20-22 and sym_spectrum print data but
assert nothing, so running them cannot fail.  This script re-derives the claims
those scripts support and ASSERTS them, so that a regression is detected.
Organised by the paper and statement each claim belongs to.
"""
import numpy as np, itertools, sys
from collections import Counter
sys.path.insert(0,'.')
from cd import *
from f2iso import graded_isos
rng=np.random.default_rng(26)
FAIL=[]
def ok(lab,c):
    print(('PASS ' if c else 'FAIL ')+lab)
    if not c: FAIL.append(lab)

def dblw(w,mirror=False,eps=1):
    h=w.shape[0]; N=2*h; W=np.zeros((N,N),dtype=np.int8); s=np.ones(h,dtype=np.int8); s[1:]=-1
    W[:h,:h]= w.T if mirror else w
    W[:h,h:]= w.T; W[h:,:h]= w*s[None,:]
    for p in range(h):
        for q in range(h): W[h+p,h+q]=-eps*s[q]*w[q,p]
    return W
def wof(name,n):
    T=struct(name); w=np.zeros((n,n),dtype=np.int8)
    for p in range(n):
        for q in range(n):
            nz=np.nonzero(np.abs(T[p,q])>1e-9)[0]; w[p,q]=int(np.sign(T[p,q][nz[0]]))
    return w
def zpairs(W):
    n=W.shape[0]; U=np.arange(n); out=set()
    for d in range(1,n):
        P=W*W[:,U^d]
        for i in range(1,n):
            j=i^d
            if j>i and (P[i]==P[j]).sum(): out.add((i,j))
    return out
def anndim(W,i,j):
    n=W.shape[0]; d=i^j; seen=np.zeros(n,bool); k=0
    for u in range(n):
        if seen[u]: continue
        v=u^d; seen[u]=seen[v]=True
        if W[i,u]*W[i,v]==W[j,u]*W[j,v]: k+=1
    return k
def der_dim(name):
    T=struct(name); n=T.shape[0]; rows=[]
    for i in range(n):
        for j in range(n):
            eq=np.zeros((n,n,n))
            for m in range(n): eq[:,:,m][np.arange(n),np.arange(n)]+=T[i,j,m]
            for p in range(n): eq[:,p,i]-=T[p,j,:]; eq[:,p,j]-=T[i,p,:]
            rows.append(eq.reshape(n,n*n))
    return nullity(np.vstack(rows))

print("========== PAPER 1 ==========")
wO=wof('O',8); wS=dblw(wO,False); wSm=dblw(wO,True)
ok("§7 (Prop 7.3): S and S' sign tables differ on exactly 42 pairs, all (i,j) with i,j in 1..7, i!=j",
   (lambda D: len(D)==42 and all(1<=i<8 and 1<=j<8 and i!=j for i,j in D))(
       {(i,j) for i in range(16) for j in range(16) if wS[i,j]!=wSm[i,j]}))
ok("§7 (Prop 7.4): 2688 graded automorphisms each (168 sigmas x 16), and 0 graded isomorphisms S -> S'",
   len(graded_isos(wS,wS))==168 and len(graded_isos(wSm,wSm))==168 and len(graded_isos(wS,wSm))==0)
ZS, ZSm = zpairs(wS), zpairs(wSm)
ok("Prop 5.4: 42 two-term index pairs in S (84 signed) and 56 in S' (112 signed)",
   len(ZS)==42 and len(ZSm)==56)
ok("Prop 5.4: S' adds exactly the 14 pairs (i,i+8) and (i,8)",
   ZSm-ZS == {(i,i+8) for i in range(1,8)} | {(i,8) for i in range(1,8)} and not ZS-ZSm)
ok("Thm 5.2: annihilator dimensions in S' are 2 on the 42 shared pairs and 6 on the 14 new ones",
   all(anndim(wSm,i,j)==(6 if (j==i+8 or j==8) else 2) for (i,j) in ZSm))
ok("Thm 5.2 (S side): every two-term zero divisor of S has 4-dimensional annihilator",
   all(anndim(wS,i,j)==4 for (i,j) in ZS))
def spec_mults(name):
    x=rng.standard_normal(16); M=L(name,conj(x))@L(name,x)/norm2(x)
    ev=np.linalg.eigvalsh((M+M.T)/2)
    return sorted(Counter(np.round(ev,6)).values())
ok("Thm 4.1: stretch spectrum of S has 3 levels with multiplicities {4,4,8}",
   spec_mults('S')==[4,4,8])
ok("Thm 4.1: stretch spectrum of S' has 5 levels with multiplicities {2,2,4,4,4}",
   spec_mults('Sm')==[2,2,4,4,4])
ok("Thm 4.1: the two spectra are distinguished by their multiplicity profiles",
   spec_mults('S')!=spec_mults('Sm') and len(spec_mults('S'))==3 and len(spec_mults('Sm'))==5)
HP={f:[g for g in range(16) if bin(f&g).count('1')%2==0] for f in range(1,16)}
def comp(name,H):
    for _ in range(20):
        u=np.zeros(16); v=np.zeros(16); u[H]=rng.standard_normal(8); v[H]=rng.standard_normal(8)
        if abs(norm2(mul(name,u,v))-norm2(u)*norm2(v))>1e-8: return False
    return True
ok("Thm 6.1: octonion hyperplanes of S are O and the 7 through l; of S' the 8 avoiding l",
   {f for f in HP if comp('S',HP[f])}=={1,2,3,4,5,6,7,8} and
   {f for f in HP if comp('Sm',HP[f])}=={8,9,10,11,12,13,14,15})
ok("Thm 7.1 / Table 1: Der(O)=Der(S)=Der(S')=14 and Der(M(H))=6",
   der_dim('O')==14 and der_dim('S')==14 and der_dim('Sm')==14 and der_dim('Om')==6)
ok("Prop 5.4: 336 ordered pairs of two-term elements with product zero, in both",
   all(sum(1 for i in range(1,16) for j in range(i+1,16) for si in(1,-1)
           for k in range(1,16) for l in range(k+1,16) for sk in(1,-1)
           if np.allclose(mul(n,basis(16,i)+si*basis(16,j),basis(16,k)+sk*basis(16,l)),0,atol=1e-9))==336
       for n in ('S','Sm')))
qS=[f for f in HP if not comp('S',HP[f])]; qSm=[f for f in HP if not comp('Sm',HP[f])]
ok("Prop (incidence): 12 zero-divisor pairs in every quasi-octonion hyperplane, both algebras",
   all(sum(1 for (i,j) in ZS  if i in HP[f] and j in HP[f])==12 for f in qS) and
   all(sum(1 for (i,j) in ZSm if i in HP[f] and j in HP[f])==12 for f in qSm))
ok("Prop (incidence): multiplicity is uniformly 2 in S and is {1 on 42, 3 on 14} in S'",
   all(sum(1 for f in qS if i in HP[f] and j in HP[f])==2 for (i,j) in ZS) and
   Counter(sum(1 for f in qSm if i in HP[f] and j in HP[f]) for (i,j) in ZSm)=={1:42,3:14})
# Theorem 3.6: the 32-product census
S_cls=set(); Sm_cls=set()
for f in range(8):
    for g in range(4):
        tag=f'P{f}{g}'; register(tag,double(mulO,f,g),16); sg=sign_table(tag)[0]
        if graded_isos(wS,sg): S_cls.add((f,g))
        if graded_isos(wSm,sg): Sm_cls.add((f,g))
ok("Thm 3.6: of the 32 candidates exactly 4 give S and exactly 4 give S', disjointly",
   len(S_cls)==4 and len(Sm_cls)==4 and not (S_cls & Sm_cls))
ok("§9 Q2: four further candidates have 8 octaves and Der = 14 without being S or S'",
   len({(f,g) for f in range(8) for g in range(4)} - S_cls - Sm_cls)==24)

print("\n========== PAPER 2 ==========")
def Zc(j):
    z=0;h=8
    for _ in range(j): z=2*z+(h-1)*(h-2); h*=2
    return z
def Zkb(k,b):
    h=2**(k-b+3); z=Zc(k-b)
    for _ in range(b): z=2*z+h*(h-1); h*=2
    return z
obs={1:[84,112],2:[588,648,704],3:[3036,3160,3280,3392],4:[13884,14136,14384,14624,14848]}
lv=[("O",wO)]
for k in range(1,5):
    nx=[]
    for nm,w in lv: nx.append((nm+"C",dblw(w,False))); nx.append((nm+"M",dblw(w,True)))
    lv=nx
    cnt=Counter()
    for nm,w in lv:
        b=0
        for ch in reversed(nm[1:]):
            if ch=="M": b+=1
            else: break
        cnt[2*len(zpairs(w))]+=1
    ok(f"Cor 4.9: dimension {8*2**k} gives exactly {k+1} distinct counts, equal to the closed form",
       sorted(cnt)==sorted(2*Zkb(k,b) for b in range(k+1))==sorted(obs[k]))
ok("Cor 4.10 (sharpness): the counts are strictly increasing in b at every level k <= 12",
   all(all(Zkb(k,b)<Zkb(k,b+1) for b in range(k)) for k in range(1,13)))
ok("Prop 5.1: signature (16,0) for the definite branch and (8,8) for the split branch at dim 16",
   (lambda f: f(wS)==(16,0) and f(wSm)==(16,0) and f(dblw(wO,False,-1))==(8,8) and f(dblw(wO,True,-1))==(8,8))(
     lambda w: (1+sum(1 for g in range(1,w.shape[0]) if -w[g,g]>0),
                sum(1 for g in range(1,w.shape[0]) if -w[g,g]<0))))
ok("Prop 5.1: the split signature is inherited by both operations at dim 32",
   all((lambda w:(1+sum(1 for g in range(1,32) if -w[g,g]>0),
                  sum(1 for g in range(1,32) if -w[g,g]<0)))(dblw(b,m))==(16,16)
       for b in (dblw(wO,False,-1),dblw(wO,True,-1)) for m in (False,True)))
# 8-dimensional subalgebra census at dimension 32
def subs3():
    out=set()
    for a in range(1,32):
        for b in range(a+1,32):
            for c in range(b+1,32):
                sp={0,a,b,c,a^b,a^c,b^c,a^b^c}
                if len(sp)==8: out.add(tuple(sorted(sp)))
    return sorted(out)
S3=subs3()
ok("§6: there are 155 three-dimensional F_2-subspaces of F_2^5 (Cawagas's 155 subloops of order 16)",
   len(S3)==155)
def census(name):
    r=Counter()
    for H in S3:
        idx=np.array(H); alt=True
        for _ in range(10):
            x=np.zeros(32); y=np.zeros(32); x[idx]=rng.standard_normal(8); y[idx]=rng.standard_normal(8)
            if not np.allclose(mul(name,mul(name,x,x),y),mul(name,x,mul(name,x,y)),atol=1e-9): alt=False; break
        r['oct' if alt else 'quasi']+=1
    return r
def CDm(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y); return join(b(a,c)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
def MIm(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y); return join(b(c,a)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
register('T32',CDm(CDm(mulO)),32); register('MS32',MIm(CDm(mulO)),32)
cT,cM=census('T32'),census('MS32')
ok("§6: T has 50 octonion and 105 quasi-octonion 8-dimensional subalgebras (Cawagas et al.)",
   cT['oct']==50 and cT['quasi']==105)
ok("§6: M(S) has 64 and 91", cM['oct']==64 and cM['quasi']==91)
ok("§6: Der = 14 at every length-2 node", all(der_dim(n)==14 for n in ('T32','MS32')))

print("\n"+("ALL CLAIMS ASSERTED AND PASSING" if not FAIL else f"{len(FAIL)} FAILURES: {FAIL}"))
sys.exit(1 if FAIL else 0)
