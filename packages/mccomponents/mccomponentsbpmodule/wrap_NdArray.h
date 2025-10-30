// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "bpext/WrappedPointer.h"
#include "histogram/NdArray.h"


namespace wrap_mccomponents {

  template <typename NdArray, typename DataType, typename IndexType>
  DataType NdArray_getitem( const NdArray & arr, const std::vector<IndexType> & indexes )
  {
    assert (indexes.size() == arr.dimension() );
    return arr[ &(indexes[0]) ];
  }

  template <typename Iterator, typename DataType,
	    typename Size, typename SuperSize,
	    unsigned int NDimension>
  void wrap_NdArray_T(const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::Histogram::NdArray<Iterator, DataType, Size, SuperSize, NDimension> w_t;

    class_<w_t>
      (classname, 
       init<
       Iterator, const Size *
       > () 
       )
      .def("__getitem__", NdArray_getitem<w_t, DataType, Size> )
      ;

  }


  // make use of bpext::WrappedPointer to pass native pointer from PyCObject
  // to this function.
  template <typename NdArray, typename DataType, typename Size>
  NdArray *
  new_NdArray
  ( const bpext::WrappedPointer & wp, const std::vector<Size> & shape)
  {
    DataType * ptr = (DataType *) (wp.pointer);
    return new NdArray(ptr, &(shape[0]) );
  }

  template <typename DataType,
	    typename Size, typename SuperSize,
	    unsigned int NDimension>
  void wrap_NdArray_T(const char * new_methodname, const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::Histogram::NdArray<DataType *, DataType, Size, SuperSize, NDimension> w_t;

    wrap_NdArray_T< DataType *, DataType, Size, SuperSize, NDimension>
      (classname);

    def(new_methodname, new_NdArray<w_t, DataType, Size>, return_value_policy< manage_new_object >() );
  }

}

// version
// $Id$

// End of file 
