import numpy as np
from cd import *
from check5_census import der_dim_fast, hyperplane_octaves
rng = np.random.default_rng(10)
register('CDOm', double(mulOm, 7, 3), 16)   # standard double of the quasi-octonions
register('MOm', double(mulOm, 5, 3), 16)    # mirror double of the quasi-octonions
for name in ['S', 'Sm', 'CDOm', 'MOm']:
    mul16 = ALG[name][0]
    octs = [f for f, cl, co in hyperplane_octaves(mul16) if co]
    dd = der_dim_fast(name)
    # dead dims: generic random elements and the (u,b) loci
    def rand_im8():
        v = rng.standard_normal(8); v[0] = 0; return unit(v)
    ann = set()
    for _ in range(40):
        ann.add(nullity(L(name, np.concatenate([rand_im8(), unit(rand(8, rng))]))))
        ann.add(nullity(L(name, np.concatenate([unit(rand(8, rng)), unit(rand(8, rng))]))))
    # dimension of the unit dead set: sample a dead point and compute tangent dim
    print(f'{name:5s}: octaves {len(octs)} {octs}; Der {dd}; ann dims seen on test loci {sorted(ann)}')
