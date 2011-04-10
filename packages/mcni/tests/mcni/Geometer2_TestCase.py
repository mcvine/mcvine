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

        from mcni.Geometer2 import Geometer, AbsoluteCoord as abs, RelativeCoord as rel
        geometer = Geometer()
        
        geometer.register('comp0', abs((0,0,0)), abs((0,0,0)))
        geometer.register('comp1', abs((0,0,0)), abs((0,90,0)))
        geometer.register('comp2', rel((0,0,1), 'comp1'), abs((0,0,0)))
        geometer.register('comp3', rel((0,0,0), 'comp2'), rel((3,4,5), 'comp2'))
        geometer.register('comp4', abs((0,0,0)), rel((0,0,90), 'comp0'))
        geometer.register('comp5', abs((0,0,0)), rel((0,90,0), 'comp4'))
        geometer.register('comp6', rel((1,2,3), 'comp5'), abs((0,0,0)))

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

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
