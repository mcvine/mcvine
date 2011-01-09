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


from mcni.components.NeutronFromStorage import NeutronFromStorage as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent

class NeutronFromStorage( AbstractComponent ):


    simple_description = "Load neutrons from a file"
    full_description = (
        "In mcvine simulation, one can save neutrons to a file and reuse them "
        "(please see NeutronToStorage for more details)."
        "Use this component to load neutrons saved from a previous simulation. "
        "You may want to make sure the position of this NeutronFromStorage "
        "component is at the same position where the NeutronToStorage component "
        "was."
        )


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = '' )
        path.meta['tip'] = "The path where neutrons will be loaded"
        pass
    

    def process(self, neutrons):
        return self.engine.process(neutrons)


    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        return


    def _init(self):
        AbstractComponent._init(self)
        if self._showHelpOnly: return
        self.engine = enginefactory( self.name, self.path )
        return

    pass # end of Source


import os, numpy


# version
__id__ = "$Id$"

# End of file 
