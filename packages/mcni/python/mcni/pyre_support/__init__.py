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
    from .NeutronComponentFacility import NeutronComponentFacility
    return NeutronComponentFacility( *args, **kwds )


def componentfactory( category, type, supplier = 'mcni'):
    from .component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    suppliername = supplier
    supplier = suppliers[ suppliername ]
    get = getattr(supplier, 'componentfactory')
    f = get(category, type)
    f.category = category
    f.type = type
    f.supplier = suppliername
    return f


def findcomponentfactory(type, category=None, supplier=None):
    from mcni._find_component import find
    found = find(type, category=category, supplier=supplier)
    if not found: 
        raise RuntimeError("cannot find component (type=%s, category=%s, supplier=%s)" % (
            type, category, supplier))
    type, category, supplier = found
    return componentfactory(category, type, supplier)
        

# version
__id__ = "$Id$"

# End of file 
