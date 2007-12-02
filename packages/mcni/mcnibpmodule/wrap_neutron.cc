// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//



#include <sstream>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include "mcni/neutron.h"
#include "wrap_vector.h"


std::string NeutronEvent_str( const mcni::Neutron::Event & ev )
{
  std::ostringstream oss;
  ev.print(oss);
  return oss.str();
}

namespace mcni {

  inline void Evts_erase(Neutron::Events &evts, size_t index1, size_t index2) { 
    evts.erase( evts.begin()+index1, evts.begin()+index2 );
  }
  
  inline size_t Evts_size(Neutron::Events &evts) { 
    return evts.size();
  }
  
  inline void NEB_resize( Neutron::EventBuffer &neb, size_t n, const Neutron::Event & ne ) 
  { neb.resize( n, ne ); }
}


void wrap_neutron() 
{
  using namespace boost::python;
  using namespace mcni;
  using namespace mcni::Neutron;

  typedef Position<double> r_t;  
  typedef Velocity<double> v_t; 

  class_<Spin>
    ("NeutronSpin",
     init< double, double > () )
    .def_readonly("s1", &Spin::s1)
    .def_readonly("s2", &Spin::s2)
    ;

  class_<State>
    ("NeutronState", 
     init< const r_t &, const v_t &, const Spin &> ( )
     )
    .def_readonly("position", &State::position)
    .def_readonly("velocity", &State::velocity)
    .def_readonly("spin", &State::spin)
    ;
  

  class_<Event>
    ("NeutronEvent",
     init< const State &, double, double> ()
     )
    .def_readonly("state", &Event::state)
    .def_readonly("probability", &Event::probability)
    .def_readonly("time", &Event::time)
    .def("__str__", &NeutronEvent_str)
    ;


  wrap::wrap_vector2<Event> ("Event");

  class_<EventBuffer, bases<Events> >
    ("NeutronEventBuffer",
     init< size_t > ()  )
    .def("snapshot", &Neutron::EventBuffer::snapshot)
    .def("resize", &NEB_resize)
    ;

  def("abs2rel_batch", abs2rel_batch);
  def("rel2abs_batch", rel2abs_batch);
}


// version
// $Id: wrap_neutron_buffer.cc 598 2007-01-21 19:48:06Z linjiao $

// Generated automatically by CxxMill on Mon Apr 11 17:40:33 2005

// End of file 
