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


import mccomposite.mccompositebp as bp

def locate(position, shape):
    from mccomposite.geometry import shapeEngine as cengine
    location = bp.locate( bp.Position( *position ), cengine( shape, "BoostPythonBinding" ) )
    global _location
    return _location[ location ]


_location = None
def _init_location( ):
    global _location
    _location = {
        bp.location.inside: "inside",
        bp.location.onborder: "onborder",
        bp.location.outside: "outside",
        }

    return
    


_init_location()


# version
__id__ = "$Id$"

# End of file 
