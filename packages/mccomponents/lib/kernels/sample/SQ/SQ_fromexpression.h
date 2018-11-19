// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_SQ_FROMEXPRESSION_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_SQ_FROMEXPRESSION_H


#include <string>
#include <vector>
#include "mcni/test/exception.h"
#include "AbstractSQ.h"
#include "fparser/fparser.hh"


namespace mccomponents {

  namespace sample {

    /// S(scalar Q, E )
    class SQ_fromexpression: public mccomponents::sample::AbstractSQ
    {

    public:

      // meta methods
      SQ_fromexpression ( const std::string & expr);
      
      // methods
      virtual inline double operator () ( double Q ) {
	static double vals[1];
	vals[0] = Q;
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


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_SQ_FROMEXPRESSION_H

// End of file 
