# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from ..cli import instruments
from mcvine.cli import pyre_app, alias

cmd_prefix = "mcvine instruments sns "

@instruments.group()
@alias("sns", cmd_prefix)
def sns():
    return

sns_app = lambda name: pyre_app(parent=sns, appname = name, cmd_prefix=cmd_prefix)

# detsys sim
@sns.command(help="""convert scattereed neutrons to events (pixelID, tofChannelNo, prob)
intercepted by SNS detector system.""")
@click.argument("neutrons", default="neutrons.dat")
@click.option("--workdir", default='work-sns-neutrons2events')
@click.option("--nodes", default=0)
@click.option("--ncount", default=0)
@click.option("--tofbinsize", default=0.1, help="unit: mus")
@click.option("--tofmax", default=0.2, help="unit: second")
@click.option("--instrument", default=None, help="instrument name. for detsys xml lookup")
@click.option("--detsys", default='', help="path to detsys xml")
@click.option("--detsys-z-rot", default=0., help="rotation angle of det sys")
@alias("sns_neutrons2events", "%s neutrons2events" % cmd_prefix)
def neutrons2events(neutrons, workdir, nodes, ncount, tofbinsize,tofmax, instrument,detsys, detsys_z_rot):
    from .applications.Neutrons2Events import run
    run(
        neutrons, workdir, nodes, ncount=ncount,
        tofbinsize=tofbinsize, tofmax=tofmax,
        instrument=instrument, detsys=detsys,
        z_rotation=detsys_z_rot,
    )
    return
    
@sns.command(help="""convert events.dat (generated by neutrons2events) to nxs file""")
@click.argument("events", default="events.dat")
@click.argument("nxs", default="sns-sim.nxs")
@click.option("--tofbinsize", default=0.1)
@click.option("--type", default="processed", type=click.Choice(['processed', 'raw']))
@click.option("--instrument", default=None, help="instrument name. for detsys xml lookup")
@alias("sns_events2nxs", "%s events2nxs" % cmd_prefix)
def events2nxs(events, nxs, tofbinsize, type, instrument):
    from .applications.Events2Nxs import run
    run(events, nxsfile=nxs, tofbinsize=tofbinsize, type=type, instrument=instrument)
    return
    
@sns.command(help="""convert scattereed neutrons to nexus file

Impl.: mcvine.instruments.SNS.applications.Neutrons2Nxs
""")
@click.option("--neutrons", default="", help='path to neutron data file')
@click.option("--nxs", default="sns-sim.nxs", help='nexus output path')
@click.option("--type", default="raw", type=click.Choice(['processed', 'raw']))
@click.option("--workdir", default='work-sns-neutrons2nxs', help="working dir to save intermediate data fiels")
@click.option("--nodes", default=0)
@click.option("--instrument", default=None, help="instrument name. for detsys xml lookup")
@click.option("--detsys", default='', help="path to detsys xml")
@click.option("--detsys-z-rot", default=0., help="rotation angle of det sys")
@click.option("--tofbinsize", default=0.1, help="unit: mus")
@click.option("--tofmax", default=0.2, help="unit: second")
@click.option("--populate-metadata/--no-populate-metadata", default=False)
@click.option("--beam", default="", help='beam simulation path. need only when populate-metadata is True')
@alias("sns_neutrons2nxs", "%s neutrons2nxs" % cmd_prefix)
@click.pass_context
def neutrons2nxs(
        ctx, neutrons, nxs, type, workdir, nodes,
        instrument, detsys, detsys_z_rot, tofbinsize, tofmax,
        populate_metadata, beam):
    if not neutrons:
        click.echo(ctx.get_help(), color=ctx.color)
        return
    from .applications.Neutrons2Nxs import run
    run(neutrons, nxs, type, workdir, nodes, instrument, detsys_z_rot, detsys, tofbinsize, tofmax)

    if populate_metadata:
        import os, shutil
        # save a copy
        base, ext = os.path.splitext(nxs)
        nometadata = base+"_no_metadata"+ext
        shutil.copyfile(nxs, nometadata)
        # populate
        prefix = 'mcvine.instruments.%s.nxs' % instrument.upper()
        mod = '%s.%s' % (prefix, type)
        nxsmod = __import__(mod, fromlist = [''])
        beam_out = os.path.abspath(os.path.join(beam, 'out'))
        nxsmod.populate_Ei_data(beam_out, nxs)
    return


# End of file 
