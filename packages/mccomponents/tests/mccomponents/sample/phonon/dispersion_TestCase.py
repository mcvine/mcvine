#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest
import numpy as np

import mcni


datapath = 'phonon-dispersion'


class TestCase(unittest.TestCase):


    def test1(self):
        from mccomponents.sample.phonon import dispersion_fromidf
        dispersion = dispersion_fromidf( datapath )
        
        from mccomponents.sample import scattererEngine
        disp = scattererEngine( dispersion )

        a = 3.52 # Ni lattice parameter
        from math import pi
        ra = 2*pi/a # reciprocal lattice parameter
        N = 10 
        qs = [ (0, 0, ra * i/N) for i in range(N) ]
        from mccomponents.sample.phonon.bindings import default
        binding = default()
        es = [ disp.energy(0, binding.Q(q)) for q in qs ]
        print(qs, es)
        return


    def test2(self):
        from mccomponents.sample.phonon import periodicdispersion_fromidf
        dispersion = periodicdispersion_fromidf( datapath )
        
        from mccomponents.sample import scattererEngine
        disp = scattererEngine( dispersion )

        a = 3.52 # Ni lattice parameter
        from math import pi
        ra = 2*pi/a # reciprocal lattice parameter
        N = 10 
        qs = [ (0, 0, ra * i/N) for i in range(N) ]
        from mccomponents.sample.phonon.bindings import default
        binding = default()
        Es1 = [
            [ disp.energy(ibr, binding.Q(q)) for ibr in range(3) ]
            for q in qs
        ]
        pols1 = [
            [[disp.polarization(ibr, iatom, binding.Q(q)) for iatom in range(1)]
             for ibr in range(3)]
            for q in qs
        ]

        q = qx, qy, qz = 1.2, 0.3, 0.22
        Q = binding.Q( q )
        self.assertAlmostEqual(
            disp.energy(0, binding.Q( qx + 2*ra, qy + 8*ra, qz - 6*ra )),
            disp.energy(0, Q ), 3 )

        Qarr = np.array(qs)
        Es2 = np.zeros((len(qs), disp.nBranches()))
        disp.energy_arr(binding.ndarray(Qarr), binding.ndarray(Es2))
        self.assertTrue(np.allclose( np.array(Es1), Es2 ))

        real_pols2 = np.zeros( (len(qs), disp.nBranches(), disp.nAtoms(), 3) )
        imag_pols2 = np.zeros( (len(qs), disp.nBranches(), disp.nAtoms(), 3) )
        disp.polarization_arr(binding.ndarray(Qarr), binding.ndarray(real_pols2), binding.ndarray(imag_pols2))
        pols2 = real_pols2 + 1j*imag_pols2
        self.assertTrue(np.allclose( np.array(pols1), pols2 ))

        Nq = 1000000
        Qbigarr = np.zeros((Nq, 3))
        Ebigarr = np.zeros((Nq, disp.nBranches()))
        disp.energy_arr(binding.ndarray(Qbigarr), binding.ndarray(Ebigarr))
        realpolbigarr = np.zeros((Nq, disp.nBranches(), disp.nAtoms(), 3))
        imagpolbigarr = np.zeros((Nq, disp.nBranches(), disp.nAtoms(), 3))
        disp.polarization_arr(binding.ndarray(Qarr), binding.ndarray(realpolbigarr), binding.ndarray(imagpolbigarr))
        return
        
        
    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
