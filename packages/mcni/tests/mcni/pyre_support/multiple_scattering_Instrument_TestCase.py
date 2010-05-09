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



import unittestX as unittest

class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: multiple scattering'
        instrument = Instrument('multiple_scattering_Instrument_TestCase')
        instrument.testFacility = self
        instrument.run()
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.AbstractComponent import AbstractComponent

class Component( AbstractComponent ):
    
    def process(self, neutrons):
        raise RuntimeError, "this method should not be called"


    def processM(self, neutrons):
        return neutrons

    pass # end of Source


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility
        source = facility('source', default = Component('source') )

        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.source = (0,0,0), (0,0,0)
        
        self.inventory.multiple_scattering = 1
        return
    
    
    pass # end of Instrument


def main():
    unittest.main()
    return


if __name__ == "__main__":
    main()

    
# version
__id__ = "$Id$"

# End of file 
