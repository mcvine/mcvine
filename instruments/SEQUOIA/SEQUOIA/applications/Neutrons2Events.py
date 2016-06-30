#!/usr/bin/env python


__doc__ = """
convert scattereed neutrons to events (pixelID, tofChannelNo, prob)
intercepted by SEQUOIA detector system.

Examples:

 $ sequoia-neutrons2nxs --neutrons=scattered-neutrons-example
"""

__implementation__ = """
This script runs a mcvine instrument simulation script consisting
of two components, a neutron player and a detector system.

The neutron player replay the neutrons stored in a neutron
storage. Those neutrons were scattered off of a sample
in SEQUOIA beam.

The detector system is of SEQUOIA.

"""


appname = 'sequoia_neutrons2events'
cmd_help = __doc__


# main methods
def run(neutrons, workdir, **kwds):
    neutrons = os.path.abspath(neutrons)
    workdir = os.path.abspath(workdir)
    if os.path.exists(workdir):
        raise IOError("%s already exists" % workdir)
    os.makedirs(workdir)
    eventdat = sendneutronstodetsys(neutronfile=neutrons, workdir=workdir, **kwds)
    return


def sendneutronstodetsys(
    neutronfile=None, scattering_rundir=None, nodes=None, ncount=None,
    workdir = None, tofbinsize = None,
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
        'detsys.instrumentxml': sequoiaxml,
        'detsys.eventsdat': 'events.dat',
        'ncount': ncount,
        'source.path': neutronfile,
        }
    if nodes:
        from mcni.pyre_support.MpiApplication \
            import mpi_launcher_choice as launcher
        args['%s.nodes' % launcher] = nodes
    cmd += ['--%s=%s' % (k,v) for k,v in args.iteritems()]
    cmd = ' '.join(cmd)
    run_sh = os.path.join(workdir, 'run.sh')
    open(run_sh, 'w').write(cmd+'\n')
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


# utils
import os, subprocess as sp, shlex
def execute(cmd, workdir):
    print '* executing %s... ' % cmd
    args = shlex.split(cmd)
    p = sp.Popen(args, cwd=workdir)
    p.communicate()
    if p.wait():
        raise RuntimeError, "%r failed" % cmd
    return


import numpy as np
from mcvine import resources as res
import os, subprocess as sp

#
sequoiaxml = os.path.join(
    res.instrument('SEQUOIA'), 'detsys', 'sequoia.xml.fornxs')

