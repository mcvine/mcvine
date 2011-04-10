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


import mcni
import mccomponents.detector as md
import mccomponents.homogeneous_scatterer as mh
import mccomponents.detector.optional_extensions.Detector
from mccomponents.detector.utils import getDetectorHierarchyDimensions, assignLocalGeometers
import numpy as N


import mccomposite.extensions.Copy
import mccomposite.extensions.HollowCylinder


outfilename = 'detector_xml2-events.dat'
nevents = 10000
absorption_weight = 0.9

coordinate_system = 'McStas'
#coordinate_system = 'InstrumentScientist'

class detector_TestCase(unittest.TestCase):

    def test1(self):
        'detector hierarchy from xml'
        from instrument.nixml import parse_file
        instrument = parse_file( 'ARCS.xml' )

        import instrument.geometers as ig
        instrument.geometer.changeRequestCoordinateSystem(
            ig.coordinateSystem( coordinate_system ) )
        
        assignLocalGeometers( instrument, coordinate_system = coordinate_system )
        
        detectorSystem = instrument.getDetectorSystem()

        tofparams = 0, 10e-3, 1e-4
        detectorSystem.tofparams = tofparams
        dims = getDetectorHierarchyDimensions( instrument )
        dims = [ dim for name, dim in dims ]
        mca = md.eventModeMCA(  outfilename, dims )
        detectorSystem.mca = mca
        
        cds = mh.scattererEngine( detectorSystem, coordinate_system = coordinate_system )

        for i in range(nevents):
            if i%1000 == 0: print i
            ev = mcni.neutron( r = (0,0,0), v = (1500,0,2000) )
            cds.scatter(ev)
            continue

        instrument.geometer = instrument.global_geometer
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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
