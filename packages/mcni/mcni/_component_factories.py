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



def build_methods( method_list ):
    methods = {}
    for method in method_list:
        code = '''
def m( category, type, supplier = 'mcni'):
    from mcni.component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    suppliername = supplier
    supplier = suppliers[ suppliername ]
    f = getattr(supplier, %r)
    return f(category, type)
''' % (method, )
        exec code in locals()
        methods[method] = m
        continue
    return methods


methods = build_methods(
    [ 'componentfactory',
      'componentinfo',
      ]
    )

for name, method in methods.iteritems():
    exec '%s = method' % name

        
__all__ = methods.keys()

# version
__id__ = "$Id$"

# End of file 
