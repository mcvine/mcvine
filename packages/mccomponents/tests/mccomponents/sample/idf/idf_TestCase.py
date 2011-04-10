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


skip = True



import unittestX as unittest
import journal

debug = journal.debug( "idf_TestCase" )
warning = journal.warning( "idf_TestCase" )


datapath = 'SQE-examples'

class idf_TestCase(unittest.TestCase):


    def test0(self):
        import histogram as H
        qaxis = H.axis( 'Q', boundaries = H.arange(0, 13.0, 0.1) )
        eaxis = H.axis( 'energy', boundaries = H.arange(-50, 50, 1.0) )
        sqe = H.histogram(
            'sqe',
            [ qaxis, eaxis ],
            fromfunction = lambda q,e: q*q+e*e )
        from mccomponents.sample.idf import writeSQE
        writeSQE( sqe, datapath )
        return

    def test1(self):
        from mccomponents.sample.idf import readSQE
        sqe = readSQE( datapath )
        import pickle
        pickle.dump(sqe, open('sqehist.pkl','w') )
        return

    def test2(self):
        import os
        os.system( 'PlotHist.py sqehist.pkl' )
        return

    pass  # end of idf_TestCase



def pysuite():
    suite1 = unittest.makeSuite(idf_TestCase)
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
