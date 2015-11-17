#include "mccomponents/math/Fx_fromExpr.h"
#include <cmath>
#include <gsl/gsl_sf_bessel.h>


class ModBessellType1:
  public FunctionParser::FunctionWrapper
{
public:
  virtual double callFunction(const double* values)
  {
    return gsl_sf_bessel_In(int(values[0]), values[1]);
  }
};

void mccomponents::math::Fx_fromExpr::_initFParser()
{
  m_fparser.AddFunctionWrapper("ModBessellType1", ModBessellType1(), 2);
}
