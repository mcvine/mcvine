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

#if !defined(pybpext_misc_h)
#define pybpext_misc_h

// copyright
extern char pybpext_copyright__name__[];
extern char pybpext_copyright__doc__[];
extern "C"
PyObject * pybpext_copyright(PyObject *, PyObject *);

// extract_ptr
extern char pybpext_extract_ptr__name__[];
extern char pybpext_extract_ptr__doc__[];
extern "C"
PyObject * pybpext_extract_ptr(PyObject *, PyObject *);

// wrap_ptr
extern char pybpext_wrap_ptr__name__[];
extern char pybpext_wrap_ptr__doc__[];
extern "C"
PyObject * pybpext_wrap_ptr(PyObject *, PyObject *);

// wrap_native_ptr
extern char pybpext_wrap_native_ptr__name__[];
extern char pybpext_wrap_native_ptr__doc__[];
extern "C"
PyObject * pybpext_wrap_native_ptr(PyObject *, PyObject *);

// extract_native_ptr
extern char pybpext_extract_native_ptr__name__[];
extern char pybpext_extract_native_ptr__doc__[];
extern "C"
PyObject * pybpext_extract_native_ptr(PyObject *, PyObject *);


#endif

// version
// $Id: misc.h 2 2004-12-07 22:46:28Z linjiao $

// End of file
