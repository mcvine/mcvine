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


standalone = True

import unittestX as unittest
import journal

debug = journal.debug( "HollowCylinder_TestCase" )
warning = journal.warning( "HollowCylinder_TestCase" )


import mccomposite, mcni
import mccomposite.extensions.HollowCylinder as HollowCylinder

class TestCase(unittest.TestCase):

    def test(self):
        '''HollowCylinder'''
        print "This test creates a hollow cylinder."\
              "It does not interact with neutrons. It prints the info "\
              "about the neutrons passing thru them, however. "\
              "This test then send one neutron through this hollow cylinder, "\
              "and we should see two printings of neutron info, "\
              "differing only on time-of-flight."
        # create a shape
        shape = HollowCylinder.HollowCylinder( 1, 1.2, 1 )
        import UseNeutronPrinter2
        nprinter = UseNeutronPrinter2.NeutronPrinter( shape )

        #render the c++ representation
        cinstance = mccomposite.scattererEngine( nprinter )

        ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )

        cinstance.scatter(ev)
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
    #journal.debug("mccomposite.ScattererComputationEngineRenderer").activate()
    #journal.debug("mccomposite.Geometer").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
