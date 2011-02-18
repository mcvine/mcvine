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

class ComponentInterface(base):

    def _get_histogram(self):
        return get_histogram(self)
    

def attr(obj, name, repl):
    """
    PSD_monitor.py script is used both by VNF and McVine. Due to issue with the
    Postgres database considering 'xmin', 'xmax', 'ymin' and 'ymax' column names 
    as special fields VNF uses replacement e.g. 'xmin' -> 'x_min' whereas McVine
    still uses 'xmin'
    """
    if hasattr(obj, repl):  # If object has replacement attribute, use it
        return getattr(obj, repl)

    # Otherwise use standard name
    return getattr(obj, name)


def get_histogram( monitor ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = monitor.core()

    nx = core.nx; ny =core.ny
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


# version
__id__ = "$Id$"

# End of file 
