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
        'mccomponents.sample.samplecomponent: IsotropicKernel for a fictitious simple cubic Fe'
        import os
        cmd = './ssd -ncount=1e5 -buffer_size=100000'
        # cmd = './ssd -ncount=1 -buffer_size=1'
        # cmd += ' --journal.debug.CompositeNeutronScatterer_Impl'
        ret = os.system(cmd)

        if ret:
            raise RuntimeError, '%s failed ' % cmd
        return
    

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
