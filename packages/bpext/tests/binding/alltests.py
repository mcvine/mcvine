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

#get current directory
curdir = os.path.split(__file__)[0]
if curdir == "": curdir = "."

#get all files
files = os.listdir(curdir)

#get names of all test cases
tests = []
for f in files:
    if f.endswith("TestCase.py"): tests.append(f.rstrip('.py'))
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


#run test
unittest.TextTestRunner(verbosity=2).run(alltests)


# version
__id__ = "$Id: alltests.py 947 2006-05-31 01:51:51Z jiao $"

# End of file 
