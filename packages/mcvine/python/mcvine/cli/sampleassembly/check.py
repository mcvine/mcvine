# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, click

from . import sampleassembly
@sampleassembly.command()
@click.argument("xml")
def check(xml):
    # import mccomponents.sample.phonon.xml
    from mccomponents.sample import samplecomponent
    c = samplecomponent("s", xml)
    c.checkShapeOverlap()
    return


# End of file 
