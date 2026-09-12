"""
check21 -- census of ALL basis subalgebras of the standard Cayley-Dickson algebras
A_n = CD^n(R), n = 4..7 (dim 16..128), by graded isomorphism.

A basis subalgebra is the span of a subgroup of F_2^n; there are Gaussian-binomial many
of each dimension.  Each is classified by (a) a cheap fingerprint and (b) a pruned
backtracking search on the associator pattern (landscape.iso_search).  Labels persist in
a registry across levels so the same class has the same name in every A_n.

usage: python3 check21_landscape.py N [KMAX] [KMIN]      (results appended to landscape_registry.pkl)
"""
import sys, time, pickle, os
import numpy as np
from collections import Counter
from landscape import *

REG = 'landscape_registry.pkl'
reg = pickle.load(open(REG, 'rb')) if os.path.exists(REG) else {'classes': {}, 'census': {}}
classes = reg['classes']      # k -> list of dict(label, w, fp, inv)
census  = reg['census']       # (n,k) -> Counter(label)

def fingerprint(w, k):
    A = assoc_pattern(w)
    nonassoc = int((A[1:, 1:, 1:] < 0).sum())
    c, dims = zd(w)
    hp = tuple(sorted(hyperplane_types(w, lambda s: classify(s, k - 1)).items())) if k >= 3 else ()
    return (nonassoc, c, tuple(dims.items()), hp)

def new_label(k, w, fp):
    lst = classes.setdefault(k, [])
    if k == 2: lab = 'H'
    elif k == 3:
        lab = 'O' if is_composition(w) else f'X8.{len(lst)}'
    elif k == 4:
        lab = f'X16.{len(lst)}'
    else:
        lab = f'X{2**k}.{len(lst)}'
    return lab

def classify(w, k):
    """graded-isomorphism class label of the 2^k-dim table w."""
    if k <= 1: return 'C' if k == 1 else 'R'
    fp = fingerprint(w, k)
    for c in classes.get(k, []):
        if c['fp'] == fp and graded_iso(c['w'], w):
            return c['label']
    lab = new_label(k, w, fp)
    classes.setdefault(k, []).append({'label': lab, 'w': w.copy(), 'fp': fp})
    return lab

# seed the standard names so labels are meaningful
def seed():
    named = [(2, cd_tower(2), 'H'), (3, cd_tower(3), 'O'), (3, dbl(cd_tower(2), True), 'P4'),
             (4, cd_tower(4), 'S'), (4, word('M'), "S'"), (5, cd_tower(5), 'T'), (5, word('MC'), 'M(S)'), (5, word('MM'), "M(S')")]
    for k, w, lab in named:
        if not any(c['label'] == lab for c in classes.get(k, [])):
            fp = fingerprint(w, k)
            assert not any(c['fp'] == fp and graded_iso(c['w'], w) for c in classes.get(k, [])), lab
            classes.setdefault(k, []).append({'label': lab, 'w': w.copy(), 'fp': fp})
seed()

n = int(sys.argv[1]); kmax = int(sys.argv[2]) if len(sys.argv) > 2 else n - 1
kmin = int(sys.argv[3]) if len(sys.argv) > 3 else 2
w = cd_tower(n)
print(f'=== A_{n}, dimension {2**n} ===')
for k in range(kmin, kmax + 1):
    t0 = time.time(); cnt = Counter()
    subs = subspaces(n, k)
    for i, B in enumerate(subs):
        cnt[classify(restrict(w, B), k)] += 1
        if (i + 1) % 500 == 0:
            print(f'   k={k}: {i+1}/{len(subs)} done, {time.time()-t0:.0f}s, classes so far {dict(cnt)}'); sys.stdout.flush()
    census[(n, k)] = cnt
    print(f'  dim {2**k:3d} subalgebras ({len(subs):5d} subgroups): {dict(sorted(cnt.items()))}   [{time.time()-t0:.0f}s]')
    sys.stdout.flush()
    pickle.dump({'classes': classes, 'census': census}, open(REG, 'wb'))
