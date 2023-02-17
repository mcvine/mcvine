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


interactive = False

import unittestX as unittest
import journal

debug = journal.debug( "detector_TestCase" )
warning = journal.warning( "detector_TestCase" )


import mcni, mccomposite, mccomponents.detector as md, \
       mccomposite.geometry.primitives as primitives, \
       mccomponents.homogeneous_scatterer as mh, \
       mccomponents.detector.units as units 

import numpy as N, sys

nevents = 100000
npixels = 100
detradius = 0.0125
detlength = 1
pressure = 10.

L = 5. #distance from source to detector
vi =3000. # velocity of neutrons

tofparams = tmin, tmax, tstep = 0, 10e-3, 1e-4

# absorption probability
from mccomponents.detector import he3_transmission_percentage
from mcni.utils import conversion
absorption_probability = 1-he3_transmission_percentage(conversion.v2e(vi), pressure, 2*detradius*100)


# monte carlo weights
from mccomponents.detector import default_mc_weights_for_detector_scatterer
absorption_weight, scattering_weight, transmission_weight = default_mc_weights_for_detector_scatterer
assert absorption_weight+scattering_weight+transmission_weight==1.

class detector_TestCase(unittest.TestCase):

    def test1(self):
        'simple. one detector'
        ndets = 1
        
        cylinder = primitives.cylinder( detradius, detlength )
        he3tube = md.he3tube(
            cylinder, id = 0,
            pressure = units.pressure.atm * pressure,
            mcweights = (
            absorption_weight, scattering_weight, transmission_weight)
            )
        mca = md.eventModeMCA( 'events.dat', (ndets,npixels,) )
        ds = md.detectorSystem( cylinder, tofparams, mca )

        m = units.length.meter
        
        for i in range(npixels):
            pixel = md.pixel( id = i )
            he3tube.addElement(
                pixel,
                N.array( [0,0,(-0.495+i*0.01)] ) * m,
                (0,0,0) )
            continue
        ds.addElement( he3tube )

        cds = mh.scattererEngine( ds, coordinate_system = "InstrumentScientist" )

        for i in range(nevents):
            if i%1000 == 0 and interactive: 
                # print i
                print('.', end=' ')
                sys.stdout.flush()
            ev = mcni.neutron( r = (-L,0,0), v = (vi,0,0) )
            cds.scatter(ev)
            continue

        return


    def test1a(self):
        "simple. one detector -- verify"
        from mccomponents.detector.reduction_utils import readevents
        events = readevents( 'events.dat' )
        n = len(events)
        self.assertTrue( abs(n-(nevents*absorption_weight)) < 3*N.sqrt(n) )

        p = sum([ e[2] for e in events ] )
        # print "%s should be almost equalt to %s" % (p, nevents*absorption_probability)
        self.assertTrue( abs( p-(nevents*absorption_probability) ) < 3*N.sqrt(p) )
        # self.assert_( abs( p-(nevents*0.908484) ) < 3*N.sqrt(p) )

        t = L/vi
        tchannel = int( (t-tmin)/tstep )
        for e in events:
            # should hit center of tube
            self.assertTrue( abs(e[0] - (npixels/2)) <= 1 )
            self.assertEqual( e[1], tchannel )
            # 
            continue
        return

    pass  # end of detector_TestCase



def pysuite():
    suite1 = unittest.makeSuite(detector_TestCase)
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
    interactive = True
    main()

# End of file
