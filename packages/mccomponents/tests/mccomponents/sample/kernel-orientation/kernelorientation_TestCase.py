#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com

"""
This test check the "orientation" parameter of kernels.

* Sub-kernels in a "KernelContainer" have the parameter "orientation"
  to specify its orientation relative to its parent kernel.
* The root level KernelContainer always has the same coordinate system
  as the scatterer.


In this test the coordinate system of the kernel
is rotated 30 deg around the y axis (vertical up)
with respect to the scatterer.
Roughtly it is illustrated below:

x'        ^ x
   |\     |
     \    |
      \   |            >  z'
       \  |        . '
        \ |    . '
         \|. ' )  30 deg
          -------------------> z

So the transformation matrix is

sqrt(3)/2    0    1/2
   0         1     0
  -1/2       0    sqrt(3)/2

This is specified in cyl/X-scatterer.xml.

In kernel's coordinate system, we set the momentum transfer
of the kernel to be [2,0,0], which is is along x' axis.

The incident neutron is along z axis with energy 100meV.

With these information, we can compute the momentum transfer
in instrument cooridnate system, and then the final energy
and energy transfer E. 
Turns out E = -37.07822meV, and this is set in cyl/X-scatterer.xml.

In the following test, we make sure the final velocities of 
the scattered neutrons are expected, and the neutrons
have valid probabilities.
"""


import unittest, numpy as np


class TestCase(unittest.TestCase):


    def test1(self):
        'kernel orientation'
        # source
        from mcni.components.MonochromaticSource import MonochromaticSource
        import mcni, numpy as np
        Ei = 100
        from mcni.utils import conversion as Conv
        ki = Conv.e2k(Ei)
        vi = Conv.e2v(Ei)
        Qdir = np.array([np.sqrt(3)/2, 0, -1./2])
        Q = Qdir * 2
        kf = np.array([0,0,ki]) - Q
        Ef = Conv.k2e(np.linalg.norm(kf))
        E  = Ei-Ef
        dv = Qdir * Conv.k2v(Q)
        vf = np.array([0,0,vi]) - dv
        # print ki, Q, kf
        # print Ei, Ef, E
        neutron = mcni.neutron(r=(0,0,-1), v=(0,0,vi), prob=1)
        source = MonochromaticSource('s', neutron, dx=0.001, dy=0.001, dE=0)
        # sample
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'cyl/sampleassembly.xml' )
        # incident
        N = 1000
        neutrons = mcni.neutron_buffer(N)
        neutrons = source.process(neutrons)
        # print neutrons
        # scatter
        scatterer.process(neutrons)
        # print neutrons
        self.assertEqual(len(neutrons), N)
        for neutron in neutrons:
            np.allclose(neutron.state.velocity, vf)
            self.assert_(neutron.probability > 0)
            continue
        return
    

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
