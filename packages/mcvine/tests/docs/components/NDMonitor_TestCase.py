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


interactive = False

simapp = 'sd'
outdir = 'out'

import os, glob, shutil
def cleanup():
    pmls = glob.glob('sd.pml*')
    map(os.remove, pmls)
    # clean up
    if os.path.exists(outdir):
        shutil.rmtree('out')


from _utils import execute


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'docs:Components:NDMonitor'
        cleanup()

        #
        cmd = 'mcvine-create-instrument-simulation-application --name=sd --components=source,detector'
        execute(cmd)

        #
        cmd = './sd --source=Source_simple --detector="NDMonitor(energy)"  --dump-pml'
        execute(cmd)

        #
        cmd = './sd \
 --geometer.detector="(0,0,10),(0,0,0)" \
 --source.width=0.1 --source.height=0.1 --source.radius=0 \
 --source.xw=0.1 --source.yh=0.1 --source.dist=10 \
 --source.E0=100 --source.dE=20 \
 --detector.title="I(E)" --detector.yheight=0.1 --detector.xwidth=0.1 \
 --detector.nenergy=100 --detector.energymin=60 --detector.energymax=140 \
 --dump-pml'
        execute(cmd)

        #
        cmd = './sd --ncount=1e5'
        execute(cmd)

        global interactive
        if interactive:
            cmd = 'PlotHist.py out/ienergy.h5'
            execute(cmd)
        
        return

    
    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    global interactive
    interactive = True
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__": main()
    
# version
__id__ = "$Id$"

# End of file 
