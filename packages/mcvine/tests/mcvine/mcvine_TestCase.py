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



import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'mcvine: simulate'
        # this is the example 1 in the mcvine package documentation
        import mcvine
        i = mcvine.instrument()
        g = mcvine.geometer()
        f = mcvine.componentfactory('sources', 'Source_simple', 'mcstas2')
        # help(f)
        s = f()
        i.append(s)
        g.register(s, (0,0,0), (0,0,0))
        neutrons = mcvine.neutron_buffer(5)
        print neutrons
        mcvine.simulate(i, g, neutrons)
        print neutrons
        return

    
    def test2(self):
        'mcvine: list component types'
        # this is the example 3 in the mcvine package documentation
        import mcvine
        mcvine.listallcomponentcategories()
        mcvine.listcomponentsincategory('sources')
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
