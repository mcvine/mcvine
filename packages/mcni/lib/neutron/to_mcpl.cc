// -*- C++ -*-
// Jiao Lin <jiao.lin@gmail.com>

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <mcpl.h>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"
#include "mcni/neutron/State.h"
#include "mcni/neutron/Spin.h"
#include "mcni/neutron/units_conversion.h"


void
write_mcpl(const mcni::Neutron::EventBuffer &buffer, const char * filename)
{
  mcpl_outfile_t f = mcpl_create_outfile(filename);
  mcpl_hdr_set_srcname(f, "mcvine");

  // By default, floating point numbers will be stored in single precision and
  // neither polarisation nor user-flags will be stored in the file. These
  // defaults can be modified by one or more of the following calls (perhaps
  // they could be options to your McStas component):
  //
  //    mcpl_enable_userflags(f);
  mcpl_enable_polarisation(f);
  //    mcpl_enable_doubleprec(f);

  // If all particles will be of the same type, optimise the file a bit by:
  //
  mcpl_enable_universal_pdgcode(f,2112);  //all particles are neutrons

  //We can add comments (strings) to the header. It is always a good idea to add
  //comments explaining things like coordinate system, contents of user-flags
  //(if any), and what the values in the "weight" field means exactly.:
  mcpl_hdr_add_comment(f,"MCViNE neutrons");
  mcpl_hdr_add_comment(f,"z: along beam; y: vertical up; xyz: right hand cartesian.");

  //It is also possible to add binary data with mcpl_hdr_add_data, if desired
  //(can be indexed by strings). So for instance, custom persistified
  //configuration meta-data could be added (or perhaps just a text file used by
  //configuration by your programme, if appropriate).

  //Allocate the particle structure we will use during the simulation loop
  //to register particle data in the output file:
  mcpl_particle_t * particle = mcpl_get_empty_particle(f);

  //Simulation loop, modify the particle struct and add to the file as many
  //times as needed (here everything will simply be filled with some stupid
  //random numbers):
  int i;
  for (i = 0; i < buffer.size(); ++i) {
    const mcni::Neutron::Event &event = buffer[i];
    //particle type:
    particle->pdgcode = 2112; //neutrons
    //position in centimeters:
    particle->position[0] = event.state.position.x*100;
    particle->position[1] = event.state.position.y*100;
    particle->position[2] = event.state.position.z*100;
    //kinetic energy in MeV:
    const mcni::Neutron::State::velocity_t& v = event.state.velocity;
    double vl = v.length();
    particle->ekin = mcni::neutron_units_conversion::v2E(vl)/1e9; //meV to MeV
    //momentum direction (unit vector):
    particle->direction[0] = v.x/vl;
    particle->direction[1] = v.y/vl;
    particle->direction[2] = v.z/vl;
    //pol
    const mcni::Neutron::Spin &spin = event.state.spin;
    double ct = std::cos(spin.s1), st = std::sin(spin.s1);
    double cp = std::cos(spin.s2), sp = std::sin(spin.s2);
    particle->polarisation[0] = st*sp;
    particle->polarisation[1] = ct;
    particle->polarisation[0] = st*cp;
    //time in milliseconds:
    particle->time = event.time*1e3;
    //weight in unspecified units:
    particle->weight = event.probability;
    //modify userflags and polarisation (what units?) as well, if enabled.

    //Finally, add the particle to the file:
    mcpl_add_particle(f,particle);
  }

  //At the end, remember to properly close the output file (and cleanup mem if desired):
  mcpl_closeandgzip_outfile(f);
  return;
}

// End of file
