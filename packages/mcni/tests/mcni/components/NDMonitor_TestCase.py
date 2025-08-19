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


interactive = False


import unittestX as unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'NDMonitor'
        from mcni.components.NDMonitor import NDMonitor, Axis
        xaxis = Axis(
            name = 'x', expression='x',
            bins = 100, range=(0, 1000.),
            unit = 'meter',
            )
        m = NDMonitor('abc', [xaxis])
        N = 100
        from mcni import neutron_buffer, neutron
        b = neutron_buffer(N)
        for i in range(N):
            b[i] = neutron()
            continue

        m.process(b)

        self.assertEqual(m.histogram.I[0], N)
        self.assertEqual(m.histogram.E2[0], N)
        self.assertEqual(m.histogram.I[1], 0.)
        self.assertEqual(m.histogram.E2[1], 0.)

        if interactive:
            from histogram.plotter import defaultPlotter as plotter
            plotter.plot(m.histogram)
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
    interactive = True
    main()

# End of file
