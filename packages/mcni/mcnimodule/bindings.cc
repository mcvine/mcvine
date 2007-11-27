// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <portinfo>
#include <Python.h>

#include "bindings.h"

#include "misc.h"          // miscellaneous methods

// the method table

struct PyMethodDef pymcni_methods[] = {

    // dummy entry for testing
    {pymcni_hello__name__, pymcni_hello,
     METH_VARARGS, pymcni_hello__doc__},

    {pymcni_copyright__name__, pymcni_copyright,
     METH_VARARGS, pymcni_copyright__doc__},


// Sentinel
    {0, 0}
};

// version
// $Id$

// End of file
