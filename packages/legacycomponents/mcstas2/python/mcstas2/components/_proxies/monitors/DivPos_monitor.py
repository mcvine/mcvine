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

    npos = _int(core.npos); ndiv =_int(core.ndiv)
    n = npos * ndiv
    shape = npos, ndiv

    xmin = core.xmin; xmax = core.xmax
    maxdiv = core.maxdiv

    dx = (xmax - xmin)/npos
    ddiv = 2*maxdiv/ndiv

    Iarr = bpptr2npyarr( core.getDiv_p_00( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getDiv_p2_00( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    posaxis = axis( 'pos', arange( xmin+dx/2., xmax, dx ) )
    divaxis = axis( 'div', arange( -maxdiv+ddiv/2., maxdiv, ddiv ) )

    h = histogram( 'I(x,y)', [posaxis,divaxis], data = Iarr, errors = E2arr )
    return h


def _int(f):
    i = int(round(f))
    if abs(i-f)>1e-3:
        raise ValueError("%s is not close to an integer" % f)
    return i


# End of file 
