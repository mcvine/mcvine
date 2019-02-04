#!/usr/bin/env python
#
#

import os, numpy as np, histogram as H
from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin
from mcni.AbstractComponent import AbstractComponent
from mcni.components.ParallelComponent import ParallelComponent

class Monitor(HistogramBasedMonitorMixin, AbstractComponent, ParallelComponent):

    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        return

    def process(self, neutrons):
        self._dumpData()
        return neutrons

    def _get_histogram(self):
        tofaxis = H.axis('tof', boundaries = np.arange(0, 100., 1.0), unit='microsecond')
        return H.histogram('I(tof)', [tofaxis])

    def _dumpData(self):
        histogram = self._get_histogram()
        outdir = self._getOutputDirInProgress()
        hout = self.filename
        self._saveHistogram(histogram, directory=outdir, filename=hout)
        return

    def _getHistogramFilename(self): return self.filename

    def _saveHistogram(self, histogram, directory, filename):
        overwrite = self.simulation_context.overwrite_datafiles
        path = os.path.join(directory, filename)
        return saveHistogram(histogram, path, overwrite=overwrite)

def saveHistogram(histogram, filename, overwrite=False):
    if os.path.exists(filename): 
        if overwrite:
            os.remove( filename )
        else:
            raise IOError, "%s already exists" % filename
    from histogram.hdf import dump
    dump( histogram, filename, '/', 'c')
    return


import mcvine, mcvine.components
instrument = mcvine.instrument()
comp = Monitor('mon', 'mon.h5')
instrument.append(comp, position=(0,0,0))

    
# End of file 
