#!/usr/bin/env python

import os, shutil, numpy as np, histogram.hdf as hh
import histogram.hdf as hh
thisdir = os.path.dirname(__file__)
instr = os.path.join(thisdir, 'spheres_instr.py')

from mcvine import run_script
import unittest

# parameters should be the same as ../xml/sampleassemblies/sans_spheres/sans_spheres-scatterer.xml and that of the sans spheres component in ./spheres_instr.py 
phi, R, delta_rho = 0.1, 500., 0.6
from mcni.utils import conversion
wl = 2*np.pi/conversion.e2k(10.) # 10meV. same as that of Ei in ./spheres_instr.py
mu = 3./2*phi*delta_rho**2*wl**2*R
thickness = 0.001
attenuation = np.exp(-mu*thickness)
print(attenuation)

class TestCase(unittest.TestCase):

    def test_mcvine(self):
        outdir = 'out.mcvine_spheres'
        if os.path.exists(outdir): shutil.rmtree(outdir)
        run_script.run_mpi(
            instr, outdir, ncount=1e8, nodes=20, overwrite_datafiles=True,
            sample_vendor='mcvine',
        )
        I_q = hh.load(os.path.join(outdir, 'I_q.h5'))
        expected = hh.load(os.path.join('expected', 'spheres_iq.h5'))
        ratio = I_q.I/expected.I
        # from matplotlib import pyplot as plt
        # plt.plot(I_q.q, ratio)
        # plt.show()
        good = ((ratio<attenuation*1.03)*(ratio>attenuation*0.97)).sum()
        self.assert_(good>0.98*ratio.size)
        return

    def test_mcstas(self):
        outdir = 'out.mcstas_spheres'
        if os.path.exists(outdir): shutil.rmtree(outdir)
        run_script.run_mpi(
            instr, outdir, ncount=1e8, nodes=10, overwrite_datafiles=True,
            sample_vendor='mcstas',
        )
        I_q = hh.load(os.path.join(outdir, 'I_q.h5'))
        expected = hh.load(os.path.join('expected', 'spheres_iq.h5'))
        ratio = I_q.I/expected.I
        # from matplotlib import pyplot as plt
        # plt.plot(I_q.q, ratio)
        # plt.show()
        good = ((ratio<1.03)*(ratio>0.97)).sum()
        self.assert_(good>0.98*ratio.size)
        return

if __name__ == '__main__': unittest.main()
