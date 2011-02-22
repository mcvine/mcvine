#include <fstream>
#include "vitess/neutronbuffer2stream.h"

int main()
{
  mcni::Neutron::Events evts(10);
  
  std::ofstream ofs("out-evts", std::ofstream::binary);
  vitess::neutronbuffer2stream(evts, ofs);
}
