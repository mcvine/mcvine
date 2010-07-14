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
from mcni.pyre_support.AbstractComponent import AbstractComponent


class DetectorSystemFromXml( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):

        import pyre.inventory as pinv
        instrumentxml = pinv.str( 'instrumentxml', default = 'instrument.xml' )
        
        tofparams = pinv.str( 'tofparams', default = '0,3e-3,1e-5' )
        tofparams.meta['tip'] = 'tof bin parameters: min, max, step'
        
        eventsdat = pinv.str( 'eventsdat', default = 'events.dat' )
        eventsdat.meta['tip'] = 'output event data file'
        pass
    

    def process(self, neutrons):
        self._debug.log( 'detector accepting neutrons: %s' % (neutrons,) )
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        tofparams = eval( self.inventory.tofparams )
        assert len(tofparams)==3
        self.tofparams = tofparams

        self.instrumentxml = self.inventory.instrumentxml
        self.eventsdat = self.inventory.eventsdat
        return


    def _init(self):
        AbstractComponent._init(self)
        if self._showHelpOnly: return
        instrumentxml = self.instrumentxml
        tofparams = self.tofparams

        eventsdat = self.eventsdat
        import os
        eventsdat = os.path.join(self._outputdir, eventsdat)
        
        self.engine = enginefactory(
            self.name, instrumentxml, coordinate_system, tofparams, eventsdat )
        return


    def _fini(self):
        if self.__dict__.has_key( 'engine' ):
            del self.engine
        AbstractComponent._fini(self)
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
