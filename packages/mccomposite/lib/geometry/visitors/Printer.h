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
#include "shapes.h"


namespace mccomposite {
  
  namespace geometry {

    struct Printer: public AbstractShapeVisitor {
      
      //meta methods
      Printer( std::ostream & os );
      virtual ~Printer( ) {};
      
      //methods
      //visiting methods 
      // for primitives
      void visit( const Box * box );
      void visit( const Cylinder * cylinder );
      void visit( const Sphere * sphere );
      // for operations      // for operations
      void visit( const Difference * difference );
      void visit( const Dilation * dilation );
      void visit( const Intersection * intersection );
      void visit( const Reflection * reflection );
      void visit( const Rotation * rotation );
      void visit( const Translation * translation );
      void visit( const Union * adunion );
      
      //data
      std::ostream & os;
    };
    
  }
}

#endif

// version
// $Id$

// End of file 
