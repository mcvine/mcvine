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

debug = journal.debug( "Qgridinfo_TestCase" )
warning = journal.warning( "Qgridinfo_TestCase" )


datapath = 'dispersion-example'
filename = 'Qgridinfo'
import os
path = os.path.join( datapath, filename )

class TestCase(unittest.TestCase):


    def test0(self):
        from mccomponents.sample.idf.Qgridinfo import read
        Qgridinfo = read( path )
        print Qgridinfo
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
