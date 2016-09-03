#!/usr/bin/env python
#
#


standalone = True

import unittestX as unittest
import journal

debug = journal.debug( "DGSSXResKernel_TestCase" )
warning = journal.warning( "DGSSXResKernel_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        target_position = mcnibp.Vector3_double(3,0,0);
        target_radius = 0.025
        tof_at_target = 0.001
        dtof = 1e-5
        absorption_coefficient = scattering_coefficient = 1.
        kernel = mccomponentsbp.DGSSXResKernel(
            target_position, target_radius,
            tof_at_target, dtof,
            absorption_coefficient, scattering_coefficient
            )

        from mcni.utils import conversion
        vil = 3000
        vi = (0,0,vil)
        ei = conversion.v2e(vil)

        import numpy.linalg as nl
        import numpy as np
        for i in range(10):
            event = mcni.neutron( 
                r = (0,0,0), v = vi,
                prob = 1, time = 0 )
            kernel.scatter( event );
            vf = np.array(event.state.velocity)
            diffv = vi - vf
            Q = conversion.v2k(nl.norm(diffv))
            ef = conversion.v2e(nl.norm(vf))
            E = ei - ef
            # print Q,E
            self.assert_(np.isclose(Q, 6.74, rtol=1e-2))
            self.assert_(np.isclose(E, 0, atol=.5))
            continue

        return
    
    
    pass  # end of TestCase

    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__": main()
    
# End of file 
