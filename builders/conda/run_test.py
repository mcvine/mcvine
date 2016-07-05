#!/usr/bin/env python

"""
script to run mcvine tests.

It requires cmake and all mcvine dependencies.

It is assumed that the tests are installed under
$MCVINE_DIR/share/mcvine/tests.

The tests will run at a separate work directory.
"""

import os, sys, psutil

if len(sys.argv)>1:
    work = sys.argv[1]
else:
    work = 'work.test'

os.makedirs(work)
os.chdir(work)

from mcvine.deployment_info import mcvinedir
testsdir = os.path.join(mcvinedir, 'share', 'mcvine', 'tests')

cores = os.environ.get('CORES', 2)
cmd = '''cmake %s && env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j%s"''' % (testsdir, cores)
sys.exit(os.system(cmd))
