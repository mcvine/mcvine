#!/usr/bin/env python

import histogram.hdf as hh, pylab as pl


p1 = 'coh-powder+phonon/ie.h5'
p2 = 'incoh-el+phonon/ie.h5'

def main():
    ie1 = hh.load(p1)
    ie2 = hh.load(p2)
    pl.plot(ie1.energy, ie1.I/1.495)
    pl.plot(ie2.energy, ie2.I/0.0082)
    pl.show()
    return

main()
