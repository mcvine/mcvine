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
npixelsperdet = 128
ndetsperpack = 8
npacks = 30
detradius = 0.0125 * meter
detlength = 1 * meter
detpressure = 10. * units.pressure.atm

sample2det = 4 * meter

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
        mcweights_absorption_scattering_transmission = (
        absorption_weight, scattering_weight, transmission_weight)
        )
    tubes = [he3tube0]
    for i in range(1,ndetsperpack):
        tubes.append( mccomposite.scatterercopy( he3tube0, id = i) )
        continue

    for i in range(ndetsperpack):
        y = -(ndetsperpack-1)/2*2*detradius + i*2*detradius
        pack.addElement( tubes[i], (0*meter, y, 0*meter) )
        continue
    return pack


class detector_TestCase(unittest.TestCase):

    def test1(self):
        'complex. pack, detector, pixel hierarchy'
        
        tofparams = 0, 10e-3, 1e-4
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
            angle = i* 5./180 * N.pi
            x = sample2det * math.cos(angle)
            y = sample2det * math.sin(angle)
            ds.addElement( packs[i], (x,y,z) )
            continue

        cds = mh.scattererEngine( ds )

        for i in range(nevents):
            if i%1000 == 0: print i
            ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
            cds.scatter(ev)
            continue

        return


    def test1a(self):
        s = open(outfilename).read()
        import struct
        fmt = 'IId'
        t = struct.unpack( fmt * (len(s) / struct.calcsize( fmt )) , s )
        #print t
        n = len(t)/len(fmt)
        print "number of cases where absorption happen: ", n
        self.assert_( abs(n-(nevents*absorption_weight)) < 3*N.sqrt(n) )

        t = N.array(t)
        t.shape = n, 3
        p = t[:, 2].sum()
        print "absorbed neutrons: ", p
        self.assert_( p>nevents*0.9 and p<nevents )
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
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
