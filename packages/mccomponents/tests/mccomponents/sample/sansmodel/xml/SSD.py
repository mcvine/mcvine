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


# An instrument base class.

from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility, componentfactory as component
        import mccomponents.pyre_support
        
        source = facility(
            'source',
            default = component('sources', 'MonochromaticSource')('source') )
        sample = facility(
            'sample',
            default = component( 'samples', 'SampleAssemblyFromXml')('sample') )
        detector = facility(
            'detector',
            default = component( 'detectors', 'DetectorSystemFromXml')('detector') )
        
        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'sample', 'detector']
        return
    
    pass # end of Instrument


# version
__id__ = "$Id$"

# End of file 
