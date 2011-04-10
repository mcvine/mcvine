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
        import mccomponents.sample.phonon.bindings as bindings
        b = bindings.get('BoostPython')
        
        nAtoms = 2
        nBranches = 3 * nAtoms
        nQx = 10; nQy = 12; nQz = 14
        Qaxes = [ ([1,1,0], nQx),
                  ([1,0,1], nQy),
                  ([0,1,1], nQz),
                  ]

        import histogram as H
        qx = H.axis('qx', H.arange(0, 1+1e-10, 1./(nQx-1)))
        qy = H.axis('qy', H.arange(0, 1+1e-10, 1./(nQy-1)))
        qz = H.axis('qz', H.arange(0, 1+1e-10, 1./(nQz-1)))
        br = H.axis('branchId', range(nBranches))
        atoms = H.axis('atomId', range(nAtoms))
        pols = H.axis('polId', range(3))
        realimags = H.axis('realimagId', range(2))
        
        eps = H.histogram(
            'eps', [qx,qy,qz,br,atoms,pols,realimags],
            fromfunction = lambda qx,qy,qz,br,atom,pol,realimag: qx+qy+qz+br+atom+pol+realimag)
        e = H.histogram(
            'e', [qx,qy,qz,br],
            fromfunction = lambda qx,qy,qz,br: qx+qy+qz+br)

        disp = b.linearlyinterpolateddispersion_3d(nAtoms, Qaxes, eps.I, e.I)

        Q = b.vector3

        self.assertAlmostEqual(disp.energy(0, Q(0,0,0)), 0)
        self.assertAlmostEqual(disp.energy(0, Q(1-1e-5,1-1e-5,0)), 1-1e-5)
        self.assertAlmostEqual(disp.energy(0, Q(0.5,0.5,0)), 0.5)
        self.assertAlmostEqual(disp.energy(0, Q(0.5,0,0.5)), 0.5)
        self.assertAlmostEqual(disp.energy(0, Q(0,0.5,0.5)), 0.5)
        self.assertAlmostEqual(disp.energy(0, Q(0.5,0.5,1-1e-10)), 1)
        return


    def test4(self):
        'LinearlyInterpolatedDispersion'
        nQs = 21
        Q_axes = [
            ( (2,0,0), nQs ),
            ( (0,2,0), nQs ),
            ( (0,0,2), nQs ),
            ]
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

        disp = bp.linearlyinterpolateddispersion( nAtoms, Q_axes, eps_data, E_data )
        return


    def test5(self):
        'periodicdispersion'
        nQs = 21
        Q_axes = [
            ( (2,0,0), nQs ),
            ( (0,2,0), nQs ),
            ( (0,0,2), nQs ),
            ]
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

        disp0 = bp.linearlyinterpolateddispersion( nAtoms, Q_axes, eps_data, E_data )
        disp = bp.periodicdispersion(
            disp0,
            ( (2,0,0), (0,3,0), (0,0,4) )
            )
        self.assertAlmostEqual( disp.energy(0, bp.Q(2,3,4)), disp.energy(0, bp.Q(0,0,0) ) )
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

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
