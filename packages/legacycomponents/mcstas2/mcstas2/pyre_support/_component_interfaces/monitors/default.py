#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcstas2.pyre_support._component_interfaces.default import ComponentInterface as base
from mcni.pyre_support.ParallelComponent import ParallelComponent

class ComponentInterface(base, ParallelComponent):

    def process(self, neutrons):
        
        # establish "iterationcount"
        iterationcount = self.__dict__.get('iterationcount')
        if iterationcount is None: iterationcount = 0
        # and process neutrons as normal
        ret = super(ComponentInterface, self).process(neutrons)
        iterationcount += 1
        self.iterationcount = iterationcount

        # save monitor data to a histogram in each round so that users
        # can see intermediate results
        hout = self._histogramOutputFilename()
        # this outputfile will be overwritten each round
        self._saveHistogramInMyoutputdir(filename=hout, overwrite=True)
        # also save a copy that mark the interation number
        self._saveHistogramInMyoutputdir(filename='%s.%s' % (hout, iterationcount))

        #
        return ret


    def _fini(self):
        if not self._showHelpOnly and self._hasEngine():
            if self.parallel:
                self._save_histogram_in_masternode_outdir()
            else:
                self._setFinalHistogram(self._get_histogram())
        super(ComponentInterface, self)._fini()
        return


    def _save_histogram_in_masternode_outdir(self):
        # save histogram to <out> instead of <out>-worker-0
        # get histogram to master node
        channel = 100
        histogram = self._get_histogram()
        if self.mpiRank != 0:
            I = histogram.I
            self.mpiSend(I, 0, channel)
        else:
            histogram = histogram.copy()
            I = histogram.I
            for rank in range(1, self.mpiSize):
                I1 = self.mpiReceive(rank, channel)
                I+=I1
                continue

        # save the histogram in the component
        self._setFinalHistogram(histogram)

        def _():
            saveHistogram(
                histogram,
                self._histogramOutputFilename(),
                overwrite=self.overwrite_datafiles)

        if self.mpiRank == 0:
            outputdir = self._master_outputdir
            self._debug.log('saving histogram to %s' % outputdir)
            self._run_in_dir(func=_, dir=outputdir)
        
        return

    
    def getFinalHistogram(self):
        k = '_final_histogram'
        if hasattr(self, k):
            return getattr(self, k)
        return


    def _setFinalHistogram(self, h):
        k = '_final_histogram'
        setattr(self, k, h)
        return


    def _hasEngine(self):
        return self.__dict__.get('engine')
    

    def _histogramOutputFilename(self):
        filename = self.inventory.filename
        b, ext = os.path.splitext(filename)
        f = '%s.h5' % b
        return f


    def _saveHistogramInMyoutputdir(self, filename, overwrite=False):
        overwrite = self.overwrite_datafiles or overwrite
        def _():
            return saveHistogram(
                self._get_histogram(), filename,
                overwrite=overwrite)
        return self._run_in_myoutputdir(_)



import os

def saveHistogram(histogram, filename, overwrite=False):
    if overwrite and os.path.exists(filename): os.remove( filename )
    from histogram.hdf import dump
    dump( histogram, filename, '/', 'c')
    return


# version
__id__ = "$Id$"

# End of file 
