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


class TestCase(unittest.TestCase):


    def test(self):
        from mccomponents.sample.phonon.register_LinearlyInterpolatedDispersion_3D import linearlyinterpolateddispersion_3d_bp as factory
        
        nQs = 21
        Q_axis = -10, 1., nQs
        Q_axes = [Q_axis, Q_axis, Q_axis]
        nAtoms = 5
        nDims = 3
        nBranches = nAtoms*nDims
        import numpy
        eps_data = numpy.zeros(
            ( nQs, nQs, nQs, nBranches, nAtoms, nDims, 2 ),
            dtype = numpy.double)
        E_data = numpy.zeros(
            ( nQs, nQs, nQs, nBranches ),
            dtype = numpy.double)

        disp = factory( nAtoms, Q_axes, eps_data, E_data )
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
