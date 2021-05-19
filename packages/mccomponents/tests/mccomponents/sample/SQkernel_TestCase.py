#!/usr/bin/env python
#
#


import unittest
import journal


sq_f = lambda q: q*q
def createSq():
    import histogram as H
    qaxis = H.axis( 'Q', boundaries = H.arange(0, 13.0, 0.1) )
    sq = H.histogram(
        'sq',
        [ qaxis],
        fromfunction = sq_f
        )
    return sq


import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh

class SQkernel_TestCase(unittest.TestCase):

    def test1(self):
        'SQkernel'
        sq = createSq()
        gridsq = ms.gridsq( sq )
        sqkernel = ms.sqkernel(
            1., 1.,
            SQ=gridsq,
            Qrange=(0, 12.))
        
        csqkernel = mh.scattererEngine( sqkernel )
        
        ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
        self.assertAlmostEqual( csqkernel.scattering_coefficient(ev), 1 )
        self.assertAlmostEqual( csqkernel.absorption_coefficient(ev), 2200./3000. )
        csqkernel.scatter(ev)
        return

    pass  # end of SQkernel_TestCase



if __name__ == "__main__": unittest.main()


# End of file 
