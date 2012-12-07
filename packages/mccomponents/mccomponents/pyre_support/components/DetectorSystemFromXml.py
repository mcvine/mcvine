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


coordinate_system = 'McStas'


from mccomponents.detector import detectorcomponent as enginefactory
from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.pyre_support.AbstractComponent import AbstractComponent


class DetectorSystemFromXml(ParallelComponent, AbstractComponent):

    __doc__ = enginefactory.__doc__
    simple_description = "Detector system constructed from xml representation"
    full_description = ""

    
    class Inventory( AbstractComponent.Inventory ):

        import pyre.inventory as pinv
        instrumentxml = pinv.str( 'instrumentxml', default = 'instrument.xml' )
        
        tofparams = pinv.str( 'tofparams', default = '0,3e-3,1e-5' )
        tofparams.meta['tip'] = 'tof bin parameters: min, max, step'
        
        eventsdat = pinv.str( 'eventsdat', default = 'events.dat' )
        eventsdat.meta['tip'] = 'output event data file'
        pass
    

    def process(self, neutrons):
        # self._debug.log( 'detector accepting neutrons: %s' % (neutrons,) )
        engine = self._resetEngine()
        engine.process(neutrons)
        # engine.close()
        return neutrons


    def _resetEngine(self):
        if self.engine is None:
            self.engine = self._createEngine()
            return self.engine
        outdir = self.simulation_context.getOutputDirInProgress()
        path = self.eventsdat
        import os
        path = os.path.join(outdir, path)
        if not self.overwrite_datafiles and os.path.exists(path):
            raise IOError, "%s already exists" % path
        self._setOutputPath(path)
        return self.engine


    def _setOutputPath(self, path):
        self.engine.mca.setOutputFile(path)
        return


    def _createEngine(self):
        # output file path
        outdir = self.simulation_context.getOutputDirInProgress()
        path = self.eventsdat
        import os
        path = os.path.join(outdir, path)
        if not self.overwrite_datafiles and os.path.exists(path):
            raise IOError, "%s already exists" % path
        
        # other parameters
        instrumentxml = self.instrumentxml
        tofparams = self.tofparams

        # XXX: probably should make coordinate_system a parameter
        # XXX: in the future
        return enginefactory(
            self.name, instrumentxml, coordinate_system, tofparams, path)


    def _saveFinalResult(self):
        context = self.simulation_context
        # make sure every node reaches here
        if context.mpiSize:
            self.mpiBarrier()
        # merge and normalize neutron files
        if context.mpiRank == 0:
            import time; time.sleep(10)
            self._merge_and_normalize()
        return


    def _merge_and_normalize(self):
        merge_and_normalize(
            self.simulation_context.outputdir,
            self.eventsdat,
            self.overwrite_datafiles,
            )
        return


    def _configure(self):
        AbstractComponent._configure(self)
        tofparams = eval( self.inventory.tofparams )
        assert len(tofparams)==3
        self.tofparams = tofparams

        self.instrumentxml = self.inventory.instrumentxml
        self.eventsdat = self.inventory.eventsdat
        return

    
    def _init(self):
        super(DetectorSystemFromXml, self)._init()
        if self._showHelpOnly: 
            return
        return


    def _fini(self):
        if self.engine:
            del self.engine
            if not self._showHelpOnly:
                self._saveFinalResult()
        super(DetectorSystemFromXml, self)._fini()
        return


    def __init__(self, name):
        AbstractComponent.__init__(self, name)
        self.engine = None
        return
    

    pass # end of Source


def merge_and_normalize(
    outputdir='out',
    eventsdat='events.dat',
    overwrite_datafiles=True):
    
    # find all output files
    from mcni.components.outputs import n_mcsamples_files, mcs_sum
    import glob, os
    filename = eventsdat
    pattern = os.path.join(outputdir, '*', filename)
    eventdatfiles = glob.glob(pattern)
    n_mcsamples = n_mcsamples_files(outputdir)
    assert len(eventdatfiles) == n_mcsamples, \
        "neutron storage files %s does not match #mcsample files %s" %(
        len(eventdatfiles), n_mcsamples)
    if not eventdatfiles:
        return

    # output
    out = os.path.join(outputdir, eventsdat)
    if overwrite_datafiles:
        if os.path.exists(out):
            os.remove(out)
    # merge
    from mccomponents.detector import mergeEventFiles
    mergeEventFiles(eventdatfiles, out)
    
    # load number_of_mc_samples
    mcs = mcs_sum(outputdir)
    # normalize
    from mccomponents.detector import normalizeEventFile
    normalizeEventFile(out, mcs)
    return



# version
__id__ = "$Id$"

# End of file 
