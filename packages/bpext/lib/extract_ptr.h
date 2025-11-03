#ifndef BPEXT_EXTRACT_PTR_H
#define BPEXT_EXTRACT_PTR_H

#include "boost/python/extract.hpp"
#include <iostream>

//! extract pointer from a boost python object
template <class T>
void *extract_ptr( PyObject *obj )
{
  using namespace boost::python;
  T  * t_ptr;
  try {
    t_ptr = extract<T  *>(obj);
  } 
  catch (...) {
    std::cerr << "The input is not a valid boost.python object!!!\n"
              << "Will return a NULL pointer from " << __FILE__ 
              << " line " << __LINE__ 
              << " in function extract_ptr."
              << std::endl;
    return NULL;
  } 
  //std::cout << t_ptr << std::endl;
  void *ptr = static_cast< void * > (t_ptr);
  
  return ptr;
}
  
#endif
