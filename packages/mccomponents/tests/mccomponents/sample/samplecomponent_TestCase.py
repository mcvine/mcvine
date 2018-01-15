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


import os, numpy as np
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
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,3000), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Ni', 'sampleassemblies/Ni/sampleassembly.xml' )
        # check mu
        hs = component2.cscatterers[0]
        assert np.isclose(hs.mu(neutron), 4 * 4.49e-28 / (3.52e-10)**3*2200/3000)
        #
        instrument = mcni.instrument( [component1, component2] )
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        neutrons = mcni.neutron_buffer( 1 )

        mcni.simulate( instrument, geometer, neutrons )

        for i in range(len(neutrons)):
            neutron = neutrons[i]
            print neutron
            continue
        
        return
    

    def test2(self):
        'mccomponents.sample.samplecomponent: inversevelocityabsorption'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,3000), time = 0, prob = 1 )
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Ni', 'sampleassemblies/Ni-inversevelocityabsorption/sampleassembly.xml' )
        # check mu
        # see sampleassemblies/Ni-inversevelocityabsorption/Ni plate-scatterer.xml
        hs = component2.cscatterers[0]
        assert np.isclose(hs.mu(neutron), 22.)
        return
    

    def test3(self):
        'mccomponents.sample.samplecomponent: interpolateabsorptionfromcurve'
        import mcni
        from mccomponents.sample import samplecomponent
        from mcni.utils import conversion
        component2 = samplecomponent(
            'Ni', 'sampleassemblies/Ni-interpolateabsorptionfromcurve/sampleassembly.xml' )
        hs = component2.cscatterers[0]
        # see sampleassemblies/Ni-interpolateabsorptionfromcurve/mu.dat
        # check mu
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(40.)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 100)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(100.)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 30)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(70.)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 65)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(30.)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 100)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(1e-5)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 100)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,conversion.e2v(1000.)), time = 0, prob = 1 )
        assert np.isclose(hs.mu(neutron), 30)
        return
    

    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
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
