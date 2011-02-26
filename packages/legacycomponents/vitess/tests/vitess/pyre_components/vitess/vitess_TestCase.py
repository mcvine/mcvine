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


skip = True
standalone = True


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

    def test3(self):
        'ndmonitor: energy'
        '''
        COMPONENT FChopper = Vitess_ChopperFermi(
                    GeomOption=2, zerotime=0, Nchannels=30,  Ngates=4,
                    freq=f1,   height=0.102,   width=0.05,
                    depth=0.017,  r_curv=2.2, diameter=0.08, Phase=-f1_tof_deg,
                    wallwidth=0.00015, sGeomFileName="FC_geom_circ.dat")
        '''
        cmd = 'mcvine-simulate -components=source,fc,monitor --- -ncount=1e4 -buffer_size=1000 -source=Source_simple -fc="Vitess(chopper_fermi_Linux)"  -fc.a=10.2 -fc.b=5 -fc.c=3 -fc.l=30 -fc.m=0.015 -fc.r=0.08 -fc.n=300 -fc.q=  -fc.G=FC_geom_circ.dat  -monitor="NDMonitor(energy)" -geometer.fc="(0,0,10),(0,0,0)" -geometer.monitor="(0,0,12),(0,0,0)" -source.E0=60 -source.dE=30 -dist=10 -width=0.05 -height=0.05 -xw=0.05 -yh=0.05 -fc. -monitor.energymin=0 -monitor.energymax=100 -monitor.nenergy=100 -monitor.filename=ienergy.h5 --output-dir=out-test3'
        import os
        if os.system(cmd):
            raise RuntimeError, "%r failed" % cmd

        from histogram.hdf import load
        from histogram.hdf.utils import getOnlyEntry
        f = 'out-test3/ienergy.h5'
        h = load(f, getOnlyEntry(f))
        self.assertEqual( h[(58, 62)].sum() , (1., 1.e-4))
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
__id__ = "$Id$"

# End of file 
