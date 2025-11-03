from __future__ import print_function

#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

USE_PYRE = 0

import unittestX as unittest
from unittest import TestCase
import bpext


import logging
logger = logging.getLogger("MCVine")

class bpext_TestCase(TestCase):

    def test1(self):
        "bpext bpext"
        from bpext import _examplebpbinding as example
        v = example.vec_d(5)
        v[:] = 0, 1, 0, 3, 0
        p = bpext.extract_ptr(v, 'vec_double')
        v1 = bpext.wrap_ptr(p, 'vec_double')
        v1[3] = 88
        self.assertAlmostEqual(v[3], v1[3])
        self.assertAlmostEqual(v[3], 88)
        return

    def test2(self):
        "bpext: double array"

        logger.debug('wrap_native_ptr')
        logger.debug('extract_native_ptr')
        
        from bpext import _bpext as binding
        arr = binding.newdblarr(10)
        print(arr)

        wrapped_ptr_bpobj = binding.wrap_native_ptr(arr)

        print(wrapped_ptr_bpobj)

        extracted = binding.extract_native_ptr(wrapped_ptr_bpobj)
        print(extracted)
        return
    
    pass # end of bpext_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(bpext_TestCase)
    return unittest.TestSuite((suite1,))

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite((pytests,))
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: bpext_TestCase.py 834 2006-03-03 14:39:02Z linjiao $"

# End of file 
