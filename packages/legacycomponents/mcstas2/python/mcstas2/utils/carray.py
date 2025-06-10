#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from danse.ins import bpext


def pycptr2npyarr( vptr, typename, size ):
    type = name2npytype( typename )
    try:
        from danse.ins.numpyext import wrapdataptr
    except ImportError:
        from numpyext import wrapdataptr
        import warnings
        warnings.warn("Using old numpyext. Should use danse.ins.numpyext")
    return wrapdataptr( vptr, type, size )


def bpptr2pycptr( bpptr ):
    'extract pointer from a boost python object of WrappedPointer type'
    return bpext.extract_native_ptr( bpptr )


def bpptr2npyarr( bpptr, typename, size ):
    pycptr = bpptr2pycptr( bpptr )
    return pycptr2npyarr( pycptr, typename, size )


def name2npytype( typename ):
    return _npytypes[ typename ]


import numpy as N
_npytypes = {
    'double': N.dtype(N.double),
    }


# version
__id__ = "$Id$"

# End of file 
