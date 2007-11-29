#include "wrap_vector3.h"

void wrapVector3s()
{
  wrapVector3<double>( "Vector3_double" );
  wrapVector3< Vector3<double> >( "Matrix3_double" );
}
