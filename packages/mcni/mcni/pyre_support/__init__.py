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


def facility(*args, **kwds):
    from NeutronComponentFacility import NeutronComponentFacility
    return NeutronComponentFacility( *args, **kwds )


def componentfactory( category, type, supplier = 'mcni'):
    from component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    suppliername = supplier
    supplier = suppliers[ suppliername ]
    f = getattr(supplier, 'componentfactory')
    return f(category, type)


# version
__id__ = "$Id$"

# End of file 
