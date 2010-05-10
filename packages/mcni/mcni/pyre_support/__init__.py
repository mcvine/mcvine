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


def findcomponentfactory(type, category=None, supplier=None):
    if category and supplier:
        return componentfactory(category, type, supplier)

    from mcni.component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    
    if supplier is None:
        suppliernames = suppliers.iterkeys()
    else:
        suppliernames = [supplier]
    
    found = []; categoryin = category
    for suppliername in suppliernames:
        supplier = suppliers[suppliername]
        if categoryin is None:
            categories = supplier.listallcomponentcategories()
        else:
            categories = [categoryin]
        for category in categories:
            types = supplier.listcomponentsincategory(category)
            if type in types:
                found.append((category, suppliername))
            continue
        continue
    if not found: return

    if len(found) > 1:
        raise RuntimeError, 'found more than 1 component factories for type %s: %s' % (
            type, found)
    
    category, suppliername = found[0]
    return componentfactory(category, type, suppliername)
        

# version
__id__ = "$Id$"

# End of file 
