#include "neutronbuffer2stream.h"


namespace vitess {

  void mcvineneutrons2vitessneutrons
  (const mcni::Neutron::Events &evts,
   std::vector<Neutron> &neutrons)
  {
    neutrons.resize(evts.size());
    std::vector<Neutron>::iterator outit=neutrons.begin();
    for (mcni::Neutron::Events::const_iterator it=evts.begin();
	 it<evts.end(); it++) {
      mcvineneutron2vitessneutron(*it, *outit);
      outit ++;
    }
  }

  std::ostream & neutronbuffer2stream
    (const mcni::Neutron::Events &evts, std::ostream &os)
  {
    std::vector<Neutron> neutrons;
    mcvineneutrons2vitessneutrons(evts, neutrons);
    os.write((char *)(&neutrons[0]), sizeof(Neutron)*neutrons.size());
    return os;
  }

} // vitess

