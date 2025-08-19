#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


standalone = True


import unittestX as unittest


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        E_Q = "Q*Q/3."
        S_Q = "1"
        Qmin = 0; Qmax = 10
        absorption_coefficient = scattering_coefficient = 1.
        kernel = mccomponentsbp.create_E_Q_Kernel(
            E_Q, S_Q,
            Qmin, Qmax,
            absorption_coefficient,
            scattering_coefficient,
            )

        ei = 500 # meV
        from mcni.utils import conversion
        vil = conversion.e2v(ei)
        vi = (0,0,vil)

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
            # print E, Q, event
            E1 = eval(E_Q)
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
__id__ = "$Id: TestCase.py 696 2010-11-09 06:23:06Z linjiao $"

# End of file 
