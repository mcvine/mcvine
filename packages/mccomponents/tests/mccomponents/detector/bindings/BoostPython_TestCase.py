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
binding = get('BoostPython')


npacks = 10
ntubes = 8
npixels = 100
eventfilename = "events.dat"

packID = 3
tubeID = 2

tofmin, tofmax, tofstep = 0, 2.e-3, 10e-6
pressure = 10
tubeLength = 1.
axisDirection = 0,0,1
pixel0position = 0,0,-0.5
neutronT = 1e-3 * (1+0.001)
pixelID = 33
neutronPosition = 0,0, -0.5 + 0.01*(pixelID+0.001)
prob = 1.222

class TestCase(unittest.TestCase):

    def test1(self):
        t2c = binding.tof2channel( tofmin, tofmax, tofstep )

        detectorDims = npacks, ntubes, npixels
        mca = binding.eventmodemca( eventfilename, detectorDims )
        
        tubeIndexes = packID, tubeID
        
        he3tubekernel = binding.he3tubekernel(
            pressure, tubeIndexes,
            tubeLength, npixels, axisDirection, pixel0position,
            t2c, mca)

        print dir(he3tubekernel)
        neutron = binding.neutron( r = neutronPosition, time = neutronT, prob = prob )

        he3tubekernel.absorb( neutron )
        return


    def test2(self):
        "read events and check them"
        from mccomponents.detector.reduction_utils import readevents
        evts = readevents( eventfilename )
        self.assertEqual( len(evts), 1 )
        evt = evts[0]
        longpixelID, tofchannel, probability = evt
        self.assertEqual( longpixelID, pixelID + npixels * (tubeID + ntubes*(packID)) )
        self.assertEqual( tofchannel, int( (neutronT-tofmin)/tofstep ) )
        self.assertEqual( probability, prob )
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
