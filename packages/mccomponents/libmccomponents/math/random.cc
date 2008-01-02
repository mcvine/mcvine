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

#include <cstdlib>
#include "mccomponents/math/random.h"


struct mccomponents::random::Generator::Details{

  Details( ) 
  {
    using namespace std;
    srand( (unsigned)time(0) );
  }
  
  Details( double seed )
  {
    using namespace std;
    srand( (unsigned)seed );
  }
  
  double generate( double min, double max ) const
  {
    using namespace std;
    return rand()*1./RAND_MAX*(max-min) + min;
  }

};


mccomponents::random::Generator::Generator()
  : m_details( new Details() )
{
}

mccomponents::random::Generator::Generator ( double seed )
  : m_details( new Details( seed ) )
{
}

mccomponents::random::Generator::~Generator()
{
}

// methods
double mccomponents::random::Generator::generate( double min, double max )
{
  return m_details->generate( min, max );
}

double mccomponents::random::Generator::generate01()
{
  return generate(0., 1.);
}


// version
// $Id$

// End of file 
