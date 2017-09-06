#!/usr/bin/env python

import histogram as H
import histogram.hdf as hh

Qaxis = H.axis('Q', H.arange(0,13,0.1), unit='angstrom**-1')
Eaxis = H.axis('energy', H.arange(-50, 50, 1.), unit='meV')
h = H.histogram('SQE', [Qaxis, Eaxis])
h.I = 1.
h.E2 = 0.
hh.dump(h, 'uniform-sqe.h5', '/', mode='c')

Qaxis = H.axis('Q', H.arange(0,13,0.1), unit='angstrom**-1')
Eaxis = H.axis('energy', H.arange(-.1, .10001, .01), unit='meV')
h = H.histogram('SQE', [Qaxis, Eaxis])
h.I = 1.
h.E2 = 0.
hh.dump(h, 'fake-elastic-line.h5', '/', mode='c')


Qaxis = H.axis('Q', H.arange(0,13,0.1), unit='angstrom**-1')
Eaxis = H.axis('energy', H.arange(-.1, .10001, .01), unit='meV')
h = H.histogram('SQE', [Qaxis, Eaxis])
h.I = 100.
h.E2 = 0.
hh.dump(h, 'fake-elastic-line-intense.h5', '/', mode='c')
