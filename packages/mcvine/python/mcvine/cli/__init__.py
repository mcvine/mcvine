# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


__doc__ = """
command line interface
"""

import click

# map aliases to long commands
aliases = dict()

# main command
@click.group()
def mcvine():
    return

# shortcut for pyre app
def pyre_app(parent, appname, cmd_prefix):
    def decorator(f):
        d1 = parent.command(
            context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
        d2 = click.pass_context
        def _f(ctx):
            import sys
            sys.argv = [appname] + ctx.args
            app = f(ctx, appname)
            app.run()
            return
        _f.__name__ = f.__name__
        aliases[appname] = '%s %s' % (cmd_prefix, f.__name__)
        return d1(d2(_f))
    return decorator        

# sub-cmds
from . import mpi, sampleassembly #, kernel
from mcvine.instrument import cli
from mcstas2 import cli

# aliases should be the last cmds to import
from . import bash_aliases

# version
__id__ = "$Id$"

# End of file 
