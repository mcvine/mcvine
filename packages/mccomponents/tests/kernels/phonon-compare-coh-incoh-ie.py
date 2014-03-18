#!/usr/bin/env python

import histogram.hdf as hh, pylab as pl
from math import pi


p1 = 'coh-phonon/iqe.h5'
p2 = 'incoh-phonon/iqe.h5'

def main():
    iqe1 = hh.load(p1)
    iqe2 = hh.load(p2)
    sigma_coh, sigma_inc = 1.495, 0.0082
    getinel = lambda iqe: iqe[(2.5, 7.), ()].sum('Q')
    coh_inel = getinel(iqe1)
    incoh_inel = getinel(iqe2) 
    pl.plot(coh_inel.energy, 0.9*coh_inel.I/sigma_coh, 'r')
    pl.plot(incoh_inel.energy, incoh_inel.I/sigma_inc, 'g')
    pl.show()
    return

main()
