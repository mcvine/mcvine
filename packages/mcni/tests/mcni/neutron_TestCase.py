#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
Test neutron and neutron buffer interfaces
"""


import unittestX as unittest
import journal

debug = journal.debug( "neutron_TestCase" )
warning = journal.warning( "neutron_TestCase" )


import mcni

class TestCase(unittest.TestCase):


    def test1(self):
        "neutron: import"
        from mcni import neutron
        return
    
        
    def test2(self):
        "neutron"
        from mcni import neutron
        n = neutron(r=(0,0,0), v=(0,0,3000))
        n = neutron(r=(0,0,0), v=(0,0,3000), time=1000.)
        n = neutron(r=(0,0,0), v=(0,0,3000), time=1000., prob=10.)
        n = neutron(r=(0,0,0), v=(0,0,3000), s=(0,1), time=1000., prob=10.)
        return


    def test3(self):
        "neutron buffer: import"
        from mcni import neutron_buffer
        return
    
        
    def test4(self):
        "neutron buffer: swap"
        from mcni import neutron_buffer
        b1 = neutron_buffer(1)
        b2 = neutron_buffer(2)
        b1.swap(b2)
        self.assertEqual(len(b1), 2)
        self.assertEqual(len(b2), 1)
        return
    
        
    def test5(self):
        "neutron buffer: appendNeutrons"
        from mcni import neutron_buffer
        b1 = neutron_buffer(1)
        b2 = neutron_buffer(2)
        
        b1.appendNeutrons(b2, 0, len(b2))
        self.assertEqual(len(b1), 3)
        
        b1.appendNeutrons(b2)
        self.assertEqual(len(b1), 5)
        return
    
        
    def test6(self):
        "neutron buffer: get element"
        from mcni import neutron_buffer
        b1 = neutron_buffer(1)
        n = b1[0]
        # print n
        return


    def test7(self):
        "neutron buffer: set element"
        from mcni import neutron_buffer, neutron
        b1 = neutron_buffer(1)
        n = neutron(r=(0,10,0))
        b1[0] = n
        self.assertEqual(b1[0].state.position[1], 10)
        return


    def test8(self):
        "neutron buffer: clear"
        from mcni import neutron_buffer, neutron
        
        b1 = neutron_buffer(10)
        self.assertEqual(len(b1), 10)

        b1.clear()
        self.assertEqual(len(b1), 0)
        return


    def test9(self):
        "neutron buffer: snapshot"
        from mcni import neutron_buffer, neutron
        
        b1 = neutron_buffer(10)
        self.assertEqual(len(b1), 10)
        b1[5] = neutron(prob=-1)

        b2 = b1.snapshot()
        self.assertEqual(len(b2), 9)

        b2 = b1.snapshot(9)
        self.assertEqual(len(b2), 8)

        b2 = b1.snapshot(4)
        self.assertEqual(len(b2), 4)
        return


    def test10(self):
        "neutron buffer <-> numpy array"
        from mcni import neutron_buffer, neutron
        nb = neutron_buffer(3)
        a = nb.to_npyarr()
        a[0,3]= 5
        nb.from_npyarr(a)
        self.assertEqual(nb[0].state.velocity[0], 5)

        import numpy
        b = numpy.arange(50.)
        nb.from_npyarr(b)
        self.assertEqual(nb[3].state.velocity[0], 33)
        self.assertEqual(nb[2].state.position[0], 20)
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
__id__ = "$Id: mcni_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
