#!/usr/bin/env python
"""
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')
"""

from mcvine.applications.InstrumentBuilder import build
components = ['source', 'monitor']
App = build(components)
name = 'sequoia_analyze_beam'

if __name__ == '__main__': App(name).run()

