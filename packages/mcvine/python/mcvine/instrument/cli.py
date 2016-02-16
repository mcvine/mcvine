# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from mcvine.cli import mcvine
@mcvine.group()
def instrument():
    return

from mcvine.instruments import cli

# End of file 
