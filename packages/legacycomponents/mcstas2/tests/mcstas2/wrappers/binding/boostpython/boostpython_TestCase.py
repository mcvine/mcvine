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


# skip = False
standalone = True


import unittestX as unittest
import os


componentname = 'E_monitor'
componentfile = '%s.comp' % componentname
projectpath = '%s' % componentname
bpbindingname = '%sbp' % componentname
wrapmethodname = 'wrap_E_monitor'

class boostpython_TestCase(unittest.TestCase):

    def test(self):
        "codes for boost python binding"
        # create directory
        dir = componentname
        if not os.path.exists(dir):
            os.makedirs(dir)

        from mcstas2.wrappers.binding.boostpython.module_cc import generate
        module_cc = generate( bpbindingname, wrapmethodname, projectpath )

        from mcstas2.wrappers.component2cppClass.component2cppClass import component2cppClass
        klass = component2cppClass( componentfile )

        from mcstas2.utils.mills.cxx.factory import createHHandCC
        createHHandCC( klass, projectpath )
        
        ctor = klass.constructors() [0]
        from mcstas2.wrappers.binding.boostpython.wrap_cc import generate
        wrap_cc = generate( klass, projectpath, wrapmethodname)

        return

    pass  # end of boostpython_TestCase



def pysuite():
    suite1 = unittest.makeSuite(boostpython_TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
