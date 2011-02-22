// -*- c++ -*-

#ifndef MCVINE_VITESS_NEUTRONBUFFER2STREAM_H
#define MCVINE_VITESS_NEUTRONBUFFER2STREAM_H

#include <iostream>
#include <cmath>
#include <vector>

#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"
#include "neutron.h"

#include "mcni/math/number.h"
#include "mcni/neutron/units_conversion.h"

// convert mcvine neutron buffer to vitess neutron stream

namespace vitess {

  template <typename V3>
  double wavelength(const V3& velocity)
  {
    double v = std::sqrt(velocity[0]*velocity[0] 
			 +velocity[1]*velocity[1]
			 +velocity[2]*velocity[2]);
    using namespace mcni::neutron_units_conversion;
    return 2*mcni::PI/(v2k*v);
  }
  
  template <typename V3a, typename V3b>
  void convertV3
  (const V3a & invec, V3b & outvec)
  {
    for (unsigned int i=0; i<3; i++) 
      outvec[i] = invec[i];
  }

  void mcvineneutron2vitessneutron(const mcni::Neutron::Event &ev,
				   Neutron & neutron)
  {
    // XXX ?
    // neutron.ID.IDGrp = ?;
    neutron.ID.IDNo = 0;
    neutron.Debug = ' ';
    neutron.Color = 0;
    // XXX ?

    neutron.Time = ev.time;
    neutron.Wavelength = wavelength(ev.state.velocity);
    neutron.Probability = ev.probability;
    convertV3<mcni::Position<double>, VectorType>
      (ev.state.position, neutron.Position);
    convertV3<mcni::Velocity<double>, VectorType>
      (ev.state.velocity, neutron.Vector);

    // XXX spin? XXX
  }

  void mcvineneutrons2vitessneutrons
  (const mcni::Neutron::Events &evts, std::vector<Neutron> &neutrons);

  std::ostream & neutronbuffer2stream
  (const mcni::Neutron::Events &evts, std::ostream &os);

} // vitess

#endif
