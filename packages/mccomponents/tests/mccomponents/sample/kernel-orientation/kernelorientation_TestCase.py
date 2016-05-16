#!/usr/bin/env python
#
#


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
            continue
        return
    

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
