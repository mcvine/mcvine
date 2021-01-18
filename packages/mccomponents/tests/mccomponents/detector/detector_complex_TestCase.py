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


long_test = True

import unittestX as unittest
import journal

debug = journal.debug( "detector_TestCase" )
warning = journal.warning( "detector_TestCase" )


import mcni, mccomposite, mccomponents.detector as md, \
       mccomposite.geometry.primitives as primitives,\
       mccomposite.geometry.operations as operations,\
       mccomponents.homogeneous_scatterer as mh, \
       mccomponents.detector.units as units 

import numpy as N, math

meter = units.length.meter

outfilename = 'detector_complex-events.dat'
nevents = 10000
npixelsperdet = 100
ndetsperpack = 7
npacks = 30
detradius = 0.0125 * meter
detlength = 1 * meter
detpressure = 10. * units.pressure.atm

L1 = 5. #distance from source to sample
vi =3000. # velocity of neutrons
L2 = 4. #distance from sample to detectors
sample2det = L2 * meter
L = L1 + L2

packindexat0 = 2 # index of the detector pack for which scattering angle=0

tofparams = tmin, tmax, tstep = 0, 10e-3, 1e-4

absorption_weight = 0.9
scattering_weight = 0
transmission_weight = 0.1
assert absorption_weight+scattering_weight+transmission_weight==1.


def makepack( ):
    pack = md.pack(
        primitives.block(
        (detradius*2, detradius*2*ndetsperpack, detlength)
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
        y = -(ndetsperpack-1.)/2*2*detradius + i*2*detradius
        pack.addElement( tubes[i], (0*meter, y, 0*meter) )
        continue
    return pack


class detector_TestCase(unittest.TestCase):

    def test1(self):
        'complex. pack, detector, pixel hierarchy'
        
        mca = md.eventModeMCA(
            outfilename,
            (npacks, ndetsperpack, npixelsperdet,) )
        cylinder = operations.subtract( primitives.cylinder( sample2det * 1.1, detlength ),
                                        primitives.cylinder( sample2det * 0.9, detlength ) )
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
            ds.addElement( packs[i], (x,y,z) )
            continue

        cds = mh.scattererEngine( ds, coordinate_system = "InstrumentScientist" )

        for i in range(nevents):
            if i%1000 == 0: print(i)
            ev = mcni.neutron( r = (-L1,0,0), v = (vi,0,0) )
            cds.scatter(ev)
            continue

        return


    def test1a(self):
        from mccomponents.detector.reduction_utils import readevents
        events = readevents( outfilename )
        n = len(events)
        print("number of cases where absorption happen: ", n)
        self.assertTrue( abs(n-(nevents*absorption_weight)) < 3*N.sqrt(n) )

        p = sum([ e[2] for e in events ] )
        print("absorbed neutrons: ", p)
        self.assertTrue( abs( p-(nevents*0.91) ) < 3*N.sqrt(p) )

        t = L/vi
        tchannel = int( (t-tmin)/tstep )
        for e in events:
            # should hit center of tube
            self.assertTrue( abs(e[0] - (npixelsperdet*((packindexat0+0.5)*ndetsperpack)) ) <= 1 )
            # tof channel
            self.assertTrue( abs(e[1] - tchannel) <= 1 )
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
    main()
    
# version
__id__ = "$Id$"

# End of file 
