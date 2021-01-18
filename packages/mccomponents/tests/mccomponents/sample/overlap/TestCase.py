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
            lastlines = '\n'.join(e.output.decode().splitlines()[-5:])
            assert 'Overlapping' in lastlines
            return
        raise RuntimeError("Expecting exiting with overlapping alert")
        return
    
    def test2(self):
        import subprocess as sp, shlex
        cmd = 'mcvine sampleassembly check %s/Ni_and_Al/good-sampleassembly.xml' % here
        args = shlex.split(cmd)
        out = sp.check_output(args, stderr=sp.STDOUT)
        return
    

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
