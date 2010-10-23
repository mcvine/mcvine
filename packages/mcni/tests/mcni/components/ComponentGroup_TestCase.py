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


from mcni.AbstractComponent import AbstractComponent
class C( AbstractComponent ):

    def __init__(self):
        self.count = 0

    def process(self, neutrons):
        self.count = len(neutrons)
        return neutrons
    

    
class TestCase(unittest.TestCase):


    def test0(self):
        'ComponentGroup'
        comps = [C() for i in range(10)]
        from mcni.components.ComponentGroup import ComponentGroup
        cg = ComponentGroup('cg', comps)
        import mcni
        b = mcni.neutron_buffer(10)
        cg.process(b)
        for c in comps:
            self.assertEqual(c.count, 10)
            continue
        return

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
