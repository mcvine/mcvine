#!/usr/bin/env python

import subprocess as sp, os, shlex

import unittest
class TestCase(unittest.TestCase):

    def test(self):
        workdir = os.path.abspath(os.path.dirname(__file__))
        workdir = os.path.join(workdir, '_work.beam_Ei100')
        if not os.path.exists(workdir):
            os.makedirs(workdir)
        sp.check_call(
            shlex.split("mcvine instruments sequoia beam --E=100 --ncount=1e7 --nodes=2"), 
            shell=False, cwd=workdir)
        return


if __name__ == '__main__': unittest.main()

# End of file 
