#!/usr/bin/env python

import os, numpy as np
from mcni.utils import conversion
from mcni.neutron_storage import readneutrons_asnpyarr

import sys
if len(sys.argv) == 1:
    nsfile = './n1e+06/scattered.mcv'
elif len(sys.argv) == 2:
    nsfile = sys.argv[1]
else:
    print("analysis.py neutron-storage.mcv")
    sys.exit(1)

neutrons = readneutrons_asnpyarr(nsfile)
v = neutrons[:, 3:6]
p = neutrons[:, -1]
k_vec = conversion.v2k(v)
k = np.linalg.norm(k_vec, axis=1)

a = 4.04932
ra = 2*np.pi/a
ki = ra * 4
ki_vec = [0., 0., ki]
Q = ki_vec - k_vec

assert(np.allclose(k, ki, rtol=0.05))
N = k.size

hkls =  np.round(Q/ra).astype(int)

unique_hkls = np.unique(hkls, axis=0)
for hkl in unique_hkls:
    mask = np.all(hkls == hkl, axis=1)
    N1 = mask.sum()
    if N1 < N/800.: continue
    p1 = p[mask].sum()/N
    print(hkl, p1, mask.sum())
