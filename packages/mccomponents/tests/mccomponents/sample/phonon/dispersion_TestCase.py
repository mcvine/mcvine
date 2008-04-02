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
import journal

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


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
        print qs, es
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
        es = [ disp.energy(0, binding.Q(q)) for q in qs ]
        print qs, es

        q = qx, qy, qz = 1.2, 0.3, 0.22
        Q = binding.Q( q )
        self.assertAlmostEqual(
            disp.energy(0, binding.Q( qx + 2*ra, qy + 8*ra, qz - 6*ra )),
            disp.energy(0, Q ), 3 )
                                            
        return
        
        
    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
