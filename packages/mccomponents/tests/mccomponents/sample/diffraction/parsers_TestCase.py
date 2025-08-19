#!/usr/bin/env python
#
#

import os
here = os.path.dirname(__file__)
datadir = os.path.join("../../..", 'data')


import unittestX as unittest

import mcni


class TestCase(unittest.TestCase):


    def test1(self):
        laz = os.path.join(datadir, 'Al.laz')
        text = open(laz).read()
        from mccomponents.sample.diffraction.parsers.laz import parse
        peaks = parse(text).peaks
        print(peaks)
        return
        
    def test2(self):
        laz = os.path.join(datadir, 'B4C.laz')
        text = open(laz).read()
        from mccomponents.sample.diffraction.parsers.laz import parse
        peaks = parse(text).peaks
        print(peaks)
        return
        
    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
