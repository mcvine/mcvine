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


#ifndef MCCOMPOSITE_GEOMETRY_ABSTRACTSHAPEVISITOR_H
#define MCCOMPOSITE_GEOMETRY_ABSTRACTSHAPEVISITOR_H

namespace mccomposite {

  struct Box;

  struct AbstractShapeVisitor {
  
    //meta methods
    virtual ~AbstractShapeVisitor( ) {};

    //methods
    virtual void onBox( const Box & box ) = 0;
  };

}

#endif

// version
// $Id$

// End of file 
