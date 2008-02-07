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

#include "exceptions.h"
#include "bindings.h"
#include "register_bp_voidptr_converters.h"


char pymcni_module__doc__[] = "";

// Initialization function for the module (*must* be called initmcni)
extern "C"
void
initmcni()
{
    // create the module and add the functions
    PyObject * m = Py_InitModule4(
        "mcni", pymcni_methods,
        pymcni_module__doc__, 0, PYTHON_API_VERSION);

    // get its dictionary
    PyObject * d = PyModule_GetDict(m);

    // check for errors
    if (PyErr_Occurred()) {
        Py_FatalError("can't initialize module mcni");
    }

    // install the module exceptions
    pymcni_runtimeError = PyErr_NewException("mcni.runtime", 0, 0);
    PyDict_SetItemString(d, "RuntimeException", pymcni_runtimeError);

    // register bp-void ptr converters
    mcnimodule::register_bp_voidptr_converters();
    return;
}

// version
// $Id$

// End of file
