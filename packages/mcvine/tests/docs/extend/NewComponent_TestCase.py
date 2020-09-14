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


simapp = 'sd'
outdir = 'out'

import os, glob, shutil
def cleanup():
    pmls = glob.glob('sd.pml*')
    for _ in pmls: os.remove(_)
    if os.path.exists(outdir):
        shutil.rmtree('out')


def execute(cmd):
    if os.system(cmd):
        raise RuntimeError("%r failed" %cmd)


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'create and use new component'
        cleanup()
        
        cmd = 'mcvine-create-instrument-simulation-application --name=sd --components=source,detector'
        execute(cmd)
        
        cmd = 'MCVINE_MPI_LAUNCHER=serial ./sd --source=Source_simple --detector=printer --dump-pml'
        execute(cmd)
        
        cmd = 'MCVINE_MPI_LAUNCHER=serial ./sd -ncount=5'
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
    main()
    
# version
__id__ = "$Id$"

# End of file 
