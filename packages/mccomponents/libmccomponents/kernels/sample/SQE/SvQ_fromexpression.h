// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2014  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQE_SVQE_FROMEXPRESSION_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQE_SVQE_FROMEXPRESSION_H


#include <string>
#include <vector>
#include "mcni/math/number.h"
#include "mcni/test/exception.h"
#include "fparser/fparser.hh"


namespace mccomponents {

  namespace sample {

    /// S(Qx,Qy,Qz) from a expr string
    /// Usage:
    ///   SvQ_fromExpr("cos(0.5*Qx)*Q*s");
    ///   Q = |vQ|
    ///   s = Q/(4pi)
    class SvQ_fromExpr
    {

    public:

      // meta methods
      SvQ_fromExpr ( const std::string & expr, std::string args="Qx,Qy,Qz,Q,s")
      {
	std::string vars = args;
	int res = m_fparser.Parse(expr, vars);
	if (res >=0 ) {
	  throw BadExpression(expr);
	}
      }
      
      // methods
      virtual inline double operator () ( double x, double y, double z) {
	double vals[5];
	vals[0] = x; vals[1] = y; vals[2] = z;
	vals[3] = std::sqrt(x*x+y*y+z*z);
	vals[4] = vals[3]/4./mcni::PI;
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


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQE_SVQE_FROMEXPRESSION_H

// version
// $Id$

// End of file 
