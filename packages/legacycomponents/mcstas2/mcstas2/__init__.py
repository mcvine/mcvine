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

def componentfactory( category, type ):
    from components import componentfactory
    from components.Registry import NotRegisteredError
    try: f = componentfactory( category, type )
    except NotRegisteredError: f = defaultcomponentfactory( category, type )
    return f


def defaultcomponentfactory( category, type ):
    libdir = defaultcomponentlibrarypath()
    import os
    path = os.path.join( libdir, category, '%s.comp' % type )
    if not os.path.exists( path ) or not os.path.isfile(path):
        raise "default component (%s, %s) does not exist. Cannot find %s" % (
            category, type, path )
    from wrappers import wrap
    wrap( path, category )
    from components import componentfactory
    return componentfactory( category, type )


def defaultcomponentlibrarypath( ):
    from utils.xos import getEnv
    var = 'MCSTAS_COMPONENT_LIBDIR'
    path = getEnv( var, None )
    if path is None:
        raise "Please specify the default path to mcstas component library "\
              "as environment variable %r.\n"\
              "For example, in bash environment, do\n"\
              "  $ export %s=/.../mcstas/lib/mcstas\n"\
              % (var, var)
    return path

    
# version
__id__ = "$Id$"

# End of file 
