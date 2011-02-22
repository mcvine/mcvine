#include <fstream>
#include <cassert>
#include "vitess/vitess2mcvine.h"

int main()
{
  mcni::Neutron::Events evts;
  std::vector<vitess::Neutron> neutrons(10);
  vitess::vitessneutrons2mcvineneutrons(neutrons, evts);
  assert(neutrons.size() == evts.size());
}
