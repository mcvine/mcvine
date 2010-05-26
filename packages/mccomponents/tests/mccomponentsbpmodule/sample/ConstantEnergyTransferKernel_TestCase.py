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



import unittestX as unittest
import journal

debug = journal.debug( "ConstantEnergyTransferKernel_TestCase" )
warning = journal.warning( "ConstantEnergyTransferKernel_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class ConstantEnergyTransferKernel_TestCase(unittest.TestCase):

    def test(self):
        E=10 #meV
        kernel = mccomponentsbp.ConstantEnergyTransferKernel(E, 1,1)

        ei = 100 # meV
        from mcni.utils import conversion
        vi = conversion.e2v(ei)

        import numpy.linalg as nl
        for i in range(10):
            event = mcni.neutron( r = (0,0,0), v = (0,0,vi), prob = 1, time = 0 )
            kernel.scatter( event );
            vf = event.state.velocity
            vf = nl.norm(vf)
            ef = conversion.v2e(vf)
            self.assertAlmostEqual(ei-ef, E, 3)
            continue

        return
    
    
    pass  # end of ConstantEnergyTransferKernel_TestCase

    
def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
