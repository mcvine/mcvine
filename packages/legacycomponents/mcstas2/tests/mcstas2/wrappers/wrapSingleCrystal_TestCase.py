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


# if ran with other tests that wrap components, will segfaults
# skip = True
standalone = False


import unittestX as unittest


componentname = 'Single_crystal'
componentfile = '%s.comp' % componentname
category = 'samples'

class wrap_TestCase(unittest.TestCase):

    def test(self):
        "wrap Single_crystal"
        from mcstas2.wrappers import wrap
        wrap( componentfile, category, buildername='distutils' )
        from mcstas2.components import componentfactory
        factory = componentfactory( category, componentname )
        component = factory(
            'component',
            )
        return

    pass  # end of wrap_TestCase



def pysuite():
    suite1 = unittest.makeSuite(wrap_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# End of file 
