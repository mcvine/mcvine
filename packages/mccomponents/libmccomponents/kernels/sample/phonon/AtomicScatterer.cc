#include "mccomponents/kernels/sample/phonon/AtomicScatterer.h"



std::ostream &  operator <<  ( std::ostream & os, const  mccomponents::kernels::AtomicScatterer & atom )
{
  os << "AtomicScatterer(" 
     << "mass = " << atom.mass << ", "
    //<< "position = " << atom.position << ", "
     << "coherent_scattering_length = " << atom.coherent_scattering_length << ", "
     << "coherent_cross_section = " << atom.coherent_cross_section << ","
     << "incoherent_cross_section = " << atom.incoherent_cross_section << ","
     << ")";
  return os;
}
