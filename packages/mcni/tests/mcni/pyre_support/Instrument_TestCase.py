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



import mcvine
import unittestX as unittest
import journal

debug = journal.debug( "mcni.pyre_support.test" )
warning = journal.warning( "mcni.pyre_support.test" )



class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: a simple pyre simulation app'
        instrument = Instrument('test')
        instrument.testFacility = self

        import sys
        save = sys.argv
        sys.argv = [
            '',
            '--ncount=10',
            '--buffer_size=4',
            '--output-dir=out-pyre_support_test',
            '--overwrite-datafiles',
            ]

        instrument.run()

        self.assertEqual(instrument.inventory.ncount,
                         instrument.inventory.verifier.count,
                         )
        
        sys.argv = save
        return


    def test_dumppml(self):
        'mcni.pyre_support.Instrument: option dumppml'
        instrument = Instrument('test-dumppml')
        instrument.testFacility = self

        import sys
        save = sys.argv
        sys.argv = [
            '',
            '--ncount=10',
            '--buffer_size=4',
            '--output-dir=out-Instrument-dumppml',
            '--dump-pml',
            '--overwrite-datafiles',
            ]

        instrument.run()

        sys.argv = save
        return


    def test2(self):
        "Instrument: _getBufferSize"
        instrument = Instrument('t')
        
        # for lower values of ncount, buffer_size=ncount/mpisize/DEFAULT_NUMBER_SIM_LOOPS
        instrument.inventory.ncount = ncount = 1e3
        self.assertEqual(instrument._getBufferSize(), ncount/DEFAULT_NUMBER_SIM_LOOPS)
        
        instrument.inventory.ncount = ncount = 2e3
        self.assertEqual(instrument._getBufferSize(), ncount/DEFAULT_NUMBER_SIM_LOOPS)

        instrument.mpiSize = mpiSize = 10
        self.assertEqual(instrument._getBufferSize(), int(ncount/mpiSize/DEFAULT_NUMBER_SIM_LOOPS))
        
        # for higher values, buffer_size is set by memory limit
        import psutil
        temp = min(psutil.TOTAL_PHYMEM/2, (psutil.avail_phymem() + psutil.avail_virtmem())*0.7)
        temp = int(temp)
        from mcni.neutron_storage.idfneutron import ndblsperneutron
        max = int(temp/ndblsperneutron/8/100) * 100
        
        instrument.inventory.ncount = ncount = 1e9
        self.assertEqual(instrument._getBufferSize(), max)
        
        instrument.inventory.ncount = ncount = 2e9
        self.assertEqual(instrument._getBufferSize(), max)

        # if user set a too high number for buffer size, it is ignored
        instrument.inventory.ncount = ncount = 2e9
        instrument.inventory.buffer_size = 2e9
        self.assertEqual(instrument._getBufferSize(), max)

        # if user set a too low value for buffer_size, a warning would be issued
        instrument.inventory.ncount = 1e8
        instrument.inventory.buffer_size = 100
        instrument._getBufferSize()
        
        return
    
        
    pass  # end of TestCase



from mcni.pyre_support.AbstractComponent import AbstractComponent

class Source( AbstractComponent ):

    def process(self, neutrons):
        import mcni
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = ( 1,2,3 ), v = (1,2,3) )
            continue
        return neutrons

    pass # end of Source


class Verifier( AbstractComponent ):

    def setTestFacility(self, testFacility):
        self.testFacility = testFacility
        return

    def process(self, neutrons):
        for i in range(len(neutrons)):
            p = neutrons[i].state.position
            r = list( p )
            self.testFacility.assertVectorAlmostEqual(
                r, (2,-1,2) )
            
            v = list( neutrons[i].state.velocity )
            self.testFacility.assertVectorAlmostEqual(
                v, (2,-1,3) )
            continue
        self.count += len(neutrons)
        return neutrons

    def __init__(self, *args, **kwds):
        self.count = 0
        super(Verifier, self).__init__(*args, **kwds)
        return

    pass # end of Verifier


from mcni.pyre_support.Instrument import Instrument as base, DEFAULT_NUMBER_SIM_LOOPS
class Instrument(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        from mcni.pyre_support import facility
        source = facility('source', default = Source('source') )
        verifier = facility('verifier', default = Verifier( 'verifier' ) )

        pass # end of Inventory


    def main(self):
        self.inventory.verifier.setTestFacility( self.testFacility )
        base.main(self)
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'verifier']
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.verifier = (0,0,1), (0,0,90)
        return
    
    pass # end of Instrument


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
