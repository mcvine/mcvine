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
arcs_app = lambda name: pyre_app(parent=arcs, appname = name, cmd_prefix=cmd_prefix)

@arcs_app("arcs_analyze_beam")
def analyze_beam(ctx, appname):
    from .applications.BeamAnalysis import App
    return App(appname)

@arcs_app('arcs_moderator2sample')
def mod2sample(ctx, appname):
    from .applications.Moderator2Sample import App
    return App(appname)


# End of file 
