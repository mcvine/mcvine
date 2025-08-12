#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

"""two detector tubes. let neutron go through the line connecting the centers
of the two detectors. Make sure mcvine simulate absorption by both tubes.
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

outfilename = 'twodets-events.dat'
nevents = 10000
npixelsperdet = 10
ndetsperpack = 2
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

absorption_weight = 0.5
scattering_weight = 0
transmission_weight = 0.5
assert absorption_weight+scattering_weight+transmission_weight==1.


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
        y = -(ndetsperpack-1.)/2*(2*detradius+detgap) + i*(2*detradius+detgap)
        # print(y)
        pack.addElement( tubes[i], (0*meter, y, 0*meter) )
        continue
    return pack


class detector_TestCase(unittest.TestCase):

    def test1(self):
        'two detectors. neutron going through centers of both dets'
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
            ds.addElement( packs[i], (x,y,z), (0,0,90) )
            continue

        cds = mh.scattererEngine( ds, coordinate_system = "InstrumentScientist" )

        for i in range(nevents):
            ev = mcni.neutron( r = (-L1,0,0), v = (vi,0,0) )
            cds.scatter(ev)
            continue

        return

    def test1a(self):
        'two detectors. neutron going through centers of both dets -- verify'
        from mccomponents.detector.reduction_utils import readevents
        events = readevents( outfilename )
        n = len(events)
        n_expected = nevents*(absorption_weight+transmission_weight*absorption_weight)
        check_counts(n, n_expected)
        # front detector
        n_pix15 = len(events[events['pixelID']==15])
        check_counts(n_pix15, nevents*absorption_weight)
        # back detector
        n_pix5 = len(events[events['pixelID']==5])
        check_counts(n_pix5, nevents*absorption_weight*transmission_weight)
        return

    pass  # end of detector_TestCase

def check_counts(n, expected):
    assert abs(n-expected) < 3 * np.sqrt(expected)


def main():
    unittest.main()

if __name__ == "__main__": main()

# End of file 
