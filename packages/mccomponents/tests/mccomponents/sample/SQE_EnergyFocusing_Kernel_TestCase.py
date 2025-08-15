#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import unittestX as unittest


sqe_f = lambda q,e: q*q+e*e
def createSqe():
    import histogram as H
    qaxis = H.axis( 'Q', boundaries = H.arange(0, 13.0, 0.1) )
    eaxis = H.axis( 'energy', boundaries = H.arange(-50, 50, 1.0) )
    sqe = H.histogram(
        'sqe',
        [ qaxis, eaxis ],
        fromfunction = sqe_f
        )
    return sqe


import os, numpy as np
import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh
from mcni.utils import conversion

class SQE_EnergyFocusing_Kernel_TestCase(unittest.TestCase):

    def test1(self):
        'SQE_EnergyFocusing_Kernel'
        sqe = createSqe()
        gridsqe = ms.gridsqe( sqe )
        kernel = ms.sqe_energyfocusing_kernel(
            1., 1., 1.,
            SQE=gridsqe,
            Qrange=(0, 12.), Erange=(-50, 50),
            Ef = 20.0, dEf = 0.1
        )
        ckernel = mh.scattererEngine( kernel )
        ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) ) # about 47 meV
        self.assertAlmostEqual( ckernel.scattering_coefficient(ev), 1 )
        self.assertAlmostEqual( ckernel.absorption_coefficient(ev), 2200./3000. )
        for i in range(1000):
            ckernel.scatter(ev)
            v = np.linalg.norm(ev.state.velocity)
            Ef = conversion.v2e(v)
            self.assertTrue(abs(Ef-20)<1)
        return

    pass  # end of SQE_EnergyFocusing_Kernel_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()

# End of file
