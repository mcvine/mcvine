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



import unittestX as unittest
import journal

debug = journal.debug( "CoherentInelastic_PolyXtal_kernel_TestCase" )
warning = journal.warning( "CoherentInelastic_PolyXtal_kernel_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        from LinearlyInterpolatedDispersion_Example import example
        disp = example()

        from DWFromDOS_Example import example
        dw_calctor = example()

        atoms = mccomponentsbp.vector_AtomicScatterer(5)

        unitcell_vol = 30
        temperature = 300
        Ei = 70
        max_omega = 55
        max_Q = 12
        nMCsteps_to_calc_RARV = 10000

        kernel = mccomponentsbp.Phonon_CoherentInelastic_PolyXtal_kernel(
            disp, atoms,
            unitcell_vol,
            dw_calctor,
            temperature,
            Ei,  max_omega, 
            max_Q,
            nMCsteps_to_calc_RARV,
            )
            
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
