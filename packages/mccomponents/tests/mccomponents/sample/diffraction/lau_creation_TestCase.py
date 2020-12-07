#!/usr/bin/env python

import numpy as np

def test_write_lau():
    from mccomponents.sample import matter
    structure = matter.loadCif('Si.cif')
    # from sampleassembly.crystal.ioutils import xyzfile2unitcell as xyz2u
    # structure = xyz2u('Si.cif')
    from mccomponents.sample.diffraction import create_lau
    create_lau('Si.lau', structure, 300., max_index=10)


def main():
    test_write_lau()
    return


if __name__ == '__main__': main()

# End of file
