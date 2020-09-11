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
        from mccomponents.sample.sansmodel import sansspheremodel_kernel
        scale=1.0e-6
        radius=60.0 #A
        contrast=1.0 #A-2
        background=0 #cm-1

        absorption_cross_section = 0
        scattering_cross_section = 1
        Qmin = 0
        Qmax = 10
        k = sansspheremodel_kernel(
            scale, radius, contrast, background,
            absorption_cross_section, scattering_cross_section,
            Qmin, Qmax)

        from mccomponents.sample import scattererEngine
        kengine = scattererEngine( k )

        print(dir(kengine))

        n = mcni.neutron( r = (0,0,0), v = (0,0,3000) )
        kengine.scatter( n )
        print(n)
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
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
