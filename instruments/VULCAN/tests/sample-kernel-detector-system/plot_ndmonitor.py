#!/usr/bin/env python

# Note: Before using this script make sure that "out/ixyt.h5" is generated!

from histogram.hdf import load
from histogram.plotter import defaultPlotter as dp

h   = load('out/ixyt.h5', 'ix_y_t')
ixy = h.sum('t')

dp.plot(ixy)
