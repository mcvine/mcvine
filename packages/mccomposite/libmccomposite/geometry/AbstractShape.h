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

#ifndef MCCOMPOSITE_GEOMETRY_ABSTRACTSHAPE_H
#define MCCOMPOSITE_GEOMETRY_ABSTRACTSHAPE_H


namespace mccomposite {

  struct AbstractShapeVisitor;
  
  struct AbstractShape {

    //meta methods
    virtual ~AbstractShape( ) {};

    //methods
    virtual void identify( AbstractShapeVisitor & visitor ) const = 0;
  };

}


#endif

// version
// $Id$

// End of file 
