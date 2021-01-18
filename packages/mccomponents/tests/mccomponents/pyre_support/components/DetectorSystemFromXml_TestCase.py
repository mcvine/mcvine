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


standalone = 1

# parallel launcher
from mcni.pyre_support.MpiApplication import mpi_launcher_choice as launcher

import unittest

class TestCase(unittest.TestCase):


    def test(self):
        "ARCS detector system. Neutrons shotting at one single pixel."
        cmd = 'MCVINE_MPI_LAUNCHER=serial ./sd'
        import os
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        eventdata = 'out/events.dat'
        from mccomponents.detector.event_utils import readEvents
        events = readEvents(eventdata)
        # print events
        # print events['p'].sum()
        p = events['p'].sum()
        print(p)
        self.assertTrue(p>0.9 and p<1)
        return


    def test1a(self):
        "ARCS detector system. Neutrons shotting at one single pixel."
        cmd = './sd --%s.nodes=2  --output-dir=out1a' % launcher
        import os
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        eventdata = 'out1a/events.dat'
        from mccomponents.detector.event_utils import readEvents
        events = readEvents(eventdata)
        # print events
        # print events['p'].sum()
        p = events['p'].sum()
        print(p)
        self.assertTrue(p>0.9 and p<1)
        return


    def test2(self):
        "ARCS detector system. A neutron missing all pixels."
        # cmd = './sd --source.velocity=1000,0,-2000 --ncount=1 --output-dir=out2'        
        cmd = 'MCVINE_MPI_LAUNCHER=serial ./sd --source.position=-0.00875,0.00462,0.005  --source.velocity=5713.19,-765.203,9068.39 --ncount=1 --output-dir=out2'
        import os
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        eventdata = 'out2/events.dat'
        from mccomponents.detector.event_utils import readEvents
        events = readEvents(eventdata)
        print(events)
        # self.assertEqual(len(events), 0)
        return


    pass  # end of homogeneous_scatterer_TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    unittest.main()
    # main()
    
# version
__id__ = "$Id: homogeneous_scatterer_TestCase.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
