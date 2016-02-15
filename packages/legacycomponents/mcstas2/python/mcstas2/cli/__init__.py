# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from mcvine.cli import mcvine

@mcvine.group()
def mcstas():
    return

from . import compilecomponent, convertinstrument

# End of file 
