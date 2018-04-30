#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from base import Component as base

class Component(base):
    
    def _get_histogram( self ):
        return get_histogram(self._cpp_instance)


def get_histogram(monitor):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()
    n = core.nchan
    Iarr = bpptr2npyarr( core.getL_p( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getL_p2( ), 'double', n ).copy()
    from histogram import histogram, axis, arange
    dL = (core.Lmax-core.Lmin)/core.nchan 
    Laxis = axis( 'wavelength', arange( core.Lmin+dL/2, core.Lmax+dL/2, dL ), unit = 'angstrom' )
    h = histogram( 'I(L)', [Laxis], data = Iarr, errors = E2arr )
    return h


# End of file 
