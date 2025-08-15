#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'MonochromaticSource'
        
        # source component
        from mcni.components.MonochromaticSource import MonochromaticSource
        from mcni import neutron_buffer, neutron
        neutron0 = neutron(v=(0,0,1000))
        s = MonochromaticSource("name", neutron0)
        
        # neutron buffer
        N = 100
        b = neutron_buffer(N)
        
        # process
        s.process(b)

        #
        for n in b:
            self.assertEqual(
                tuple(n.state.position),
                tuple(neutron0.state.position),
                )
            self.assertEqual(
                tuple(n.state.velocity),
                tuple(neutron0.state.velocity),
                )
            self.assertEqual(
                n.time,
                neutron0.time,
                )
            self.assertEqual(
                n.probability,
                neutron0.probability,
                )

        return
        

    def test2(self):
        'MonochromaticSource - x-y spread'
        
        # source component
        from mcni.components.MonochromaticSource import MonochromaticSource
        from mcni import neutron_buffer, neutron
        neutron0 = neutron(v=(0,0,1000), r=(0.3, 0.4, 1.5))
        dx=0.1; dy=0.8
        s = MonochromaticSource("name", neutron0, dx=dx, dy=dy)
        
        # neutron buffer
        N = 10
        b = neutron_buffer(N)
        
        # process
        s.process(b)

        #
        for n in b:

            # print n
            r = n.state.position
            # not always true but usually true
            r0 = neutron0.state.position
            self.assertTrue(r[0]!=r0[0])
            self.assertTrue(r[1]!=r0[1])
            # always true
            self.assertTrue(abs(r[0]-r0[0])<=dx/2)
            self.assertTrue(abs(r[1]-r0[1])<=dy/2)
            self.assertTrue(abs(r[2])==r0[2])

            self.assertEqual(
                tuple(n.state.velocity),
                tuple(neutron0.state.velocity),
                )
            self.assertEqual(
                tuple(n.state.velocity),
                tuple(neutron0.state.velocity),
                )
            self.assertEqual(
                n.time,
                neutron0.time,
                )
            self.assertEqual(
                n.probability,
                neutron0.probability,
                )

        return
        

    def test3(self):
        'MonochromaticSource - energy spread'
        
        # source component
        from mcni.components.MonochromaticSource import MonochromaticSource
        from mcni import neutron_buffer, neutron
        neutron0 = neutron(v=(0,0,3000), r=(0.3, 0.4, 1.5))
        dx=0.1; dy=0.8; dE = 5
        s = MonochromaticSource("name", neutron0, dx=0, dy=0, dE=dE)
        
        # neutron buffer
        N = 100000
        b = neutron_buffer(N)
        
        # process
        s.process(b)

        #
        E0 = neutron0.energy()
        #
        n_in_onesigma = 0
        n_in_twosigma = 1
        for n in b:

            E = n.energy()
            # print n
            # print E, E0
            # not always true but usually true
            self.assertNotEqual(E, E0)

            #
            if abs(E-E0) < dE:
                n_in_onesigma += 1
            if abs(E-E0) < 2*dE:
                n_in_twosigma += 1

            self.assertEqual(
                tuple(n.state.position),
                tuple(neutron0.state.position),
                )
            self.assertEqual(
                n.time,
                neutron0.time,
                )
            self.assertEqual(
                n.probability,
                neutron0.probability,
                )

            continue

        self.assertTrue( abs(n_in_onesigma*1./N-0.68) < 0.01)
        self.assertTrue( abs(n_in_twosigma*1./N-0.95) < 0.01)
        return
        

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__": 
    main()

    
# version
__id__ = "$Id: NDMonitor_TestCase.py 1144 2011-04-28 04:02:13Z linjiao $"

# End of file 
