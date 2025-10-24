#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import os
import sys

#get current directory
curdir = os.path.split(__file__)[0]
if curdir == "": curdir = "."

#get all files
files = os.listdir(curdir)

#get names of all test cases
tests = []
for f in files:
    if f.endswith("TestCase.py") and '#' not in f:
        tests.append(f.rstrip('.py'))
    continue

#make a list of test suites
allsuites = []
for test in tests:
    testmodule = __import__(test)
    suite = testmodule.pysuite()
    allsuites.append(suite)
    continue

import unittest
alltests = unittest.TestSuite(allsuites)


import all_tk_tests
if sys.version_info < (3,):
    reload(all_tk_tests)
elif sys.version_info < (3, 4):
    import imp
    imp.reload(all_tk_tests)
else:
    import importlib\
    importlib.reload(all_tk_tests)
tktests = all_tk_tests.alltests
alltests = unittest.TestSuite((alltests, tktests))


#run test
unittest.TextTestRunner(verbosity=2).run(alltests)


# version
__id__ = "$Id: alltests.py 947 2006-05-31 01:51:51Z jiao $"

# End of file 
