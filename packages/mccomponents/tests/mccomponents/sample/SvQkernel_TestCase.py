#!/usr/bin/env python
#
#


import unittest


svq_f = lambda qx,qy,qz: qx*qx
def createSvq():
    import histogram as H
    qxaxis = H.axis( 'Qx', boundaries = H.arange(-5, 5.0, 0.1) )
    qyaxis = H.axis( 'Qy', boundaries = H.arange(-5, 6.0, 0.1) )
    qzaxis = H.axis( 'Qz', boundaries = H.arange(-5, 7.0, 0.1) )
    svq = H.histogram(
        'svq',
        [ qxaxis, qyaxis, qzaxis ],
        fromfunction = svq_f
        )
    return svq


import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh

class SvQkernel_TestCase(unittest.TestCase):

    def test1(self):
        'SvQkernel'
        svq = createSvq()
        gridsvq = ms.gridsvq( svq )
        svqkernel = ms.svqkernel(
            1., 1.,
            SvQ=gridsvq,
        )
        csvqkernel = mh.scattererEngine( svqkernel )
        ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
        self.assertAlmostEqual( csvqkernel.scattering_coefficient(ev), 1 )
        self.assertAlmostEqual( csvqkernel.absorption_coefficient(ev), 2200./3000. )
        csvqkernel.scatter(ev)
        print(dir(csvqkernel))
        return

    pass  # end of SvQkernel_TestCase

if __name__ == "__main__": unittest.main()

# End of file
