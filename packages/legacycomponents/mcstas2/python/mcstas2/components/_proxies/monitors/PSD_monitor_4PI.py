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

    nx = core.nx; ny =core.ny
    assert nx == int(nx); nx = int(nx)
    assert ny == int(ny); ny = int(ny)
    n = nx * ny
    shape = nx, ny

    Iarr = bpptr2npyarr( core.getPSD_p_00( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getPSD_p2_00( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    dx = 360./nx
    xaxis = axis( 'x', arange( 0, 360, dx ), unit = 'deg' )

    dy = 180./ny
    yaxis = axis( 'y', arange( -90, 90, dy ), unit = 'deg' )

    h = histogram( 'I(x,y)', [xaxis,yaxis], data = Iarr, errors = E2arr )
    return h


# End of file 
