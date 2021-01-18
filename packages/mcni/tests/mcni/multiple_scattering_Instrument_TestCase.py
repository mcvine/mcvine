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
import mcni


class TestCase(unittest.TestCase):


    def test(self):
        component1 = Component('comp')
        instrument = mcni.instrument( [component1] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )

        neutrons = mcni.neutron_buffer( 2 )

        mcni.simulate( instrument, geometer, neutrons, multiple_scattering=1)
        return
    
        
    pass  # end of TestCase


from mcni.AbstractComponent import AbstractComponent
class Component( AbstractComponent ):

    def process(self, neutrons):
        raise RuntimeError("this method should not be called")


    def processM(self, neutrons):
        return neutrons

    pass # end of Source


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
