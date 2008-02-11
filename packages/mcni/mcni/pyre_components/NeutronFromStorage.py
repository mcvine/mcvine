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


from mcni.components.NeutronToStorage import NeutronToStorage as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent

class NeutronFromStorage( AbstractComponent ):


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = '' )
        pass
    

    def process(self, neutrons):
        return self.engine.process(neutrons)


    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        return


    def _init(self):
        AbstractComponent._init(self)
        self.engine = enginefactory( self.name, self.path )
        return

    pass # end of Source


import os, numpy


# version
__id__ = "$Id$"

# End of file 
