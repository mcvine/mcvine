#!/usr/bin/env python
#
#


import unittest


class TestCase(unittest.TestCase):


    def test1(self):
        'shape positioning: cylinder'
        from mccomponents.sample import samplecomponent
        scatterer = samplecomponent('sa', 'cyl/sampleassembly.xml' )
        return
    

    pass  # end of scattererxml_TestCase


def main(): unittest.main()

if __name__ == "__main__": main()
    
# End of file 
