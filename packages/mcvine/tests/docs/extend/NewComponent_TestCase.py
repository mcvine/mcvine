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


interactive = False

simapp = 'sd'
outdir = 'out'

import os, glob, shutil
def cleanup():
    # clean up
    if os.path.exists(outdir):
        shutil.rmtree('out')


def execute(cmd):
    if os.system(cmd):
        raise RuntimeError, "%r failed" %cmd


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'create and use new component'
        cmd = './sd -ncount=5'
        execute(cmd)
        return

    
    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    global interactive
    interactive = True
    main()
    
# version
__id__ = "$Id$"

# End of file 
