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

debug = journal.debug( "detectorcomponent_TestCase" )
warning = journal.warning( "detectorcomponent_TestCase" )


import mcni
import mccomponents.detector as md
import numpy as N

instrumentxml = 'ARCS.xml'
outfilename = 'detectorcomponent_TestCase-events.dat'
nevents = 10000
absorption_weight = 0.9
tofparams = 0, 10e-3, 1e-4
coordinate_system = 'McStas'

class TestCase(unittest.TestCase):

    def test1(self):
        'detector component'
        import mcni
        neutron = mcni.neutron( r = (0,0,0), v = (1500,0,2000), time = 0, prob = 1 )
        from mcni.components.MonochromaticSource import MonochromaticSource
        component1 = MonochromaticSource('source', neutron)
        from mccomponents.detector import detectorcomponent
        component2 = detectorcomponent(
            'detectorsystem', instrumentxml, coordinate_system, tofparams, outfilename )
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,0), (0,0,0) )

        neutrons = mcni.neutron_buffer( nevents )

        mcni.simulate( instrument, geometer, neutrons )
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
