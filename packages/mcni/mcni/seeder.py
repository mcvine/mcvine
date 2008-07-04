# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



def register( seeding_function ):
    'register a function that needs seed'
    _registry.append( seeding_function )
    return


def feed( ):
    'feed seeds to all functions that need seed'
    import rng_seed
    for seeding_function in _registry:
        seed = rng_seed.seed( )
        seeding_function( seed )
        continue
    return


_registry = []


# version
__id__ = "$Id$"

# End of file 
