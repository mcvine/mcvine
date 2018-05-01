# Jiao Lin <jiao.lin@gmail.com>

from ..default import Component as base
from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin

class Component(HistogramBasedMonitorMixin, base):


    def __init__(self, *args, **kwds):
        base.__init__(self, *args, **kwds)
        return

    def _dumpData(self):
        # save monitor data to a histogram in each round so that users
        # can see intermediate results
        histogram = self._get_histogram()
        outdir = self._getOutputDirInProgress()
        hout = self._histogramOutputFilename()
        self._saveHistogram(histogram, directory=outdir, filename=hout)
        return
    
        
    def _get_histogram(self):
        raise NotImplementedError


    def _histogramOutputFilename(self):
        # assumes all monitor components have the parameter "filename"
        filename = self.filename
        b, ext = os.path.splitext(filename)
        f = '%s.h5' % b
        return f
    _getHistogramFilename = _histogramOutputFilename
    
    
    def _saveHistogram(self, histogram, directory, filename):
        overwrite = self.simulation_context.overwrite_datafiles
        path = os.path.join(directory, filename)
        return saveHistogram(histogram, path, overwrite=overwrite)


import os

def saveHistogram(histogram, filename, overwrite=False):
    if os.path.exists(filename): 
        if overwrite:
            os.remove( filename )
        else:
            raise IOError, "%s already exists" % filename
    #
    from histogram.hdf import dump
    dump( histogram, filename, '/', 'c')
    return


# End of file 
