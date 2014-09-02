#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import units
meV = units.energy.meV
angstrom = units.length.angstrom


def simplepowderdiffractionkernel(
    Dd_over_d, DebyeWaller_factor, peaks, **kwds
    ):
    from SimplePowderDiffractionKernel import SimplePowderDiffractionKernel as f
    return f(Dd_over_d, DebyeWaller_factor, peaks, **kwds)


import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    import bindings
    return

_import_bindings()



# version
__id__ = "$Id$"

# End of file 
