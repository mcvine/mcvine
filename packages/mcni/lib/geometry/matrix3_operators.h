// -*- C++ -*-
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

#ifndef MCNI_GEOMETRY_MATRIX3_OPERATORS_H
#define MCNI_GEOMETRY_MATRIX3_OPERATORS_H

namespace mcni{
  
  namespace matrix3_operators{
    
    // matrix3 dot vector3
    template <typename M3, typename V3>
    V3 dot_mv
    (const M3 & m, const V3 & v)
    {
      V3 ret;
      ret[0] = m(0,0)*v[0] + m(0,1)*v[1] + m(0,2)*v[2];
      ret[1] = m(1,0)*v[0] + m(1,1)*v[1] + m(1,2)*v[2];
      ret[2] = m(2,0)*v[0] + m(2,1)*v[1] + m(2,2)*v[2];
      return ret;
    }
    
  } // matrix3_operators:
} // mcni:

#endif


// version
// $Id$

// End of file

