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

debug = journal.debug( "GridSQE_TestCase" )
warning = journal.warning( "GridSQE_TestCase" )


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

class GridSQE_TestCase(unittest.TestCase):

    def test1(self):
        'GridSQE'
        sqe = createSqe()
        gridsqe = ms.gridsqe( sqe )
        
        cgridsqe = mh.scattererEngine( gridsqe )
        
        Q, E = 5.05, 10.5
        self.assertAlmostEqual( sqe[ Q,E ][0], sqe_f(Q,E) )
        self.assertAlmostEqual( cgridsqe( Q,E ), sqe_f(Q,E) )
        return

    pass  # end of GridSQE_TestCase



def pysuite():
    suite1 = unittest.makeSuite(GridSQE_TestCase)
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
