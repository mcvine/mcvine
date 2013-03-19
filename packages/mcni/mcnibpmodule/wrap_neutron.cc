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

  inline void NEB_clear( Neutron::EventBuffer &neb)
  {
    neb.clear();
  }

  inline void Evts_append_events_it
  (Neutron::Events &evts, Neutron::Events::const_iterator eit1, Neutron::Events::const_iterator eit2 ) 
  {
    assert (eit2-eit1>=0);
    size_t n = evts.size();
    evts.resize( n+eit2-eit1 );
    std::copy( eit1, eit2, evts.begin() + n );
  }

  inline void Evts_append_events
  (Neutron::Events & evts, const Neutron::Events & newevts, size_t start_index, size_t end_index )
  {
    Evts_append_events_it( evts, newevts.begin()+start_index, newevts.begin()+end_index );
  }
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
    .def_readwrite("position", &State::position)
    .def_readwrite("velocity", &State::velocity)
    .def_readwrite("spin", &State::spin)
    ;
  

  class_<Event>
    ("NeutronEvent",
     init< const State &, double, double> ()
     )
    .def_readonly("state", &Event::state)
    .def_readwrite("probability", &Event::probability)
    .def_readwrite("time", &Event::time)
    .def("energy", &Event::energy)
    .def("__str__", &NeutronEvent_str)
    ;


  wrap::wrap_vector2<Event> ("Event");

  class_<EventBuffer, bases<Events> >
    ("NeutronEventBuffer",
     init< size_t > ()  )
    .def("snapshot", &Neutron::EventBuffer::snapshot)
    .def("resize", &NEB_resize)
    .def("clear", &NEB_clear)
    .def("append", &Evts_append_events)
    .def("fromCevents", &events_fromCevents)
    .def("toCevents", &events_toCevents)
    .def("swap", &Neutron::EventBuffer::swap)
    ;

  
  class_<cEvent>
    ("cNeutronEvent")
    .def_readwrite("x", &cEvent::x)
    .def_readwrite("y", &cEvent::y)
    .def_readwrite("z", &cEvent::z)
    .def_readwrite("vx", &cEvent::vx)
    .def_readwrite("vy", &cEvent::vy)
    .def_readwrite("vz", &cEvent::vz)
    .def_readwrite("s1", &cEvent::s1)
    .def_readwrite("s2", &cEvent::s2)
    .def_readwrite("time", &cEvent::time)
    .def_readwrite("probability", &cEvent::probability)
    ;

  def("abs2rel_batch", abs2rel_batch);
  def("rel2abs_batch", rel2abs_batch);
}


// version
// $Id$

// Generated automatically by CxxMill on Mon Apr 11 17:40:33 2005

// End of file 
