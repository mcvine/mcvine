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

debug = journal.debug( "geometry_TestCase" )
warning = journal.warning( "geometry_TestCase" )


import mccomposite.geometry as geometry, mcni
primitives = geometry.primitives
operations = geometry.operations


#register new scatterer type
class geometry_TestCase(unittest.TestCase):

    def test(self):
        # create a weird shape
        block = primitives.block( (1,1,1) )
        sphere = primitives.sphere( 1 )
        cylinder = primitives.cylinder( 2,2.001 )

        dilated = operations.dilate( sphere, 2 )
        translated = operations.translate( block, (0,0,0.5) )
        united = operations.unite( dilated, translated )

        rotated = operations.rotate( united, (90,0,0) )

        intersect = operations.intersect( rotated, cylinder )

        difference = operations.subtract( intersect, sphere )
        
        print geometry.shapeEngine( difference )

        return


    def test_locate(self):
        c = primitives.cylinder(1,1)

        assert geometry.locate( (0,0,0), c ) == "inside"
        return


    pass  # end of geometry_TestCase



def pysuite():
    suite1 = unittest.makeSuite(geometry_TestCase)
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
