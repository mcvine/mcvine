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

debug = journal.debug( "Copy_TestCase" )
warning = journal.warning( "Copy_TestCase" )


import mccomposite, mcni
import mccomposite.extensions.Copy as Copy
import UseNeutronPrinter2

class TestCase(unittest.TestCase):

    def test_copy(self):
        '''copy'''
        print "This test creates two identical blocks, each of which "\
              "does not interact with neutrons. They print the info "\
              "about the neutrons passing thru them, however. "\
              "This test then send one neutron through these two "\
              "blocks, so we should see two printings of neutron info, "\
              "differing only on time-of-flight."
        # create a shape
        from mccomposite.geometry import primitives
        smallblock = primitives.block( (1,1,1) )

        #create pure python representation of scatterer composite
        composite1 = mccomposite.composite( smallblock )
        nprinter = UseNeutronPrinter2.NeutronPrinter( smallblock )
        composite1.addElement( nprinter )
        #create a copy
        copy = Copy.Copy( composite1 )
        
        #create a larget composite
        largeblock = primitives.block( (1,1,2) )
        composite = mccomposite.composite( largeblock )
        composite.addElement( composite1, (0,0,-0.5) )
        #composite.addElement( nprinter, (0,0,-0.5) )
        composite.addElement( copy, (0,0,+0.5) )

        #render the c++ representation
        ccomposite = mccomposite.scattererEngine( composite )

        ev = mcni.neutron( r = (0,0,-5), v = (0,0,1) )

        ccomposite.scatter(ev)
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
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
