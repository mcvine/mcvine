#!/usr/bin/env python
#
#


import os, numpy as np, unittest

class fxyz_TestCase(unittest.TestCase):

    def test1(self):
        import mccomponents.mccomponentsbp as b
        import histogram as H
        X = H.axis('x', boundaries=np.arange(-5.5, 5, 1.))
        Y = H.axis('y', boundaries=np.arange(-5.5, 6, 1.))
        Z = H.axis('z', boundaries=np.arange(-5.5, 7, 1.))
        f = lambda x,y,z: x + y*y + z**3
        h = H.histogram('h', (X,Y,Z), fromfunction=f)
        a = h.I.reshape(-1)
        sv = b.vector_double(a.size)
        sv[:] = a
        print(X.binBoundaries().asList())
        fxyz = b.new_fxyz(
            -5.5, 4.5, 1.,
            -5.5, 5.5, 1.,
            -5.5, 6.5, 1.,
            sv
        )
        for x in h.x:
            for y in h.y:
                for z in h.z:
                    self.assertAlmostEqual(fxyz(x, y, z), f(x,y,z))
                    # print(x,y,z, f(x,y,z))
        self.assertEqual(fxyz(0.1, 0., 0.), 0.)
        self.assertEqual(fxyz(-0.1, 0., 0.), 0.)
        self.assertEqual(fxyz(0.4, 0., 0.), 0.)
        self.assertEqual(fxyz(-0.4, 0., 0.), 0.)
        self.assertEqual(fxyz(10., 10., 10.), 0.)
        print(fxyz(4.5, 0, 0))
        return

    pass  # end of fxyz_TestCase

if __name__ == "__main__": unittest.main()

# End of file
