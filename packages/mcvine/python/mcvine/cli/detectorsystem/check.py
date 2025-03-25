# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, click, warnings, tempfile, yaml
thisdir = os.path.abspath(os.path.dirname(__file__))
from mcvine import run_script as mrs
import mantid2mcvine as m2m
from . import detectorsystem

@detectorsystem.command()
@click.argument("xml")
@click.option("--ncount", default=1e3)
@click.option("--nodes", default=10)
def checkxml(xml, ncount, nodes):
    script = os.path.join(thisdir, '_s2d.py')
    tmpdir = tempfile.mkdtemp(suffix='mcvine-check-ds')
    mrs.run_mpi(script, tmpdir, ncount, nodes, xml=xml, overwrite_datafiles=True)
    return

@detectorsystem.command()
@click.argument("ymlfile")
@click.option("--ncount", default=1e6)
@click.option("--nodes", default=10)
@click.option("--outnxs", default='sim.nxs')
def checkyml(ymlfile, ncount, nodes, outnxs):
    if os.path.exists(outnxs):
        raise IOError("{} already exists".format(outnxs))
    im = m2m.InstrumentModel(**yaml.safe_load(open(ymlfile, 'rt')))
    script = os.path.join(thisdir, '_s2d.py')
    tmpdir = tempfile.mkdtemp(suffix='mcvine-check-ds-yaml')
    mrs.run_mpi(script, tmpdir, ncount, nodes, overwrite_datafiles=True)
    # !rm -rf n2e/ {outnxs}
    scattered = os.path.join(tmpdir, 'saved.mcv')
    n2edir = os.path.join(tmpdir, 'n2e')
    events = im.neutrons2events(scattered, nodes=nodes, workdir=n2edir)
    simnxs = im.events2nxs(events, outnxs)
    print(simnxs)
    return

# End of file
