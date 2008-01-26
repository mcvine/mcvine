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


## export directory of python modules at user's home directory

from dotmcstas import dotmcstas
import os
path = os.path.join( dotmcstas, 'python' )



def init_package( package ):
    """init a package

    init_package( 'a.b.c' )
    """
    packagepath = os.path.join( path, package.replace( '.', '/' ) )
    if os.path.exists( packagepath ) and os.path.isdir(packagepath): return
    if os.path.exists( packagepath ):
        raise IOError, "%s exists and not a directory. "

    #make path
    os.makedirs( packagepath )
    #add __init__.py
    open( os.path.join( packagepath, '__init__.py' ), 'w').write('')
    return


    
# version
__id__ = "$Id$"

# End of file 
