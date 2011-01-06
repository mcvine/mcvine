#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittestX as unittest

class TestCase(unittest.TestCase):

    def test1(self):
        cmd = 'mcvine-simulate -components=source,monitor --- -source=Source_simple -monitor=tofmonitor -geometer.monitor="(0,0,10),(0,0,0)" -source.E0=100 -source.dE=10 -source.width=0.05 -source.height=0.05 -source.radius=0 -source.dist=9.5 -source.xw=0.05 -source.yh=0.05 -monitor.tofmin=0 -monitor.tofmax=0.005 -monitor.ntof=100 -monitor.filename=itof.h5 --output-dir=out-ndmonitor-test1'
        import os
        os.system(cmd)
        return

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id: MultiMonitors_TestCase.py 659 2010-10-24 18:20:07Z linjiao $"

# End of file 
