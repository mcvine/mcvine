#!/usr/bin/env python
#
#  Jiao Lin, Alex Dementsov
#


from ..default import ComponentInterface as base
from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin

class ComponentInterface(HistogramBasedMonitorMixin, base, ParallelComponent):


    def process(self, neutrons):
        ret = base.process(self, neutrons)
        # recreate engine to discard the old one
        # now everything is fresh. the monitor data is already saved
        # in _dumpData, so 
        # we dont lose any useful things
        self._createEngine()
        return ret


    def _dumpData(self):
        self.engine.simulation_context = self.simulation_context
        return self.engine._dumpData()
    
        
    def _fini(self):
        if not self._showHelpOnly and self._hasEngine():
            self._saveFinalResult()
            pass
        super(ComponentInterface, self)._fini()
        return


    def _saveFinalResult(self):
        self.engine.simulation_context = self.simulation_context
        return self.engine._saveFinalResult()

    
'''
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
'''


# End of file 
