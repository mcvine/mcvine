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

debug = journal.debug( "Dispersion_TestCase" )
warning = journal.warning( "Dispersion_TestCase" )


datapath = 'dispersion-example'

class TestCase(unittest.TestCase):

    def test0(self):
        from mccomponents.sample.idf import readDispersion
        nAtoms, dimension, Qaxes, polarizations, energies, dos \
                = readDispersion( datapath )
        print(nAtoms, dimension, Qaxes)
        print(energies)
        
        if interactive:
            import pylab
            pylab.plot( dos[0], dos[1] )
            pylab.show()
            input('Press ENTER to continue...')
        return

    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    global interactive
    interactive = True
    
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
