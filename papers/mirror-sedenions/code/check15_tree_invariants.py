"""The {CD, M} word tree above O, with split variants. Invariant profile per node."""
import numpy as np, itertools, sys
from cd import *
rng = np.random.default_rng(7)

def CD(base, eps=1):
    def m(x,y):
        a,b=split(x); c,d=split(y)
        return join(base(a,c)-eps*base(conj(d),b), base(d,a)+base(b,conj(c)))
    return m
def MIR(base, eps=1):
    def m(x,y):
        a,b=split(x); c,d=split(y)
        return join(base(c,a)-eps*base(conj(d),b), base(d,a)+base(b,conj(c)))
    return m

def der_dim(name):
    T=struct(name); n=T.shape[0]; rows=[]
    for i in range(n):
        for j in range(n):
            eq=np.zeros((n,n,n))
            for mm in range(n): eq[:,:,mm][np.arange(n),np.arange(n)]+=T[i,j,mm]
            for p in range(n):
                eq[:,p,i]-=T[p,j,:]; eq[:,p,j]-=T[i,p,:]
            rows.append(eq.reshape(n,n*n))
    return nullity(np.vstack(rows))

def two_term(name,n):
    return sum(1 for i in range(1,n) for j in range(i+1,n) for s in (1,-1)
               if nullity(L(name,basis(n,i)+s*basis(n,j)))>0)

def hyper_census(name,n):
    """basis hyperplanes: (closed, composition) counts"""
    nb=n.bit_length()-1
    comp=0; tot=0
    for f in range(1,n):
        H=[g for g in range(n) if bin(f&g).count('1')%2==0]
        idx=np.array(H); ok=True
        for _ in range(8):
            x=np.zeros(n); y=np.zeros(n); x[idx]=rng.standard_normal(len(H)); y[idx]=rng.standard_normal(len(H))
            z=mul(name,x,y)
            if abs(norm2(z)-norm2(x)*norm2(y))>1e-8: ok=False; break
        tot+=1; comp+= ok
    return comp, tot

def props(name,n):
    out={}
    X=[rng.standard_normal(n) for _ in range(12)]
    out['flex']=all(np.allclose(mul(name,mul(name,x,y),x),mul(name,x,mul(name,y,x)),atol=1e-9)
                    for x in X[:6] for y in X[6:])
    out['posdef']=min(mul(name,x,conj(x))[0] for x in X)>0
    out['alt']=all(np.allclose(mul(name,mul(name,x,x),y),mul(name,x,mul(name,x,y)),atol=1e-9)
                   for x in X[:6] for y in X[6:])
    # annihilator dim on the S'-type locus (a imaginary, |a|=|b|) and the S-type locus (a,b imaginary orthogonal)
    h=n//2; dims_m=set(); dims_s=set()
    for _ in range(8):
        u=rng.standard_normal(h); u[0]=0; u=unit(u)
        b=unit(rng.standard_normal(h))
        dims_m.add(nullity(L(name,join(u,b))))
        v=rng.standard_normal(h); v[0]=0; v=v-(v@u)*u; v=unit(v)
        dims_s.add(nullity(L(name,join(u,v))))
    out['ann_Sm_locus']=sorted(dims_m); out['ann_S_locus']=sorted(dims_s)
    return out

# ---- build the tree ----
register('O8', mulO, 8)
NODES=[('O',mulO,8)]
LEVELS={8:[('O',mulO)]}
for target in (16,32):
    prev=LEVELS[target//2]; cur=[]
    for wname,base in prev:
        cur.append((f'CD({wname})', CD(base)))
        cur.append((f'M({wname})',  MIR(base)))
    LEVELS[target]=cur
# split variants applied once at the last step from O
LEVELS[16]+= [('CD-(O)',CD(mulO,-1)), ('M-(O)',MIR(mulO,-1))]

for dim in (16,32):
    print("="*78); print(f"DIMENSION {dim}"); print("="*78)
    for wname,m in LEVELS[dim]:
        register(wname,m,dim)
        p=props(wname,dim); c,t=hyper_census(wname,dim)
        tt=two_term(wname,dim)
        d = der_dim(wname) if dim<=32 else None
        print(f"  {wname:14s} Der={d:3d}  comp-hyperplanes={c:2d}/{t}  2-term ZD={tt:4d}  "
              f"flex={str(p['flex'])[:5]:5s} posdef={str(p['posdef'])[:5]:5s} alt={str(p['alt'])[:5]:5s} "
              f"annS={p['ann_S_locus']} annS′={p['ann_Sm_locus']}")
        sys.stdout.flush()
