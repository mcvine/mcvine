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


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQE_SQE_FROMEXPRESSION_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQE_SQE_FROMEXPRESSION_H


#include <string>
#include <vector>
#include "mcni/test/exception.h"
#include "AbstractSQE.h"
#include "fparser/fparser.hh"


namespace mccomponents {

  namespace sample {

    /// S(scalar Q, E )
    class SQE_fromexpression: public mccomponents::sample::AbstractSQE
    {

    public:

      // meta methods
      SQE_fromexpression ( const std::string & expr);
      SQE_fromexpression ( const char * expr) : SQE_fromexpression(std::string(expr)) {}
      
      // methods
      virtual inline double operator () ( double Q, double E ) {
	static double vals[2];
	vals[0] = Q; vals[1] = E;
	return m_fparser.Eval(vals);
      }

      class BadExpression: public mcni::Exception {
      public:
	BadExpression(const std::string &s) : mcni::Exception(s) {}
      };
        
    private:
      FunctionParser m_fparser;
    } ;

  } // Simulation::

} // DANSE::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQE_SQE_FROMEXPRESSION_H

// version
// $Id$

// End of file 
