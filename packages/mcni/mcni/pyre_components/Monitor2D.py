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


from mcni.components.Monitor2D import Monitor2D as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent


class Monitor2D( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):

        import pyre.inventory

        x = pyre.inventory.str('x', default='x')
        y = pyre.inventory.str('y', default='y')

        xmin = pyre.inventory.float('xmin')
        xmax = pyre.inventory.float('xmax')

        ymin = pyre.inventory.float('ymin')
        ymax = pyre.inventory.float('ymax')

        nx = pyre.inventory.int('nx', default=10)
        ny = pyre.inventory.int('ny', default=10)

        filename = pyre.inventory.str('filename', default='')
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _fini(self):
        h = self.engine.histogram
        from histogram.hdf import dump
        dir = self.getOutputDir()
        f = self.inventory.filename or ('%s.h5' % self.name)
        import os
        f = os.path.join(dir, f)
        dump(h, f, '/', 'c')
        super(Monitor2D, self)._fini()
        return


    def _init(self):
        AbstractComponent._init(self)
        x = self.inventory.x
        y = self.inventory.y
        nx = self.inventory.nx
        ny = self.inventory.ny
        xmin = self.inventory.xmin
        xmax = self.inventory.xmax
        ymin = self.inventory.ymin
        ymax = self.inventory.ymax
        self.engine = enginefactory(
            self.name,
            x, y,
            nx, ny,
            xmin, xmax,
            ymin, ymax,
            )
        return

    pass # end of Monitor2D



# version
__id__ = "$Id: NeutronPrinter.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
