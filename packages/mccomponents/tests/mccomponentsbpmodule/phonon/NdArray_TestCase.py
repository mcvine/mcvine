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

debug = journal.debug( "NdArray_TestCase" )
warning = journal.warning( "NdArray_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        import numpyext
        import numpy
        a = numpy.arange(12, dtype = numpy.double)
        a.shape = 3,4
        ptr = numpyext.getdataptr( a )
        
        import bpext
        wp = bpext.wrap_native_ptr( ptr )
        
        shape = mccomponentsbp.vector_uint( 0 )
        for i in a.shape: shape.append( i )
        a1 = mccomponentsbp.new_NdArray_dblarr_2( wp, shape )
        a1.origin = a

        indexes = mccomponentsbp.vector_uint( 0 )
        indexes.append( 2 ); indexes.append( 1 )
        self.assertEqual( a1[ indexes ], 9 )
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
