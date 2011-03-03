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
        cmd = '''./testapp1.py \
 --monitor.geometer.m1="(0,0,1),(0,0,0)" \
 --monitor.geometer.m2="(0,0,0),(0,90,0)" \
 --journal.debug.monitor \
'''
        execute(cmd)
        return

    def test2(self):
        cmd = '''./testapp1.py \
 --monitor.m1=E_monitor \
 --output-dir=out-test2 \
 --overwrite-datafiles \
 --monitor.geometer.m1="(0,0,1),(0,0,0)" \
 --monitor.geometer.m2="(0,0,0),(0,90,0)" \
 --journal.debug.monitor \
'''
        execute(cmd)
        return

    def test3(self):
        "two monitors facing the incident beam shoulder by shoulder"
        
        cmd = '''./testapp1.py \
 --ncount=1e5 \
 --source=Source_simple \
 --source.width=0.01 \
 --source.height=0.01 \
 --source.radius=0 \
 --source.xw=0.2 \
 --source.yh=0.1 \
 --source.dist=1 \
 --source.E0=60 \
 --monitor.m1="NDMonitor(x,y)" \
 --monitor.m2="NDMonitor(x,y)" \
 --monitor.geometer.m1="(0.05,0,0,),(0,0,0)" \
 --monitor.geometer.m2="(-0.05,0,0),(0,0,0)" \
 --monitor.m1.xwidth=0.1 \
 --monitor.m1.yheight=0.1 \
 --monitor.m1.xmin=-0.05 \
 --monitor.m1.xmax=0.05 \
 --monitor.m1.nx=10 \
 --monitor.m1.ymin=-0.05 \
 --monitor.m1.ymax=0.05 \
 --monitor.m1.ny=10 \
 --monitor.m1.filename=m1.h5 \
 --monitor.m2.xwidth=0.1 \
 --monitor.m2.yheight=0.1 \
 --monitor.m2.xmin=-0.05 \
 --monitor.m2.xmax=0.05 \
 --monitor.m2.nx=10 \
 --monitor.m2.ymin=-0.05 \
 --monitor.m2.ymax=0.05 \
 --monitor.m2.ny=10 \
 --monitor.m2.filename=m2.h5 \
 --geometer.monitor="(0,0,1),(0,0,0)" \
 --output-dir=out-test3 \
 --overwrite-datafiles \
 --journal.debug.monitor \
'''
        execute(cmd)

        # the solid angle for each monitor is
        # about 0.1*0.1/(1*1) = 0.01
        # there are totally 100 pixels per monitor
        # so each pixel has about 1e-4 counts
        from histogram.hdf import load
        from histogram.hdf.utils import getOnlyEntry
        import numpy
        def loadhist(f):
            return load(f, getOnlyEntry(f))

        m1 = loadhist('out-test3/m1.h5')
        self.assert_(numpy.abs(m1.I - 1e-4).max() < 1.5e-5)

        m2 = loadhist('out-test3/m2.h5')
        self.assert_(numpy.abs(m2.I - 1e-4).max() < 1.5e-5)
        return

    pass # end of TestCase


def execute(cmd):
    import os
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd

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
__id__ = "$Id$"

# End of file 
