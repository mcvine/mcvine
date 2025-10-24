// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#include <boost/python.hpp>

namespace bpext{
  void wrap();  
}

BOOST_PYTHON_MODULE(_examplebpbinding)
{
  using namespace bpext;
  wrap();
}

// version
// $Id: simulation_phononmodule.cc 33 2005-06-13 06:59:43Z linjiao $

// End of file
