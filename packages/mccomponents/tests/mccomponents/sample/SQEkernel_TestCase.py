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

debug = journal.debug( "SQEkernel_TestCase" )
warning = journal.warning( "SQEkernel_TestCase" )


sqe_f = lambda q,e: q*q+e*e 
def createSqe():
    import histogram as H
    qaxis = H.axis( 'Q', boundaries = H.arange(0, 13.0, 0.1) )
    eaxis = H.axis( 'energy', boundaries = H.arange(-50, 50, 1.0) )
    sqe = H.histogram(
        'sqe',
        [ qaxis, eaxis ],
        fromfunction = sqe_f
        )
    return sqe


import mcni, mccomposite, mccomponents.sample as ms, mccomponents.homogeneous_scatterer as mh

class SQEkernel_TestCase(unittest.TestCase):

    def test1(self):
        'SQEkernel'
        sqe = createSqe()
        gridsqe = ms.gridsqe( sqe )
        sqekernel = ms.sqekernel(
            1., 1., 1.,
            SQE=gridsqe,
            Qrange=(0, 12.), Erange=(-50, 50) )
        
        csqekernel = mh.scattererEngine( sqekernel )
        
        ev = mcni.neutron( r = (-5,0,0), v = (3000,0,0) )
        self.assertAlmostEqual( csqekernel.absorption_coefficient(ev), 1 )
        return

    pass  # end of SQEkernel_TestCase



def pysuite():
    suite1 = unittest.makeSuite(SQEkernel_TestCase)
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
