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


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.samplecomponent: E_Q_Kernel'
        import mcni
        from mcni.utils import conversion

        ei = 60
        vil = conversion.e2v(ei)
        vi = (0,0,vil)
        neutron = mcni.neutron( 
            r = (0,0,0), v = vi, 
            time = 0, prob = 1 )
        
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        
        from mccomponents.sample import samplecomponent
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-E_Q-kernel/sampleassembly.xml' )
        E_Q = '30+5*sin(Q)' # in sampleassemblies/Al-E_Q-kernel/Al-scatterer.xml

        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)

        import numpy.linalg as nl
        import numpy as np
        from math import sin
        for i in range(N):
            neutron = neutrons[i]
            vf = np.array(neutron.state.velocity)
            diffv = vi - vf
            Q = conversion.v2k(nl.norm(diffv))
            ef = conversion.v2e(nl.norm(vf))
            E = ei - ef
            # print E, Q, neutron
            E1 = eval(E_Q)
            # print E, E1
            self.assertAlmostEqual(E, E1)
            continue

        return
    

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id: samplecomponent_ConstantEnergyTransferKernel_TestCase.py 696 2010-11-09 06:23:06Z linjiao $"

# End of file 
