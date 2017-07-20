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


skip = True


import unittestX as unittest
import journal


from mcni.pyre_support.MpiApplication import usempi

# parallel launcher
from mcni.pyre_support.MpiApplication import mpi_launcher_choice as launcher

# from E_monitor_TestCase.pml
outputdir = 'out-E_monitor_TestCase'
ncount = 100 


class TestCase(unittest.TestCase):

    def test1(self):
        # remove the output directory
        if os.path.exists(outputdir):
            shutil.rmtree(outputdir)
        
        # build the command to ru
        cmd = ['python E_monitor_TestCase_app.py']
        if usempi():
            cmd.append('--%s.nodes=2' % launcher)
        cmd = ' '.join(cmd)

        # run command
        if os.system(cmd):
            raise RuntimeError, "%s failed" % cmd

        # checks
        import time
        ctime = time.time()

        #check output directory exists
        self.assert_( os.path.exists( outputdir ) )
        
        # make sure that the final histogram is identical to the 
        # sum of all the final histograms in different nodes
        from mcni.components.HistogramBasedMonitorMixin import hist_mcs_sum
        h, n = hist_mcs_sum(outputdir, 'IE.h5')
        self.assertEqual(n, ncount)
        h.I/=n; h.E2/=n*n
        
        from histogram.hdf import load
        from histogram.hdf.utils import getOnlyEntry
        p = os.path.join(outputdir, 'IE.h5')
        ha = load(p, getOnlyEntry(p))
        
        self.assert_((h.I == ha.I).all())
        self.assert_((h.E2 == ha.E2).all())
        
        return
    
    pass  # end of TestCase


import os, shutil

def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
