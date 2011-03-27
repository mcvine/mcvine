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


import unittest

class TestCase(unittest.TestCase):


    def test(self):
        cmd = './sd'
        import os
        if os.system(cmd):
            raise RuntimeError, "%s failed" % cmd
        eventdata = 'out/events.dat'
        from mccomponents.detector.event_utils import readEvents
        events = readEvents(eventdata)
        # print events
        # print events['p'].sum()
        p = events['p'].sum()
        self.assert_(p>0.9 and p<1)
        return


    pass  # end of homogeneous_scatterer_TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id: homogeneous_scatterer_TestCase.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
