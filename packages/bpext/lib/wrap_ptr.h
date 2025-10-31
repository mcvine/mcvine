#include <iostream>
#include "boost/python/object.hpp"

//! wrap a pointer to become a boost python object
/// This is not a copy!
/// The returned boost python object share a pointer with the original pointer.
/// So please make sure you keep the original pointer around!
template <class T>
PyObject *wrap_ptr( void *ptr )
{
  using namespace boost::python;
  T  * t_ptr = static_cast<T *> (ptr);


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


