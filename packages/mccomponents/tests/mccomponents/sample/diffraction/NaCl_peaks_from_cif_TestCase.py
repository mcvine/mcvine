#!/usr/bin/env python

import numpy as np

def test_write_peaks_py():
    from mccomponents.sample import matter
    structure = matter.loadCif('NaCl.cif')
    from mccomponents.sample.diffraction import create_peaks_py
    create_peaks_py(
        'NaCl-peaks_from_cif.py', structure, 300., max_index=15, min_dspacing=0.70)

def main():
    test_write_peaks_py()
    return

if __name__ == '__main__': main()

# End of file
