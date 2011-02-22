// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2008  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include "boost/python.hpp"
#include "vitess/mcvine2vitess.h"
#include "vitess/vitess2mcvine.h"


namespace wrap_vitess {

  struct VitessNeutronBuffer {
    typedef std::vector<vitess::Neutron> vNeutrons_t;
    vNeutrons_t neutrons;
    // const char * getCharPtr() const{
    //   return (char *)(&neutrons[0]);
    // }
    PyObject * getCharPtr() const {
      void *ptr = (void *)(&neutrons[0]);
      return PyBuffer_FromMemory(ptr, sizeof(vitess::Neutron)*neutrons.size());
    }
  };

  VitessNeutronBuffer neutronbuffer2vitess(const mcni::Neutron::Events &evts)
  {
    VitessNeutronBuffer vnb;
    vnb.neutrons.resize(evts.size());
    mcvineneutrons2vitessneutrons(evts, vnb.neutrons);
    return vnb;
  }

  void vitessbuffer2mcvinebuffer(const char *s, size_t n, mcni::Neutron::Events &evts)
  {
    typedef std::vector<vitess::Neutron> vNeutrons_t;
    const vitess::Neutron *p = (const vitess::Neutron *)s;
    vNeutrons_t neutrons(p, p+n);
    vitessneutrons2mcvineneutrons(neutrons, evts);
  }

  void wrap_converters() 
  {
    using namespace boost::python;

    def( "neutronbuffer2vitess", neutronbuffer2vitess);
    class_<VitessNeutronBuffer>
      ("VitessNeutronBuffer")
      .def("getCharPtr", &VitessNeutronBuffer::getCharPtr)
      ;

    def("vitessbuffer2mcvinebuffer", vitessbuffer2mcvinebuffer);
  }

}

// version
// $Id$

// End of file 
