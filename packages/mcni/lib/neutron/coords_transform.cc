// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#include <vector>
#include <algorithm>
#include "mcni/geometry.h"
#include "mcni/neutron/Event.h"
#include "mcni/neutron/EventBuffer.h"
#include "mcni/neutron/coords_transform.h"


// transform a bunch of neutrons
namespace mcni{
  namespace Neutron{
    namespace coords_transform_helper{
 
      typedef Position<double> r_t;
      typedef Velocity<double> v_t;
      typedef RotationMatrix<double> rotmat_t;

      struct uf_abs2rel: public std::unary_function<mcni::Neutron::Event &, void>
      {
	uf_abs2rel(const r_t &comp_pos, 
		    const rotmat_t &comp_rot) :
	  _comp_pos(comp_pos), _comp_rot(comp_rot) {}
	inline void operator() (mcni::Neutron::Event &ev) 
	{ abs2rel( ev, _comp_pos, _comp_rot); }
	const r_t &_comp_pos; 
	const rotmat_t &_comp_rot;
      };
      
      struct uf_rel2abs: public std::unary_function<mcni::Neutron::Event &, void>
      {
	uf_rel2abs(const r_t &comp_pos,
		    const rotmat_t &comp_rot) :
	  _comp_pos(comp_pos), _comp_rot(comp_rot) {}
	inline void operator() (mcni::Neutron::Event &ev) 
	{ rel2abs( ev, _comp_pos, _comp_rot); }
	const r_t &_comp_pos; 
	const rotmat_t &_comp_rot;
      };
      
      
      
      struct uf_abs2rel_fast: public \
      std::unary_function<mcni::Neutron::Event &, void>
      {
	uf_abs2rel_fast(const r_t &comp_pos )
	  : _comp_pos(comp_pos) {}
	inline void operator() (mcni::Neutron::Event &ev) 
	{ abs2rel( ev, _comp_pos); }
	const r_t &_comp_pos; 
      };
      
      struct uf_rel2abs_fast: public \
      std::unary_function<mcni::Neutron::Event &, void>
      {
	uf_rel2abs_fast(const r_t &comp_pos) 
	  : _comp_pos(comp_pos) {}
	inline void operator() (mcni::Neutron::Event &ev) 
	{ rel2abs( ev, _comp_pos); }
	const r_t &_comp_pos; 
      };
      
    }
  }
}

void mcni::abs2rel_batch
( Neutron::Events &buffer, 
  const Position<double> & comp_pos, const RotationMatrix<double> & comp_rot)
{
  using namespace mcni::Neutron::coords_transform_helper;

  if ( is_almost_0( comp_pos ) && is_almost_I( comp_rot ) )
    return;
  
  if ( is_almost_I( comp_rot ) ) 
    for_each( buffer.begin(), buffer.end(), uf_abs2rel_fast(comp_pos) );
  else
    for_each( buffer.begin(), buffer.end(), uf_abs2rel(comp_pos, comp_rot) );
  
}

void mcni::rel2abs_batch
( Neutron::Events &buffer,
  const Position<double> & comp_pos, const RotationMatrix<double> & comp_rot)
{
  using namespace mcni::Neutron::coords_transform_helper;

  if ( is_almost_0( comp_pos ) && is_almost_I( comp_rot ) )
    return;
  
  if ( is_almost_I( comp_rot ) ) 
    for_each( buffer.begin(), buffer.end(), uf_rel2abs_fast(comp_pos) );
  else
    for_each( buffer.begin(), buffer.end(), uf_rel2abs(comp_pos, comp_rot) );
}



// version
// $Id$

// End of file
