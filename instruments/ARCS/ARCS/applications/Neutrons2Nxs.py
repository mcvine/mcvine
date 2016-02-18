#!/usr/bin/env python


"""
convert scattereed neutrons to nexus file.
"""


appname = 'arcs-neutrons2nxs'
cmd_help = """
convert scattereed neutrons to nexus file.

Examples:

 $ arcs-neutrons2nxs --neutrons=scattered-neutrons-example --nodes=2
"""
tofbinsize = 0.1 # microsecond


import os
from .utils import execute


# main methods
def run(neutrons, nxs, type, workdir, nodes):
    import time
    eventdat = sendneutronstodetsys(neutronfile=neutrons, workdir=os.path.join(workdir, 'todetsys'), nodes=nodes)
    time.sleep(10)
    event2nxs(eventdat, nxs, type, os.curdir)
    return


def sendneutronstodetsys(
    neutronfile=None,
    nodes=None,
    workdir = None,
    ):
    d = locals()
    cmd = 'mcvine instrument arcs neutrons2events %(neutronfile)s --nodes=%(nodes)s --workdir=%(workdir)s' % d
    execute(cmd, os.curdir)
    return os.path.join(workdir, 'out', 'events.dat')


def event2nxs(eventdat, nxs, type, workdir):
    d = dict(globals())
    d.update(locals())
    cmd = 'mcvine instrument arcs events2nxs %(eventdat)s %(nxs)s --type=%(type)s --tofbinsize=%(tofbinsize)s' % d
    execute(cmd, workdir)
    return

