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


from mcvine.deployment_info import mcvine_resources
if not mcvine_resources:
    skip = True


import unittestX as unittest
import journal, os

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


import mcni
from mccomponents.sample.phonon import read_dos
import histogram as H

class TestCase(unittest.TestCase):


    def test1(self):
        "dos from ascii"
        p = 'V-dos.dat'
        dos = read_dos.doshist_fromascii(p)
        # H.plot(dos)
        read_dos.dos_fromascii(p)
        return
        
        
    def test2(self):
        "dos from idf"
        # p = 'V-DOS.idf'
        p = os.path.join(
            mcvine_resources, "examples", "samples", "vanadium",
            "phonons", "DOS")
        dos = read_dos.doshist_fromidf(p)
        # H.plot(dos)
        read_dos.dos_fromidf(p)
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
__id__ = "$Id: dispersion_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
