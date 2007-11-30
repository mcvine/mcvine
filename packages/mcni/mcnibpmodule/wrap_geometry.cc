#include "wrap_geometry.h"

void wrap_geometry()
{
  using namespace wrap;

  wrap_Position<double>("double");
  wrap_Velocity<double>("double");
  wrap_RotationMatrix<double>("double");
}
