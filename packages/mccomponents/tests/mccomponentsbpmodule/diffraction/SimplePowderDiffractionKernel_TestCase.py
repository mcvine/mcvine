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

debug = journal.debug( "SimplePowderDiffractionKernel_TestCase" )
warning = journal.warning( "SimplePowderDiffractionKernel_TestCase" )


import mcni
from mcni import mcnibp
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test1(self):
        'vector<SimplePowderDiffractionData_Peak>'
        peaks = mccomponentsbp.vector_SimplePowderDiffractionData_Peak(2)
        return


    def test2(self):
        'SimplePowderDiffractionData'
        data = mccomponentsbp.SimplePowderDiffractionData()
        peaks = data.peaks
        Peak = mccomponentsbp.SimplePowderDiffractionData_Peak
        peaks.append(Peak())
        self.assertEqual(len(peaks), 1)
        self.assertEqual(len(data.peaks), 1)
        
        peaks[0].q = 10.
        self.assertEqual(data.peaks[0].q, 10.)
        
        data.density = 1.2
        self.assertEqual(data.density, 1.2)
        
        return

    
    def test3(self):
        'SimplePowderDiffractionKernel'
        data = mccomponentsbp.SimplePowderDiffractionData()
        kernel = mccomponentsbp.SimplePowderDiffractionKernel(data)
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
