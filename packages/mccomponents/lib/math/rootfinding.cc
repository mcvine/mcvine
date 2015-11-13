#include <iostream>
#include <vector>
#include <cmath>
#include "mccomponents/math/misc.h"
#include "mccomponents/math/rootfinding.h"

namespace mccomponents { namespace math {

  std::vector<double> 
  FindRootsEvenly::solve
  ( double x1, double x2, const Functor & function) 
    const
  {
    // resutl
    std::vector<double> root_list;
    solve(x1, x2, function, root_list);
    return root_list;
  }//solve


  void
  FindRootsEvenly::solve
  ( double x1, double x2, const Functor & function,  std::vector<double> & root_list) 
    const
  {
    root_list.clear();
    // temp vars
    double root,range=x2-x1;
    double step = range/m_nSteps;
	
    for (size_t i=0; i<m_nSteps; i++) {
      bool failed = 0;
      try {
	root = m_rootFinder.solve (x1+step*i, x1+step*(i+1), function, failed);
	if (failed) continue;
	root_list.push_back(root);
      }
      catch (const char *str) {
	std::cerr << "caught " << str 
		  << " from function findaroot " << std::endl;
      }
      catch (const RootNotFound & rnf) {
	std::cerr << "caght root not found " << std::endl;
      }
	    
    }//for loop i

  }//solve


  namespace Algorithms{

    namespace Bracketing{
      
      namespace Ridder{

        void check_answer( double ans ) {
          if (ans == UNUSED) {
            throw RootNotFound();
          }
        }

	double zridd(double (*func)(double, const std::vector<double> &), 
		     double x1, double x2, 
		     const std::vector<double> &parameters, double xacc,
		     bool &failed)
	{
	  
	  using misc::sign;

	  unsigned long j;
	  double ans, fh, fl, fm, fnew, s, xh, xl, xm, xnew;
	  
// 	  printf("zridd called with brackets %g %g acceptance %g \n",x1,x2,xacc);
// 	  printf("and %i parameters %g %g %g %g %g \n",Nparms,parms[0],parms[1],parms[2],parms[3], parms[4]); 
	  
	  fl=(*func)(x1,parameters);
	
	  fh=(*func)(x2,parameters);

// 	  printf("Function values: %g %g \n",fl,fh); 

	  if (fl*fh >= 0) {

	    if (fl==0) return x1;
	    if (fh==0) return x2;
	    failed = 1;
	    return 0;

	  } else {

	    xl=x1;
	    xh=x2;
	    ans=UNUSED;
	    for (j=1; j<MAX_NUM_LOOPS; j++) {

	      xm=0.5*(xl+xh);
	      
	      fm=(*func)(xm, parameters);
	      s=sqrt(fm*fm-fl*fh);
	      if (s == 0.0) {
		check_answer(ans);
		return ans;
	      }
	      xnew=xm+(xm-xl)*((fl >= fh ? 1.0 : -1.0)*fm/s);
	      if (fabs(xnew-ans) <= xacc) {
		check_answer(ans);
		return ans;
	      }
	      ans=xnew;
		
	      fnew=(*func)(ans, parameters);
	      if (fnew == 0.0) {
		check_answer(ans);
		return ans;
	      }
	      if (sign(fm,fnew) != fm) {

		xl=xm;
		fl=fm;
		xh=ans;
		fh=fnew;

	      } else if (sign(fl,fnew) != fl)  {

		xh=ans;
		fh=fnew;

	      } else if(sign(fh,fnew) != fh)  {

			xl=ans;
			fl=fnew;
	      } else {

		throw "never get here in zridd";

	      }

	      if (fabs(xh-xl) <= xacc) {
		check_answer(ans);
		return ans;
	      }
	    }

	    throw "zridd exceeded maximum iterations";
	  
	  }
	  
	  return 0.0;  // Never get here 
	} //zridd

	double zridd(const Functor &f,
		     double x1, double x2, double xacc, bool &failed)
	{
	  
	  using misc::sign;

	  unsigned long j;
	  double ans, fh, fl, fm, fnew, s, xh, xl, xm, xnew;
	  
	  try {
	    fl=f.evaluate(x1);
	  } 
	  catch (...) {
	    std::cerr << "zridd - x1 = " << x1 << std::endl;
	    throw;
	  }

	  try {
	  fh=f.evaluate(x2);
	  } 
	  catch (...) {
	    std::cerr << "zridd - x2 = " << x2 << std::endl;
	    throw;
	  }

// 	  printf("Function evaluates: %g %g \n",fl,fh); 

	  if (fl*fh >= 0) {

	    if (fl==0) return x1;
	    if (fh==0) return x2;       
	    failed = 1;
	    return 0;

	  } else {

	    xl=x1;
	    xh=x2;
	    ans=UNUSED;
	    for (j=1; j<MAX_NUM_LOOPS; j++) {

	      xm=0.5*(xl+xh);

	      try {
		fm = f.evaluate(xm);
	      } 
	      catch (...) {
		std::cerr << "zridd - xm = " << xm << std::endl;
		throw;
	      }
	      double temp = fm*fm-fh*fl;
	      if (temp>=0) {
		s=sqrt(temp);
	      
		if (s == 0.0) {
		  check_answer(ans);
		  return ans;
		}
		xnew=xm+(xm-xl)*((fl >= fh ? 1.0 : -1.0)*fm/s);
	      } else {
		xnew = xm;
	      }
	      if (fabs(xnew-ans) <= xacc) {
		check_answer(ans);
		return ans;
	      }
	      ans=xnew;
		
	      try {
		fnew=f.evaluate(ans);
	      } 
	      catch (...) {
		std::cerr << "zridd: "
			  << "fm, fl, fh = " << fm << ',' << fl << ',' << fh
			  << std::endl
			  << "s = " << s << std::endl
			  << "xm, xl = " << xm << ',' << xl << std::endl
			  << "ans = " << ans << std::endl;
		throw;
	      }

	      if (fnew == 0.0) {
		check_answer(ans);
		return ans;
	      }
	      if (sign(fm,fnew) != fm) {

		xl=xm;
		fl=fm;
		xh=ans;
		fh=fnew;

	      } else if (sign(fl,fnew) != fl)  {

		xh=ans;
		fh=fnew;

	      } else if(sign(fh,fnew) != fh)  {

			xl=ans;
			fl=fnew;
	      } else {

		std::cerr << "never get here in zridd";
		throw "never get here in zridd";

	      }

	      if (fabs(xh-xl) <= xacc) {
		check_answer(ans);
		return ans;
	      }
	    }

	    throw "zridd exceeded maximum iterations";
	  
	  }
	  
	  return 0.0;  // Never get here 
	} //zridd

      } //Ridder


    }//Bracketing

  }//Algorithm

}}//mccomponents::math
