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
        
        # save monitor data to a histogram in each round so that users
        # can see intermediate results
        histogram = self._get_histogram()
        outdir = self._getOutputDirInProgress()
        hout = self._histogramOutputFilename()
        self._saveHistogram(histogram, directory=outdir, filename=hout)
        
        # restore neutrons if requested
        if restore_neutron:
            neutrons.swap(saved)
            
        return ret


    def _fini(self):
        if not self._showHelpOnly and self._hasEngine():
            context = self.simulation_context
            if context.mpiSize:
                histogram = self._get_histogram_summed_over_nodes()
            else:
                histogram = self._get_histogram()
            #
            outdir = self._getOutputDir()
            filename = self._histogramOutputFilename()
            # only the master node need to save the final histogram
            if self.simulation_context.mpiRank == 0:
                self._saveHistogram(histogram, directory=outdir, filename=filename)
            pass
        
        super(ComponentInterface, self)._fini()
        return


    def _get_histogram(self):
        raise NotImplementedError


    def _get_histogram_summed_over_nodes(self):
        # get histogram to master node
        channel = 100
        histogram = self._get_histogram()
        context = self.simulation_context
        if context.mpiRank != 0:
            I = histogram.I
            self.mpiSend(I, 0, channel)
        else:
            histogram = histogram.copy()
            I = histogram.I
            for rank in range(1, context.mpiSize):
                I1 = self.mpiReceive(rank, channel)
                I+=I1
                continue
        return histogram

    
    def _histogramOutputFilename(self):
        filename = self.inventory.filename
        b, ext = os.path.splitext(filename)
        f = '%s.h5' % b
        return f
    
    
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
