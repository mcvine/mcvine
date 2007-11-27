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

#ifndef MCNI_TEST_EXCEPTION_H
#define MCNI_TEST_EXCEPTION_H


#include "journal/error.h"
#include <string>


namespace mcni {
  
  /// Exception base class for mcni codes
  class Exception: public std::exception{
    
  public:
    
    /// ctor
    Exception(const char *m) {_msg = std::string(m);}

    /// dtor
    ~Exception() throw() {}


    // methods

    /// report exception details.
    const char *what() const throw()  { return _msg.c_str(); }

    
  private:
    // data
    std::string _msg;
    
  };
  
  

  /// throw an exception and print out error message through journal
  /*!
    @param channel:  journal channel name
    @param where: usually journal::at(__HERE__)
    @param e: exception instance
  */
  template <typename loc_t>
  void throw_( const char *channel, const loc_t &where, const mcni::Exception &e)
  {
    journal::error_t err(channel);
    err << where
	<< e.what()
	<< journal::endl;
    throw e;
  }
  
  

  /// throw an exception and print out error message through journal
  /*!
    the type of exception to throw is given as template parameter
    @param channel: journal channel name
    @param where: usually journal::at(__HERE__)
  */
  template <typename exception_t, typename loc_t>
  void throw_( const char *channel, const loc_t &where)
  {
    journal::error_t err(channel);
    exception_t e;
    err << where
	<< e.what()
	<< journal::endl;
    throw e;
  }
  
  
  //   void throw_( const char *channel, const journal::loc3_t & whre, const Exception & e );
  //   void throw_( const char *channel, const journal::loc2_t & whre, const Exception & e );

} //mcni

#endif //MCNI_TEST_EXCEPTION_H


// version
// $Id: exception.h 543 2006-04-28 00:52:08Z jiao $

// End of file 
