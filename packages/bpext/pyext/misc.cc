// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Jiao Lin
//                        California Institute of Technology
//                        (C) 2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <iostream>
#include <string>
#include <sstream>

#include "supported_types.h"
#include <Python.h>

// #ifdef USE_PYRE
// #include <portinfo>
// #include "journal/debug.h"
// #endif

#include "misc.h"
#include "bpext/bpext.h"
#include "capsulethunk.h"


//-------------------- copyright --------------------

char pybpext_copyright__doc__[] = "";
char pybpext_copyright__name__[] = "copyright";

static char pybpext_copyright_note[] = 
    "bpext python module: Copyright (c) 2004-2007 Jiao Lin";


PyObject * pybpext_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pybpext_copyright_note);
}
    
void pycapsule_donothing( PyObject *target)
{}


//-------------------- extract_ptr --------------------

char pybpext_extract_ptr__doc__[] = 
"Convert a  boost.python object "
"to a void pointer in a PyCObject."
" The void pointer is pointing to the C++ object underlying the"
" boost.python object "
"so that it can be used by hand-binded"
" codes."
" A description of the pointer is attached to the returned PyCObject. "
"\n\n"
"  Arguments:\n"
"\n"
"    - boost_object: the input \n"
"    - class: class name of the C++ object \n"
"\n"
"  Example:\n"
"\n"
"    extract_ptr( an_object, 'std::vector<double>' )\n"
"\n"
"  Return:\n" 
"\n"
"    PyCObject of a void pointer to the original C++ object\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pybpext_extract_ptr__name__[] = "extract_ptr";

PyObject * pybpext_extract_ptr(PyObject *, PyObject *args)
{
  //std::cout << "pybpext_extract_ptr: ";

  PyObject *obj;
  char *desc;
  char *desc2=NULL;

  int ok = PyArg_ParseTuple(args, "Os|s", &obj, &desc, &desc2);
  if(!ok) return NULL;

  using std::string;

  void *ptr;

  using namespace bpext;
  const Extractor & extractor = extractorRegistry[ (const char *)(desc) ];
  
  if (extractor != 0) {
    
    ptr = extractor(obj);
    
  } else {
  
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "extractor of boost.python object type \"" << desc 
	<< "\" has not been registered."
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }

  if (ptr==NULL) {
    
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "not a boost.python object or contains NULL pointer!"
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }

  PyObject *ret = PyCapsule_New(ptr, NULL, pycapsule_donothing);
  if (desc2!=NULL)
    PyCapsule_SetContext(ret, desc2);
  return ret;
}


//-------------------- wrap_ptr --------------------

char pybpext_wrap_ptr__doc__[] = 
"Convert a PyCObject of a pointer to a boost.python object\n"
"The created boost.python object shares the original pointer.\n"
"So you must keep the original pointer around.\n"
"\n\n"
"  Arguments:\n"
"\n"
"    - pycobject: the input \n"
"    - class: class name of the C++ object \n"
"\n"
"  Example:\n"
"\n"
"    wrap_ptr( pycobject, 'std::vector<double>' )\n"
"\n"
"  Return:\n" 
"\n"
"    boost python object\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pybpext_wrap_ptr__name__[] = "wrap_ptr";

PyObject * pybpext_wrap_ptr(PyObject *, PyObject *args)
{
  //std::cout << "pybpext_wrap_ptr: ";

  PyObject *obj;
  char *desc;

  int ok = PyArg_ParseTuple(args, "Os", &obj, &desc);
  if(!ok) return NULL;

  using std::string;

  if (!PyCapsule_CheckExact( obj )) {
    std::ostringstream oss;
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "1st argument must be a PyCObject." 
	<< std::endl;
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }
  void *ptr = PyCapsule_GetPointer( obj, NULL );

  PyObject *bpobj;

  using namespace bpext;
  const Wrapper & wrapper = wrapperRegistry[ (const char *)(desc) ];
  
  if (wrapper != 0) {
    
    bpobj = wrapper(ptr);
    
  } else {
  
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "wrapper of type \"" << desc 
	<< "\" has not been registered."
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }

  if (bpobj==NULL) {
    
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "unable to convert PyCObject at " 
	<< obj << " of type " << desc << " to boost python object!"
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }
  
  return bpobj;
}





#include "bpext/WrappedPointer.h"

