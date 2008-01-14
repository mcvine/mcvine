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

debug = journal.debug( "hsxml_TestCase" )
warning = journal.warning( "hsxml_TestCase" )


class hsxml_TestCase(unittest.TestCase):

    def test(self):
        from mccomponents.homogeneous_scatterer.hsxml import parse_file
        hs = parse_file( 'Ni-scatterer.xml' )
        print hs
        return
    
    def test1(self):
        from mccomponents.homogeneous_scatterer.hsxml import parse_file
        hs = parse_file( 'Ni1-scatterer.xml' )
        shape = hs.shape()
        self.assertEqual( shape.__class__.__name__, 'Sphere' )

        from mccomponents.homogeneous_scatterer.Kernel import Kernel
        self.assert_( isinstance( hs.kernel(), Kernel) )
        return
    
    pass  # end of hsxml_TestCase



def pysuite():
    suite1 = unittest.makeSuite(hsxml_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("mccomposite.geometry.ArrowIntersector").activate()
    #journal.debug("mccomposite.geometry.Locator").activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
