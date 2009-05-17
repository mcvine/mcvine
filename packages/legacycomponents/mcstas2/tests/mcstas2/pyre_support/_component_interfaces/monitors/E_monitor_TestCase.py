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



import unittestX as unittest
import journal

from TestInstrument1 import Instrument as base
class Instrument(base):

    def __init__(self, name='E_monitor_TestCase'):
        base.__init__(self, name)
        return
    

def _outdir():
    try:
        import mpi
        nompi = False
    except ImportError:
        nompi = True
    outputdir = 'E_monitor_TestCase-out'
    if not nompi: outputdir = outputdir  +'-0'
    return outputdir
        

class TestCase(unittest.TestCase):

    def test1(self):
        instrument = Instrument()
        instrument.run()

        import time
        ctime = time.time()

        #check output directory exists
        outputdir = _outdir()
        self.assert_( os.path.exists( outputdir ) )
        
        #make sure files were just created
        for item in os.listdir( outputdir ):
            path = os.path.join( outputdir, item )
            self.assert_( os.path.exists( path ) )

            mtime = os.path.getmtime( path )
            self.assert_( ctime - mtime >= 0 )
            #print "path:", path, "timediff:", ctime - mtime 
            self.assert_( ctime - mtime < 10 )
            continue
        
        return
    
    pass  # end of TestCase


import os


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
