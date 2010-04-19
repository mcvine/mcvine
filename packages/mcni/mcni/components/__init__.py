#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def listallcomponentcategories( ):
    global _registry
    return _registry.listallcomponentcategories()


def listcomponentsincategory( category ):
    global _registry
    return _registry.listcomponentsincategory( category )


def registered( category, type ):
    global _registry
    return _registry.registered( category, type )


def categoriesInRegistry( ):
    global _registry
    return _registry.types.keys()


def registeredComponentsInCategory( category ):
    global _registry
    return _registry.types.get( category ) or []


def componentfactory( category, type ):
    global _registry
    return _registry.getFactory( category, type )


def componentinfo( category, type ):
    global _registry
    return _registry.getInfo( category, type )


def registercomponent( category, type, factory ):
    global _registry
    _registry.register( category, type, factory )
    return


from Registry import Registry
_registry = Registry()
del Registry



# version
__id__ = "$Id$"

# End of file 
