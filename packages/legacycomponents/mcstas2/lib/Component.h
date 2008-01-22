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


#ifndef H_MCSTAS2_COMPONENT
#define H_MCSTAS2_COMPONENT

#include <string>

#include "Gravity.h"

namespace mcstas2{

  class Component{

  public:

    Component( const char * name ) : m_name(name), m_gravity_on(0)  {}
    Component( ) : m_name("no name"), m_gravity_on(0)  {}

    virtual ~Component() { save(); }

    // methods
    inline const char * name() const { return m_name.c_str(); }
    inline void subjectTo( const Gravity & g ) { m_g = g; m_gravity_on = 1; }
    inline bool gravityIsOn() const { return m_gravity_on; }
    inline const Gravity & gravity() const { return m_g; }
    inline void setName( const char * name ) { m_name = name; }

    /// finding trace of a neutron in myself
    virtual void trace(double & x,double & y,double & z,
		       double & vx,double & vy,double & vz,
		       double & t,
		       double & s1,double & s2,
		       double & p) = 0;
    
    /// save data. for monitors
    virtual void save( ) {} // default implementation does nothing

  protected:

    std::string m_name;
    bool m_gravity_on;
    Gravity m_g;

  }; // Component

} // namespace mcstas2


#endif //H_MCSTAS2_COMPONENT


// version
// $Id$

// Generated automatically by CxxMill on Tue Jun 27 12:57:31 2006

// End of file 
