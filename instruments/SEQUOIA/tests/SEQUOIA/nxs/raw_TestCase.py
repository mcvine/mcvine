#!/usr/bin/env python
#
# Jiao Lin <linjiao@caltech.edu>

import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        "SEQUOIA.nxs.raw"
        from mcvine.instruments.SEQUOIA.nxs import raw
        import os
        assert os.path.exists(raw.nxs_template)
        return

    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
if __name__ == "__main__": main()
    
# End of file 
