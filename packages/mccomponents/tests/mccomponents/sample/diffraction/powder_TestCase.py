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


interactive = False

import unittestX as unittest
import journal

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


import mcni


class TestCase(unittest.TestCase):


    def test1(self):
        # load peaks
        laz = 'Al.laz'
        text = open(laz).read()
        from mccomponents.sample.diffraction.parsers.laz import parse
        peaks = parse(text).peaks
        
        # load structure
        from sampleassembly.crystal.ioutils import xyzfile2unitcell
        xyz = 'Al.xyz'
        structure = xyzfile2unitcell(xyz)
        
        # diffraction pattern
        from mccomponents.sample.diffraction.powder import total_scattering_cross_section, DiffractionPattern
        dp = DiffractionPattern(structure, peaks)
        
        # compute
        for Ei in [10, 100, 1000, 10000]:
            print Ei, total_scattering_cross_section(Ei, dp)
        return
    
    
    def test2(self):
        from mccomponents.sample.diffraction.powder import loadPattern, total_scattering_cross_section
        dp = loadPattern("Al.xyz", "Al.laz")
        import numpy as np
        Ei = np.arange(5, 100, 1.)
        xs = np.zeros(Ei.size, dtype='d')
        for i,e in enumerate(Ei):
            xs[i] = total_scattering_cross_section(e, dp)
            continue
        if interactive:
            import pylab
            pylab.plot(Ei, xs)
            pylab.show()
        return
        
        
    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    global interactive
    interactive = True
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
