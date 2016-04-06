#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import os, subprocess as sp
from mcvine.resources import instrument


cwd = os.path.abspath(os.path.dirname(__file__))

def execute(cmd):
    import subprocess as sp, shlex
    p = sp.Popen(shlex.split(cmd), shell=False, stdout=sp.PIPE, stderr=sp.PIPE, cwd=cwd)
    out, err = p.communicate()
    if p.wait():
        raise RuntimeError, "%s failed.\nOUT:%s\nERR:%s\n" % (
            cmd, out, err)
    print out, err
    return out, err


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        source_file = os.path.join(instrument('ARCS'), "moderator/source_sct521_bu_17_1.dat")
        cmd = "mcvine instruments arcs m2s -E=100 --- --moderator.S_filename=%s --ncount=1e5 --buffer_size=10000 --overwrite-datafiles" % source_file
        execute(cmd)
        return


    pass  # end of TestCase



def main(): unittest.main()
if __name__ == "__main__":  main()
    
# End of file 
