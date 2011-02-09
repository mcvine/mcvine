#include <vector>
#include <iostream>

#include "mcni/math/number.h"
#include "mcni/test/assert.h"
#include "mccomponents/math/misc.h"
#include "mccomponents/math/rootfinding.h"


using std::vector;
using std::cout;
using std::endl;
using mcni::assertAlmostEqual;
using mcni::assertNumberEqual;
using mcni::PI;
using mccomponents::math::Algorithms::Bracketing::Ridder::zridd;
using namespace mccomponents::math;


//! sin(ax+b)
double cSin(double x, const vector<double> &parms)
{
  if (parms.size()==2) {
    return sin(parms[0]*x+parms[1]);
  } else {
    throw "cSin(x, parms): Dont' understand parameters given";
  }
}

using mccomponents::math::Functor;
class SinFunctor : public Functor{
private:
  double _a; double _b;
public:
  SinFunctor(double a, double b): _a(a), _b(b) {}
  double evaluate(double x) const { return sin(_a*x+_b); }
};

void test_zridd()
{
  cout << "* Testing zridd with normal c function..."<< endl;
  double xacc = 1.e-7, root;
  
  vector<double> parms(2), root_list;
  bool failed;
  
  //----------sin(x) in (-1,1)----------------------------------------
  //function parameters
  parms[0] = 1.; parms[1] = 0.; 
  //find root
  // cout << "-> A root of sin(x) is in (-1, 1):" 
  //      << zridd( cSin, -1, 1, parms, xacc, failed) <<endl;
  //check answer
  assertAlmostEqual(  zridd( cSin, -1, 1, parms, xacc, failed), 0);
  
  //--------sin(x) in PI/2, PI*5/2------------------------------------
  //root not found exception
  // zridd is a simple algorithm that won't work for a region that is too large
  root = zridd( cSin, PI/2, PI*5/2, parms, xacc, failed);
  if (!failed) 
    throw mcni::Exception("should catch error");
  else
    //std::cerr << "-> sin(x): root not found in (PI/2, PI*5/2)!" <<endl;
    // do nothing
    ;

  //---------sin(x+0.5) in (-1, 1)------------------------------------
  parms[1] = 0.5;
  // cout << "-> A root of sin(x+0.5) in (-1,1): " << zridd( cSin, -1, 1, parms, xacc, failed) <<endl;
  assertAlmostEqual(  zridd( cSin, -1, 1, parms, xacc, failed), -0.5, 1e-7, 1e-7 );
}


void test_zridd_functor()
{
  cout << "* Testing zridd with functor..."<< endl;
  double xacc = 1.e-7;
  
  // try functor
  SinFunctor sin_f(1.0, 0.0); bool failed;
  // cout << "-> A root of sin(x) is in (-1, 1):" 
  //      << zridd( sin_f, -1, 1,  xacc, failed) <<endl;
  assertAlmostEqual(  zridd( sin_f, -1, 1,  xacc, failed), 0 );
}

void test_ZRidd()
{
  cout << "* Testing ZRidd, a root finder..." << endl;
  Algorithms::Bracketing::Ridder::ZRidd rootFinder( 1.e-7 );
  SinFunctor sin_f(1.0, 0.0);
  double root = rootFinder.solve( -0.5, 0.5,  sin_f) ;
  // cout << "-> A root of sin(x) is in (-1, 1):" << root <<endl;
  assertAlmostEqual(  root, 0 );
}

void test_findRootsEvenly()
{
  cout << "* Testing FindRootsEvently, a roots finder..." << endl;
  Algorithms::Bracketing::Ridder::ZRidd rootFinder( 1.e-7 );
  size_t nSteps = 10000;
  FindRootsEvenly rootsFinder( rootFinder, nSteps );

  SinFunctor sin_f(1.0, 0.0);

  cout << " - test method 'solve' version 1..." << endl;
  std::vector<double> roots = rootsFinder.solve( PI/2, PI*5/2,  sin_f) ;
  // cout << "-> sin(x) has roots in (PI/2, PI*5/2): " << roots << endl;
  assertNumberEqual( roots.size(), 2 );
  assertAlmostEqual(  roots[0], PI );
  assertAlmostEqual(  roots[1], PI*2 );


  cout << " - test method 'solve' version 2..." << endl;
  std::vector<double> roots1;
  rootsFinder.solve( PI/2, PI*5/2,  sin_f, roots1) ;
  // cout << "-> sin(x) has roots in (PI/2, PI*5/2): " << roots1 << endl;
  assertNumberEqual( roots1.size(), 2 );
  assertAlmostEqual(  roots1[0], PI );
  assertAlmostEqual(  roots1[1], PI*2 );

  cout << " . succeeded." << endl;
}

int main()
{
  std::cout << "== rootfinding tests ==" << std::endl;
  test_zridd();
  test_zridd_functor();
  test_ZRidd();
  test_findRootsEvenly();
  std::cout << "* All tests passed" << std::endl;
}
