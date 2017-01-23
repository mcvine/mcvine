# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from ..cli import instruments
from mcvine.cli import pyre_app, alias

cmd_prefix = "mcvine instruments hyspec "

@instruments.group()
@alias("hyspec", cmd_prefix)
def hyspec():
    return

hyspec_app = lambda name: pyre_app(parent=hyspec, appname = name, cmd_prefix=cmd_prefix)

# beam sim
@hyspec_app('hyspec_moderator2sample') # has to match the name of the pyre app for pml lookup
def mod2sample(ctx):
    "moderator to sample simulation"
    from .applications import Moderator2Sample as mod
    return mod.App, mod.__file__

@hyspec_app('hyspec_config_m2s')
def config_mod2sample(ctx):
    "simplified moderator to sample simulation app"
    from .applications import Config_Moderator2Sample as mod
    return mod.App, mod.__file__

@hyspec_app('hyspec_beam')
def beam(ctx):
    "beam simulation. include mod2sample sim and post-processing"
    from .applications import Beam as mod
    return mod.App, mod.__file__


@hyspec.command(help="""convert scattereed neutrons to nexus file

Impl.: mcvine.instruments.HYSPEC.applications.Neutrons2Nxs
""")
@click.option("--neutrons", default="", help='path to neutron data file')
@click.option("--nxs", default="hyspec-sim.nxs", help='nexus output path')
@click.option("--workdir", default='work-hyspec-neutrons2nxs', help="working dir to save intermediate data fiels")
@click.option("--nodes", default=0)
@click.option("--type", default="raw", type=click.Choice(['processed', 'raw']))
@click.option("--populate-metadata/--no-populate-metadata", default=False)
@click.option("--beam", default="", help='beam simulation path. need only when populate-metadata is True')
@alias("hyspec_neutrons2nxs", "%s neutrons2nxs" % cmd_prefix)
@click.pass_context
def neutrons2nxs(ctx, neutrons, nxs, workdir, nodes, type, populate_metadata, beam):
    if not neutrons:
        click.echo(ctx.get_help(), color=ctx.color)
        return
    from .applications.Neutrons2Nxs import run
    run(neutrons, nxs, type, workdir, nodes)

    if populate_metadata:
        import os, shutil
        # save a copy
        base, ext = os.path.splitext(nxs)
        nometadata = base+"_no_metadata"+ext
        shutil.copyfile(nxs, nometadata)
        # populate
        from .applications import nxs as nxsmod
        beam_out = os.path.abspath(os.path.join(beam, 'out'))
        nxsmod.populate_Ei_data(beam_out, nxs)
    return


# nexus file utilities
@hyspec.group()
def nxs():
    "nexus utils"
    return

@nxs.command()
@click.option('--beam_outdir', help='path to the output directory of hyspec beam simulation')
@click.option('--nxs', help='path to the nexus file to be decorated')
@click.option('--sample', default=0., help='sample angle (psi)')
@click.option('--detector', default=0., help='angle of detector system')
@alias("hyspec_nxs_populate_metadata", "%s nxs populate_metadata" % cmd_prefix)
@click.pass_context
def populate_metadata(ctx, beam_outdir, nxs, sample, detector):
    "populate metadata into the simulated nexus file"
    if not nxs or not beam_outdir:
        click.echo(ctx.get_help(), color=ctx.color)
        return
    from .applications import nxs as nxsmod
    f = getattr(nxsmod, "populate_metadata")
    f(beam_outdir, nxs, sample, detector)
    return


# End of file 
