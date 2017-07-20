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
        engine = self._createEngine()
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
        context = self.simulation_context
        if context.mpiRank != 0:
            return
        # create post processing script
        import os
        path = os.path.join(context.post_processing_scripts_dir, "%s.py" % self.name)
        content = """from mcni.pyre_components.NeutronToStorage import merge_and_normalize
merge_and_normalize(%r, %r, %r)
""" % (os.path.abspath(self.simulation_context.outputdir),
       self.path,
       self.overwrite_datafiles)
        open(path, 'wt').write(content)
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
    # XXX: should rewrite using mcni.neutron_storage.merge_and_normalize
    # find all output files
    from mcni.components.outputs import n_mcsamples_files, mcs_sum
    import glob, os
    pattern = os.path.join(outdir, '*', filename)
    nsfiles = glob.glob(pattern)
    n_mcsamples = n_mcsamples_files(outdir)
    assert len(nsfiles) == n_mcsamples, \
        "neutron storage files %s does not match #mcsample files %s" %(
        len(nsfiles), n_mcsamples)
    if not nsfiles:
        return None, None

    # output
    out = os.path.join(outdir, filename)
    if overwrite_datafiles:
        if os.path.exists(out):
            os.remove(out)
    # merge
    from mcni.neutron_storage import merge
    merge(nsfiles, out)

    # number of neutron events totaly in the neutron file
    from mcni.neutron_storage.idf_usenumpy import count
    nevts = count(out)
    if nevts == 0: # no neutron saved
        return

    # load number_of_mc_samples
    mcs = mcs_sum(outdir)

    # normalization factor. this is a bit tricky!!!
    nfactor = mcs/nevts

    # normalize
    from mcni.neutron_storage import normalize
    normalize(out, nfactor)
    return

import os

# version
__id__ = "$Id$"

# End of file 
