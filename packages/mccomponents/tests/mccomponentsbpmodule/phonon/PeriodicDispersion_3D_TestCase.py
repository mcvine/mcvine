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

debug = journal.debug( "PeriodicDispersion_3D_TestCase" )
warning = journal.warning( "PeriodicDispersion_3D_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        from LinearlyInterpolatedDispersion_Example import example
        dispersion = example()

        Q = mcnibp.Vector3_double
        
        b1 = Q( 2,0,0 )
        b2 = Q( 0,3,0 )
        b3 = Q( 0,0,4 )
        rc = mccomponentsbp.ReciprocalCell( )
        rc.b1 = b1; rc.b2 = b2; rc.b3 = b3
        disp = mccomponentsbp.PeriodicDispersion_3D( dispersion, rc )
        self.assertAlmostEqual( disp.energy(0, Q(2,3,4)), disp.energy(0, Q(0,0,0) ) )
        return

    pass  # end of TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
