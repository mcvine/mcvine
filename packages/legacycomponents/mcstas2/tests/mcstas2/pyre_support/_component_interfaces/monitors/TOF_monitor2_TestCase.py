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


skip = False
standalone = True


import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


import unittestX as unittest

from TestInstrument1 import Instrument as base
class Instrument(base):

    def __init__(self, name='TOF_monitor2_TestCase'):
        base.__init__(self, name)
        return


    def _defaults(self):
        super(Instrument, self)._defaults()
        self.inventory.mode = 'worker'
        from mcstas2.pyre_support import componentfactory
        self.inventory.monitor = componentfactory \
            ( 'monitors', 'TOF_monitor2' ) \
            ('monitor')
        return


    def _fini(self):
        super(Instrument, self)._fini()
        if self._showHelpOnly: return
        
        monitor = self.inventory.monitor
        h = monitor._get_histogram()
        self.testFacility.assertEqual(h.tof[0], 6e-3/60/2)
        return
    

def _outdir():
    try:
        import mpi
        nompi = False
    except ImportError:
        nompi = True
    outputdir = 'TOF_monitor2_TestCase-out'
    if not nompi: outputdir = outputdir  +'-0'
    return outputdir
        

class TestCase(unittest.TestCase):

    def test1(self):
        instrument = Instrument()
        instrument.testFacility = self
        instrument.run()
        instrument.run_postprocessing()
        return
    
    pass  # end of TestCase


import os


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
