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


#ifndef MCNI_EXCEPTIONS_H
#define MCNI_EXCEPTIONS_H


#include "mcni/test/exception.h"
#include "journal/error.h"

namespace mcni {

  //! exception for events in which a neutron entering a fatal path
  class neutron_fatal_path: public Exception{
  public:
    neutron_fatal_path(const char *m="neutron in fatal path") : Exception(m) {}
  };

  // convenient methods
  inline void throw_fatal_path_error
  ( const char *channel, const journal::loc3_t & where, const char *msg );
  inline void throw_fatal_path_error
  ( const char *channel, const journal::loc2_t & where, const char *msg );
}

#include "exceptions.icc"

#endif // MCNI_EXCEPTIONS_H



// version
// $Id: Exceptions.h 41 2005-06-13 07:29:25Z linjiao $

// Generated automatically by CxxMill on Thu Apr  7 15:02:19 2005

// End of file 
