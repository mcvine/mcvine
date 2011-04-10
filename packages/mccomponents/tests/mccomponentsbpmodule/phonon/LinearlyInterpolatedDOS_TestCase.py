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

debug = journal.debug( "LinearlyInterpolatedDOS_TestCase" )
warning = journal.warning( "LinearlyInterpolatedDOS_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        vector = mccomponentsbp.vector_double
        Z = vector( 50 )
        area = 0
        for i in range(50):
            Z[i] = i*i
            area += Z[i]
            continue
        dos = mccomponentsbp.LinearlyInterpolatedDOS_dbl(
            0, 1., 50, Z )
        self.assertAlmostEqual( dos( 3 ), 3.**2/area )
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
