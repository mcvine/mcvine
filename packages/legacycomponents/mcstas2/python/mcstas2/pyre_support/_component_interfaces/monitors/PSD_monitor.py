#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from default import ComponentInterface as base
from default import attr

class ComponentInterface(base):

    def _get_histogram(self):
        return get_histogram(self)
    

def get_histogram( monitor ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()

    nx = _int(core.nx); ny =_int(core.ny)
    n = nx * ny
    shape = nx, ny

#    xmin = core.x_min; xmax = core.x_max
#    ymin = core.y_min; ymax = core.y_max

    xmin = attr(core, "xmin", "x_min");
    xmax = attr(core, "xmax", "x_max");
    ymin = attr(core, "ymin", "y_min");
    ymax = attr(core, "ymax", "y_max");

    dx = (xmax - xmin)/nx
    dy = (ymax - ymin)/ny

    Iarr = bpptr2npyarr( core.getPSD_p_00( ), 'double', n ).copy()
    E2arr = bpptr2npyarr( core.getPSD_p2_00( ), 'double', n ).copy()
    Iarr.shape = E2arr.shape = shape

    from histogram import histogram, axis, arange
    xaxis = axis( 'x', arange( xmin, xmax, dx ) )
    yaxis = axis( 'y', arange( ymin, ymax, dy ) )

    h = histogram( 'I(x,y)', [xaxis,yaxis], data = Iarr, errors = E2arr )
    return h


def _int(f):
    i = int(round(f))
    if abs(i-f)>1e-3:
        raise ValueError("%s is not close to an integer" % f)
    return i


# version
__id__ = "$Id$"

# End of file 
