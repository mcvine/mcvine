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

#include "misc.h"


// copyright

char pymcni_copyright__doc__[] = "";
char pymcni_copyright__name__[] = "copyright";

static char pymcni_copyright_note[] = 
    "mcni python module: Copyright (c) 1998-2005 Michael A.G. Aivazis";


PyObject * pymcni_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pymcni_copyright_note);
}
    
    
// version
// $Id$

// End of file
