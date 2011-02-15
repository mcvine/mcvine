#!/usr/bin/env python

# Sample script

from histogram.hdf import load
from histogram.plotter import defaultPlotter as dp

h   = load('out/ixyt.h5', 'ix_y_t')
ixy = h.sum('t')

dp.plot(ixy)
