# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#


__doc__ = """
command line interface
"""

import click, json

# map aliases to long commands
aliases = dict()

# main command
# enable -h seems to interfere with the pyre_app decorator.
# disable it for now
# CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
# @click.group(context_settings=CONTEXT_SETTINGS)
@click.group()
def mcvine():
    return

from ._provenance import save_metadata

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
            App, path = f(ctx)
            import sys
            # path of app need to be sys.argv so that pyre mpi app mechanism
            # can pick this up and run it using mpirun
            sys.argv = [path] + ctx.args
            # create app instance
            app = App(appname)
            # and run
            app.run()
            return
        # nicer cmd name
        _f.__name__ = f.__name__
        _f.__doc__ = f.__doc__
        # register the alias
        # sth like arcs_analyze_beam -> mcvine instrument arcs analyze_beam
        aliases[appname] = '%s %s' % (cmd_prefix, f.__name__)
        return d1(save_metadata(d2(_f)))
    return decorator

# sub-cmds
from . import test, mpi, mantid, phonon, _phonopy
from . import sampleassembly #, kernel
from mcvine.instrument import cli
from mcvine.instruments import cli
from mcstas2 import cli

# workflow
from .. import deployment_info
from mcvine_workflow import cli

# aliases should be the last cmds to import
from . import bash

# End of file 
