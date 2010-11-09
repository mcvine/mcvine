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


interactive = False

import unittestX as unittest
import journal

debug = journal.debug( "DOS_TestCase" )
warning = journal.warning( "DOS_TestCase" )


datapath = 'dispersion-example'
filename = 'DOS'
import os
path = os.path.join( datapath, filename )

class TestCase(unittest.TestCase):


    def test0(self):
        from mccomponents.sample.idf.DOS import read
        (filetype, version, comment), e, Z = read( path )
        print filetype, version, comment
        self.assertEqual( filetype, 'DOS' )
        if interactive:
            import pylab
            pylab.plot( e, Z )
            pylab.show()
            raw_input('Press ENTER to continue...')
        return

    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    global interactive
    interactive = True
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
