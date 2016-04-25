#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import mcvine, os
import unittest

class TestCase(unittest.TestCase):


    def test1(self):
        'mcni: relative coordinates for geometer'
        args = [
            'MCVINE_MPI_LAUNCHER=serial',
            'python',
            'geometer_relative_coords_testapp.py',
            '--mode=worker',
            '--geometer.comp0="(0,0,0),(0,0,0)"',
            '--geometer.comp1="(0,0,0),(0,90,0)"',
            '''--geometer.comp2="relative((0,0,1),'comp1'),(0,0,0)"''',
            '''--geometer.comp3="relative((0,0,0),'comp2'),relative((3,4,5),'comp2')"''',
            '''--geometer.comp4="(0,0,0),relative((0,0,90),'comp0')"''',
            '''--geometer.comp5="(0,0,0),relative((0,90,0),'comp4')"''',
            '''--geometer.comp6="relative((1,2,3),'comp5'),(0,0,0)"''',
            '--geometer.dump',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=out.geometer_relative_coords' ,
            '--overwrite-datafiles',
            ]
        cmd = ' '.join(args)
        if os.system(cmd):
            raise RuntimeError("%s failed" %cmd)
        return
        
    pass  # end of TestCase


if __name__ == "__main__": unittest. main()
    
# End of file 
