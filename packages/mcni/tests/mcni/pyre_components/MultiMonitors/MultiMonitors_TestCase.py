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

class TestCase(unittest.TestCase):

    def test1(self):
        cmd = '''./test-MultiMonitors-app.py \
 --monitor.geometer.m1="(0,0,1),(0,0,0)" \
 --monitor.geometer.m2="(0,0,0),(0,90,0)" \
 --journal.debug.monitor \
'''
        execute(cmd)
        return

    def test2(self):
        cmd = '''./test-MultiMonitors-app.py \
 --monitor.m1=E_monitor \
 --output-dir=out-test2 \
 --overwrite-datafiles \
 --monitor.geometer.m1="(0,0,1),(0,0,0)" \
 --monitor.geometer.m2="(0,0,0),(0,90,0)" \
 --journal.debug.monitor \
'''
        execute(cmd)
        return

    pass # end of TestCase


def execute(cmd):
    import os
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd

def pysuite():
    suite1 = unittest.makeSuite(TestCase)
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
