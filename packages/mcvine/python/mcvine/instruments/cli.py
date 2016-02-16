# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import importlib
from ..instrument.cli import instrument

instruments = ['ARCS']
for inst in instruments:
    mod = "mcvine.instruments.%s.cli" % inst
    importlib.import_module(mod)
    continue

# End of file 
