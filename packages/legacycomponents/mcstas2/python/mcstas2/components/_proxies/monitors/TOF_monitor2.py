#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .base import Component as base

class Component(base):

    def _get_histogram(self):
        return get_histogram(self._cpp_instance)
    
    
def get_histogram( monitor ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()
    n = core.nchan
    Iarr = bpptr2npyarr( core.getTOF_p( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getTOF_p2( ), 'double', n ).copy()
    from histogram import histogram, axis, arange
    dt = (core.tmax-core.tmin)/core.nchan
    taxis = axis( 'tof', arange( core.tmin+dt/2., core.tmax+dt/2-0.1*dt, dt ), unit = 's' )
    h = histogram( 'I(tof)', [taxis], data = Iarr, errors = E2arr )
    return h


# version
__id__ = "$Id$"

# End of file 
