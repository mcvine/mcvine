#!/usr/bin/env python

import numpy as np
from mccomponents.sample.diffraction import calcpeaks

from fccNi import fccNi


def test_F_i():
    assert np.isclose(calcpeaks.F_i(0, fccNi, (1,1,1), 300), 10.11, rtol=0.002)
    return

def test_F():
    assert np.isclose(calcpeaks.F(fccNi, (1,1,1), 300), 40.44, rtol=0.002)
    assert np.isclose(calcpeaks.F(fccNi, (2,0,0), 300), 40.19, rtol=0.002)
    assert np.isclose(calcpeaks.F(fccNi, (4,4,4), 300), 30.6, rtol=0.002)
    return

def test_d():
    assert np.isclose(calcpeaks.d(fccNi.lattice, (1,1,1)), 2.03447)
    return

def test_peaks():
    for pk in calcpeaks.iter_peaks(fccNi, 300):
        print pk
    return


def test_write_peaks_py():
    from mccomponents.sample.diffraction import create_peaks_py
    create_peaks_py('fccNi-peaks.py', fccNi, 300., max_index=5)


def main():
    test_F_i()
    test_F()
    test_d()
    test_peaks()
    test_write_peaks_py()
    return


if __name__ == '__main__': main()


# End of file
