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

#include "misc.h"
#include "libmcni/hello.h"


// copyright

char pymcni_copyright__doc__[] = "";
char pymcni_copyright__name__[] = "copyright";

static char pymcni_copyright_note[] = 
    "mcni python module: Copyright (c) 1998-2005 Michael A.G. Aivazis";


PyObject * pymcni_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pymcni_copyright_note);
}
    
// hello

char pymcni_hello__doc__[] = "";
char pymcni_hello__name__[] = "hello";

PyObject * pymcni_hello(PyObject *, PyObject *)
{
    return Py_BuildValue("s", hello());
}
    
// version
// $Id$

// End of file
