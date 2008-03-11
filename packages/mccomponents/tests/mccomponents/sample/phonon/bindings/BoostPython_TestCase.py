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

debug = journal.debug( "BoostPython_TestCase" )
warning = journal.warning( "BoostPython_TestCase" )


from mccomponents.sample.phonon.bindings import get
bp = get('BoostPython')


class TestCase(unittest.TestCase):


    def test1(self):
        'linearlyinterpolateddos'
        import numpy as N
        Z = N.zeros( 50 )
        area = 0
        for i in range(50):
            Z[i] = i*i
            area += Z[i]
            continue
        dos = bp.linearlyinterpolateddos(0, 1., 50, Z )
        self.assertAlmostEqual( dos( 3 ), 3.**2/area )
        return


    def test2(self):
        'NdArray'
        import numpy as N
        a = N.arange(12, dtype = N.double)
        a.shape = 3,4
        a1 = bp.ndarray( a )
        assert a1.origin is a
        self.assertEqual( a[2,1], 9 )
        self.assertEqual( a1[ 2,1 ], 9 )
        return


    def test3(self):
        'LinearlyInterpolatedDispersion_3D'
        nQs = 21
        Q_axis = -10, 1., nQs
        Q_axes = [Q_axis, Q_axis, Q_axis]
        nAtoms = 5
        nDims = 3
        nBranches = nAtoms*nDims
        import numpy
        eps_data = numpy.zeros(
            ( nQs, nQs, nQs, nBranches, nAtoms, nDims, 2 ),
            dtype = numpy.double)
        E_data = numpy.zeros(
            ( nQs, nQs, nQs, nBranches ),
            dtype = numpy.double)

        disp = bp.linearlyinterpolateddispersion_3d( nAtoms, Q_axes, eps_data, E_data )
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
