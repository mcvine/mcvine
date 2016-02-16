# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click
from ..cli import instrument

@instrument.group()
def arcs():
    return


@arcs.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def analyze_beam(ctx):
    appname = 'arcs_analyze_beam'
    import sys
    sys.argv = [appname] + ctx.args
    from .applications.BeamAnalysis import App
    app = App('arcs_analyze_beam')
    app.run()
    return


# End of file 
