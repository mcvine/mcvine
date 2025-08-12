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

from setup_sampleassemblies import mcvine_resources
if not mcvine_resources:
    skip = True

standalone = True


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample: SimplePowderDiffractionKernel'
        import mcni
        from mcni.utils import conversion
        
        from mcstas2 import componentfactory as cf
        f = cf('sources', 'Source_simple')
        component1 = f(
            name = "component1",
            E0=60, dE=20,
            height = 0.01, width = 0.01, radius=0,
            dist=4, 
            xw = 0.1, yh = 0.1,
            )
        
        from mccomponents.sample import samplecomponent
        import mccomponents.sample.diffraction.xml
        component2 = samplecomponent( 'Al', 'sampleassemblies/Al-simplepowderdiffractionkernel/sampleassembly.xml' )
        
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,5), (0,0,0) )

        N0 = 1000
        neutrons = mcni.neutron_buffer(N0)

        mcni.simulate( instrument, geometer, neutrons )

        N = len(neutrons)
        print(N)

        import numpy.linalg as nl, numpy as np
        for i in range(10):
            neutron = neutrons[i]
            Vf = np.array(neutron.state.velocity)
            print(Vf)
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
