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


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage.idfneutron import ndblsperneutron, filesize

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
        from mcni.components.NeutronFromStorage import NeutronFromStorage
        self.engine = NeutronFromStorage( self.name, self.path )
        return

    pass # end of Source


import os, numpy


# version
__id__ = "$Id$"

# End of file 
