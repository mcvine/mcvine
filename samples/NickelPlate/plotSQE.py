#!/usr/bin/env python
import sys
path = sys.argv[1]
from mccomponents.sample.idf  import readSQE
sqe = readSQE( path )
from histogram.plotter import defaultPlotter
defaultPlotter.plot( sqe )
