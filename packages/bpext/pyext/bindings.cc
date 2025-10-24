// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <bpext/portinfo>
#include <Python.h>

#include "bindings.h"

#include "misc.h"          // miscellaneous methods
#include "dblarr.h"

// the method table

struct PyMethodDef pybpext_methods[] = {

    {pybpext_copyright__name__, pybpext_copyright,
     METH_VARARGS, pybpext_copyright__doc__},

    {pybpext_extract_ptr__name__, 
     pybpext_extract_ptr,
     METH_VARARGS, pybpext_extract_ptr__doc__},

    {pybpext_wrap_ptr__name__, 
     pybpext_wrap_ptr,
     METH_VARARGS, pybpext_wrap_ptr__doc__},

    {pybpext_wrap_native_ptr__name__, 
     pybpext_wrap_native_ptr,
     METH_VARARGS, pybpext_wrap_native_ptr__doc__},

    {pybpext_extract_native_ptr__name__, 
     pybpext_extract_native_ptr,
     METH_VARARGS, pybpext_extract_native_ptr__doc__},

    {pybpext_newdblarr__name__, 
     pybpext_newdblarr,
     METH_VARARGS, pybpext_newdblarr__doc__},

// Sentinel
    {0, 0}
};

// version
// $Id: bindings.cc 2 2004-12-07 22:46:28Z linjiao $

// End of file
