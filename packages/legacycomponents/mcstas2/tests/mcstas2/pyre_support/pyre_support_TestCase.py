#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

standalone = True


import unittestX as unittest
import journal


class TestCase(unittest.TestCase):

    def test1(self):
        args = [
            'MCVINE_MPI_LAUNCHER=serial',
            'python',
            'TestInstrument1.py',
            '--mode=worker',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=pyre_support_test1_out',
            '--overwrite-datafiles',
            ]

        cmd = ' '.join(args)
        import os
        if os.system(cmd):
            raise RuntimeError('%s failed')
        return
    
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()

# End of file 
