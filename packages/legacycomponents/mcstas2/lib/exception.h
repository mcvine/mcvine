// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef H_MCSTAS2_EXCEPTION
#define H_MCSTAS2_EXCEPTION


#ifndef STRING_INCLUDED
#define STRING_INCLUDED
#include <string>
#endif

#ifndef EXCEPTION_INCLUDED
#define EXCEPTION_INCLUDED
#include <exception>
#endif


#include <sstream>
namespace mcstas2{


  /// Exception base class for mcstas2 codes
  class Exception: public std::exception{

  public:
  
    Exception(const char *m) {_msg = std::string(m);}
    const char *what() const throw()  { return _msg.c_str(); }
    ~Exception() throw() {}

  private:
    std::string _msg;

  };

  inline void exit(int code) {
    std::stringstream ss;
    ss << "exit " << code << " called";
    throw mcstas2::Exception(ss.str().c_str());
  }

} //mcstas2



#endif //H_MCSTAS2_EXCEPTION


// version
// $Id$

// End of file 
