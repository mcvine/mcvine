#!/usr/bin/env python

import histogram.hdf as hh, pylab as pl


p1 = 'coh-powder+phonon/iqe.h5'
p2 = 'incoh-el+phonon/iqe.h5'

def main():
    iqe1 = hh.load(p1)
    iqe2 = hh.load(p2)
    sigma_coh, sigma_inc = 1.495, 0.0082
    getel = lambda iqe: iqe[(0.2, None),(-1.2,1.2)].I.sum()
    getinel = lambda iqe: iqe[(2.4, 7.1), (None, -1.2)].I.sum() + iqe[(2.4, 7.1), (1.2, None)].I.sum()
    coh_el = getel(iqe1) / sigma_coh
    coh_inel = getinel(iqe1) / sigma_coh
    incoh_el = getel(iqe2) / sigma_inc
    incoh_inel = getinel(iqe2) / sigma_inc
    print "coherent", coh_el, coh_inel
    print "incoherent", incoh_el, incoh_inel
    # pl.plot(ie1.energy, ie1.I/sigma_coh, 'r')
    # pl.plot(ie2.energy, ie2.I/sigma_inc, 'g')
    # pl.show()
    return

main()
