#!/usr/bin/env python

"""
ARCS simulation from moderator to sample position.

The configurations are in ../etc/arcs_moderator2sample/

Make sure to read ../../README
"""

"""
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')
"""

from mcvine.instruments.ARCS.Instrument import Instrument as App
name = 'arcs_moderator2sample'

if __name__ == '__main__': App(name).run()
