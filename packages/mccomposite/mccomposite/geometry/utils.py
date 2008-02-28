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


import mccomposite.bindings as bindings
defaultbinding = bindings.default()
del bindings


def locate(position, shape):
    from mccomposite.geometry import shapeEngine as cengine
    location = defaultbinding.locate(
        defaultbinding.position( position ),
        cengine( shape, "BoostPythonBinding" )
        )
    return location


# version
__id__ = "$Id$"

# End of file 
