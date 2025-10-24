#!/usr/bin/env python
# 

__version__ = "0.1.4"

def copyright():
    return "bpext python module: Copyright (c) 2004-2018 Jiao Lin";


from . import _bpext as binding


def extract_ptr(bpobject, typename):
    '''Extract pointer out of a boost python object and return a PyCObject
holding that pointer. pointer is shared.

Parameters:

  bpobject: boost python object
  typename: type name

Examples:

  extract_ptr( bpo, 'vec_double' )
  '''
    return binding.extract_ptr(bpobject, typename)



def wrap_ptr(pycobject, typename):
    '''Wrap a pointer in a PyCObject to become a boost python object.
pointer is shared.

Parameters:

  pycobject: PyCObject instance
  typename: type name

Examples:

  wrap_ptr( pycobj, 'vec_double' )
  '''
    return binding.wrap_ptr(pycobject, typename)


def wrap_native_ptr(pycobject):
    '''Wrap a pointer of a native type (for example, double *)
in a simple c struct which only contains one void pointer.
Then return a boost python object of that c struct.
pointer is shared.

Parameters:

  pycobject: PyCObject instance

Examples:

  wrap_native_ptr( pycobj )
  '''
    return binding.wrap_native_ptr(pycobject)



def extract_native_ptr(bpobj):
    '''Extract a pointer of a native type (for example, double *)
from a boost python object of WrappedPointer type.
WrappedPointer is a simple struct that a member "pointer"
that contains the pointer of a native type.
Pointer is shared.

Parameters:

  bpobj: boost python object of WrappedPointer type

Output:

  PyCObject instance

Examples:

  extract_native_ptr( bpobj )
  '''
    return binding.extract_native_ptr(bpobj)



# version
__id__ = "$Id: __init__.py 17 2005-06-01 23:58:56Z linjiao $"

#  End of file 
