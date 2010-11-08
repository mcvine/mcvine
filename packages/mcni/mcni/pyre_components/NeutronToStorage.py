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
        return


    def _fini(self):
        if self.engine:
            self.engine.close()
        super(NeutronToStorage, self)._fini()
        return
    


    def _create_engine(self):
        path = self.path
        if os.path.split( path )[0] != '':
            raise ValueError, "path must be relative path: path=%s" % path
        
        if self._outputdir: path = os.path.join( self._outputdir, path )

        append = False
        if self.overwrite_datafiles:
            append = False
            if os.path.exists(path):
                os.remove(path)
        if self.append:
            append = True
            
        return enginefactory(
            self.name, path, append=append)
    

    pass # end of NeutronToStorage


import os

# version
__id__ = "$Id$"

# End of file 
