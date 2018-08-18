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


import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


standalone = True


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample: ConstantQEKernel'
        # momentum and energy transfer. defined in the scatterer xml file
        Q0 = 3
        E0 = 30

        import mcni
        from mcni.utils import conversion
        
        ei = 60
        vi = conversion.e2v(ei)
        Vi = (0,vi,0)
        neutron = mcni.neutron( r = (0,0,0), v = Vi, time = 0, prob = 1 )
        
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-constantqekernel/sampleassembly.xml' )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,1,0), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)

        import numpy.linalg as nl, numpy as np
        for i in range(10):
            neutron = neutrons[i]
            Vf = np.array(neutron.state.velocity)
            print Vf

            ef = conversion.v2e(nl.norm(Vf))
            E = ei-ef
            
            dV = np.array(Vf) - np.array(Vi)
            qasv = nl.norm(dV)
            Q = conversion.v2k(qasv)

            self.assertAlmostEqual(E, E0, 7)
            self.assertAlmostEqual(Q, Q0, 7)
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
