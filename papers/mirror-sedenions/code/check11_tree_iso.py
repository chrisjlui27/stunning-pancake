import numpy as np
from cd import *
from f2iso import graded_isos
register('CDOm', double(mulOm, 7, 3), 16)
register('MOm', double(mulOm, 5, 3), 16)
def sf(name):
    s, idx = sign_table(name); return s
for name in ['CDOm', 'MOm']:
    print(name, 'graded-iso to S:', len(graded_isos(sf('S'), sf(name))) > 0, '; to Sm:', len(graded_isos(sf('Sm'), sf(name))) > 0)
