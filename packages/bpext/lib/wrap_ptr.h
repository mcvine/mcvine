#include <iostream>
#include "boost/python/object.hpp"
#ifdef USE_PYRE
#include "journal/debug.h"
#endif

//! wrap a pointer to become a boost python object
/// This is not a copy!
/// The returned boost python object share a pointer with the original pointer.
/// So please make sure you keep the original pointer around!
template <class T>
PyObject *wrap_ptr( void *ptr )
{
  using namespace boost::python;
  T  * t_ptr = static_cast<T *> (ptr);

#ifdef DEBUG
#ifdef USE_PYRE
  journal::debug_t debug("bpext.wrap_ptr");
  debug 
    << journal::at(__HERE__)
    << "pointer to c++ object: " << t_ptr 
    << journal::endl;
#else
  std::cerr << "pointer to c++ object: " << t_ptr  << std::endl;
#endif
#endif

  //std::cout << t_ptr << std::endl;
  try {
    return incref(converter::detail::pointer_shallow_arg_to_python<T *>(t_ptr).get());
  }
  catch (...) {
    std::cerr 
      << "Cannot convert the given pointer to a boost python object!!!\n"
      << "Will return a NULL pointer from " << __FILE__ 
      << " line " << __LINE__ 
      << " in function wrap_ptr."
      << std::endl;
    return NULL;
  }
}


