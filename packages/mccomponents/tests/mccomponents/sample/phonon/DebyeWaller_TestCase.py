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


class TestCase(unittest.TestCase):


    def test1(self):
        dos = loadDOS()
        from mccomponents.sample.phonon.bindings.BoostPythonBinding  import New
        b = New()
        bpdos = b.dos_fromhistogram(dos)

        mass = 51
        temperature = 300
        nsampling = 100
        bpdw = b.dwfromDOS(bpdos, mass, temperature, nsampling)
        self.assertAlmostEqual(bpdw.core(), 0.00669632)
        return
        
        
    pass  # end of TestCase


def loadDOS():
    f = 'V-dos.dat'
    from mcni.utils.constants import hbar, e
    from math import pi
    # constant to convert frequency on terahertz to energy in meV
    toenergy = hbar * 1e12 * 2*pi / e * 1e3
    
    lines = open(f).readlines()
    es, Is = [], []
    for line  in lines:
        if line.startswith('#'): continue
        line = line.strip()
        e, I = line.split()
        es.append(float(e)*toenergy)
        Is.append(float(I))
        continue
    import histogram
    h = histogram.histogram(
        'dos', 
        [('energy', es, 'meV')],
        Is)
    return h



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
__id__ = "$Id: dispersion_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
