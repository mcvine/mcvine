// -*- c++ -*-

#ifndef MCVINE_VITESS_NEUTRONBUFFER2STREAM_H
#define MCVINE_VITESS_NEUTRONBUFFER2STREAM_H


#include <vector>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"
#include "neutron.h"
#include "utils.h"


// convert mcvine neutron buffer to vitess neutron stream

namespace vitess {

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
