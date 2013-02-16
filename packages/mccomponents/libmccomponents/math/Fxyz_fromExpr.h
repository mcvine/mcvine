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


#ifndef MCCOMPONENTS_MATH_FXYZ_FROMEXPRESSION_H
#define MCCOMPONENTS_MATH_FXYZ_FROMEXPRESSION_H


#include <string>
#include <vector>
#include "mcni/test/exception.h"
#include "fparser/fparser.hh"


namespace mccomponents {

  namespace math {

    /// f(x,y,z) from a expr string
    /// Usage:
    ///   Fxyz_fromExpr f("sin(x+y+z)");
    ///   f(3.14, 0, 0);
    ///   Fxyz_fromExpr f("sin(Qx+Qy+Qz)", "Qx,Qy,Qz");
    ///   f(3.14, 0, 0);
    class Fxyz_fromExpr
    {

    public:

      // meta methods
      Fxyz_fromExpr ( const std::string & expr, std::string args="x,y,z")
      {
	std::string vars = args;
	int res = m_fparser.Parse(expr, vars);
	if (res >=0 ) {
	  throw BadExpression(expr);
	}
      }
      
      // methods
      virtual inline double operator () ( double x, double y, double z) {
	static double vals[3];
	vals[0] = x; vals[1] = y; vals[2] = z;
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


#endif // MCCOMPONENTS_MATH_FXYZ_FROMEXPRESSION_H

// version
// $Id$

// End of file 
