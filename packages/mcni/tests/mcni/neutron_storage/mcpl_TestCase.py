#!/usr/bin/env python
#

import unittestX as unittest
import os, numpy as np
import mcni.neutron_storage as mns
import mcni.neutron_storage.mcpl as mcpl
toarr = mns.neutrons_as_npyarr

class TestCase(unittest.TestCase):

    def test(self):
        import mcni
        neutrons = mcni.neutron_buffer( 7 )
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron(
                r=(i,i,i), v = (i+1,i+1,i+1), s=(np.pi/6,np.pi/3),
                time=2, prob=3
            )
        mns.dump(neutrons, 'neutrons.mcv')
        mcpl.mcv2mcpl("neutrons.mcv", "neutrons.mcpl")
        mcpl.mcpl2mcv('neutrons.mcpl.gz', 'neutrons2.mcv', False)
        neutrons2 = mns.load('neutrons2.mcv')
        assert np.allclose(toarr(neutrons), toarr(neutrons2))
        return

if __name__ == "__main__":
    unittest.main()

# End of file
