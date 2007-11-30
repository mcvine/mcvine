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
import journal

debug = journal.debug( "mcni_TestCase" )
warning = journal.warning( "mcni_TestCase" )


import mcni

class mcni_TestCase(unittest.TestCase):


    def test(self):
        component1 = Source('source')
        component2 = Verifier('dummy2', self)
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,90) )

        neutrons = mcni.neutron_buffer( 1 )

        mcni.simulate( instrument, geometer, neutrons )

        for i in range(len(neutrons)):
            neutron = neutrons[i]
            r = list( neutron.state.position )
            v = list( neutron.state.velocity )
            self.assertVectorAlmostEqual( r, (1,2,3) )
            self.assertVectorAlmostEqual( v, (1,2,3) )
            continue
        return
    
        
    pass  # end of mcni_TestCase



from mcni.AbstractComponent import AbstractComponent
class Source( AbstractComponent ):

    def process(self, neutrons):
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = ( 1,2,3 ), v = (1,2,3) )
            continue
        return neutrons

    pass # end of Source


class Verifier( AbstractComponent ):

    def __init__(self, name, testFacility):
        AbstractComponent.__init__(self, name)
        self.testFacility = testFacility
        return

    def process(self, neutrons):
        for i in range(len(neutrons)):
            r = list( neutrons[i].state.position )
            self.testFacility.assertVectorAlmostEqual(
                r, (2,-1,2) )
            
            v = list( neutrons[i].state.velocity )
            self.testFacility.assertVectorAlmostEqual(
                v, (2,-1,3) )
            continue
        return neutrons

    pass # end of Verifier


    
def pysuite():
    suite1 = unittest.makeSuite(mcni_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
