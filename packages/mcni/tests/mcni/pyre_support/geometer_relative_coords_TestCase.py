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

import numpy.testing as nt
from mcni.neutron_coordinates_transformers.mcstasRotations import toMatrix

class TestCase(unittest.TestCase):


    def test1(self):
        'mcni: relative coordinates for geometer'
        class Instrument(InstrumentBase):
            
            def main(self):
                geometer = self.inventory.geometer

                comp2pos = geometer.position('comp2')
                nt.assert_array_almost_equal(comp2pos, (1,0,0))

                comp2ori = geometer.orientation('comp2')
                nt.assert_array_almost_equal(comp2ori, (0,0,0))
                
                comp3pos = geometer.position('comp3')
                nt.assert_array_almost_equal(comp3pos, (1,0,0))

                comp3ori = geometer.orientation('comp3')
                nt.assert_array_almost_equal(comp3ori, toMatrix((3,4,5)))
                
                comp5ori = geometer.orientation('comp5')
                nt.assert_array_almost_equal(comp5ori, toMatrix((-90,0,90)))
                
                comp6pos = geometer.position('comp6')
                nt.assert_array_almost_equal(comp6pos, (-2,3,-1))
                
                return

        instrument = Instrument('geometer-relative-coords-test1')
        instrument.testFacility = self

        import sys
        save = sys.argv
        sys.argv = [
            '',
            '--geometer.comp0=(0,0,0),(0,0,0)',
            '--geometer.comp1=(0,0,0),(0,90,0)',
            '--geometer.comp2=relative((0,0,1),"comp1"),(0,0,0)',
            '--geometer.comp3=relative((0,0,0),"comp2"),relative((3,4,5),"comp2")',
            '--geometer.comp4=(0,0,0),relative((0,0,90),"comp0")',
            '--geometer.comp5=(0,0,0),relative((0,90,0),"comp4")',
            '--geometer.comp6=relative((1,2,3),"comp5"),(0,0,0)',
            '--geometer.dump',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=%s-out' % instrument.name,
            '--overwrite-datafiles',
            ]

        instrument.run()
        sys.argv = save
        return
    
        
    pass  # end of TestCase



from mcvine.applications.InstrumentBuilder import build
components = ['comp%s' % i for i in range(10)]
InstrumentBase = build(components)


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
