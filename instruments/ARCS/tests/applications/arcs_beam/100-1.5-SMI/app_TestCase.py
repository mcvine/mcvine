#!/usr/bin/env python

import subprocess as sp, os, shlex

import unittest
class TestCase(unittest.TestCase):

    def test(self):
        workdir = os.path.abspath(os.path.dirname(__file__))
        sp.check_call(
            shlex.split("mcvine instruments arcs beam --E=100 --ncount=1e5"), 
            shell=False, cwd=workdir)
        return


if __name__ == '__main__': unittest.main()

# End of file 
