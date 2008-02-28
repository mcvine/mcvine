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

debug = journal.debug( "mcnimodule_TestCase" )
warning = journal.warning( "mcnimodule_TestCase" )


import mcni

class mcnimodule_TestCase(unittest.TestCase):

    def test1(self):
        'numpy array --> spin'
        import numpy
        arr = numpy.array( [1., 2.] )
        from numpyext import getdataptr
        ptr = getdataptr( arr )
        from bpext import wrap_ptr
        import mcni.mcni
        spin = wrap_ptr( ptr, 'NeutronSpin' )
        self.assertEqual( spin.s1, 1 )
        self.assertEqual( spin.s2, 2 )
        return

    def test2(self):
        'numpy array --> cevent'
        import numpy
        arr = numpy.arange( 0, 10, 1. )
        from numpyext import getdataptr
        ptr = getdataptr( arr )
        from bpext import wrap_ptr
        import mcni.mcni
        event = wrap_ptr( ptr, 'cNeutronEvent' )
        self.assertEqual( event.x, 0 )
        self.assertEqual( event.y, 1 )
        self.assertEqual( event.z, 2 )
        return

    def test3(self):
        'numpy array --> event buffer'
        import numpy
        arr = numpy.arange( 0, 20, 1. )
        from numpyext import getdataptr
        ptr = getdataptr( arr )
        from bpext import wrap_ptr
        import mcni.mcni
        cevents = wrap_ptr( ptr, 'cNeutronEvent' )

        events = mcni.neutron_buffer(2)
        events.fromCevents( cevents, 2 )

        for event in events: print event
        return

    pass  # end of mcnimodule_TestCase

    
def pysuite():
    suite1 = unittest.makeSuite(mcnimodule_TestCase)
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
