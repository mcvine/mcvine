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


class Binding:
    
    def neutron_buffer( self, n ):
        return b.NeutronEventBuffer( n )
    
    
    def position( self, x,y,z ):
        return b.Position_double( x,y,z )
    
    
    def velocity( self, x,y,z ):
        return b.Velocity_double( x,y,z )
    
    
    def spin( self, s1, s2):
        return b.NeutronSpin( s1, s2 )
    
    
    def state(self, r = (0,0,0), v = (0,0,3000), s = (0,1)):
        return b.NeutronState( self.position( *r ), self.velocity( *v ), self.spin( *s ) )
    

    def neutron(self, r = (0,0,0), v = (0,0,3000), s = (0,1), time = 0, prob = 1.):
        return b.NeutronEvent(self.state(r,v,s), time, prob)


    def applyOffsetRotation(self, offset, rotation, neutrons):
        'apply offset vector (3-tuple) and rotation matrix (3X3 npy array) to neutrons'
        r = b.Position_double(*offset)
        rotmat = rotation.copy()
        rotmat.shape = -1,
        m = b.RotationMatrix_double( *rotmat )
        b.abs2rel_batch( neutrons, r, m )
        return
    

    def cevents_from_npyarr( self, npyarr ):
        '''convert a numpy array to a boost-python instance of Neutron::cEvent pointer'''
        from numpyext import getdataptr
        ptr = getdataptr( npyarr )
        from bpext import wrap_ptr
        import mcni.mcni
        cevents = wrap_ptr( ptr, 'cNeutronEvent' )
        cevents.origin = npyarr
        return cevents


    pass # end of Binding
    

def _import():
    import mcni.mcnibp
    import _patch_neutronevents_bp_interface
    import bpext, mcni.mcni
    return

_import()



# version
__id__ = "$Id$"

# End of file 
