#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
Test neutron and neutron buffer interfaces
"""


from mcni.utils import conversion

import unittestX as unittest
class TestCase(unittest.TestCase):


    def test1(self):
        "conversion: e2v"
        e = 100
        v = conversion.e2v(e)
        self.assertAlmostEqual(v, 4373.9331, 3)
        
        e1 = conversion.v2e(v)
        self.assertAlmostEqual(e1, e, 3)
        return
    
        
    pass  # end of TestCase


    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id: mcni_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
