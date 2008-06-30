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

class NeutronToStorage( AbstractComponent ):


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = '' )
        append = pinv.bool( 'append', default = False )
        packetsize = pinv.int( 'packetsize', default = 100 )
        pass
    

    def process(self, neutrons):
        ret = self.engine.process( neutrons )
        return ret
    
    
    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        self.append = self.inventory.append
        self.packetsize = self.inventory.packetsize
        return


    def _init(self):
        AbstractComponent._init(self)
        if self._showHelpOnly: return
        self.engine = enginefactory(
            self.name, self.path, self.append, packetsize = self.packetsize )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
