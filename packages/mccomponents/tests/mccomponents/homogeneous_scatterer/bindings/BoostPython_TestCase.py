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

debug = journal.debug( "BoostPython_TestCase" )
warning = journal.warning( "BoostPython_TestCase" )


class TestCase(unittest.TestCase):

    def test(self):
        'mccomponents.homogeneous_scatterer: Boost python binding'
        from mccomponents.homogeneous_scatterer.bindings import get
        bp = get('BoostPython')
        
        kernels = bp.kernelcontainer( )
        average = False
        ck = bp.compositekernel( kernels, average )

        cylinder = bp.cylinder( 0.02, 0.1 )

        #this scatterer does not really have a kernel
        hs = bp.homogeneousscatterer( cylinder, ck, (0,1,0) )
        return
    
    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("mccomposite.geometry.ArrowIntersector").activate()
    #journal.debug("mccomposite.geometry.Locator").activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
