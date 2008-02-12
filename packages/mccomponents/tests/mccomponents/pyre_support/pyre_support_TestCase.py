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

debug = journal.debug( "pyre_support_TestCase" )
warning = journal.warning( "pyre_support_TestCase" )


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility, componentfactory as component
        import mccomponents.pyre_support
        source = facility(
            'source',
            default = component('sources', 'MonochromaticSource')('source') )
        sample = facility(
            'sample',
            default = component( 'samples', 'SampleAssemblyFromXml')('sample') )
        detector = facility(
            'detector',
            default = component( 'detectors', 'DetectorSystemFromXml')('detector') )
        pass # end of Inventory


    def __init__(self, name = 'test'):
        base.__init__(self, name)
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'sample', 'detector']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.source = (0,0,0), (0,0,0)
        self.inventory.geometer.inventory.sample = (0,0,10), (0,0,0)
        self.inventory.geometer.inventory.detector = (0,0,10), (0,0,0)
        return
    
    pass # end of Instrument



class TestCase(unittest.TestCase):


    def test1(self):
        instrument = Instrument( 'test' )

        import sys
        save = sys.argv
        sys.argv = [
            '',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=pyre_support_test_out',
            '--overwrite-datafiles',
            ]

        instrument.run()
        return
    

    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
