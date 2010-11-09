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

import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent'
        # energy transfer. defined in the scatterer xml file
        E0 = 10

        import mcni
        from mcni.utils import conversion
        
        ei = 60
        vi = conversion.e2v(ei)
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,vi), time = 0, prob = 1 )
        
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-constantenergytransfer/sampleassembly.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)

        import numpy.linalg as nl
        for i in range(10):
            neutron = neutrons[i]
            vf = nl.norm(neutron.state.velocity)
            ef = conversion.v2e(vf)
            E = ei-ef
            self.assertAlmostEqual(E, E0, 7)
            continue

        return
    

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
