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

debug = journal.debug( "mccompositebpmodule_TestCase" )
warning = journal.warning( "mccompositebpmodule_TestCase" )


from mccomposite import mccompositebp as binding

class mccompositebpmodule_TestCase(unittest.TestCase):

    def testGeometer(self):
        geometer = binding.Geometer_NeutronScatterer( );
        return
        

    pass  # end of mccompositebpmodule_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(mccompositebpmodule_TestCase)
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
