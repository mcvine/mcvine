#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest
import journal

debug = journal.debug( "mcni.components.test" )
warning = journal.warning( "mcni.components.test" )



class TestCase(unittest.TestCase):


    def test1(self):
        'NeutronFromStorage'
        from mcni.components.NeutronFromStorage import NeutronFromStorage
        comp = NeutronFromStorage('storage', 'neutron-storage-for-NeutronFromStorage_TestCase')

        from mcni import neutron_buffer
        neutrons = neutron_buffer(1)
        comp.process(neutrons)
        self.assertEqual(neutrons[0].probability, 9)
        comp.process(neutrons)
        self.assertEqual(neutrons[0].probability, 19)
        return


    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":  main()

    
# version
__id__ = "$Id$"

# End of file 
