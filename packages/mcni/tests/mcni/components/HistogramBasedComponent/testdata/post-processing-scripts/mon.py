from mcni.components.HistogramBasedMonitorMixin import merge_and_normalize
import os
here = os.path.dirname(__file__)
simdir = os.path.join(here, '..')
merge_and_normalize('mon.h5', simdir)
