#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


category = 'monitors'


from mcni.AbstractComponent import AbstractComponent

class Monitor2D( AbstractComponent ):

    def process(self, neutrons):
        self._engine.process(neutrons)
        self.histogram = self._engine.histogram
        del self._engine.histogram
        return


    def __init__(self, name, x,y, nx, ny, xmin, xmax, ymin, ymax):
        exprs = [x,y]
        bins = [nx, ny]
        ranges = [
            (xmin, xmax),
            (ymin, ymax),
            ]
        from NDMonitor import NDMonitor
        self._engine = NDMonitor(name, exprs, bins, ranges)
        return
    
    
    pass # end of Monitor2D


# version
__id__ = "$Id: Monitor2D.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
