"""
check22 -- invariants of every basis-subalgebra class found by check21, the absorption
test (which hyperplanes of A_n are isomorphic to A_{n-1}), and Wilmot's P12 / P14 triads.
"""
import pickle, sys, time
import numpy as np
from collections import Counter
from landscape import *
reg = pickle.load(open('landscape_registry_n6.pkl', 'rb')); classes = reg['classes']; census = reg['census']
byk = {k: {c['label']: c['w'] for c in lst} for k, lst in classes.items()}
def classify(w, k):
    A = assoc_pattern(w)
    for lab, rep in byk[k].items():
        if iso_search(assoc_pattern(rep), A) is not None: return lab
    return '?'

print('=== census (standard tower) ===')
for (n, k), cnt in sorted(census.items()):
    print(f'  A_{n} (dim {2**n:3d}), subalgebras of dim {2**k:3d}: {dict(sorted(cnt.items()))}')

print('\n=== class invariants ===')
print(f"{'class':8s} {'dim':>4s} {'nonassoc':>9s} {'triads':>7s} {'2-term ZD':>9s} {'ann dims':>22s} {'Der':>4s} {'|sigma|':>8s} {'alt':>4s} {'comp':>5s}  codim-1 census")
for k in (3, 4, 5):
    for lab, w in byk[k].items():
        A = assoc_pattern(w); nona = int((A[1:, 1:, 1:] < 0).sum())
        tri = nonassoc_triads(w)[0] if k <= 4 else -1
        c, dims = zd(w)
        hp = dict(sorted(hyperplane_types(w, lambda s: classify(s, k - 1)).items()))
        t0 = time.time(); dd = der_dim(w) if k <= 5 else -1
        sc = sigma_count(w) if k <= 4 else -1
        print(f'{lab:8s} {2**k:4d} {nona:9d} {tri:7d} {c:9d} {str(dims):>22s} {dd:4d} {sc:8d} {str(is_alternative(w))[0]:>4s} {str(is_composition(w))[0]:>5s}  {hp}')
        sys.stdout.flush()

print('\n=== absorption: hyperplanes of A_n isomorphic to A_{n-1} ===')
for n in (5, 6):
    w = cd_tower(n); N = 2 ** n; top = N // 2
    res = Counter(); where = {}
    for f in range(1, N):
        H = [g for g in range(N) if bin(f & g).count('1') % 2 == 0]
        basis = []; sp = {0}
        for g in H:
            if g not in sp: basis.append(g); sp |= {s ^ g for s in sp}
        lab = classify(restrict(w, tuple(basis)), n - 1)
        through = (f & top) == 0        # hyperplane contains the top unit e_top  iff f(top)=0
        res[(lab, 'through top' if through else 'avoiding top')] += 1
    for key, v in sorted(res.items()): print(f'  A_{n}: {key[0]:7s} {key[1]:13s} {v}')

print("\n=== Wilmot's generating triads (graded notation o_i = e_{2^(i-1)}) ===")
wT = cd_tower(5); w6 = cd_tower(6)
def tri(w, gens, k):
    return classify(restrict(w, tuple(gens)), k)
print('  (o1,o2,o3)   = (e1,e2,e4)    in A_5 :', tri(wT, (1, 2, 4), 3), '   -- octonions')
print('  (o1,o24,o34) = (e1,e10,e12)  in A_5 :', tri(wT, (1, 10, 12), 3), '  -- Wilmot: P4')
print('  (o1,o24,o345)= (e1,e10,e28)  in A_5 :', tri(wT, (1, 10, 28), 3), '  -- Wilmot: P12')
print('  (o14,o25,o36)= (e9,e18,e36)  in A_6 :', tri(w6, (9, 18, 36), 3), '  -- Wilmot: P14')
# explicit isomorphism witnesses
for gens, w, nm in [((1, 10, 28), wT, 'P12'), ((9, 18, 36), w6, 'P14')]:
    sub = restrict(w, gens); sg = iso_search(assoc_pattern(byk[3]['P4']), assoc_pattern(sub))
    print(f'  sigma carrying P4 = M(H) onto the {nm} triad subalgebra (images of the 3 basis bits): {sg}')
# ordering-dependent counts that distinguish Wilmot's representations
def ordered_profile(w):
    A = assoc_pattern(w); N = w.shape[0]; prof = Counter()
    for p in range(1, N):
        for q in range(p + 1, N):
            for r in range(q + 1, N):
                if r == p ^ q: continue
                prof[tuple(int(A[a, b, c]) for a, b, c in [(p,q,r),(p,r,q),(q,p,r),(q,r,p),(r,p,q),(r,q,p)])] += 1
    return dict(prof)
for gens, w, nm in [((1, 10, 12), cd_tower(4), 'P4 in S'), ((1, 10, 28), wT, 'P12 triad in T'), ((9, 18, 36), w6, 'P14 triad in A6')]:
    print(f'  {nm:16s} associator signs over the 6 orderings of each triad, in the given basis:', ordered_profile(restrict(w, gens)))
