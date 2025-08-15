#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
'''


import unittestX as unittest

class TestCase(unittest.TestCase):

    def test(self):
        "fcc Ni dispersion read from idf data directory: primitive reciprocal unitcell"
        disp = makeDispersion()
        Q = bp.vector3
        a = 3.57 # angstrom
        b = 2*N.pi/a
        print(disp.energy(0, Q(0,0,0)))
        for i in range(3):
            print(disp.energy(i, Q(b*1.05,b*1.05,b*1.05)))
        return

    pass  # end of TestCase



def makeDispersion():
    from mccomponents.sample.phonon import periodicdispersion_fromidf
    disp = periodicdispersion_fromidf('phonon-dispersion-fccNi-primitive-reciprocal-unitcell')
    from mccomponents.homogeneous_scatterer import kernelEngine, scattererEngine
    disp = scattererEngine(disp)
    return disp


import numpy as N
import mccomponents.sample.phonon.bindings as bindings
bp = bindings.get('BoostPython')


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
