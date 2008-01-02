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

#ifndef MCCOMPONENTS_RANDOM_H
#define MCCOMPONENTS_RANDOM_H


#include <memory>

namespace mccomponents {

  namespace random {

    /// random number generator
    class Generator {
    public:
      
      // meta methods
      Generator();
      Generator( double seed );
      ~Generator();

      // methods
      /// generate a random number between min and max 
      double generate( double min, double max );
      /// generate a random number between 0 and 1
      double generate01();

    private:

      // hide implementation 
      struct Details;
      std::auto_ptr<Details> m_details;
  
    };
  }
}

#endif 

// version
// $Id$

// End of file 
