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

debug = journal.debug( "LinearlyInterpolatedDispersion_3D_TestCase" )
warning = journal.warning( "LinearlyInterpolatedDispersion_3D_TestCase" )


import mcni
from mccomposite import mccompositebp 
from mccomponents import mccomponentsbp

class TestCase(unittest.TestCase):

    def test(self):
        nQs = 20
        Qx_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -10, 1., nQs )
        Qy_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -10, 1., nQs )
        Qz_axis = mccomponentsbp.LinearlyInterpolatableAxis_dbl( -10, 1., nQs )
        nAtoms = 5
        nDims = 3
        nBranches = nAtoms*nDims
        import numpy
        eps_data = numpy.zeros(
            ( nQs+1, nQs+1, nQs+1, nBranches, nAtoms, nDims, 2 ),
            dtype = numpy.double)
        E_data = numpy.zeros(
            ( nQs+1, nQs+1, nQs+1, nBranches ),
            dtype = numpy.double)

        from mccomponents.sample.phonon.bindings import get
        binding = get('BoostPython')
        eps_arr = binding.ndarray( eps_data )
        E_arr = binding.ndarray( E_data )

        disp = mccomponentsbp.LinearlyInterpolatedDispersionOnGrid_3D_dblarrays(
            nAtoms, Qx_axis, Qy_axis, Qz_axis, eps_arr, E_arr )
        return

    pass  # end of TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
