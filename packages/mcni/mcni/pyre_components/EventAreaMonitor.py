#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2012  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.pyre_support.AbstractComponent import AbstractComponent

from mcni.components.EventAreaMonitor import EventAreaMonitor as enginefactory, category

class EventAreaMonitor(ParallelComponent, AbstractComponent):

    __doc__ = enginefactory.__doc__
    
    simple_description = "event mode area detector"
    full_description = __doc__
    
    
    class Inventory( AbstractComponent.Inventory ):
        
        import pyre.inventory as pinv
        
        tofmin = pinv.float( 'tofmin', default = 0 )
        tofmin.meta['tip'] = 'tof min'
        tofmax = pinv.float( 'tofmax', default = 0.01 )
        tofmax.meta['tip'] = 'tof max'
        ntof = pinv.int( 'ntof', default = 100 )
        ntof.meta['tip'] = 'number of tof channels'
        
        xmin = pinv.float( 'xmin', default = -0.1 )
        xmin.meta['tip'] = 'x min'
        xmax = pinv.float( 'xmax', default = 0.1 )
        xmax.meta['tip'] = 'x max'
        nx = pinv.int( 'nx', default = 100 )
        nx.meta['tip'] = 'number of x bins'
        
        ymin = pinv.float( 'ymin', default = -0.1 )
        ymin.meta['tip'] = 'y min'
        ymax = pinv.float( 'ymax', default = 0.1 )
        ymax.meta['tip'] = 'y max'
        ny = pinv.int( 'ny', default = 100 )
        ny.meta['tip'] = 'number of y bins'
        
        eventsdat = pinv.str( 'eventsdat', default = 'events.dat' )
        eventsdat.meta['tip'] = 'output event data file'
        pass
    
    
    def process(self, neutrons):
        # self._debug.log( 'detector accepting neutrons: %s' % (neutrons,) )
        engine = self._getEngine()
        engine.process(neutrons)
        self._saveResult()
        return neutrons
    
    
    def _saveResult(self):
        events = self.engine.events
        path = self._getOutputPath()
        events.tofile(path)
        return
    
    
    def _getEngine(self):
        if self.engine is None:
            self.engine = self._createEngine()
            return self.engine
        self._resetEngine(self.engine)
        return self.engine


    def _resetEngine(self, engine):
        "override this if engine needs to be reset for each sim iteration"
        return

    
    def _getOutputPath(self):
        outdir = self.simulation_context.getOutputDirInProgress()
        path = self.eventsdat
        import os
        path = os.path.join(outdir, path)
        # output file path
        if not self.overwrite_datafiles and os.path.exists(path):
            raise IOError, "%s already exists" % path
        return path


    def _createEngine(self):
        path = self._getOutputPath()
        # other parameters
        xmin, xmax, nx = self.xmin, self.xmax, self.nx
        ymin, ymax, ny = self.ymin, self.ymax, self.ny
        tofmin, tofmax, ntof = self.tofmin, self.tofmax, self.ntof

        return enginefactory(
            self.name, 
            xmin = xmin, xmax = xmax, nx = nx,
            ymin = ymin, ymax = ymax, ny = ny,
            tofmin = tofmin, tofmax = tofmax, ntof = ntof,
            )


    def _saveFinalResult(self):
        context = self.simulation_context
        # make sure every node reaches here
        if context.mpiSize:
            self.mpiBarrier()
        # merge and normalize neutron files
        if context.mpiRank == 0:
            import time; time.sleep(5)
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
        self.eventsdat = self.inventory.eventsdat
        self.xmin = self.inventory.xmin
        self.xmax = self.inventory.xmax
        self.nx = self.inventory.nx
        self.ymin = self.inventory.ymin
        self.ymax = self.inventory.ymax
        self.ny = self.inventory.ny
        self.tofmin = self.inventory.tofmin
        self.tofmax = self.inventory.tofmax
        self.ntof = self.inventory.ntof
        return

    
    def _init(self):
        super(EventAreaMonitor, self)._init()
        if self._showHelpOnly: 
            return
        return


    def _fini(self):
        if self.engine:
            del self.engine
            if not self._showHelpOnly:
                self._saveFinalResult()
        super(EventAreaMonitor, self)._fini()
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
