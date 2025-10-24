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


#include <sstream>

#include <bpext/portinfo>

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

#include "register_converters.h"


#include "bpext/WrappedPointer.h"
#include "boost/python.hpp"


const char * WrappedPointer_str( const bpext::WrappedPointer & wp )
{
  std::ostringstream oss;
  oss << wp.pointer;
  return oss.str().c_str();
}


void **PyArray_API;

char pybpext_module__doc__[] = "";

// Initialization function for the module (*must* be called initbpext)
extern "C"
MOD_INIT(_bpext)
{
    // create the module and add the functions
    PyObject * m;
    MOD_DEF(m, "_bpext", pybpext_module__doc__, pybpext_methods)
    if (m == NULL)
        return MOD_ERROR_VAL;

    // get its dictionary
    PyObject * d = PyModule_GetDict(m);

    // check for errors
    if (PyErr_Occurred()) {
        Py_FatalError("can't initialize module bpext");
    }

    // install the module exceptions
    pybpext_runtimeError = PyErr_NewException("bpext.runtime", 0, 0);
    PyDict_SetItemString(d, "RuntimeException", pybpext_runtimeError);

    wrap::register_converters();

    using namespace boost::python;
    class_<bpext::WrappedPointer>
      ("WrappedPointer", no_init)
      .def("__str__", WrappedPointer_str)
      ;

    return MOD_SUCCESS_VAL(m);
}

// version
// $Id: bpextmodule.cc 2 2004-12-07 22:46:28Z linjiao $

// End of file
