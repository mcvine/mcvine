#!/usr/bin/env python

"""
SEQUOIA simulation from moderator to sample position.
The configurations are in ../../etc/sequoia_moderator2sample/
Make sure to read ../../README
"""

import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')

# import journal
# journal.error("pyre.inventory").activate()

from mcvine.instruments.SEQUOIA.Instrument import Instrument
name = 'sequoia_moderator2sample'
App = Instrument

if __name__ == '__main__': App(name).run()


