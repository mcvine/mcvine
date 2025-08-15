#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import os, numpy as np, mcni
from mcni.utils import conversion as muc
from mcni.neutron_storage import readneutrons_asnpyarr
os.environ['MCVINE_MPI_BINDING'] = 'NONE'

standalone = True
batch = True
nsfile = 'SCtest-scattered.mcv'
a = 4.04932
ra = 2*np.pi/a
ki = ra * 4
Ei = muc.k2e(ki)

import unittestX as unittest

class TestCase(unittest.TestCase):

    def test1(self):
        'mccomponents.sample: SingleCrystalDiffractionKernel'
        instrument, geometer = createInstrument()
        # clean up
        if os.path.exists(nsfile): os.remove(nsfile)
        # simulate
        if batch:
            N0 = 300000
        else:
            N0 = 30
        neutrons = mcni.neutron_buffer(N0)
        mcni.simulate( instrument, geometer, neutrons )
        if batch:
            self._analyze()
        else:
            self._print(neutrons)
        return

    def _analyze(self):
        neutrons = readneutrons_asnpyarr(nsfile)
        v = neutrons[:, 3:6]
        p = neutrons[:, -1]
        k_vec = muc.v2k(v)
        k = np.linalg.norm(k_vec, axis=1)
        ki_vec = [0., 0., ki]
        Q = ki_vec - k_vec
        #
        assert(np.allclose(k, ki, rtol=0.05))
        N = k.size
        hkls =  np.round(Q/ra).astype(int)
        unique_hkls = np.unique(hkls, axis=0)
        probs = {}; Ns = {}
        for hkl in unique_hkls:
            mask = np.all(hkls == hkl, axis=1)
            N1 = mask.sum()
            if N1 < N/800.: continue
            p1 = p[mask].sum()/N
            t_hkl = tuple(hkl.tolist())
            probs[t_hkl] = p1
            Ns[t_hkl] = mask.sum()
        self.assertEqual(len(probs), 5)
        expected = [(0,0,8), (0, 4, 4), (0, -4, 4), (4, 0, 4), (-4, 0, 4)]
        # print(probs)
        # print(Ns)
        self.assertTrue(sorted(expected)==sorted(list(probs.keys())))
        for hkl in expected:
            if hkl == (0,0,8): continue
            self.assertTrue(np.isclose(probs[hkl], 3.76e-41, atol=0.1e-41))
            # the following are good when constants in units_conversion.h were not calculated from formulas
            # self.assertTrue(np.isclose(probs[hkl], 3.9e-41, atol=0.1e-41))
            # self.assertTrue(np.isclose(Ns[hkl], N//4, atol=np.sqrt(N)*2))
            continue
        return

    def _print(self, neutrons):
        N = len(neutrons)
        print(N)
        # check
        import numpy.linalg as nl
        for i in range(N):
            neutron = neutrons[i]
            print(neutron)
            # Vf = np.array(neutron.state.velocity)
            continue
        return

    pass  # end of TestCase

def createInstrument():
    from mcstas2 import componentfactory as cf
    f = cf('sources', 'Source_simple')
    component1 = f(
        name = "component1",
        E0=Ei, dE=Ei*1e-10,
        height = 1e-10, width = 1e-10, radius=0,
        dist=10,
        xw = 1e-10, yh = 1e-10,
        )
    from mccomponents.sample import samplecomponent
    import mccomponents.sample.diffraction.xml
    component2 = samplecomponent( 'Al', 'sampleassemblies/Al-singlecrystaldiffractionkernel/sampleassembly.xml' )

    from mcni.components.NeutronToStorage import NeutronToStorage
    component3 = NeutronToStorage('save', nsfile)
    instrument = mcni.instrument( [component1, component2, component3] )
    geometer = mcni.geometer()
    geometer.register( component1, (0,0,0), (0,0,0) )
    geometer.register( component2, (0,0,10), (0,0,0) )
    geometer.register( component3, (0,0,10), (0,0,0) )
    return instrument, geometer

def main():
    unittest.main()
    return

if __name__ == "__main__": main()

# End of file
