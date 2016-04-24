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


import os, shutil

import unittestX as unittest

class TestCase(unittest.TestCase):

    def test3(self):
        outdir = 'out-testmpi'
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        from mcni.pyre_support.MpiApplication \
            import mpi_launcher_choice as launcher            
        cmd = './testmpi -%s.nodes=2' % launcher
        if os.system(cmd):
            raise RuntimeError, "%r failed" % cmd

        from histogram.hdf import load
        from histogram.hdf.utils import getOnlyEntry
        f = '%s/ienergy.h5' % (outdir,)
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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
