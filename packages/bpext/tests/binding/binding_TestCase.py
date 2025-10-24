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


import unittest
from bpext import _bpext as binding
from bpext import _examplebpbinding as example

import unittestX as unittest
from unittest import TestCase
class binding_TestCase(TestCase):

    def test1(self):
        "bpext binding"
        v = example.vec_d(5)
        v[:] = 0, 1, 0, 3, 0
        p = binding.extract_ptr(v, 'vec_double')
        v1 = binding.wrap_ptr(p, 'vec_double')
        v1[3] = 88
        self.assertAlmostEqual(v[3], v1[3])
        self.assertAlmostEqual(v[3], 88)
        return
    
    def test2(self):
        "bpext binding"
        v = example.new_vec_d(5)
        v[:] = 0, 1, 0, 3, 0
        p = binding.extract_ptr(v, 'vec_double')
        v1 = binding.wrap_ptr(p, 'vec_double')
        v1[3] = 88
        self.assertAlmostEqual(v[3], v1[3])
        self.assertAlmostEqual(v[3], 88)
        return
    
    pass # end of binding_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(binding_TestCase)
    return unittest.TestSuite((suite1,))

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite((pytests,))
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: binding_TestCase.py 834 2006-03-03 14:39:02Z linjiao $"

# End of file 
