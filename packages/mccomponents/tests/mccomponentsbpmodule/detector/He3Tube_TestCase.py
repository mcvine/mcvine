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

debug = journal.debug( "He3Tube_TestCase" )
warning = journal.warning( "He3Tube_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class He3Tube_TestCase(unittest.TestCase):

    def testTof2Channel(self):
        t2c = mccomponentsbp.Tof2Channel(1000, 3000, 1)
        self.assertEqual( t2c( 2000 ), 1000 )
        return
            
    def testZ2Channel(self):
        z_direction = mccompositebp.Vector(0,0,1)
        pixel0 = mccompositebp.Vector(0,0,-0.5)
        z2c = mccomponentsbp.Z2Channel(1., 100, z_direction, pixel0)

        position = mccompositebp.Vector(0,0,0.001)
        self.assertEqual( z2c( position ), 50 )
        return

    def test(self):
        npixels = 100
        detlength = 1. # meter
        tofmin = 1000. ; tofmax = 3000.; tofstep = 1.
        detID = 23
        atm = 1.013e5
        pressure = 10 * atm
        prob = 3.3
        tof = 2000
        
        t2c = mccomponentsbp.Tof2Channel(tofmin, tofmax, tofstep)

        z_direction = mccompositebp.Vector(0,0,1)
        pixel0 = mccompositebp.Vector(0,0,-0.5)
        z2c = mccomponentsbp.Z2Channel(detlength, npixels, z_direction, pixel0)

        datafile = "test.out"
        dims = mccomponentsbp.vector_uint(0)
        dims.append( detID+1 ) # The first dimension is for detectors. must be larger than the largest number of detector IDs.
        dims.append( npixels )
        mca = mccomponentsbp.EventModeMCA( datafile, dims )
        
        tube_channels = mccomponentsbp.vector_int(0)
        tube_channels.append( detID )
        
        tube = mccomponentsbp.He3TubeKernel( pressure, tube_channels, z2c, t2c, mca);

        event = mcni.neutron( r = (0,0,0.001), prob = prob, time = tof )
        tube.absorb( event );

        del tube, mca

        s = open( datafile ).read()
        import struct
        pixelID, tofChannelNo, prob1 = struct.unpack( 'IId', s )
        self.assertEqual( pixelID, detID * npixels + npixels/2 )
        self.assertEqual( tofChannelNo, (tof-tofmin)/tofstep)
        self.assertEqual( prob, prob1 )
        return

            
    pass  # end of He3Tube_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(He3Tube_TestCase)
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
