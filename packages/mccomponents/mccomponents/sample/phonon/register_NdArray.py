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


def ndarray_bp( npyarr ):
    '''create boost python instance of NdArray object
arguments:
    npyarr: numpy array. it must be a contiguous array.
    '''
    import numpy
    assert npyarr.dtype == numpy.double, "only work for double array for this time"
    
    import numpyext
    ptr = numpyext.getdataptr( npyarr )
        
    import bpext
    wp = bpext.wrap_native_ptr( ptr )

    import mccomponents.mccomponentsbp as binding
    shape = binding.vector_uint( 0 )
    for i in npyarr.shape: shape.append( i )

    factory = 'new_NdArray_dblarr_%d' % len(shape)
    a1 = getattr(binding,factory)( wp, shape )
    a1.origin = npyarr # keep a reference to avoid seg fault
    return a1


# method __getitem__ to replace the boost python generated __getitem__
def bp_ndarray_getitem(self, indexes):
    import mccomponents.mccomponentsbp as binding
    cindexes = binding.vector_uint( 0 )
    for ind in indexes: cindexes.append( ind )
    return self._getitem_bp( cindexes )


# go thru ndarray bp types and change interfaces
def _fix_bp_ndarray_interface( ):
    import mccomponents.mccomponentsbp as binding
    for i in range( 1,7 ):
        clsname = 'NdArray_dblarr_%d' % i
        cls = getattr( binding, clsname )
        cls._getitem_bp = cls.__getitem__
        cls.__getitem__ = bp_ndarray_getitem
        continue
    return


_fix_bp_ndarray_interface()
        

# version
__id__ = "$Id$"


# End of file 
