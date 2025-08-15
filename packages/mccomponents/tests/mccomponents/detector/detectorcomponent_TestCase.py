#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                        (C) 2007-2023 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


standalone = True
long_test = True


import unittestX as unittest


import mcni
import mccomponents.detector as md
import numpy as N


def makeTestCase(
        instrumentxml = 'ARCS.xml',
        outfilename = 'detectorcomponent_TestCase-events.dat',
        nevents = 100000,
        absorption_weight = 0.9,
        tofparams = (0, 10e-3, 1e-4),
        coordinate_system = 'McStas',
):
    class TestCase(unittest.TestCase):

        def setUp(self):
            'detector component'
            import mcni
            neutron = mcni.neutron( r = (0,0,0), v = (1500,0,2000), time = 0, prob = 1 )
            from mcni.components.MonochromaticSource import MonochromaticSource
            component1 = MonochromaticSource('source', neutron)
            from mccomponents.detector import detectorcomponent
            component2 = detectorcomponent(
                'detectorsystem', instrumentxml, coordinate_system, tofparams, outfilename )
            instrument = mcni.instrument( [component1, component2] )
            # geometer
            geometer = mcni.geometer()
            geometer.register( component1, (0,0,0), (0,0,0) )
            geometer.register( component2, (0,0,0), (0,0,0) )
            # neutrons
            neutrons = mcni.neutron_buffer( nevents )
            mcni.simulate( instrument, geometer, neutrons )
            return

        def test1a(self):
            s = open(outfilename, 'rb').read()
            import struct
            fmt = 'IId'
            t = struct.unpack( fmt * (len(s) // struct.calcsize( fmt )) , s )
            #print t
            n = len(t)//len(fmt)
            print("number of cases where absorption happen: ", n)
            self.assertLessThan(abs(n-(nevents*absorption_weight)), 3*N.sqrt(n))

            t = N.array(t)
            t.shape = n, 3
            p = t[:, 2].sum()
            print("absorbed total neutron weight: ", p)
            self.assertTrue( p>nevents*0.9 and p<nevents )
            return

        def assertLessThan(self, left, right):
            if left >= right:
                raise AssertionError("%s is not smaller than %s" % (left, right))

        pass  # end of TestCase

    return TestCase


def pysuite():
    TestCase1 = makeTestCase()
    TestCase2 = makeTestCase(
        instrumentxml = 'ARCS-0.5_abs.xml',
        outfilename = 'detectorcomponent_TestCase-0.5_abs-events.dat',
        absorption_weight = 0.5,
    )
    suite1 = unittest.makeSuite(TestCase1)
    suite2 = unittest.makeSuite(TestCase2)
    return unittest.TestSuite( (suite1, suite2) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

if __name__ == "__main__": main()

# End of file
