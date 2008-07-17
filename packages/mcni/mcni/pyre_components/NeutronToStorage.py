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
        path = pinv.str( 'path', default = 'neutrons' )
        append = pinv.bool( 'append', default = False )
        packetsize = pinv.int( 'packetsize', default = 1000 )
        pass


    def __init__(self, name):
        AbstractComponent.__init__(self, name)
        self.engine = None
        return


    def process(self, neutrons):
        engine = self.engine
        if engine is None: engine = self.engine = self._create_engine()
        ret = engine.process( neutrons )
        return ret
    
    
    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        self.append = self.inventory.append
        self.packetsize = self.inventory.packetsize
        return


    def _create_engine(self):
        path = self.path
        if os.path.split( path )[0] != '':
            raise ValueError, "path must be relative path: path=%s" % path
        
        if self._outputdir: path = os.path.join( self._outputdir, path )

        append = self.append or self.overwrite_datafiles
        packetsize = self.packetsize
        return enginefactory(
            self.name, path, append, packetsize = packetsize )
    

    pass # end of Source


import os

# version
__id__ = "$Id$"

# End of file 
