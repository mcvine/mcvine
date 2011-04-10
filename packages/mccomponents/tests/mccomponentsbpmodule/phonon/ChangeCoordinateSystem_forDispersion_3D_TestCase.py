#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest
import journal

debug = journal.debug( "ChangeCoordinateSystem_forDispersion_3D_TestCase" )
warning = journal.warning( "ChangeCoordinateSystem_forDispersion_3D_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        from LinearlyInterpolatedDispersion_Example import example
        dispersion = example()

        M = mcnibp.Matrix3_double
        Q = mcnibp.Vector3_double
        m = M( 1,2,0,
               2,0,3,
               3,1,0)
        
        disp = mccomponentsbp.ChangeCoordinateSystem_forDispersion_3D( dispersion, m )
        
        self.assertAlmostEqual( disp.energy(0, Q(1,0,0)), disp.energy(0, Q(1,2,3) ) )
        self.assertAlmostEqual( disp.energy(0, Q(0,1,0)), disp.energy(0, Q(2,0,1) ) )
        self.assertAlmostEqual( disp.energy(0, Q(0,0,1)), disp.energy(0, Q(0,3,0) ) )
        
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
