#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

"""
Two row detector pack.
There was a bug that prevents mcvine from couting the events
passing through the first tube and absorbed by the second tube
when there are more than two tubes in the pack.
This test check that bug.
"""

long_test = False

import os, numpy as np
import unittestX as unittest

import mcni, mccomposite, mccomponents.detector as md, \
       mccomposite.geometry.primitives as primitives,\
       mccomposite.geometry.operations as operations,\
       mccomponents.homogeneous_scatterer as mh, \
       mccomponents.detector.units as units 

import numpy as N, math
meter = units.length.meter

outfilename = 'tworows-events.dat'
nevents = 1
npixelsperdet = 10
npacks = 1
detradius = 0.0125 * meter
detgap = 0.0001 * meter
detlength = 1 * meter
detpressure = 10. * units.pressure.atm

L1 = 5. #distance from source to sample
vi =3000. # velocity of neutrons
L2 = 4. #distance from sample to detectors
sample2det = L2 * meter
L = L1 + L2

packindexat0 = 0 # index of the detector pack for which scattering angle=0

tofparams = tmin, tmax, tstep = 0, 10e-3, 1e-4

absorption_weight = 1.
scattering_weight = 0.
transmission_weight = 0.
assert absorption_weight+scattering_weight+transmission_weight==1.

tube_positions = [
    (0, -0.0735, 0.),
    (0.021, -0.0525,  0.),
    (0, -0.0315,  0.),
    (0.021, -0.0105,  0.),
    (0, 0.0105,  0.),
    (0.021, 0.0315,  0.),
    (0, 0.0525,  0.),
    (0.021, 0.0735,  0.)
]
ndetsperpack = len(tube_positions)

def makepack( ):
    pack = md.pack(
        primitives.block(
        (detradius*2, detradius*2*ndetsperpack + detgap*(ndetsperpack-1), detlength)
        )
    )
    he3tube0 = md.he3tube_withpixels(
        radius = detradius,
        height = detlength,
        npixels = npixelsperdet, direction = 'z',
        id = 0, pressure = detpressure,
        mcweights = (
            absorption_weight, scattering_weight, transmission_weight)
    )
    tubes = [he3tube0]
    for i in range(1,ndetsperpack):
        tubes.append( mccomposite.scatterercopy( he3tube0, id = i) )
        continue

    for i in range(ndetsperpack):
        x,y,z = tube_positions[i]
        pack.addElement( tubes[i], (x*meter, y*meter, z*meter) )
        continue
    return pack


class detector_TestCase(unittest.TestCase):

    def test1(self):
        mca = md.eventModeMCA(
            outfilename,
            (npacks, ndetsperpack, npixelsperdet,) )
        cylinder = operations.subtract(
            primitives.cylinder( sample2det * 1.1, detlength ),
            primitives.cylinder( sample2det * 0.9, detlength )
        )
        ds = md.detectorSystem( cylinder, tofparams, mca )

        pack0 = makepack()
        packs = [pack0]
        for i in range(1, npacks):
            packs.append( mccomposite.scatterercopy( pack0, id = i ) )
            continue

        for i in range( npacks ):
            z = 0 * meter
            angle = (i-packindexat0)* 5./180 * N.pi
            x = sample2det * math.cos(angle)
            y = sample2det * math.sin(angle)
            # print(x,y,z)
            ds.addElement( packs[i], (x,y,z), (0,0,0) )
            continue

        cds = mh.scattererEngine( ds, coordinate_system = "InstrumentScientist" )

        for i in range(nevents):
            # ev = mcni.neutron( r = (-L1,0,0), v = (vi,0,0) )
            ev = mcni.neutron( r = (L2+0.00678233,0,0), v = (vi,0,0) )
            cds.scatter(ev)
            continue

        return

    def test1a(self):
        from mccomponents.detector.reduction_utils import readevents
        events = readevents( outfilename )
        self.assertEqual(len(events), 1)
        self.assertEqual(events['pixelID'][0], 35)
        return

    pass  # end of detector_TestCase

def check_counts(n, expected):
    assert abs(n-expected) < 3 * np.sqrt(expected)


def main():
    unittest.main()

if __name__ == "__main__": main()

# End of file 
