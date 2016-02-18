# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import importlib

import click
from mcvine.cli import mcvine
@mcvine.group()
def instruments():
    return

instrument_list = ['ARCS']
for inst in instrument_list:
    mod = "mcvine.instruments.%s.cli" % inst
    importlib.import_module(mod)
    continue

# End of file 
