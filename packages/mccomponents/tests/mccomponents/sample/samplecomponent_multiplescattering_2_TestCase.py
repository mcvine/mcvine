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



standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


import unittestX as unittest
import journal

debug = journal.debug( "samplecomponent_TestCase" )
warning = journal.warning( "samplecomponent_TestCase" )


scattererxml = 'Ni-scatterer.xml'


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,4149.48), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'bmg', 'sampleassemblies/bmg/sampleassembly.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )
        
        neutrons = mcni.neutron_buffer( 1 )
        
        from mcni.pyre_support.ConsoleNeutronTracer import ConsoleNeutronTracer
        tracer = ConsoleNeutronTracer()
        mcni.simulate( 
            instrument, geometer, neutrons, 
            multiple_scattering=True,
            tracer = tracer
            )

        return
    

    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    import journal
    # journal.debug('CompositeNeutronScatterer_Impl').activate()
    # journal.debug('HomogeneousNeutronScatterer').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
