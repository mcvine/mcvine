#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# methods that is needed for most monitor components
class MonitorMixin(object):

    def _saveFinalResult(self):
        """save final result. should be called within _fini in most cases"""
        context = self.simulation_context
        final_result = self._getFinalResult()
        # only the master node need to do the io
        if context.mpiRank == 0:
            self._saveResult(final_result, context.outputdir)
        return
    
    
    def _getFinalResult(self):
        """get the final result of this monitor"""
        raise NotImplementedError


    def _saveResult(self, res, directory):
        """save result to the given directory"""
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
