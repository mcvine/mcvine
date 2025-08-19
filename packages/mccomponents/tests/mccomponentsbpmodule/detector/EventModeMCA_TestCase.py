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

class EventModeMCA_TestCase(unittest.TestCase):

    def test(self):
        dims = mccomponentsbp.vector_uint( 0 )
        dims.append( 100 )
        mca = mccomponentsbp.EventModeMCA( "test.out", dims )
        return
            
    pass  # end of EventModeMCA_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(EventModeMCA_TestCase)
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
