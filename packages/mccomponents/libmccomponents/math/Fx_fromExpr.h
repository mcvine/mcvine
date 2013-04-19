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


#ifndef MCCOMPONENTS_MATH_FX_FROMEXPRESSION_H
#define MCCOMPONENTS_MATH_FX_FROMEXPRESSION_H


#include <string>
#include <vector>
#include "mcni/test/exception.h"
#include "fparser/fparser.hh"
#include <gsl/gsl_sf_bessel.h>

namespace mccomponents {

  namespace math {

    class ModBessellType1:
      public FunctionParser::FunctionWrapper
    {
    public:
      virtual double callFunction(const double* values)
      {
        return gsl_sf_bessel_In(int(values[0]), values[1]);
      }
    };

    /// f(x) from a expr string
    /// Usage:
    ///   Fx_fromExpr f("sin(x)");
    ///   f(3.14);
    ///   Fx_fromExpr f("sin(Q)", "Q");
    ///   f(3.14);
    class Fx_fromExpr
    {

    public:

      // meta methods
      Fx_fromExpr ( const std::string & expr, std::string arg="x")
      {
	m_fparser.AddFunctionWrapper("ModBessellType1", ModBessellType1(), 2);
	std::string vars = arg;
	int res = m_fparser.Parse(expr, vars);
	if (res >=0 ) {
	  throw BadExpression(expr);
	}
      }
      
      // methods
      virtual inline double operator () ( double x) {
	static double vals[1];
	vals[0] = x;
	return m_fparser.Eval(vals);
      }

      class BadExpression: public mcni::Exception {
      public:
	BadExpression(const std::string &s) : mcni::Exception(s) {}
      };
        
    private:
      FunctionParser m_fparser;
    } ;

  } // math::

} // mccomponents::


#endif // MCCOMPONENTS_MATH_FX_FROMEXPRESSION_H

// version
// $Id: SQE_fromexpression.h 601 2010-10-03 19:55:29Z linjiao $

// End of file 
