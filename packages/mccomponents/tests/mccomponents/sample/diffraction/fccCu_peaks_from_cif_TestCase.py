#!/usr/bin/env python

import numpy as np

def test_write_peaks_py():
    from mccomponents.sample import matter
    structure = matter.loadCif('Cu.cif')
    from mccomponents.sample.diffraction import create_peaks_py
    create_peaks_py('fccCu-peaks_from_cif.py', structure, 300., max_index=5)


def main():
    test_write_peaks_py()
    return


if __name__ == '__main__': main()


# End of file
