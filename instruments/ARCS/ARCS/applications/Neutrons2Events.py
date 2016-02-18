#!/usr/bin/env python


__doc__ = """
convert scattereed neutrons to events (pixelID, tofChannelNo, prob)
intercepted by ARCS detector system.

Examples:

 $ arcs_neutrons2evens scattered-neutrons-example
"""


appname = 'arcs_neutrons2events'
cmd_help = __doc__
tofbinsize = 0.1 # microsecond


# main methods
def run(neutrons, workdir, nodes, ncount=None):
    neutrons = os.path.abspath(neutrons)
    workdir = os.path.abspath(workdir)
    if os.path.exists(workdir):
        raise IOError("%s already exists" % workdir)
    os.makedirs(workdir)
    eventdat = sendneutronstodetsys(
        neutronfile=neutrons, workdir=workdir, nodes=nodes, ncount=ncount)
    return


def sendneutronstodetsys(
    neutronfile=None, scattering_rundir=None, nodes=None, ncount=None,
    workdir = None,
    ):
    """
    run a simulation to send neutrons to det system
    
    workdir: directory where the simulation is run
    """
    # create workdir if it does not exist
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        
    # number of neutrons scattered
    if not neutronfile:
        neutronfile = os.path.join(scattering_rundir, 'out', 'scattered-neutrons')
    if not ncount:
        from mcni.neutron_storage.idf_usenumpy import count
        ncount = count(neutronfile)
        
    # create simulation command
    cmd_name = 'sd'
    sim_cmd = os.path.join(workdir, cmd_name)
    open(sim_cmd, 'wt').write(sd_txt)
    
    
    # build command
    cmd = ['python '+cmd_name]
    args = {
        'source': 'NeutronFromStorage',
        'detsys': 'DetectorSystemFromXml',
        'output-dir': 'out',
        'detsys.tofparams': '0,0.02,%s' % (1e-6*tofbinsize,), 
        'detsys.instrumentxml': arcsxml,
        'detsys.eventsdat': 'events.dat',
        'ncount': ncount,
        'source.path': neutronfile,
        }
    if nodes:
        args['mpirun.nodes'] = nodes
    cmd += ['--%s=%s' % (k,v) for k,v in args.iteritems()]
    cmd = ' '.join(cmd)
    run_sh = os.path.join(workdir, 'run.sh')
    open(run_sh, 'w').write(cmd+'\n')
    from .utils import execute
    execute(cmd, workdir)

    # events.dat
    outfile = os.path.join(workdir, 'out', 'events.dat')
    return outfile

sd_txt = """
import mcvine
from mcvine.applications.InstrumentBuilder import build
components = ['source', 'detsys']
App = build(components)
app = App('sd')
app.run()
"""


import numpy as np
from mcvine import resources
import os

#
arcsxml = os.path.join(
    resources.instrument('ARCS'), 'resources', 'ARCS.xml.fornxs')


