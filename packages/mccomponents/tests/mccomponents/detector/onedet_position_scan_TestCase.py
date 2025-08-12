#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

'''one detector tube. tube axis along z. neutron moving along x.
neutron starting position y scan from 0 to r.
making sure all neutrons inside the radius are captured by the tube.
'''

import unittestX as unittest


import mcni, mccomposite, mccomponents.detector as md, \
       mccomposite.geometry.primitives as primitives, \
       mccomponents.homogeneous_scatterer as mh, \
       mccomponents.detector.units as units 

import numpy as N, sys

outfilename = 'onedet_position_scan-events.dat'
nevents = 1000
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
# absorption_weight, scattering_weight, transmission_weight = default_mc_weights_for_detector_scatterer
absorption_weight = 1.
scattering_weight = transmission_weight =0.
assert absorption_weight+scattering_weight+transmission_weight==1.

class detector_TestCase(unittest.TestCase):

    def test1(self):
        'one detector. scan transverse position of neutron'
        ndets = 1
        cylinder = primitives.cylinder( detradius, detlength )
        he3tube = md.he3tube(
            cylinder, id = 0,
            pressure = units.pressure.atm * pressure,
            mcweights = (
            absorption_weight, scattering_weight, transmission_weight)
            )
        mca = md.eventModeMCA( outfilename, (ndets,npixels,) )
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
            y = detradius * i / (nevents-1) * (1+1e-7) 
            # print(y)
            ev = mcni.neutron( r = (-L,y,0), v = (vi,0,0) )
            cds.scatter(ev)
            continue

        return


    def test1a(self):
        'one detector. scan transverse position of neutron. verify'
        from mccomponents.detector.reduction_utils import readevents
        events = readevents( outfilename )
        # print(events)
        self.assertEqual(len(events), nevents-1)
        return

    pass  # end of detector_TestCase


def main():
    unittest.main()

if __name__ == "__main__": main()

# End of file 
