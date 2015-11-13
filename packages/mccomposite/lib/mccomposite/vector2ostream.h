// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCCOMPOSITE_VECTOR2STREAM_H
#define MCCOMPOSITE_VECTOR2STREAM_H

#include <iostream>
#include <vector>

template <typename T>
std::ostream & operator << (std::ostream &os, const std::vector<T> & v)
{
  typedef typename std::vector<T>::const_iterator Iterator;

  for (Iterator it = v.begin(); it < v.end(); it ++)
    os << *it << ", ";
  
  return os;
}


#endif // MCCOMPOSITE_VECTOR2STREAM_H


// version
// $Id$

// End of file 
