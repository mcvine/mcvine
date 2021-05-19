#!/usr/bin/env python
#
#


import unittest
import journal


class fxy_TestCase(unittest.TestCase):

    def test1(self):
        import mccomponents.mccomponentsbp as b
        sv = b.vector_double(100)
        fxy = b.new_fxy(
            -5., 5., 1.,
            -5., 5., 1.,
            sv
        )
        print(fxy(0., 0.))
        return

    pass  # end of fxy_TestCase

if __name__ == "__main__": unittest.main()

# End of file
