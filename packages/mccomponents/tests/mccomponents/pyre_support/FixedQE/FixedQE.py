#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



## This simulation mimic a sample that has a delta function like S(Q,E), i.e.
## the sample only send neutrons that have the exact momentum and energy
## transfer (Q, E).


from sim_params import *


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility, componentfactory as component
        import mccomponents.pyre_support
        source = facility(
            'source',
            default = component('sources', 'NeutronsOnCone_FixedQE')('source') )
        detector = facility(
            'detector',
            default = component( 'detectors', 'DetectorSystemFromXml')('detector') )
        pass # end of Inventory


    def __init__(self, name = 'test-FixedQE'):
        base.__init__(self, name)
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'detector']

        geometer = self.inventory.geometer
        geometer.inventory.source = (0,0,mod2sample), (0,0,0)
        geometer.inventory.detector = (0,0,mod2sample), (0,0,0)

        source = self.inventory.source
        source.inventory.Ei = Ei
        source.inventory.E = E
        source.inventory.Q = Q
        source.inventory.L1 = mod2sample

        detector = self.inventory.detector
        detector.inventory.eventsdat = eventsdat
        detector.inventory.instrumentxml = instrumentxml
        detector.inventory.tofparams = str(tofparams)
        return
    
    pass # end of Instrument


def main():
    Instrument().run()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
