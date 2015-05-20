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


standalone = True


import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )


outdir = 'test-output-dir-option_out'
import os, sys, mcvine


class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: output_dir_option'

        if os.path.exists( outdir ):
            import shutil
            shutil.rmtree( outdir )
        
        instrument = Instrument('output_dir_option_TestCase')
        instrument.testFacility = self
        instrument.run()

        self.assert_( os.path.exists( outdir ) )
        IEh5 = os.path.join( outdir, 'IE.h5' )
        self.assert_( os.path.exists( IEh5 ) )
        import time
        ctime = time.time()
        mtime = os.path.getmtime( IEh5 )
        self.assert_( ctime >= mtime and ctime < mtime + 10 )
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.AbstractComponent import AbstractComponent

class Source( AbstractComponent ):

    def process(self, neutrons):
        open( 'tmp', 'w').write( 'hello' )
        return neutrons

    pass # end of Source


from mcstas2.pyre_support import componentfactory


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility, componentfactory
        source = facility('source', default = Source('source') )

        monitor = facility(
            'monitor',
            default = componentfactory(
            'monitors', 'E_monitor', supplier = 'mcstas2') ('monitor')
            )
        
        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'monitor']
        geometer = self.inventory.geometer
        geometer.inventory.monitor = (0,0,1), (0,0,0)
        return
    
    pass # end of Instrument


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
