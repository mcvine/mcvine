#!/usr/bin/env python

import histogram as H
Qaxis = H.axis('Q', H.arange(0,13,0.1), unit='angstrom**-1')
Eaxis = H.axis('energy', H.arange(-50, 50, 1.), unit='meV')
h = H.histogram('SQE', [Qaxis, Eaxis])
h.I = 1.
h.E2 = 0.
import histogram.hdf as hh
hh.dump(h, 'isotropicsqe.h5', '/', mode='c')
