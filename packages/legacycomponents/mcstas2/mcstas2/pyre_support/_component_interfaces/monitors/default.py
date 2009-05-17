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
        self._saveHistogramInMyoutputdir(filename=hout)
        self._saveHistogramInMyoutputdir(filename='%s.%s' % (hout, iterationcount))

        #
        return ret


    def _fini(self):
        if not self._showHelpOnly and self._hasEngine() and self.parallel:
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
                
            def _():
                saveHistogram(
                    histogram,
                    self._histogramOutputFilename(),
                    overwrite=self.overwrite_datafiles)

            outputdir = self._master_outputdir
            self._run_in_dir(func=_, dir=outputdir)
            
        super(ComponentInterface, self)._fini()
        return


    def _hasEngine(self):
        return self.__dict__.get('engine')
    

    def _histogramOutputFilename(self):
        filename = self.inventory.filename
        b, ext = os.path.splitext(filename)
        f = '%s.h5' % b
        return f


    def _saveHistogramInMyoutputdir(self, filename):
        def _():
            return saveHistogram(
                self._get_histogram(), filename,
                overwrite=self.overwrite_datafiles)
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
