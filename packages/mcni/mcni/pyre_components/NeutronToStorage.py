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


    simple_description = "Save neutrons to a file"
    full_description = (
        "At times, it could be useful to save the simulated neutrons into file, "
        "so that they can be reused. "
        "When you add this component into the instrument component chain, "
        "all neutrons reach its position will be saved into a file."
        )


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = 'neutrons' )
        path.meta['tip'] = "The path at which neutrons will be saved"
        
        append = pinv.bool( 'append', default = False )
        append.meta['tip'] = "Append to an existing neutron file"
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
        
        path = os.path.join( self._getOutputDir(), path )

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
