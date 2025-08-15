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

class mcni_TestCase(unittest.TestCase):


    def test(self):
        from mcni.units import parser, mass
        parser = parser()
        self.assertAlmostEqual(parser.parse('u')/mass.kg, 1.66054e-27)
        return
    
        
    pass  # end of mcni_TestCase



def pysuite():
    suite1 = unittest.makeSuite(mcni_TestCase)
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
