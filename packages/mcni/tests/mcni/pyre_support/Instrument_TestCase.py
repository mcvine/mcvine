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
            '--buffer_size=5',
            '--output-dir=pyre_support_test_out',
            '--overwrite-datafiles',
            ]

        instrument.run()
        sys.argv = save
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
        return neutrons

    pass # end of Verifier


from mcni.pyre_support.Instrument import Instrument as base
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
