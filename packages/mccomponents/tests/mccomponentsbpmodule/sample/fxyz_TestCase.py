#!/usr/bin/env python
#
#


import os, numpy as np, unittest
import journal


class fxyz_TestCase(unittest.TestCase):

    def test1(self):
        import mccomponents.mccomponentsbp as b
        a = np.arange(1000, dtype='double')
        sv = b.vector_double(1000)
        sv[:] = a
        fxyz = b.new_fxyz(
            -5., 5., 1.,
            -5., 5., 1.,
            -5., 5., 1.,
            sv
        )
        print(fxyz(0., 0., 0.))
        print(fxyz(10., 10., 10.))
        return

    pass  # end of fxyz_TestCase

if __name__ == "__main__": unittest.main()

# End of file
