#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import os
import unittest


def findAllTests():
    #get current directory
    curdir = os.path.abspath( os.path.split( __file__ ) [0] )
    if curdir == "": curdir = "."

    #get all files
    files = os.listdir( curdir )

    #get names of all test cases
    tests = []
    for f in files:
        if f.endswith("TestCase.py"): tests.append( f.rstrip('.py') )
        continue

    #make a list of test suites
    allsuites = []
    for test in tests:
        testmodule = __import__( test )
        if hasattr(testmodule, 'pysuite'):
            suite = testmodule.pysuite()
            allsuites.append( suite )
        else:
            testcases = _iterTestCases(testmodule)
            for c in testcases:
                suite = unittest.makeSuite(c)
                allsuites.append(suite)
        continue

    alltests = unittest.TestSuite( allsuites )
    return alltests


def _iterTestCases(mod):
    for item in mod.__dict__.values():
        if item == unittest.TestCase:
            continue
        try:
            t = issubclass(item, unittest.TestCase)
            yield item
        except:
            continue
    return


def main():
    alltests = findAllTests()
    #run test
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__": main()


# version
__id__ = "$Id$"

# End of file 
