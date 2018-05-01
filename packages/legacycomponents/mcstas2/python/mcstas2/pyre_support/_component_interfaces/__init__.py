#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



def getInterface(category, type):
    thispackage = 'mcstas2.pyre_support._component_interfaces'
    package = '.'.join([thispackage, category, type])
    try:
        # specific component
        package = _import(package)
    except ImportError:
        # category default
        package = '.'.join([thispackage, category, 'default'])
        try:
            package = _import(package)
        except ImportError:
            # general default
            from . import default as package
    return getattr(package, 'ComponentInterface')


def _import(package):
    return __import__(package, {}, {}, [''])


# version
__id__ = "$Id$"

# End of file 
