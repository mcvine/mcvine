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


class Binding:
    
    def neutron_buffer( self, n ):
        return b.NeutronEventBuffer( n )
    
    
    def position( self, x,y,z ):
        return b.Position_double( float(x), float(y), float(z) )
    
    
    def velocity( self, x,y,z ):
        return b.Velocity_double( float(x), float(y), float(z) )
    
    
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
        from ._patch_neutronevents_bp_interface import cevents_from_npyarr
        return cevents_from_npyarr(npyarr)


    def vector3(self, *args):
        if len(args) == 1 and len(args[0]) == 3: v = args[0]
        elif len(args) == 3: v = args
        else: raise ValueError("Need 3 elements: %r" % (args, ))
        return b.Vector3_double( *v )


    def matrix3(self, *args):
        if len(args) == 1: m = args[0]
        elif len(args) == 3: m = args
        elif len(args) == 9: m = args
        import numpy
        m = numpy.array(m)
        try:
            m.shape = 3,3
        except:
            raise RuntimeError('Cannot convert input %s to a 3X3 matrix' % (args,))

        #m.shape = -1,
        m = tuple(m[0])+tuple(m[1])+tuple(m[2])
        return b.Matrix3_double( *m )


    pass # end of Binding



def _import():
    import mcni.mcnibp
    from . import _patch_neutronevents_bp_interface
    import mcni._mcni
    try:
        from danse.ins import bpext
    except ImportError:
        import bpext
        import warnings
        warnings.warn("Using old bpext. Should use danse.ins.bpext\n%s")
    return

try:
    _import()
except ImportError:
    import warnings, traceback as tb
    warnings.warn("Unable to load boost python binding of mcni\n%s" \
                  % tb.format_exc())
    binding_imported = False
else:
    import mcni.mcnibp as b


# version
__id__ = "$Id$"

# End of file 
