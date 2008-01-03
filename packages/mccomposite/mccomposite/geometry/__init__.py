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


def locate(position, shape):
    import mccomposite.mccompositebp as b
    from mccomposite import scattererEngine as cengine
    location = b.locate( b.Position( *position ), cengine( shape, "BoostPythonBinding" ) )
    global _location
    return _location[ location ]


_location = None
def _init_location( ):
    import mccomposite.mccompositebp as b
    global _location
    _location = {
        b.location.inside: "inside",
        b.location.onborder: "onborder",
        b.location.outside: "outside",
        }

    return
    


_init_location()


# version
__id__ = "$Id$"

# End of file 
