#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcni.components.NeutronPrinter import NeutronPrinter as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent


class NeutronPrinter( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        return


    def _init(self):
        AbstractComponent._init(self)
        self.engine = enginefactory( self.name )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
