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

#include <Python.h>
#if PY_MAJOR_VERSION >= 3
  #define MOD_ERROR_VAL NULL
  #define MOD_SUCCESS_VAL(val) val
  #define MOD_INIT(name) PyMODINIT_FUNC PyInit_##name(void)
  #define MOD_DEF(ob, name, doc, methods) \
          static struct PyModuleDef moduledef = { \
            PyModuleDef_HEAD_INIT, name, doc, -1, methods, }; \
          ob = PyModule_Create(&moduledef);
#else
  #define MOD_ERROR_VAL
  #define MOD_SUCCESS_VAL(val)
  #define MOD_INIT(name) void init##name(void)
  #define MOD_DEF(ob, name, doc, methods) \
          ob = Py_InitModule3(name, methods, doc);
#endif

#include "exceptions.h"
#include "bindings.h"
#include "register_bp_voidptr_converters.h"


char pymcni_module__doc__[] = "";

// Initialization function for the module (*must* be called initmcni)
extern "C"
MOD_INIT(mcni)
{
    // create the module and add the functions
    PyObject * m;
    MOD_DEF(m, "mcni", pymcni_module__doc__, pymcni_methods)
    if (m == NULL)
        return MOD_ERROR_VAL;

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
    return MOD_SUCCESS_VAL(m);
}

// version
// $Id$

// End of file
