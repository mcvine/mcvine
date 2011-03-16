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


def find(type, category=None, supplier=None):
    if category and supplier:
        return type, category, supplier

    from component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    
    if supplier is None:
        suppliernames = suppliers.iterkeys()
    else:
        suppliernames = [supplier]
    
    found = []; categoryin = category
    close_matches = []
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
            matches = get_close_matches(type, types)
            if matches:
                close_matches += matches
            continue
        continue
    if not found: 
        if close_matches:
            import warnings
            marker = '*'*70
            msg = ("\n%s\nCannot find the component you requested: %r, \n"
                   "maybe you mean %r?\n%s\n") %(
                marker, type, close_matches[0], marker)
            warnings.warn(msg)
        return

    if len(found) > 1:
        raise RuntimeError, 'found more than 1 component for type %s: %s' % (
            type, found)
    
    category, suppliername = found[0]
    return type, category, suppliername
        
from difflib import get_close_matches

# version
__id__ = "$Id$"

# End of file 
