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
    struct Cylinder;
    struct Pyramid;
    struct Cone;
    struct Sphere;
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
      virtual void visit( const Box * box ) = 0;
      virtual void visit( const Cylinder * cylinder ) = 0;
      virtual void visit( const Pyramid * pyramid ) = 0;
      virtual void visit( const Cone * cone ) = 0;
      virtual void visit( const Sphere * sphere ) = 0;
      // for operations
      virtual void visit( const Difference * difference ) = 0;
      virtual void visit( const Dilation * dilation ) = 0;
      virtual void visit( const Intersection * intersection ) = 0;
      virtual void visit( const Reflection * reflection ) = 0;
      virtual void visit( const Rotation * rotation ) = 0;
      virtual void visit( const Translation * translation ) = 0;
      virtual void visit( const Union * aunion ) = 0;
    };
    
  }

}

#endif

// version
// $Id$

// End of file 
