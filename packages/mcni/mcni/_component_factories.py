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

## build componenet factory methods

def build_methods( method_list ):
    methods = {}
    for method in method_list:
        code = '''
def %s( category, type, supplier = 'mcni'):
    from mcni.component_suppliers import all as getsuppliers
    suppliers = getsuppliers()
    suppliername = supplier
    supplier = suppliers[ suppliername ]
    f = getattr(supplier, %r)
    return f(category, type)
''' % (method, method, )
        exec code in locals()
        methods[method] = eval(method)
        continue
    return methods


methods = build_methods(
    [ 'componentfactory',
      'componentinfo',
      ]
    )

for name, method in methods.iteritems():
    exec '%s = method' % name


componentinfo.__doc__ = '''constructs a ComponentInfo object for the given component. You can print the returned object to see the information of the component.

Examples:

  >>> componentinfo('sources', 'Source_simple', 'mcstas2')

'''
        
componentfactory.__doc__ = '''returns a factory method for the given component.

For example:

  >>> f = componentfactory('sources', 'Source_simple', 'mcstas2')

You can find help for the returned factory method by

  >>> help(f)

You can also use method componentinfo to find information of a component

  >>> print componentinfo('sources', 'Source_simple', 'mcstas2')

'''
        
__all__ = methods.keys()

# version
__id__ = "$Id$"

# End of file 
