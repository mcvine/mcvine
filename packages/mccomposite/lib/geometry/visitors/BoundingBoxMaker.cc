#include <cassert>
#include "mccomposite/geometry/visitors/BoundingBoxMaker.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/exception.h"

#include "journal/debug.h"


namespace BoundingBoxMaker_impl{

  char * jrnltag = "mccomposite.geometry.BoundingBoxMaker";
  
}

namespace {
  using namespace mccomposite::geometry;
  BoundingBox uniteBB(const BoundingBox &bb1, const BoundingBox &bb2)
  {
    double xmin = std::min(bb1.cx-bb1.sx/2, bb2.cx-bb2.sx/2);
    double xmax = std::max(bb1.cx+bb1.sx/2, bb2.cx+bb2.sx/2);
    double ymin = std::min(bb1.cy-bb1.sy/2, bb2.cy-bb2.sy/2);
    double ymax = std::max(bb1.cy+bb1.sy/2, bb2.cy+bb2.sy/2);
    double zmin = std::min(bb1.cz-bb1.sz/2, bb2.cz-bb2.sz/2);
    double zmax = std::max(bb1.cz+bb1.sz/2, bb2.cz+bb2.sz/2);
    BoundingBox bb;
    bb.cx = (xmin+xmax)/2.; bb.sx = xmax-xmin;
    bb.cy = (ymin+ymax)/2.; bb.sy = ymax-ymin;
    bb.cz = (zmin+zmax)/2.; bb.sz = zmax-zmin;
    return bb;
  }
  BoundingBox intersectBB(const BoundingBox &bb1, const BoundingBox &bb2)
  {
    double xmin = std::max(bb1.cx-bb1.sx/2, bb2.cx-bb2.sx/2);
    double xmax = std::min(bb1.cx+bb1.sx/2, bb2.cx+bb2.sx/2);
    double ymin = std::max(bb1.cy-bb1.sy/2, bb2.cy-bb2.sy/2);
    double ymax = std::min(bb1.cy+bb1.sy/2, bb2.cy+bb2.sy/2);
    double zmin = std::max(bb1.cz-bb1.sz/2, bb2.cz-bb2.sz/2);
    double zmax = std::min(bb1.cz+bb1.sz/2, bb2.cz+bb2.sz/2);
    BoundingBox bb;
    bb.cx = (xmin+xmax)/2.; bb.sx = std::max(xmax-xmin,0.);
    bb.cy = (ymin+ymax)/2.; bb.sy = std::max(ymax-ymin,0.);
    bb.cz = (zmin+zmax)/2.; bb.sz = std::max(zmax-zmin,0.);
    return bb;
  }
}


mccomposite::geometry::BoundingBoxMaker::BoundingBoxMaker
()
{
}


mccomposite::geometry::BoundingBox
mccomposite::geometry::BoundingBoxMaker::make
( const AbstractShape & shape )
{
  shape.identify( *this );
  return bb;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Box * box )
{ 
  bb.sx = box->edgeX;
  bb.sy = box->edgeY;
  bb.sz = box->edgeZ;
  bb.cx = bb.cy = bb.cz = 0;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Cylinder * cylinder ) 
{
  bb.sx = cylinder->radius*2;
  bb.sy = bb.sx;
  bb.sz = cylinder->height;
  bb.cx = bb.cy = bb.cz = 0;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Pyramid * pyramid ) 
{
  const double & X = pyramid->edgeX;
  const double & Y = pyramid->edgeY;
  const double & height = pyramid->height;
  bb.sx = X; bb.sy = Y; bb.sz = height;
  bb.cx = 0; bb.cy = 0; bb.cz = -height/2;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Cone * cone ) 
{
  const double & X = cone->radius*2;
  const double & height = cone->height;
  bb.sx = X; bb.sy = X; bb.sz = height;
  bb.cx = 0; bb.cy = 0; bb.cz = -height/2;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Sphere * sphere ) 
{
  bb.cx = bb.cy = bb.cz = 0;
  bb.sx = bb.sy = bb.sz = sphere->radius*2;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Difference * difference ) 
{
  const AbstractShape &body1 = *(difference->shapes[0]) ; 
  const AbstractShape &body2 = *(difference->shapes[1]) ;
  body1.identify(*this); BoundingBox bb1 = bb;
  body2.identify(*this); BoundingBox bb2 = bb;
  bb = uniteBB(bb1, bb2);
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Intersection * intersection ) 
{
  const Composition::shapecontainer_t & shapes = intersection->shapes;

  assert(shapes.size()>0);
  shapes[0]->identify(*this);
  BoundingBox ret = bb;
  
  for (size_t i=1; i<shapes.size(); i++) {
    shapes[i]->identify(*this);
    ret = intersectBB(ret, bb);
  }
  bb = ret;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Union * aunion ) 
{
  const Composition::shapecontainer_t & shapes = aunion->shapes;

  assert(shapes.size()>0);
  shapes[0]->identify(*this);
  BoundingBox ret = bb;
  
  for (size_t i=0; i<shapes.size(); i++) {
    shapes[i]->identify(*this);
    ret = uniteBB(ret, bb);
  }
  bb = ret;
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Dilation * dilation ) 
{
  const AbstractShape &body = dilation->body ;
  const double &scale = dilation->scale ;
  body.identify(*this);
  bb.sx *= scale; bb.sy *= scale; bb.sz *= scale;
  bb.cx *= scale; bb.cy *= scale; bb.cz *= scale;
}


void
mccomposite::geometry::BoundingBoxMaker::visit
( const Reflection * reflection ) 
{
  throw Exception("handler for Reflection not implemented");
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Translation * translation ) 
{
  const AbstractShape &body = translation->body ; 
  const Vector &vector = translation->vector ;
  body.identify(*this);
  bb.cx+=vector[0];
  bb.cy+=vector[1];
  bb.cz+=vector[2];
}

void
mccomposite::geometry::BoundingBoxMaker::visit
( const Rotation * rotation )
{
  const AbstractShape &body = rotation->body ; 
  RotationMatrix rotationMatrix = rotation->rotmat ;
  body.identify(*this);
  Vector point(bb.cx, bb.cy, bb.cz);
  point = rotationMatrix * point;
  bb.cx = point[0]; bb.cy = point[1]; bb.cz = point[2];
  bb.sx = bb.sy = bb.sz = std::max(bb.sx, std::max(bb.sy, bb.sz));
}

