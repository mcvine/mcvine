#!/usr/bin/env python

import histogram.hdf as hh, os, sys, numpy as np

if len(sys.argv) == 2:
  sim = sys.argv[1]
else:
  sim = '.'

simiqe = hh.load(os.path.join(sim, 'iqe.h5'))

simiq = simiqe[(2,8), (7,39)].sum('energy')

import pylab
Q = simiq.Q
expected = Q*Q*np.exp(-0.012*Q*Q)
pylab.plot(Q, simiq.I/expected, 'b')
# pylab.plot(Q, simiq.I, 'b')
# pylab.plot(Q, 3e-13*expected, 'r')
pylab.show()

