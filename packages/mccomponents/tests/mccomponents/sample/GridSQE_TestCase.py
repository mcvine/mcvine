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
import numpy as np, histogram as H, histogram.hdf as hh


sqe_f = lambda q,e: q*q+e*e 
def createSqe():
    qaxis = H.axis( 'Q', boundaries = H.arange(0, 13.0, 0.1) )
    eaxis = H.axis( 'energy', boundaries = H.arange(-50, 50, 1.0) )
    sqe = H.histogram(
        'sqe',
        [ qaxis, eaxis ],
        fromfunction = sqe_f
        )
    return sqe


import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh

class GridSQE_TestCase(unittest.TestCase):

    def test1(self):
        'GridSQE'
        sqe = createSqe()
        gridsqe = ms.gridsqe( sqe )
        cgridsqe = mh.scattererEngine( gridsqe )
        Q, E = 5.05, 10.5
        self.assertAlmostEqual( sqe[ Q,E ][0], sqe_f(Q,E) )
        self.assertAlmostEqual( cgridsqe( Q,E ), sqe_f(Q,E) )
        return

    def test2(self):
        qaxis = H.axis( 'Q', boundaries = H.arange(0, 499.1, 1.))
        eaxis = H.axis( 'E', boundaries = H.arange(0, 8001.1, 1.))
        I = np.arange(499*8001)
        I.shape = 499, 8001
        sqe = H.histogram('sqe', [qaxis, eaxis])
        sqe.I[:] = I
        gridsqe = ms.gridsqe( sqe )
        cgridsqe = mh.scattererEngine( gridsqe )
        assert cgridsqe(300.5, 0.5) == 2400300.0
        return

    def test3(self):
        qaxis = H.axis( 'Q', centers = H.arange(0.2, 99.8, .2))
        ebb = np.load('GridSQE_test3_ebb.npy')
        eaxis = H.axis( 'E', boundaries = ebb)
        sqe = H.histogram('sqe', [qaxis, eaxis])
        sqe[(), 0.].I[:] = 1
        gsqe = ms.gridsqe( sqe )
        cgsqe = mh.scattererEngine( gsqe )
        for E in [-50, -10, 10, 50]:
            S = np.array([cgsqe(q,10) for q in np.linspace(1, 10, 200)])
            assert np.allclose(S, 0)
        S = np.array([cgsqe(q,0) for q in np.linspace(1, 10, 200)])
        assert np.allclose(S, 1)
        return
    pass  # end of GridSQE_TestCase



def pysuite():
    suite1 = unittest.makeSuite(GridSQE_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

if __name__ == "__main__": main()

# End of file
