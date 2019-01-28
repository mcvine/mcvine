#!/usr/bin/env python
#
#


interactive = False

import numpy as np
import unittestX as unittest
import journal
import mcni


class TestCase(unittest.TestCase):


    def test1(self):
        from mcni.utils import conversion as C
        from mccomponents.sample import samplecomponent
        cu = samplecomponent( 'Cu', 'Cu/sampleassembly.xml')
        cs = cu.cscatterers[0]
        k = cs.getKernel()
        vz = C.k2v(np.pi*2/1.5)
        n = mcni.neutron(v=(0,0,vz))
        self.assert_(k.scattering_coefficient(n)<100)
        self.assert_(k.absorption_coefficient(n)<100)
        return
        
        
    pass  # end of TestCase


if __name__ == "__main__":   unittest.main()
    
# End of file 
