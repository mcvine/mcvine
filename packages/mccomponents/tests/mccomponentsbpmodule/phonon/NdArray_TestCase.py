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


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

import numpy
try:
    from danse.ins import numpyext
except ImportError:
    import numpyext
    import warnings
    warnings.warn("Using old numpyext. Should use danse.ins.numpyext")
import bpext


class TestCase(unittest.TestCase):

    def test(self):
        a = numpy.arange(12, dtype = numpy.double)
        a.shape = 3,4
        ptr = numpyext.getdataptr( a )
        
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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
