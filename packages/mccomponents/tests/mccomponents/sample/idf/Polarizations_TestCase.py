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

debug = journal.debug( "Polarizations_TestCase" )
warning = journal.warning( "Polarizations_TestCase" )


datapath = 'dispersion-example'
filename = 'Polarizations'
import os
path = os.path.join( datapath, filename )

class TestCase(unittest.TestCase):


    def test0(self):
        from mccomponents.sample.idf.Polarizations import read
        (filetype, version, comment), Polarizations = read( path )
        print filetype, version, comment
        self.assertEqual( filetype, 'Polarizations' )
        import numpy
        self.assertEqual( type(Polarizations), numpy.ndarray )
        print len(Polarizations)
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
