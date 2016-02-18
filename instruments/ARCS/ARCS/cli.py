# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from ..cli import instrument
from mcvine.cli import pyre_app, alias

cmd_prefix = "mcvine instrument arcs "

@instrument.group()
@alias("arcs", cmd_prefix)
def arcs():
    return

arcs_app = lambda name: pyre_app(parent=arcs, appname = name, cmd_prefix=cmd_prefix)

# beam sim
@arcs_app("arcs_analyze_beam")
def analyze_beam(ctx, appname):
    from .applications.BeamAnalysis import App
    return App(appname)

@arcs_app('arcs_moderator2sample')
def mod2sample(ctx, appname):
    "moderator to sample simulation"
    from .applications.Moderator2Sample import App
    return App(appname)

@arcs_app('arcs_m2s')
def m2s(ctx, appname):
    "simplified moderator to sample simulation app"
    from .applications.M2S import App
    return App(appname)

@arcs_app('arcs_beam')
def beam(ctx, appname):
    "beam simulation. include mod2sample sim and post-processing"
    from .applications.Beam import App
    return App(appname)


# detsys sim
@arcs.command(help="""convert scattereed neutrons to events (pixelID, tofChannelNo, prob)
intercepted by ARCS detector system.""")
@click.argument("neutrons", default="neutrons.dat")
@click.option("--workdir", default='work-arcs-neutrons2events')
@click.option("--nodes", default=0)
@click.option("--ncount", default=None)
@alias("arcs_neutrons2events", "%s neutrons2events" % cmd_prefix)
def neutrons2events(neutrons, workdir, nodes, ncount):
    from .applications.Neutrons2Events import run
    run(neutrons, workdir, nodes, ncount=ncount)
    return
    

# End of file 
