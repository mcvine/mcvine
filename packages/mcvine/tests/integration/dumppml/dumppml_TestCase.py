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


outdir = 'out'
pml = 'ssd.pml'

import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'

import glob, shutil
def cleanup():
    # clean up
    pmls = glob.glob('ssd.pml*')
    for _ in pmls: os.remove(_)
    if os.path.exists(outdir):
        shutil.rmtree('out')


def execute(cmd):
    if os.system(cmd):
        raise RuntimeError("%r failed" %cmd)


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mcvine instrument sim app: dumppml'
        cleanup()

        # do dump pml first time
        cmd = './ssd -dump-pml'
        execute(cmd)
        # make sure output directory is not created
        self.assertTrue(not os.path.exists(outdir))
        # make sure ssd.pml is created
        self.assertTrue(os.path.exists(pml))

        # do dump pml second time
        cmd = './ssd -dump-pml'
        execute(cmd)
        # make sure output directory is not created
        self.assertTrue(not os.path.exists(outdir))
        # make sure ssd.pml-<time> is created
        timeformat = '%m-%d-%Y--'
        import time
        timestr = time.strftime(timeformat)
        pattern = '%s.saved-%s*' % (pml, timestr)
        self.assertTrue(glob.glob(pattern))

        # run simulation
        cmd = './ssd'
        execute(cmd)
        # make sure output directory is created
        self.assertTrue(os.path.exists(outdir))

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
