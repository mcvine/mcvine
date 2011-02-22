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
#include "vitess/neutronbuffer2stream.h"


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

  void wrap_converters() 
  {
    using namespace boost::python;

    def( "neutronbuffer2vitess", neutronbuffer2vitess);
    class_<VitessNeutronBuffer>
      ("VitessNeutronBuffer")
      .def("getCharPtr", &VitessNeutronBuffer::getCharPtr)
      ;				
  }

}

// version
// $Id$

// End of file 
