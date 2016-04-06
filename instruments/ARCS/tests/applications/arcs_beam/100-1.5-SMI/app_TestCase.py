#!/usr/bin/env python

import subprocess as sp, os

import unittest
class TestCase(unittest.TestCase):

    def test(self):
        workdir = os.path.dirname(__file__)
        sp.check_call("bash run", shell=True, cwd=workdir)
        return


if __name__ == '__main__': unittest.main()

# End of file 
