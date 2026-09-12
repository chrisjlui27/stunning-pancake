"""
check14 -- the dimension-32 analogue of Theorem 6.1 / claim (A).

For each length-2 word in {CD, M} applied to O, classify the 31 basis hyperplanes
(each 16-dimensional) as S, S', or neither, by graded isomorphism.

Result (2026-09-12):

    T = CD(CD(O))        S: 16   S': 1    other: 14
    M(S) = M(CD(O))      S: 16   S': 8    other:  7
    CD(S') = CD(M(O))    S: 16   S': 1    other: 14
    M(S') = M(M(O))      S:  0   S': 24   other:  7

The first line independently reproduces claim (A) and Cawagas et al.: inside T,
S occupies 16 basis hyperplanes and S' = S_gamma exactly one.  The last line is
its mirror image: M(S') contains no copy of S at all and 24 copies of S'.
"""
import numpy as np, sys
from cd import *
from f2iso import graded_isos
rng=np.random.default_rng(31)
def CD(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y)
        return join(b(a,c)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
def MIR(b,eps=1):
    def m(x,y):
        a,bb=split(x); c,d=split(y)
        return join(b(c,a)-eps*b(conj(d),bb), b(d,a)+b(bb,conj(c)))
    return m
W={'T = CD(CD(O))':CD(CD(mulO)), 'M(S) = M(CD(O))':MIR(CD(mulO)),
   'CD(S′) = CD(M(O))':CD(MIR(mulO)), 'M(S′) = M(M(O))':MIR(MIR(mulO))}
for k,m in W.items(): register(k,m,32)
sS=sign_table('S')[0]; sM=sign_table('Sm')[0]
def sub_sign(name,H):
    """sign table of the 16-dim subalgebra on index set H, reindexed 0..15 by F_2^4 structure"""
    T=struct(name); n=len(H); pos={g:i for i,g in enumerate(H)}
    sg=np.zeros((16,16),dtype=int)
    for i,g in enumerate(H):
        for j,h in enumerate(H):
            v=T[g,h]; nz=np.nonzero(np.abs(v)>1e-12)[0]
            if len(nz)!=1 or nz[0] not in pos: return None
            sg[i,j]=int(np.sign(v[nz[0]]))
    return sg
for name in W:
    types={'S':0,"S'":0,'other':0}; others=[]
    for f in range(1,32):
        H=[g for g in range(32) if bin(f&g).count('1')%2==0]
        sg=sub_sign(name,H)
        if sg is None: types['other']+=1; continue
        if   graded_isos(sS,sg): types['S']+=1
        elif graded_isos(sM,sg): types["S'"]+=1
        else: types['other']+=1; others.append(f)
    print(f"{name:20s} 31 hyperplanes -> S:{types['S']:3d}  S′:{types[chr(83)+chr(39)]:3d}  other:{types['other']:3d}   (other f: {others[:8]})")
    sys.stdout.flush()
