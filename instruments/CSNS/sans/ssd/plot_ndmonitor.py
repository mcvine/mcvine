#!/usr/bin/env python

# Note: Before using this script make sure that "out/ixyt.h5" is generated!
from histogram.hdf import load
from histogram.plotter import defaultPlotter as dp
import sys
f = sys.argv[1]
# h   = load('out/monitor_0.h5', 'ix_y_t')
# h   = load('out/monitor_1.h5', 'ix_y_t')
# h   = load('out/detector.h5', 'ix_y_t')
# h   = load('out/rank0-step0/detector.h5', 'ix_y_t')
h   = load(f, 'ix_y_t')
ixy = h.sum('t')
iyt = h.sum('x')
it =iyt.sum('y')

dp.plot(ixy)
