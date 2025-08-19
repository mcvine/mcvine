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
        
        from mcni.components.EventAreaMonitor import EventAreaMonitor
        m = EventAreaMonitor('eam')
        
        N = 10
        from mcni import neutron_buffer, neutron
        b = neutron_buffer(N)
        for i in range(N):
            b[i] = neutron()
            continue

        m.process(b)

        self.assertEqual(len(m.events), N)
        self.assertTrue((m.events == m.events[0]).all())
        e = m.events[0]
        self.assertEqual(e['pixelID'], 5050)
        self.assertEqual(e['tofChannelNo'], 0)
        self.assertEqual(e['p'], 1.)
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

    
# version
__id__ = "$Id$"

# End of file 
