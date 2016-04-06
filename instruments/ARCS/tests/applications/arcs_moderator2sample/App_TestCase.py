#!/usr/bin/env python
#

import os
cwd = os.path.dirname(__file__)

def execute(cmd):
    import subprocess as sp
    p = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=cwd)
    out, err = p.communicate()
    if p.wait():
        raise RuntimeError, "%s failed.\nOUT:%s\nERR:%s\n" % (
            cmd, out, err)
    return out, err


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        cmd = "bash run.sh"
        out, err = execute(cmd)
        return


    pass  # end of TestCase



def main(): unittest.main()
if __name__ == "__main__":  main()
    
# End of file 
