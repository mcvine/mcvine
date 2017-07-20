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
