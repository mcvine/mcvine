#!/usr/bin/env python
#


standalone = True

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

import numpy as np

import unittestX as unittest
class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent: DGSSXResKernel'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (0,0,3000), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-DGSSXResKernel/sampleassembly.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,6), (0,0,0) )

        N0 = 10
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)

        for i in range(10):
            neutron = neutrons[i]
            # print neutron
            self.assert_(np.allclose(neutron.state.velocity, [3000, 0, 0], atol=20))
            continue

        return

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__": main()
    
# End of file 
