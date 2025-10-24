#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from unittest import *

from unittest import TestCase as TCBase

class TestCase(TCBase):

    def assertVectorEqual(self, v1, v2):
        self.assertEqual(len(v1), len(v2))
        for x1, x2 in zip(v1, v2): self.assertEqual(x1, x2)
        return

            
    def assertVectorAlmostEqual(self, v1, v2, places=7):
        self.assertEqual(len(v1), len(v2))
        for x1, x2 in zip(v1, v2): self.assertAlmostEqual(x1, x2, places=places)
        return
            
    def assertMatrixEqual(self, m1, m2):
        self.assertEqual(len(m1), len(m2))
        for x1, x2 in zip(m1, m2): self.assertVectorEqual(x1, x2)
        return
            
    def assertMatrixAlmostEqual(self, m1, m2, places=7):
        self.assertEqual(len(m1), len(m2))
        for x1, x2 in zip(m1, m2): self.assertVectorAlmostEqual(x1, x2, places=places)
        return

    pass # end of TestCaae

# version
__id__ = "$Id: unittestX.py 1330 2007-10-18 00:32:44Z linjiao $"

# End of file 
