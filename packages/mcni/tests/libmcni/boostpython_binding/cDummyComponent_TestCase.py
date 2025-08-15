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


import mcni.mcnibp as c

class cDummyComponent_TestCase(unittest.TestCase):


    def test(self):
        name = 'dummy'
        dummy = c.DummyComponent(name)
        self.assertEqual( dummy.name, name )

        neutrons = c.NeutronEventBuffer( 10 )
        dummy.process( neutrons )
        return
    
        
    pass  # end of cDummyComponent_TestCase



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
    suite1 = unittest.makeSuite(cDummyComponent_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
