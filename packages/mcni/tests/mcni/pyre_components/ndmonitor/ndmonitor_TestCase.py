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


import os, shutil
for entry in os.listdir('.'):
    if not entry.startswith('out-test'):
        continue
    if not os.path.isdir(entry):
        continue
    shutil.rmtree(entry)
    continue


import unittestX as unittest

class TestCase(unittest.TestCase):

    def test1(self):
        cmd = 'mcvine-simulate -components=source,monitor --- -source=Source_simple -monitor=tofmonitor -geometer.monitor="(0,0,10),(0,0,0)" -source.E0=100 -source.dE=10 -source.width=0.05 -source.height=0.05 -source.radius=0 -source.dist=9.5 -source.xw=0.05 -source.yh=0.05 -monitor.tofmin=0 -monitor.tofmax=0.005 -monitor.ntof=100 -monitor.filename=itof.h5 --output-dir=out-test1'
        import os
        os.system(cmd)
        return


    def test2(self):
        cmd = 'mcvine-simulate -components=source,monitor --- -source=Source_simple -monitor=xdivxmonitor -geometer.monitor="(0,0,10),(0,0,0)" -source.E0=100 -source.dE=10 -source.width=0.05 -source.height=0.05 -source.radius=0 -source.dist=9.5 -source.xw=0.05 -source.yh=0.05 -monitor.xmin=-0.1 -monitor.xmax=0.1 -monitor.nx=100  -monitor.divxmin=-0.01 -monitor.divxmax=0.01 -monitor.ndivx=100 -monitor.filename=ixdivx.h5 --output-dir=out-test2'
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
