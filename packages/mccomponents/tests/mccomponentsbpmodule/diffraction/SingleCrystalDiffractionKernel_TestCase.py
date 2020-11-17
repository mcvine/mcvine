#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, numpy as np
import unittestX as unittest
import journal

debug = journal.debug( "SingleCrystalDiffractionKernel_TestCase" )
warning = journal.warning( "SingleCrystalDiffractionKernel_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test3(self):
        'SingleCrystalDiffractionKernel'
        a = mcnibp.Vector3_double(3.0, 0., 0.)
        b = mcnibp.Vector3_double(0.0, 3., 0.)
        c = mcnibp.Vector3_double(0.0, 0., 3.)
        lattice = mccomponentsbp.Lattice(a,b,c)
        ra = np.array(lattice.ra)
        rb = np.array(lattice.rb)
        rc = np.array(lattice.rc)
        tosort = []
        for h in range(-5, 6):
            for k in range(-5, 6):
                for l in range(-5, 6):
                    if h==0 and k==0 and l==0: continue
                    q = h*ra + k*rb + l*rc
                    hkl = h,k,l
                    tosort.append((np.linalg.norm(q), hkl))
        tosort = sorted(tosort)
        hkllist = mccomponentsbp.vector_HKL(0)
        for q, (h,k,l) in tosort:
            hkl = mccomponentsbp.HKL(h,k,l, 1.)
            hkllist.append(hkl)
        mosaic=5./60/180*np.pi
        delta_d_d=1e-4
        absorption_cross_section=10.
        kernel = mccomponentsbp.SingleCrystalDiffractionKernel(
            lattice, hkllist, mosaic, delta_d_d, absorption_cross_section
        )
        return

    pass  # end of TestCase

if __name__ == "__main__": unittest.main()

# End of file
