#!/usr/bin/env python

import unittest, os, sys, subprocess as sp, shlex, numpy as np
import mcvine, mcvine.resources
from mcni.neutron_storage.idf_usenumpy import count


class TestCase(unittest.TestCase):

    def test_from_mcpl(self):
        "mcvine neutronstorage from_mcpl"
        # test data "test.mcpl.gz" is created using script "run_make_mcpl_file.sh"
        cmd = "mcvine neutronstorage from_mcpl --out test.mcv test.mcpl.gz"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        cmd = "mcvine neutronstorage print --n 10 --start=0 test.mcv"
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)


if __name__ == '__main__': unittest.main()
