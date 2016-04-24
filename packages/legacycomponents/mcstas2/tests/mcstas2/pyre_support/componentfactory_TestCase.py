#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


skip = False
standalone = True


import unittestX as unittest
import journal


class TestCase(unittest.TestCase):

    def test1(self):
        args = [
            'MCVINE_MPI_LAUNCHER=serial',
            'python',
            'componentfactory_demoapp.py',
            '--mode=worker',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=componentfactory_testcase_out',
            '--overwrite-datafiles',
            ]
        cmd = ' '.join(args)
        import os
        if os.system(cmd):
            raise RuntimeError('%s failed')
        return
    
    pass  # end of TestCase


def main():
    unittest.main()
    return
    
    
if __name__ == "__main__": main()
    
# End of file 
