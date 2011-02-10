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
from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin

class ComponentInterface(HistogramBasedMonitorMixin, base, ParallelComponent):

    # Hack!
    overwrite_datafiles = False     # Not sure if it is the right place

    class Inventory(base.Inventory):

        import pyre.inventory
        restore_neutron = pyre.inventory.bool('restore_neutron')


    def process(self, neutrons):
        restore_neutron = self.inventory.restore_neutron
        if restore_neutron:
            # create a copy to be processed
            saved = neutrons.snapshot(len(neutrons))
            
        # and process neutrons as normal
        ret = super(ComponentInterface, self).process(neutrons)
    
        # dump all calculated data
        self._dumpData()
        
        # restore neutrons if requested
        if restore_neutron:
            neutrons.swap(saved)
            
        # recreate engine to discard the old one
        # now everything is fresh. the monitor data is already saved
        # in _dumpData, so 
        # we dont lose any useful things
        self._createEngine()
        return ret


    def _dumpData(self):
        # save monitor data to a histogram in each round so that users
        # can see intermediate results
        histogram = self._get_histogram()
        outdir = self._getOutputDirInProgress()
        hout = self._histogramOutputFilename()
        self._saveHistogram(histogram, directory=outdir, filename=hout)
        return
    
        
    def _fini(self):
        if not self._showHelpOnly and self._hasEngine():
            self._saveFinalResult()
            pass
        
        super(ComponentInterface, self)._fini()
        return

    
    def _get_histogram(self):
        raise NotImplementedError


    def _histogramOutputFilename(self):
        filename = self.inventory.filename
        b, ext = os.path.splitext(filename)
        f = '%s.h5' % b
        return f
    _getHistogramFilename = _histogramOutputFilename
    
    
    def _saveHistogram(self, histogram, directory, filename):
        overwrite = self.overwrite_datafiles or overwrite
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


# version
__id__ = "$Id$"

# End of file 
