#!/usr/bin/env python


import unittest

class TestCase(unittest.TestCase):

    def test(self):
        cmd = "events2iqe events.dat 3 intensities.dat 9 11 0.1 80 120 1.0 700.0 arcs-pixelID2position.bin arcs-solidangles.bin 117760 1e-6 13.6 0 15000.0"
        
        import subprocess as sp
        p = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = p.communicate()
        if p.wait():
            raise RuntimeError, "%s failed with error:\n%s\n" % (
                cmd, err)
        self.assertEqual(eval( out), (20,40))
        return


def main():
    unittest.main()
    return


if __name__ == '__main__': main()

