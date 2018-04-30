#!/usr/bin/env python
#
#  Jiao Lin, Alex Dementsov
#


from mcstas2.pyre_support._component_interfaces.default import ComponentInterface as base
from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin

class ComponentInterface(HistogramBasedMonitorMixin, base, ParallelComponent):


    class Inventory(base.Inventory):

        import pyre.inventory
        restore_neutron = pyre.inventory.bool('restore_neutron')


    def process(self, neutrons):
        # self.engine is created by self._createEngine()
        # earlier in self._init.
        # See mcstas2.utils.pyre_support.ElementaryComponentGenerator
        # self.engine should be an instance of mcstas2.AbstractComponent.AbstractComponent
        # and are created by factories methods registered in
        # mcstas2.components.Registry
        self.engine.restore_neutron = self.inventory.restore_neutron
        ret = self.engine.process(neutrons)
            
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


def attr(obj, name, repl):
    """
    Scripts in this directory are used both by VNF and McVine. Due to issue with the
    Postgres database considering 'xmin', 'xmax', 'ymin' and 'ymax' column names
    as special fields VNF uses replacement e.g. 'xmin' -> 'x_min' whereas McVine
    still uses 'xmin'
    """
    if hasattr(obj, repl):  # If object has replacement attribute, use it
        return getattr(obj, repl)

    # Otherwise use standard name
    return getattr(obj, name)



# version
__id__ = "$Id$"

# End of file 
