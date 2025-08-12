#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest



class TestCase(unittest.TestCase):


    def test_MonochromaticSource(self):
        'mcni.pyre_support.componentfactory: sources/MonochromaticSource'
        from mcni.pyre_support import componentfactory
        f = componentfactory( 'sources', 'MonochromaticSource' )
        from mcni.pyre_components.MonochromaticSource import MonochromaticSource
        self.assertEqual( f, MonochromaticSource )
        return


    def test_NeutronFromStorage(self):
        'mcni.pyre_support.componentfactory: sources/NeutronFromStorage'
        from mcni.pyre_support import componentfactory
        f = componentfactory( 'sources', 'NeutronFromStorage' )
        from mcni.pyre_components.NeutronFromStorage import NeutronFromStorage
        self.assertEqual( f, NeutronFromStorage )
        return


    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