//-------------------- wrap_native_ptr --------------------

char pybpext_wrap_native_ptr__doc__[] = \
"Convert a PyCObject of a native-type pointer (double *, char *, etc)"
" to a boost.python object of WrappedPointer type\n"
"WrappedPointer is a simple c struct that contains only one member, "
"a void pointer."
"The created boost.python object shares the original pointer.\n"
"So you must keep the original pointer around.\n"
"\n\n"
"  Arguments:\n"
"\n"
"    - pycobject: the input \n"
"\n"
"  Example:\n"
"\n"
"    wrap_native_ptr( pycobject )\n"
"\n"
"  Return:\n" 
"\n"
"    boost python object\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pybpext_wrap_native_ptr__name__[] = "wrap_native_ptr";

PyObject * pybpext_wrap_native_ptr(PyObject *, PyObject *args)
{
  //std::cout << "pybpext_wrap_native_ptr: ";

  PyObject *obj;

  int ok = PyArg_ParseTuple(args, "O", &obj);
  if(!ok) return NULL;

  using std::string;

  if (!PyCapsule_CheckExact( obj )) {
    std::ostringstream oss;
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "1st argument must be a PyCObject." 
	<< std::endl;
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }
  void *ptr = PyCapsule_GetPointer( obj, NULL );
  using namespace bpext;
  WrappedPointer *wp = new WrappedPointer;
  wp->pointer = ptr;

#ifdef DEBUG
#ifdef USE_PYRE
  journal::debug_t debug("wrap_native_ptr");
  debug << journal::at(__HERE__)
	<< "wrapped pointer: " << ptr 
	<< journal::endl;
#else
  std::cerr << "wrapped pointer: " << ptr << std::endl;
#endif
#endif

  using namespace boost::python;
  PyObject * ret;
  ret = incref
    (converter::detail::pointer_deep_arg_to_python<WrappedPointer *>(wp).get());
  
  delete wp;
  
  return ret;
}



//-------------------- extract_native_ptr --------------------

char pybpext_extract_native_ptr__doc__[] = 
"Convert a  boost.python object containing a wrapped native pointer"
"to a pointer in a PyCObject."
" The void pointer is the pointer inside the WrappedPointer object"
" carried in the boost.python object."
" The extracted pointer then can be used by hand-binded"
" codes."
"\n\n"
"  Arguments:\n"
"\n"
"    - boost_object: the input \n"
"\n"
"  Example:\n"
"\n"
"    extract_native_ptr( an_object )\n"
"\n"
"  Return:\n" 
"\n"
"    PyCObject of a pointer of a native type\n"
"\n"
"  Exceptions:\n"
"\n"
"    ValueError"
;
char pybpext_extract_native_ptr__name__[] = "extract_native_ptr";

PyObject * pybpext_extract_native_ptr(PyObject *, PyObject *args)
{
  //std::cout << "pybpext_extract_native_ptr: ";

  PyObject *obj;

  int ok = PyArg_ParseTuple(args, "O", &obj);
  if(!ok) return NULL;

  using std::string;

  void *ptr;

  using namespace bpext;
  char * desc = "WrappedPointer";
  const Extractor & extractor = extractorRegistry[ desc ];
  
  if (extractor != 0) {
    
    ptr = extractor(obj);
    
  } else {
  
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "extractor of boost.python object type \"" << desc 
	<< "\" has not been registered."
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }

  if (ptr==NULL) {
    
    std::ostringstream oss;
    
    oss << "In " << __FILE__ << " line " << __LINE__ << ": "
	<< "not a boost.python object or contains NULL pointer!"
	<< std::endl;
    
    PyErr_SetString(PyExc_ValueError, oss.str().c_str());

    return NULL;
  }

  WrappedPointer *wptr = (WrappedPointer *)ptr;

  void *nptr = wptr->pointer;

#ifdef DEBUG
#ifdef USE_PYRE
  journal::debug_t debug("extract_native_ptr");
  debug << journal::at(__HERE__)
	<< "extracted pointer: " << nptr 
	<< journal::endl;
#else
  std::cerr << "extracted pointer: " << nptr << std::endl;
#endif
#endif

  return PyCapsule_New( nptr, NULL, pycapsule_donothing );
}



// version
// $Id: misc.cc 18 2005-07-18 23:03:29Z linjiao $

// End of file
