#!/usr/bin/env python

"""
script to run mcvine tests.

It requires cmake and all mcvine dependencies.

It is assumed that the tests are installed under
$MCVINE_DIR/share/mcvine/tests.

The tests will run at a separate work directory.
"""

import os
cmd = 'CORES=2 mcvine test'
print("THIS test is about to run")
if os.system(cmd):
    raise RuntimeError("%s failed" % cmd)
