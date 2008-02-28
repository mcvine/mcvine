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


#include "wrap_NdArray.h"
#include "histogram/NdArray.h"


namespace wrap_mccomponents {

  void wrap_NdArray()
  {
    wrap_NdArray_T< double, unsigned int, size_t, 1 >
      ( "new_NdArray_dblarr_1", "NdArray_dblarr_1" );
    wrap_NdArray_T< double, unsigned int, size_t, 2 >
      ( "new_NdArray_dblarr_2", "NdArray_dblarr_2" );
    wrap_NdArray_T< double, unsigned int, size_t, 3 >
      ( "new_NdArray_dblarr_3", "NdArray_dblarr_3" );
    wrap_NdArray_T< double, unsigned int, size_t, 4 >
      ( "new_NdArray_dblarr_4", "NdArray_dblarr_4" );
    wrap_NdArray_T< double, unsigned int, size_t, 5 >
      ( "new_NdArray_dblarr_5", "NdArray_dblarr_5" );
    wrap_NdArray_T< double, unsigned int, size_t, 6 >
      ( "new_NdArray_dblarr_6", "NdArray_dblarr_6" );
    wrap_NdArray_T< double, unsigned int, size_t, 7 >
      ( "new_NdArray_dblarr_7", "NdArray_dblarr_7" );
  }

}

// version
// $Id$

// End of file 
