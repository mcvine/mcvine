#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


coordinate_system = 'McStas'


from mccomponents.detector import detectorcomponent as enginefactory
from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.pyre_support.AbstractComponent import AbstractComponent


class DetectorSystemFromXml(ParallelComponent, AbstractComponent):

    __doc__ = enginefactory.__doc__
    simple_description = "Detector system constructed from xml representation"
    full_description = ""

    
    class Inventory( AbstractComponent.Inventory ):

        import pyre.inventory as pinv
        instrumentxml = pinv.str( 'instrumentxml', default = 'instrument.xml' )
        
        tofparams = pinv.str( 'tofparams', default = '0,3e-3,1e-5' )
        tofparams.meta['tip'] = 'tof bin parameters: min, max, step'
        
        eventsdat = pinv.str( 'eventsdat', default = 'events.dat' )
        eventsdat.meta['tip'] = 'output event data file'
        pass
    

    def process(self, neutrons):
        # self._debug.log( 'detector accepting neutrons: %s' % (neutrons,) )
        engine = self._resetEngine()
        self.engine.simulation_context = self.simulation_context
        engine.process(neutrons)
        # engine.close()
        return neutrons


    def _resetEngine(self):
        if self.engine is None:
            self.engine = self._createEngine()
        return self.engine


    def _setOutputPath(self, path):
        self.engine.mca.setOutputFile(path)
        return


    def _createEngine(self):
        path = self.eventsdat
        # other parameters
        instrumentxml = self.instrumentxml
        tofparams = self.tofparams
        return enginefactory(
            self.name, instrumentxml, coordinate_system, tofparams, path)


    def _saveFinalResult(self):
        self._debug.log("Entering _saveFinalResult")
        engine = self.engine
        engine.simulation_context = self.simulation_context
        engine.create_pps()
        del self.engine
        return


    def _configure(self):
        AbstractComponent._configure(self)
        tofparams = eval( self.inventory.tofparams )
        assert len(tofparams)==3
        self.tofparams = tofparams

        self.instrumentxml = self.inventory.instrumentxml
        self.eventsdat = self.inventory.eventsdat
        return

    
    def _init(self):
        super(DetectorSystemFromXml, self)._init()
        if self._showHelpOnly: 
            return
        return


    def _fini(self):
        if self.engine:
            if not self._showHelpOnly:
                self._saveFinalResult()
        super(DetectorSystemFromXml, self)._fini()
        return


    def __init__(self, name):
        AbstractComponent.__init__(self, name)
        self.engine = None
        return
    

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
