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

  namespace geometry {

    /// forward declaration
    struct Box;
    struct Difference;
    struct Dilation;
    struct Intersection;
    struct Reflection;
    struct Rotation;
    struct Translation;
    struct Union;


    /// abstract shape visitor.
    struct AbstractShapeVisitor {
      
      //meta methods
      virtual ~AbstractShapeVisitor( ) {};
      
      //methods
      // for primitives
      virtual void onBox( const Box & box ) = 0;
      // for operations
      virtual void onDifference( const Difference & difference ) = 0;
      virtual void onDilation( const Dilation & dilation ) = 0;
      virtual void onIntersection( const Intersection & intersection ) = 0;
      virtual void onReflection( const Reflection & reflection ) = 0;
      virtual void onRotation( const Rotation & rotation ) = 0;
      virtual void onTranslation( const Translation & translation ) = 0;
      virtual void onUnion( const Union & aunion ) = 0;
    };
    
  }

}

#endif

// version
// $Id$

// End of file 
