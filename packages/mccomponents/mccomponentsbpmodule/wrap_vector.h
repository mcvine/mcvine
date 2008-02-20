// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/python/iterator.hpp>
#include <vector>
#include <string>

namespace wrap_mccomponents {
  
  using namespace boost::python;
  using namespace std;
  
  // wrap_vector using vector_indexing_suite of boost python
  template <typename ElementType>
  void wrap_vector( const char * elementTypeName )
  {
    std::string name("vector_");
    name += elementTypeName;

    typedef vector<ElementType> w_t;

    class_<w_t>
      (name.c_str(), init<size_t>())
      .def( vector_indexing_suite<w_t> () )
      ;
  }
  
  
  // another implementation of wrap_vector
  template <typename Type>
  inline Type v_getitem( const vector<Type> & v, size_t i)
  {
    return v[i];
  }
  
  template <typename Type>
  inline Type v_setitem( vector<Type> & v, size_t i, const Type &value)
  {
    return v[i] = value;
  }
  
  template <typename Type>
  inline size_t v_size( const vector<Type> & v)
  {
    return v.size();
  }
  

  template <typename Type>
  inline void v_append( vector<Type> & v, const Type & e)
  {
    v.push_back( e );
  }
  
  
  template <typename ElementType>
  void wrap_vector2( const char * elementTypeName )
  {
    std::string name("vector_");
    name += elementTypeName;

    typedef vector<ElementType> w_t;
    class_<w_t>
      (name.c_str(), init<size_t>())
      .def("__len__", &v_size<ElementType> )
      .def("__getitem__", &v_getitem<ElementType>)
      .def("__setitem__", &v_setitem<ElementType>)
      .def("__iter__", boost::python::iterator<w_t>() )
      .def("append", &v_append<ElementType> )
      ;
  }
  
  template <typename Type>
  inline void v_append_pointer_of_reference( vector<Type *> & v, Type & e)
  {
    v.push_back( &e );
  }
  
  template <typename ElementType>
  void wrap_pointer_vector( const char * elementTypeName )
  {
    std::string name("pointer_vector_");
    name += elementTypeName;

    typedef vector<ElementType *> w_t;
    class_<w_t>
      (name.c_str(), init<size_t>())
      .def("__len__", &v_size<ElementType *> )
      .def("__getitem__", &v_getitem<ElementType *>, return_internal_reference<1>())
      .def("__setitem__", &v_setitem<ElementType *>, return_internal_reference<1>())
      .def("__iter__", boost::python::iterator<w_t>() )
      .def("append", &v_append_pointer_of_reference<ElementType>, with_custodian_and_ward<1,2>())
      ;
  }
  
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
