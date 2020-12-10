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

    nv = _int(core.nv); nh =_int(core.nh)
    n = nv * nh
    shape = nh, nv

    h_maxdiv = core.h_maxdiv
    v_maxdiv = core.v_maxdiv

    dhdiv = 2.*h_maxdiv/nh
    dvdiv = 2.*v_maxdiv/nv

    Iarr = bpptr2npyarr( core.getDiv_p_00( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getDiv_p2_00( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    hdivaxis = axis( 'xdiv', arange( -h_maxdiv+dhdiv/2., h_maxdiv, dhdiv ) )
    vdivaxis = axis( 'ydiv', arange( -v_maxdiv+dvdiv/2., v_maxdiv, dvdiv ) )

    h = histogram( 'I(divx,divy)', [hdivaxis,vdivaxis], data = Iarr, errors = E2arr )
    return h


def _int(f):
    i = int(round(f))
    if abs(i-f)>1e-3:
        raise ValueError("%s is not close to an integer" % f)
    return i


# End of file 
