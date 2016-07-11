#!/usr/bin/env python

"""
script to run mcvine tests.

It requires cmake and all mcvine dependencies.

It is assumed that the tests are installed under
$MCVINE_DIR/share/mcvine/tests.

The tests will run at a separate work directory.
"""

import os, sys, psutil

prefix = os.path.dirname(os.path.dirname(sys.executable))

if len(sys.argv)>1:
    work = sys.argv[1]
else:
    work = 'work.test'

os.makedirs(work)
os.chdir(work)

from mcvine.deployment_info import mcvinedir
testsdir = os.path.join(mcvinedir, 'share', 'mcvine', 'tests')

cores = os.environ.get('CORES', 2)
conda_py = os.environ.get("CONDA_PY")
pyver = '%s.%s' % (conda_py[0], conda_py[1])
py_lib = '%s/lib/libpython%s.so' % (prefix, pyver)
py_include = '%s/include/python%s' % (prefix, pyver)
cmd = '''cmake -DPYTHON_LIBRARY=%s -DPYTHON_INCLUDE_DIR=%s %s && CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j%s"''' % (py_lib, py_include, testsdir, cores)
sys.exit(os.system(cmd))
