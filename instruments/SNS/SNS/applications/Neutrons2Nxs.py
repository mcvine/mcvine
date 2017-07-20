#!/usr/bin/env python
#


"""
convert scattereed neutrons to nexus file.
"""


cmd_help = """
convert scattereed neutrons to nexus file.

Examples:

 $ <cmd> --help
 $ <cmd> --neutrons=scattered-neutrons-example --nxs=out.nxs --nodes=2
"""


# main methods
def run(
        neutrons, nxs, type,
        workdir, nodes,
        instrument, z_rotation, detsys,
        tofbinsize=0.1, tofmax=1.0
):
    neutrons = os.path.abspath(neutrons)
    nxs = os.path.abspath(nxs)
    workdir = os.path.abspath(workdir)
    if os.path.exists(workdir):
        # raise IOError("%s already exists" % workdir)
        pass
    else:
        os.makedirs(workdir)
    import time
    eventdat = sendneutronstodetsys(
        neutronfile=neutrons,
        workdir=os.path.join(workdir, 'todetsys'), nodes=nodes,
        instrument=instrument, z_rotation=z_rotation, detsys=detsys,
        tofbinsize=tofbinsize, tofmax=tofmax)
    time.sleep(10)
    event2nxs(eventdat, nxs, type, workdir, instrument, tofbinsize)
    return


def sendneutronstodetsys(
        neutronfile=None,
        nodes=None,
        workdir = None,
        instrument = None,
        z_rotation = None,
        detsys = None,
        tofbinsize = None,
        tofmax = None,
):
    outfile = os.path.join(workdir, 'out', 'events.dat')
    if os.path.exists(outfile) and os.path.getmtime(outfile)>os.path.getmtime(neutronfile):
        return outfile
    d = locals()
    cmd = 'mcvine instruments sns neutrons2events %(neutronfile)s --nodes=%(nodes)s --workdir=%(workdir)s --instrument=%(instrument)s --detsys-z-rot=%(z_rotation)s' % d
    if detsys:
        cmd += ' --detsys=%(detsys)s' % d
    if tofbinsize:
        cmd += ' --tofbinsize=%(tofbinsize)s' % d
    if tofmax:
        cmd += ' --tofmax=%(tofmax)s' % d
    execute(cmd, os.curdir)
    return outfile


def event2nxs(eventdat, nxs, type, workdir, instrument, tofbinsize):
    d = locals()
    cmd = 'mcvine instruments sns events2nxs %(eventdat)s %(nxs)s --type=%(type)s --tofbinsize=%(tofbinsize)s --instrument=%(instrument)s' % d
    execute(cmd, workdir)
    return


# utils
import os, subprocess as sp, shlex
def execute(cmd, workdir):
    print '* executing %s... at %s' % (cmd, workdir)
    args = shlex.split(cmd)
    p = sp.Popen(args, cwd=workdir)
    p.communicate()
    if p.wait():
        raise RuntimeError, "%r failed" % cmd
    return


# End of file 
