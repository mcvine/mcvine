#!/usr/bin/env python

standalone = True

import os, subprocess as sp, shlex, numpy as np, shutil
os.environ['MCVINE_MPI_BINDING'] = 'NONE'
here = os.path.abspath(os.path.dirname(__file__))

import unittest
class TestCase(unittest.TestCase):


    def test1(self):
        'kernel: E_Q_Kernel flat S(Q)'
        shutil.rmtree('out')
        cmd = "./ssm --ncount=1e5 --journal.debug.instrument"
        args = shlex.split(cmd)
        sp.check_call(args, cwd=here)
        import histogram.hdf as hh
        iqe = hh.load('out/iqe_monitor.h5')
        iq = iqe.sum('energy')[(2,9)]
        I = iq.I
        median = np.median(I)
        diff = np.abs(I-median)/median
        self.assert_((diff<0.2).all())
        return

    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__": main()
    
# End of file 
