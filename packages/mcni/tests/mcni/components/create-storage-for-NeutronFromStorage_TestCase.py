#!/usr/bin/env python

import numpy

arr = numpy.arange(1000.)
arr.shape = -1, 10

from mcni.neutron_storage import neutrons_from_npyarr, storage
neutrons = neutrons_from_npyarr(arr)

s = storage('neutron-storage-for-NeutronFromStorage_TestCase', 'w')
s.write(neutrons)
