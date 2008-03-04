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


from mccomponents.detector.bindings import get
bp = get('BoostPython')


class TestCase(unittest.TestCase):

    def test1(self):
        t2c = (tofmin, tofmax, tofstep) = 0, 2.e-3, 100
        t2c = bp.tof2channel( *t2c )

        eventfilename = "events.dat"
        detectorDims = 10, 8 # 10 packs, 8 tubes per pack
        mca = bp.eventmodemca( eventfilename, detectorDims )
        
        pressure = 10
        tubeIndexes = 3, 2
        tubeLength = 1.
        npixels = 128
        axisDirection = 0,0,1
        pixel0position = 0,0,-0.5
        
        he3tubekernel = bp.he3tubekernel(
            pressure, tubeIndexes,
            tubeLength, npixels, axisDirection, pixel0position,
            t2c, mca)

        print dir(he3tubekernel)
        neutron = bp.neutron( r = (-1,0,0), v = (1000,0,0) )

        he3tubekernel.absorb( neutron )
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
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
