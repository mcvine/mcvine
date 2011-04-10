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

debug = journal.debug( "wrap_c_neutroncomponent_TestCase" )
warning = journal.warning( "wrap_c_neutroncomponent_TestCase" )


import mcni

class wrap_c_neutroncomponent_TestCase(unittest.TestCase):


    def test(self):
        component1 = Source('source')
        import mcni.mcnibp as c
        component2 = c.DummyComponent('dummy2')
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,90) )

        neutrons = mcni.neutron_buffer( 1 )

        mcni.simulate( instrument, geometer, neutrons )

        return
    
        
    pass  # end of wrap_c_neutroncomponent_TestCase



from mcni.AbstractComponent import AbstractComponent
class Source( AbstractComponent ):

    def process(self, neutrons):
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = ( 1,2,3 ), v = (1,2,3) )
            continue
        return neutrons

    pass # end of Source


    
def pysuite():
    suite1 = unittest.makeSuite(wrap_c_neutroncomponent_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
