#!/usr/bin/env python
#
#


import os
here = os.path.abspath(os.path.dirname(__file__))


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        import subprocess as sp, shlex
        cmd = 'mcvine sampleassembly check %s/Ni_and_Al/sampleassembly.xml' % here
        args = shlex.split(cmd)
        try:
            out = sp.check_output(args, stderr=sp.STDOUT)
        except sp.CalledProcessError as e:
            lastline = e.output.splitlines()[-1]
            assert 'Overlapping" in lastline'
            return
        raise RuntimeError("Expecting exiting with overlapping alert")
        return
    

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
