#!/usr/bin/env python

"""
CNCS simulation from moderator to sample position.

The configurations are in .../etc/cncs_moderator2sample/
"""

"""
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')
"""

def buildApp():
    from mcvine.applications.InstrumentBuilder import build
    components = [
        'arm1', 'moderator', 'Guide1', 'FChopper', 'tof1b', 'Guide4', 'Chopper2',
        'Guide5', 'Guide6', 'Guide7', 'Guide8', 'Chopper3', 'Guide9', 'Chopper41',
        'Chopper42', 'tof3a', 'Guide10', 'Guide11', 'save_neutrons', 'Div_monh'
    ]
    App = build(components)
    return App


App = buildApp()
name = 'cncs_moderator2sample'

if __name__ == '__main__': App(name).run()
