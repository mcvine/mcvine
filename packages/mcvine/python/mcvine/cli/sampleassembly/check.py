# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os, click
import warnings

from . import sampleassembly
@sampleassembly.command()
@click.argument("xml")
def check(xml):
    # import mccomponents.sample.phonon.xml
    from mccomponents.sample import samplecomponent
    c = samplecomponent("s", xml)
    c.checkShapeOverlap()
    # check multiple scattering setting
    import  mcni
    neutron = mcni.neutron(r=(0,0,0), v=(0,0,1))
    from mccomposite import mccompositebp
    nsegments = mccompositebp.countIntersections(neutron, c.shape())/2
    if c.max_multiplescattering_loops_among_scatterers < nsegments:
        warnings.warn("For multiple-scattering, `max_multiplescattering_loops_among_scatterers` should be larger than %s." % nsegments)
    if c.min_neutron_probability == 0:
        warnings.warn("Please set `min_neutron_probability` to a positive value to avoid excessive multiple-scattering loops")
    return


# End of file 
