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

import mcni


class TestCase(unittest.TestCase):


    def test1(self):
        from dos import loadDOS
        dos = loadDOS()
        # from histogram import plot
        # plot(dos)
        
        # create c object
        from mccomponents.sample.phonon.bindings.BoostPythonBinding  import New
        b = New()
        bpdos = b.dos_fromhistogram(dos)
        
        mass = 51
        temperature = 300
        nsampling = 100
        bpdw = b.dwfromDOS(bpdos, mass, temperature, nsampling)
        self.assertAlmostEqual(bpdw.core(), 0.0067, places=4)
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
__id__ = "$Id: dispersion_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
