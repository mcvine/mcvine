#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import mcni.mcnibp as b

def neutron_buffer( n ):
    return b.NeutronEventBuffer( n )


def position( x,y,z ):
    return b.Position_double( x,y,z )


def velocity( x,y,z ):
    return b.Velocity_double( x,y,z )


def spin(s1, s2):
    return b.NeutronSpin( s1, s2 )


def state(r = (0,0,0), v = (0,0,3000), s = (0,1)):
    return b.NeutronState( position( *r ), velocity( *v ), spin( *s ) )


def neutron(r = (0,0,0), v = (0,0,3000), s = (0,1), time = 0, prob = 1.):
    return b.NeutronEvent(state(r,v,s), time, prob)


def applyOffsetRotation(offset, rotation, neutrons):
    'apply offset vector (3-tuple) and rotation matrix (3X3 npy array) to neutrons'
    r = b.Position_double(*offset)
    rotmat = rotation.copy()
    rotmat.shape = -1,
    m = b.RotationMatrix_double( *rotmat )
    b.abs2rel_batch( neutrons, r, m )
    return


def cevents_from_npyarr( npyarr ):
    '''convert a numpy array to a boost-python instance of Neutron::cEvent pointer'''
    from numpyext import getdataptr
    ptr = getdataptr( npyarr )
    from bpext import wrap_ptr
    import mcni.mcni
    cevents = wrap_ptr( ptr, 'cNeutronEvent' )
    cevents.origin = npyarr
    return cevents


def _import_bindings():
    import mcni.mcnibp
    import _patch_neutronevents_bp_interface
    import bpext, mcni
    return

_import_bindings()



# version
__id__ = "$Id$"

# End of file 
