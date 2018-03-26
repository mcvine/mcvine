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

debug = journal.debug( "geometry_TestCase" )
warning = journal.warning( "geometry_TestCase" )


import mcni, mccomposite.geometry as geometry
primitives = geometry.primitives
operations = geometry.operations


#register new scatterer type
class geometry_TestCase(unittest.TestCase):

    def test(self):
        # create a weird shape
        block = primitives.block( (1,1,1) )
        sphere = primitives.sphere( 1 )
        cylinder = primitives.cylinder( 2,2.001 )
        pyramid = primitives.pyramid( 1., 2, 5 )

        dilated = operations.dilate( sphere, 2 )
        from mcni import units
        meter = units.length.meter
        translated = operations.translate( block, vector=(0*meter,0*meter,0.5*meter) )
        united = operations.unite( dilated, translated )
        deg = units.angle.degree
        rotated = operations.rotate( united, euler_angles=(90*deg,0*deg,0*deg) )

        intersect = operations.intersect( rotated, cylinder )

        difference = operations.subtract( intersect, sphere )

        united2 = operations.unite( difference, pyramid)
        
        print geometry.shapeEngine( united2 )

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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
