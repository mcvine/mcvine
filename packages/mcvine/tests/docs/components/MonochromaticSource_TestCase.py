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
        cmd = './sd \
 --source=MonochromaticSource --source.energy=70 \
 --detector=E_monitor --detector.filename=IE.dat \
 --dump-pml'
        execute(cmd)

        #
        cmd = './sd --ncount=1e3'
        execute(cmd)

        global interactive
        if interactive:
            cmd = 'PlotHist.py out/IE.h5'
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
