// -*- c++ -*-

#ifndef MCVINE_VITESS_STREAM2NEUTRONBUFFER_H
#define MCVINE_VITESS_STREAM2NEUTRONBUFFER_H

#include <vector>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"
#include "neutron.h"
#include "utils.h"

// convert vitess neutron stream to mcvine neutron buffer

namespace vitess {

  void vitessneutron2mcvineneutron
  (const Neutron & neutron, mcni::Neutron::Event &ev)
  {
    ev.time =  neutron.Time;
    ev.probability = neutron.Probability;
    convertV3<VectorType, mcni::Position<double> >
      (neutron.Position, ev.state.position);
    convertV3<VectorType, mcni::Velocity<double> >
      (neutron.Vector, ev.state.velocity);

    // XXX spin? XXX
  }

  void vitessneutrons2mcvineneutrons
  (const std::vector<Neutron> &neutrons, mcni::Neutron::Events &evts);

} // vitess

#endif
