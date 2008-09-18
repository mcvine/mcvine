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



def _get_histogram( self ):
    from mcstas2.utils.carray import bpptr2npyarr
    core = self.core()
    
    nx = core.nx; ny =core.ny
    n = nx * ny
    shape = nx, ny

    xmin = core.xmin; xmax = core.xmax
    ymin = core.ymin; ymax = core.ymax
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


methods = [ '_get_histogram',
            ]

# version
__id__ = "$Id$"

# End of file 
