#!/usr/bin/env python


import unittest

class TestCase(unittest.TestCase):

    def test1(self):
        from mcvine.instruments.HYSPEC import instrument_spec as insspec
        insspec.computeOptions(
            Edes = 20, E_min = 10, E_max = 30,
            )
        return


def main():
    unittest.main()
    return

if __name__ == '__main__': 
    main()
