# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group(help='Commands to manipulate neutron storage')
def neutronstorage():
    return

@neutronstorage.command()
@click.argument("path")
def count(path):
    from mcni.neutron_storage.idf_usenumpy import count
    print count(path)
    return


# End of file 
