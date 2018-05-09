#!/usr/bin/env python

import os, subprocess as sp, shlex, unittest

class TestCase(unittest.TestCase):

    def test1(self):
        cmd = "mcvine sampleassembly check collimator/sampleassembly.xml"
        args = shlex.split(cmd)
        sp.check_call(args)
        return


if __name__ == '__main__': unittest.main()
