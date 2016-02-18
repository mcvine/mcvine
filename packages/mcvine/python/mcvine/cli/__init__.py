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

# decorator to create bash alias of a command
def alias(shortname, longname):
    def decorate(f):
        aliases[shortname] = longname
        return f
    return decorate

# decorator for pyre app
def pyre_app(parent, appname, cmd_prefix):
    def decorator(f):
        # pass extra args and options to pyre app
        d1 = parent.command(
            context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
        d2 = click.pass_context
        def _f(ctx):
            # build the sys argv list for pyre app
            import sys
            sys.argv = [appname] + ctx.args
            # create app instance
            app = f(ctx, appname)
            # and run
            app.run()
            return
        # nicer cmd name
        _f.__name__ = f.__name__
        _f.__doc__ = f.__doc__
        # register the alias
        # sth like arcs_analyze_beam -> mcvine instrument arcs analyze_beam
        aliases[appname] = '%s %s' % (cmd_prefix, f.__name__)
        return d1(d2(_f))
    return decorator

# sub-cmds
from . import mpi, sampleassembly #, kernel
from mcvine.instrument import cli
from mcstas2 import cli

# aliases should be the last cmds to import
from . import bash

# version
__id__ = "$Id$"

# End of file 
