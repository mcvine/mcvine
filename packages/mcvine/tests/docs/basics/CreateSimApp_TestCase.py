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

simapp = 'test'
outdir = 'out'

import os, glob, shutil
def cleanup():
    pmls = glob.glob('test.pml*')
    map(os.remove, pmls)
    # clean up
    if os.path.exists(outdir):
        shutil.rmtree('out')


def execute(cmd):
    if os.system(cmd):
        raise RuntimeError, "%r failed" %cmd


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mcvine instrument sim app: dumppml'
        cleanup()

        # 
        cmd = 'mcvine-create-instrument-simulation-application -h'
        execute(cmd)
        
        #
        cmd = 'mcvine-create-instrument-simulation-application  --name=%s --components=source,monitor' % simapp
        execute(cmd)

        #
        cmd = './%s -h' % simapp
        execute(cmd)

        #
        cmd = './%s --source=MonochromaticSource --monitor=E_monitor' % simapp
        execute(cmd)

        #
        cmd = './%s --source=MonochromaticSource --monitor=E_monitor --overwrite-datafiles --dump-pml' % simapp
        execute(cmd)

        #
        cmd = './%s -h' % simapp
        execute(cmd)

        #
        cmd = './%s --source.help-properties' % simapp
        execute(cmd)

        #
        cmd = './%s --source.energy=60 --monitor.Emin=50 --monitor.Emax=70 --monitor.nchan=200 --dump-pml' % simapp
        execute(cmd)
        
        #
        cmd = './%s --ncount=1e4' % simapp
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
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    global interactive
    interactive = True
    main()
    
# version
__id__ = "$Id$"

# End of file 
