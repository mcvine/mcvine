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


from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.pyre_support.AbstractComponent import AbstractComponent

class NeutronToStorage(ParallelComponent, AbstractComponent):


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
        path.meta['tip'] = "The path where neutrons will be saved. This must be a relative path within the output directory of the instrument simulation application."
        pass


    def __init__(self, name):
        AbstractComponent.__init__(self, name)
        self.engine = None
        return


    def process(self, neutrons):
        self.engine = engine = self._createEngine()
        engine.process( neutrons )
        engine.close()
        return neutrons
    
    
    def _createEngine(self):
        outdir = self.simulation_context.getOutputDirInProgress()
        path = self.path
        path = os.path.join(outdir, path)
        if self.overwrite_datafiles:
            if os.path.exists(path):
                os.remove(path)
        return enginefactory(self.name, path)


    def _saveFinalResult(self):
        self._debug.log("Entering _saveFinalResult")
        engine = self.engine
        engine.simulation_context = self.simulation_context
        engine.create_pps()
        del self.engine
        return


    def _configure(self):
        super(NeutronToStorage, self)._configure()
        self.path = self.inventory.path
        return


    def _fini(self):
        if not self._showHelpOnly:
            self._saveFinalResult()
        super(NeutronToStorage, self)._fini()
        return


    pass # end of NeutronToStorage


def merge_and_normalize(outdir, filename, overwrite_datafiles):
    import warnings
    warnings.warn("Obsolete. Please use mcni.components.NeutronToStorage.merge_and_normalize instead")
    from ..components.NeutronToStorage import merge_and_normalize
    return merge_and_normalize(outdir, filename, overwrite_datafiles)

import os

# version
__id__ = "$Id$"

# End of file 
