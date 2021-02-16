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
    nh = _int(core.nh)
    Iarr = bpptr2npyarr( core.getDiv_p( ), 'double', nh ).copy()
    E2arr = bpptr2npyarr( core.getDiv_p2( ), 'double', nh ).copy()
    from histogram import histogram, axis, arange
    h_maxdiv = core.h_maxdiv
    dx = 2*h_maxdiv/nh
    xaxis = axis( 'hdiv', arange( -h_maxdiv+dx/2, h_maxdiv, dx ), unit = 'degree' )
    h = histogram( 'I(div)', [xaxis], data = Iarr, errors = E2arr )
    return h

def _int(f):
    i = int(round(f))
    if abs(i-f)>1e-3:
        raise ValueError("%s is not close to an integer" % f)
    return i

# End of file
