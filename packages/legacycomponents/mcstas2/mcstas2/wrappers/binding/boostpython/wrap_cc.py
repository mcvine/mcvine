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

#Generate wrap.cc, which wraps a mcstas component using boost python

template = '''
#include "mcstas2/boostpython_binding/wrap_component.h"
#include "%(headername)s.h"

void wrap() 
{
  using namespace mcstas2::boostpython_binding;
  using namespace boost::python;

  component_wrapper<mcstas2::%(classname)s>::wrap
    ("%(classname)s", init<%(ctor_args)s>()
    %(ctor_policies)s
    );
}
'''

def generate( classname, ctor_args, path, headername = None ):
    #default header name is the same as class name
    if not headername: headername = classname

    #convert args to a string
    ctor_args_str = _build_args_str( ctor_args )
    ctor_policies_str = _build_policies( ctor_args )
    
    content = template % {
        'headername': headername,
        'classname': classname,
        'ctor_args': ctor_args_str,
        'ctor_policies': ctor_policies_str,
        }
    import os
    filename = os.path.join( path, "wrap.cc" )
    open(filename, 'w').write( content )
    return filename


def _build_args_str( args ):
    return ",".join( [ _arg_str( arg ) for arg in args] )


def _arg_str( arg ):
    return "%s" % (arg.type,)


def _build_policies( args ):
    '''return
with_custodian_and_ward<1, 2,
with_custodian_and_ward<1, 5,
....
> > ()
'''
    types = ['int', 'float', 'double', 'char *', 'const char *']
    pointertypes = [ 'char *', 'const char *']
    
    indexes_of_args_need_wards = []
    for index, arg in enumerate(args):
        if arg.type not in types: raise NotImplementedError , \
           "type not supported: %s" % (arg.type, )
        if arg.type in pointertypes:
            indexes_of_args_need_wards.append( index + 2 )
            continue
        continue

    if len(indexes_of_args_need_wards) == 0: return ''
    
    ward = 'with_custodian_and_ward'
    policies = ',\n'.join(
        ['%s<1, %d' % (ward, index) for index in indexes_of_args_need_wards]) \
        + '> ' * len(indexes_of_args_need_wards) \
        + '()'
    return '[' + policies + ']'
    

# version
__id__ = "$Id$"


# End of file 
