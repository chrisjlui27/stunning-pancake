"""
check25 -- the 64-dimensional landscape L_5 = hyperplanes of A_7, by the generation theorem:
L_5 = {A_6} u {R_{A_6}(K) : K a hyperplane of A_6}.  The 63 relative mirrors are grouped by a
cheap fingerprint (non-associative ordered triples, two-term zero divisors, annihilator profile)
and then same-fingerprint pairs are tested for graded isomorphism by the associator search.
"""
import pickle, sys, time
import numpy as np
from collections import Counter, defaultdict
from landscape import *
reg = pickle.load(open('landscape_registry_n6.pkl', 'rb')); classes = reg['classes']
byk = {k: {c['label']: c['w'] for c in lst} for k, lst in classes.items()}
def classify(w):
    k = w.shape[0].bit_length() - 1; A = assoc_pattern(w)
    for lab, rep in byk[k].items():
        if iso_search(assoc_pattern(rep), A) is not None: return lab
    return '?'
def hyperplane_basis(N, f):
    H = [g for g in range(N) if bin(f & g).count('1') % 2 == 0]
    basis = []; sp = {0}
    for g in H:
        if g not in sp: basis.append(g); sp |= {s ^ g for s in sp}
    return tuple(basis)
def relative_mirror(w, f):
    N = w.shape[0]; W = dbl(w); top = N
    c = next(g for g in range(1, N) if bin(f & g).count('1') % 2 == 1)
    return restrict(W, tuple(list(hyperplane_basis(N, f)) + [c ^ top]))
def fp(w):
    A = assoc_pattern(w); c, dims = zd(w)
    return (int((A[1:, 1:, 1:] < 0).sum()), c, tuple(dims.items()))

w6 = cd_tower(6); N = 64
print('fingerprint of A_6 itself:', fp(w6))
groups = defaultdict(list); t0 = time.time()
for f in range(1, N):
    K = classify(restrict(w6, hyperplane_basis(N, f)))
    # finer: which hyperplane of T does K double / mirror (orbit label)
    R = relative_mirror(w6, f)
    groups[fp(R)].append((f, K))
    if f % 8 == 0: print(f'  {f}/63  {time.time()-t0:.0f}s'); sys.stdout.flush()
print(f'\n{len(groups)} distinct fingerprints among the 63 relative mirrors R_A6(K):')
for key, mem in sorted(groups.items(), key=lambda kv: (Counter(k for _, k in kv[1]).most_common(1)[0][0], kv[0])):
    print(f'  nonassoc={key[0]:6d}  ZD={key[1]:5d}  ann={dict(key[2])}   x{len(mem):2d}   K classes: {dict(Counter(k for _, k in mem))}   f: {[f for f,_ in mem][:8]}')
sys.stdout.flush()
# isomorphism within fingerprint groups: test each member against the first member of its group
print('\ngraded-isomorphism check within fingerprint groups (associator search at k=6):')
tot_classes = 0
for key, mem in groups.items():
    reps = []
    for f, K in mem:
        R = relative_mirror(w6, f); A = assoc_pattern(R); placed = False
        for i, (rf, rA) in enumerate(reps):
            t1 = time.time(); s = iso_search(rA, A)
            if s is not None: placed = True; break
        if not placed: reps.append((f, A))
    tot_classes += len(reps)
    print(f'  fingerprint {key[:2]} x{len(mem)}: {len(reps)} class(es)  reps f={[r[0] for r in reps]}   [{time.time()-t0:.0f}s]'); sys.stdout.flush()
print(f'\n|L_5| = 1 (A_6) + {tot_classes} = {1 + tot_classes}')
