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


def componentfactory( category, type ):
    global _registry
    return _registry.get( category, type )


def registercomponentfactory( category, type, factory ):
    global _registry
    _registry.register( category, type, factory )
    return


from Registry import Registry
_registry = Registry()
del Registry



# version
__id__ = "$Id$"

# End of file 
