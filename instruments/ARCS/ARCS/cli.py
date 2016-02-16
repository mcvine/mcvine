# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from ..cli import instrument
from mcvine.cli import pyre_app

@instrument.group()
def arcs():
    return


cmd_prefix = "mcvine instrument arcs "
@pyre_app(parent=arcs, appname = 'arcs_analyze_beam', cmd_prefix=cmd_prefix)
def analyze_beam(ctx, appname):
    from .applications.BeamAnalysis import App
    return App(appname)


# End of file 
