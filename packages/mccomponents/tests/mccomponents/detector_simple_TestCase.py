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
       mccomposite.geometry.primitives as primitives, \
       mccomponents.homogeneous_scatterer as mh, \
       mccomponents.detector.units as units 

import numpy as N

nevents = 10000
npixels = 100
detradius = 0.0125
detlength = 1

absorption_weight = 0.9
scattering_weight = 0
transmission_weight = 0.1
assert absorption_weight+scattering_weight+transmission_weight==1.

class detector_TestCase(unittest.TestCase):

    def test1(self):
        'simple. one detector'
        ndets = 1
        
        cylinder = primitives.cylinder( detradius, detlength )
        he3tube = md.he3tube(
            cylinder, id = 0,
            pressure = units.pressure.atm * 10,
            mcweights_absorption_scattering_transmission = (
            absorption_weight, scattering_weight, transmission_weight)
            )
        tofparams = 0, 10e-3, 1e-4
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
            if i%1000 == 0: print i
            ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
            cds.scatter(ev)
            continue

        return


    def test1a(self):
        s = open('events.dat').read()
        import struct
        fmt = 'IId'
        t = struct.unpack( fmt * (len(s) / struct.calcsize( fmt )) , s )
        n = len(t)/len(fmt)
        self.assert_( abs(n-(nevents*absorption_weight)) < 3*N.sqrt(n) )

        t = N.array(t)
        t.shape = n, 3
        p = t[:, 2].sum()
        self.assert_( abs( p-(nevents*0.908484) ) < 3*N.sqrt(p) )
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
