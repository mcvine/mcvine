// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                 Jiao Lin
//                      California Institute of Technology
//                      (C) 2004-2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#ifndef MCNI_NEUTRON_NEUTRON_H
#define MCNI_NEUTRON_NEUTRON_H

#include "common.h"
#include <iostream>
#include <vector>


// forward declaration for operator << s
namespace DANSE { namespace Simulation {

  class Spin;
  class NeutronState;
  class NeutronEvent;

}} // DANSE::Simulation

// declare them outside any namespace to avoid a gcc bug that will prevent
// journal codes from compiling
std::ostream & operator <<
  ( std::ostream &os, const DANSE::Simulation::Spin & s ) ;
std::ostream & operator <<
  ( std::ostream &os, const DANSE::Simulation::NeutronState & s ) ;
std::ostream & operator <<
  ( std::ostream &os, const DANSE::Simulation::NeutronEvent & s ) ;


namespace DANSE { namespace Simulation {

  /// neutron spin
  class Spin{
    
  public:
    
    // might want to change to use three numbers, sx,sy,sz (normalized to one)
    /// ctor
    Spin(double s1, double s2): _s1(s1),_s2(s2) { }
    Spin(): _s1(0), _s2(0) {}
    
    // might want to change this interface to return sx, sy, and sz
    const double &s1() const { return _s1; }
    const double &s2() const { return _s2; }
    
    void print( std::ostream &os ) const {
      os << "(" <<_s1 << "," << _s2 <<")" ;
    }

  private:
    
    double _s1,_s2;
  };
  

  /// neutron state
  /*! This class holds information about the state of a neutron. Currently
    it knows about:
    - position
    - velocity
    - spin
   */
  class NeutronState{
    
  public:
    
    ///ctor
    NeutronState(const Vector3<double> &position, 
		 const Vector3<double> &velocity,
		 const Spin & s) :
      _pos(position), _vel(velocity), _s(s) { }
    
    ///default ctor
    NeutronState(): _pos(Vector3<double>(0,0,0)),
		    _vel(Vector3<double>(0,0,0)), _s(Spin()) {}
    
    const Vector3<double> &position() const { return _pos; }
    Vector3<double> &position() { return _pos; }
    const Vector3<double> &velocity() const { return _vel; }
    Vector3<double> &velocity() { return _vel; }
    const Spin &spin() const { return _s; }
    Spin &spin() { return _s; }
    
    void print( std::ostream &os ) const {
      os << "position=" << _pos <<","
	 << "velocity=" << _vel <<","
	 << "spin=" << _s;
    }  

  private:
    
    Vector3<double> _pos, _vel;
    Spin _s;
  };

  
  /// Neutron event
  /*! This class is supposed to have all the information of a neutron.
    Objects of NeutronEvent will be passed to any neutron component that
    will do scatterings. Neutron component will update the event after a
    scattering process is done.

    Currently a neutron event has following information:
    - neutron state: velocity, position, spin
    - time: how long has it been away from moderator?
    - probability: this is for the ease of doing Monte-Carlo simulation.
         We follow the practice taken in the McStas package; we update 
	 the probability of an event anytime it is scattered, by
	 multiplying the original probability
	 by the probability of the current scattering process.
   */
  class NeutronEvent{

  public:

    /// ctor
    NeutronEvent( const NeutronState &ns,
		  double time, double probability ) 
      : _ns(ns), _time(time), _prob(probability) {
    }
    
    /// default ctor
    NeutronEvent() : _ns(NeutronState()), _time(0), _prob(0) {}

    NeutronState &state() { return _ns; }
    const NeutronState &state() const { return _ns; }
    
    double &time() { return _time; }
    const double &time() const { return _time; }
    
    double &prob() { return _prob; }
    const double &prob() const { return _prob; }
    
    void print( std::ostream &os) const {
      os << "Neutron state=" <<_ns << ",time=" << _time 
	 << "probability="<<_prob;
    }

  private:
    
    NeutronState _ns;
    double _time; 
    double _prob;
  };
  

  typedef std::vector<NeutronEvent> Evts;

  /// array of neutron event
  /*! to reduce the function calls to each neutron component, we pass a bunch
    of neutrons to a neutron component, instead of passing one neutron a time.
    This class represents a bucket of neutrons.
   */
  class NtrnEvtBuffer : public std::vector<NeutronEvent>{
    
  public:

    typedef std::vector<NeutronEvent> base;

    /// ctor
    NtrnEvtBuffer( size_t n ): base(n) {}
    /// default ctor
    NtrnEvtBuffer(): base() {}
    
    /// snapshot of first n valid neutron events 
    /*! valid means the probability of the neutron event is positive.
      In simulation we use negative possibility to tag absorbed neutrons.
      ??? should not it return NtrnEvtBuffer???
     */
    base snapshot( size_t n );
  };
  
}} //DANSE::Simulation



#endif // MCNI_NEUTRON_NEUTRON_H

// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
