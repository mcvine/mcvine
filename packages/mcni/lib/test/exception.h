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


#include <string>


namespace mcni {
  
  /// Exception base class for mcni codes
  class Exception: public std::exception{
    
  public:
    
    /// ctor
    Exception(const char *m) : _msg( m ) {}
    Exception(const std::string &m) : _msg(m) {}

    /// dtor
    ~Exception() throw() {}


    // methods

    /// report exception details.
    const char *what() const throw()  { return _msg.c_str(); }

    
  private:
    // data
    std::string _msg;
    
  };
  
  

  /// throw an exception
  /*!
    @param e: exception instance
  */
  inline void throw_(const mcni::Exception &e)
  {
    throw e;
  }
  
  

  /// throw an exception
  /*!
    the type of exception to throw is given as template parameter
  */
  template <typename exception_t, typename loc_t>
  void throw_()
  {
    exception_t e;
    throw e;
  }
  
  
} //mcni

#endif //MCNI_TEST_EXCEPTION_H


// version
// $Id$

// End of file 
