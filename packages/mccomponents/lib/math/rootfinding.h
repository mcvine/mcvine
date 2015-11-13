// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCCOMPONENTS_MATH_ROOTFINDING_H
#define MCCOMPONENTS_MATH_ROOTFINDING_H

#include <vector>
#include "mccomponents/exception.h"
#include "Functor.h"

namespace mccomponents{ namespace math{

  class RootNotFound :public mccomponents::Exception {
  public:
    RootNotFound(const char *m = "root not found") :Exception(m) {}
  };

  /// base class for a root finder
  class RootFinder{
  public:
    ///ctor
    /// xacc....desired x accuracy
    RootFinder( double xacc ) :
      m_xacc(xacc) 
    {}
    virtual ~RootFinder() {}

    /// solve given function in the region (x1, x2) and return the first root found
    virtual double solve( double x1, double x2, const Functor & function ) const = 0;

    /// solve given function in the region (x1, x2) and return the first root found. if failed is set, it means it fails to find a solution
    virtual double solve( double x1, double x2, const Functor & function, bool &failed ) const = 0;
  protected:
    //data
    double m_xacc;
  };

  /// base class of roots finder
  class RootsFinder {
  public:
    virtual ~RootsFinder() {}
    /// solve given function in the region (x1, x2) and return all roots found
    virtual std::vector<double> solve( double x1, double x2, const Functor & function) const = 0;
    /// solve given function in the region (x1, x2) and return all roots found
    virtual void solve( double x1, double x2, const Functor & function, std::vector<double> & res) const = 0;
  };

  /// an implementation of roots finder that looks for roots in evenly divided steps
  class FindRootsEvenly: public RootsFinder {
  public:
    /// ctor
    ///  nSteps: number of steps in which roots will be found
    FindRootsEvenly( const RootFinder & rootFinder, size_t nSteps )
      : m_rootFinder(rootFinder), m_nSteps (nSteps)
    {}
    std::vector<double> solve( double x1, double x2, const Functor & function) const;
    void solve( double x1, double x2, const Functor & function, std::vector<double> & res) const;
  private:
    //data
    const RootFinder & m_rootFinder;
    size_t m_nSteps;
  };

  // collection of algorithms to find root
  namespace Algorithms{

    namespace Bracketing{
      
      namespace Ridder{
  
	const double UNUSED = (-1.11e30);
	const unsigned long MAX_NUM_LOOPS = 60;

	void check_answer( double ans ); 

	//! find a root between x1 and x2 using Ridder's algorithm (brackets)
	/*!
	  \param func f(x, parameters), the function to found root. 
	  \param parameters parameters for the function func
	  \param xacc accuracy requirement
	*/
	double zridd(double (*func)(double, const std::vector<double> &), 
		     double x1, double x2, 
		     const std::vector<double> &parameters, double xacc,
		     bool &failed);

	//! find a root between x1 and x2 using Ridder's algorithm (brackets)
	/*!
	  \param f the function to found root. 
	  \param xacc accuracy requirement
	*/
	double zridd(const Functor &f,
		     double x1, double x2, double xacc, bool &failed);

	/// zridd as a subclass of RootFinder
	class ZRidd : public RootFinder{
	public:
	  ZRidd( double xacc) : RootFinder(xacc) {}
	  double solve( double x1, double x2, const Functor &f ) const {
	    bool failed=0;
	    double rt = zridd( f, x1, x2, m_xacc, failed);
	    if (failed) throw RootNotFound();
	    return rt;
	  }
	  double solve( double x1, double x2, const Functor &f, bool &failed ) const {
	    return zridd( f, x1, x2, m_xacc, failed);
	  }
	};

      }//Ridder

    }//Bracketing

  }//Algorithms


}}//mccomponents:math


#endif // MCCOMPONENTS_MATH_ROOTFINDING_H
