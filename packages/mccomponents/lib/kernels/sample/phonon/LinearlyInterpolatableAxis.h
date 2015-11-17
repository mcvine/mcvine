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



#ifndef PHONON_LINEARLYINTERPOLATABLEAXIS_H
#define PHONON_LINEARLYINTERPOLATABLEAXIS_H


namespace DANSE { 
  namespace phonon {

  /// describe an "axis" for a physical quantity that is continuous.
  /// The axis has "ticks" at positions defined by "start", "n"
  /// and "step":
  ///    start, start+step, start +2*step, ..., start+n*step
  /// ebd 
  template <typename Float, typename N = unsigned int>
  struct LinearlyInterpolatableAxis {
    Float start, step;
    N n;
    LinearlyInterpolatableAxis( Float i_start, Float i_step, N i_n )
      : start(i_start), step(i_step), n(i_n)
    {
//       std::cout << "Linearlyinterpolatableaxis: "
// 		<< "start: " << i_start 
// 		<< std::endl;
    }
  };


  } //phonon::
} //DANSE::
  

#endif // PHONON_LINEARLYINTERPOLATABLEAXIS_H

// version
// $Id$

// End of file 
