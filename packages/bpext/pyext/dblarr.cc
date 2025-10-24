// -*- C++ -*-
// 
// Jiao Lin <jiao.lin@gmail.com>
// 

// provide a way to create double C array. This is useful for tests.


#include <iostream>
#include <string>
#include <sstream>

#include <Python.h>

#include <bpext/portinfo>

#include "bpext/bpext.h"
#include "dblarr.h"
#include "capsulethunk.h"


void deleteDblArr( void *ptr )
{
  double *arr = (double *)ptr;
  delete [] arr;
}
void pycapsule_deleteDblArr( PyObject *target)
{
  double *arr = (double *)PyCapsule_GetPointer(target, NULL);
  delete [] arr;
}

//-------------------- newdblarr --------------------

char pybpext_newdblarr__doc__[] = 
"Convert a C double array. return a PyCObject"
"\n\n"
"  Arguments:\n"
"\n"
"    - n: size of array \n"
"\n"
"  Example:\n"
"\n"
"    newdblarr( 10 )\n"
"\n"
"  Return:\n" 
"\n"
"    PyCObject of a void pointer\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pybpext_newdblarr__name__[] = "newdblarr";

PyObject * pybpext_newdblarr(PyObject *, PyObject *args)
{
  //std::cout << "pybpext_newdblarr: ";

  int n;

  int ok = PyArg_ParseTuple(args, "i", &n);
  if(!ok) return NULL;

  double *arr = new double[ n ];
  void * ptr = arr;
  // return PyCObject_FromVoidPtr( ptr, deleteDblArr);
  PyObject *obj = PyCapsule_New(ptr, NULL, pycapsule_deleteDblArr);
  return obj;
}





// version
// $Id: dblarr.cc 18 2005-07-18 23:03:29Z linjiao $

// End of file
