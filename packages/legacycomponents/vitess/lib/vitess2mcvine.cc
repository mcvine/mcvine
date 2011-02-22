#include "vitess2mcvine.h"


namespace vitess {

  void vitessneutrons2mcvineneutrons
  (const std::vector<Neutron> &neutrons, mcni::Neutron::Events &evts)
  {
    evts.resize(neutrons.size());
    mcni::Neutron::Events::iterator outit=evts.begin();
    for (std::vector<Neutron>::const_iterator it=neutrons.begin();
	 it<neutrons.end(); it++) {
      vitessneutron2mcvineneutron(*it, *outit);
      outit ++;
    }
  }

} // vitess

