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

## This package contains some subpackages, each represent
## a binding of mcni.
## Each subpackage should provide factory methods of creating binded c++
## objects useful in mcni.


def default( ): return get('BoostPython')


def get( type ):
    """retrieve binding of given type

    Example: get('BoostPython')
    """
    return classes()[ '%s' % type ]( )


def classes():
    '''return all binding classes'''
    import boostpython
    return {'BoostPython': boostpython.Binding}


current = default()


# version
__id__ = "$Id$"

# End of file 
