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


standalone = True
# skip = False


import unittestX as unittest
import os


componentname = 'E_monitor'
componentfile = '%s.comp' % componentname
projectpath = '%s' % componentname
bpbindingname = '%sbp' % componentname

class TestCase(unittest.TestCase):

    def test(self):
        "codes for boost python binding"
        from mcstas2.wrappers.component2cppClass.component2cppClass import component2cppClass
        klass = component2cppClass( componentfile )

        from mcstas2.utils.parsers import parseComponent
        compinfo = parseComponent( componentfile )
        
        # create directory
        dir = "E_monitor"
        if not os.path.exists(dir):
            os.makedirs(dir)

        from mcstas2.wrappers.pymodule import generate
        sources = generate( compinfo, bpbindingname, projectpath )

        self.assertEqual( sources[0], '%s/%s.py' %(componentname, componentname) )
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

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
