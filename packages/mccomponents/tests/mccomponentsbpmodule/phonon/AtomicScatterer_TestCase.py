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

debug = journal.debug( "AtomicScatterer_TestCase" )
warning = journal.warning( "AtomicScatterer_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        'AtomicScatterer'
        position = mcnibp.Position_double( 0,0,0 )
        mass = 50
        import math
        coherent_scattering_length = math.sqrt(5)
        coherent_cross_section = 5
        atom = mccomponentsbp.AtomicScatterer(
            position, mass, coherent_scattering_length, coherent_cross_section,
            )
        return


    def test2(self):
        'vector<AtomicScatterer>'
        atoms = mccomponentsbp.vector_AtomicScatterer(2)
        return

    pass  # end of TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
