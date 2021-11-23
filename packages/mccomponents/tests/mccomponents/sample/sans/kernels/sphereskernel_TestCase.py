#!/usr/bin/env python
#
#


skip = True
need_user_interaction = True

import unittest
import journal


class TestCase(unittest.TestCase):

    interactive = False

    def test(self):
        kernel = makeKernel()
        import mcni
        N = 5
        vi = 3000.
        neutrons = mcni.neutron_buffer( N )
        for i in range(N):
            neutron = mcni.neutron(r=(0,0,0), v=(0,0,vi), time=0, prob=1)
            kernel.scatter(neutron)
            neutrons[i] = neutron
            print(neutrons[i])
            continue
        return

    pass  # end of TestCase


def makeKernel():
    return b.sans_spheres_kernel(0., 100., 1e-3, 0.6, 2)

import mccomponents.sample.sans.bindings as bindings
b = bindings.get('BoostPython')

def main(): unittest.main()
if __name__ == "__main__": main()

# End of file
