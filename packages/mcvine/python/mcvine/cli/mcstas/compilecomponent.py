# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, click

from . import mcstas
@mcstas.command()
@click.option("--debug/--no-debug", default=False)
@click.option("--filename")
@click.option("--type")
@click.option("--category")
def compilecomponent(debug=None, type=None, category=None, filename=None):
    if debug:
        import mcstas2
        mcstas2.DEBUG = True

    if filename:
        if not os.path.exists(filename):
            raise IOError("File %r does not exist" % filename)
        click.echo("Compiling %s..." % filename)
        compileFile(filename, category)
        return
    
    from mcvine import findcomponentfactory
    click.echo("Compiling component %s in category %r ..." % (
        type, category))
    cf = findcomponentfactory(
        type=type, category=category or None, supplier='mcstas2',
        )
    # instantiate a component will trigger automatic build procedure
    cf()
    return


def compileFile(filename, category):
    from mcstas2 import wrapcomponent
    wrapcomponent(filename, category)
    return


# End of file 
