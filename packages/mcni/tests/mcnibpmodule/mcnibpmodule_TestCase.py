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

debug = journal.debug( "mcnibpmodule_TestCase" )
warning = journal.warning( "mcnibpmodule_TestCase" )


from mcni import mcnibp as binding

class mcnibpmodule_TestCase(unittest.TestCase):

    def testVector3(self):
        v3 = binding.Vector3_double(1,2,3)
        list(v3)
        return
    

    def testNeutronEventBuffer(self):
        n = 100
        events = binding.NeutronEventBuffer( n )
        self.assertEqual( len(events), n )
        list(events)
        return

    def testNeutronCoordsTransform(self):
        n = 100
        events = binding.NeutronEventBuffer( n )
        r = binding.Position_double(1,2,3)
        m = binding.RotationMatrix_double( 0, -1, 0,
                                           1, 0, 0,
                                           0, 0, 1 )
        binding.abs2rel_batch( events, r, m )
        return
        

    pass  # end of mcnibpmodule_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(mcnibpmodule_TestCase)
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
