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


class TestCase(unittest.TestCase):


    def test(self):
        from mccomponents.sample.phonon.register_NdArray import ndarray_bp
        import numpy as N
        a = N.arange(12, dtype = N.double)
        a.shape = 3,4
        a1 = ndarray_bp( a )
        assert a1.origin is a
        self.assertEqual( a[2,1], 9 )
        self.assertEqual( a1[ 2,1 ], 9 )
        return
    

    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    journal.debug('wrap_native_ptr').activate()
    journal.debug('NdArray').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
