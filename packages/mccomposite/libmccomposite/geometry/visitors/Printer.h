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
      void onBox( const Box & box );
      // for operations
      void onDifference( const Difference & difference );
      void onDilation( const Dilation & dilation );
      void onIntersection( const Intersection & intersection );
      void onReflection( const Reflection & reflection );
      void onRotation( const Rotation & rotation );
      void onTranslation( const Translation & translation );
      void onUnion( const Union & adunion );
      
      //data
      std::ostream & os;
    };
    
  }
}

#endif

// version
// $Id$

// End of file 
