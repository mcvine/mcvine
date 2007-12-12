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


#ifndef MCCOMPOSITE_GEOMETRY_PRINTER_H
#define MCCOMPOSITE_GEOMETRY_PRINTER_H

#include <iostream>
#include "AbstractShapeVisitor.h"


namespace mccomposite {

  struct Printer: public AbstractShapeVisitor {
  
    //meta methods
    Printer( std::ostream & os );
    virtual ~Printer( ) {};

    //methods
    virtual void onBox( const Box & box );

    //data
    std::ostream & os;
  };

}

#endif

// version
// $Id$

// End of file 
