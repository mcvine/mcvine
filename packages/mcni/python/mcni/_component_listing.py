#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .component_suppliers import all as getsuppliers


def listallcomponentcategories( ):
    '''list all component categories'''
    ret = []
    for name, supplier in getsuppliers().items():
        ret += supplier.listallcomponentcategories()
        continue
    from .utils import uniquelist
    return uniquelist( ret )


def listcomponentsincategory( category ):
    ret = []
    for name, supplier in getsuppliers().items():
        if category not in supplier.listallcomponentcategories(): 
            continue
        l = supplier.listcomponentsincategory( category )
        l = [ (i, name) for i in l ]
        ret += l
        continue
    return ret


__all__ = ['listallcomponentcategories', 'listcomponentsincategory']

# version
__id__ = "$Id$"

# End of file 
