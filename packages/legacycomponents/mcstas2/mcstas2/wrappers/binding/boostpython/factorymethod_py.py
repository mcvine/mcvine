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

#Generate <component_name>.py, which contains a "factory" method
#to create instance of the boost python binding of mcstas component 

template = '''
def factory( %(ctor_kwds)s ):
    from mcstas2.bindings import boostpython
    from %(bindingmodulename)s import %(component)s as f
    from mcstas2.mcstas2bp import McStasComponentAsMcniComponent as component
    return component( f( %(ctor_args)s ) )

from mcstas2.utils.parsers.ComponentInfo import Parameter
class info:
    name = %(name)r
    copyright = """%(copyright)s"""
    simple_description = """%(simple_description)s"""
    full_description = """%(full_description)s""" 
    definition_parameters = %(definition_parameters)s
    setting_parameters = %(setting_parameters)s
    output_parameters = %(output_parameters)s
    state_parameters = %(state_parameters)s
    declare = %(declare)s
    initialize = %(initialize)s
    trace = %(trace)s
    save = %(save)s
    finalize = %(finalize)s
''' 

def generate( classname, ctorargs, bindingmodulename, path ):
    ctorargs_str = _build_args_str( ctorargs )
    ctorkwds_str = _build_kwds_str( ctorargs )
    content = template % {
        'ctor_args': ctorargs_str,
        'ctor_kwds': ctorkwds_str,
        'component': classname,
        'bindingmodulename': bindingmodulename,
        }
    import os
    filename = os.path.join( path, "%s.py" % classname)
    open(filename, 'w').write( content )
    return filename


def _build_kwds_str( args ):
    return ",".join( [ _arg_str( arg ) for arg in args] )
def _kwd_str( arg ):
    return "%s=%r" % (arg.name, arg.default)

def _build_args_str( args ):
    return ",".join( [ _arg_str( arg ) for arg in args] )
def _arg_str( arg ):
    return "%s" % (arg.name, )


# version
__id__ = "$Id$"


# End of file 
