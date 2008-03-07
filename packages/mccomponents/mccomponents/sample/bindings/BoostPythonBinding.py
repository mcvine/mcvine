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



from mccomponents.homogeneous_scatterer.bindings.BoostPythonBinding \
     import BoostPythonBinding, extend

import mccomponents.mccomponentsbp as b
import mccomposite.mccompositebp as b1


class New:

    def gridsqe(self, qbegin, qend, qstep,
                ebegin, eend, estep,
                s ):
        '''gridsqe: S(Q,E) on grid

        qbegin, qend, qstep: Q axis
        ebegin, eend, estep: E axis
        s: numpy array of S
        '''
        shape = s.shape
        assert len(shape) == 2
        assert shape[0] == int( (qend-qbegin)/qstep )
        assert shape[1] == int( (eend-ebegin)/estep )
        size = shape[0] * shape[1]
        
        svector = b.vector_double( size )
        s.shape = -1,
        svector[:] = s
        
        fxy = b.new_fxy(
            qbegin, qend, qstep,
            ebegin, eend, estep,
            svector)
        
        return b.GridSQE( fxy )

    
    def sqekernel(self, absorption_cross_section, scattering_cross_section,
                  sqe, Qrange, Erange):
        '''sqekernel: a kernel takes S(Q,E) a functor

        absorption_cross_section: absorption cross section
        scattering_cross_section: scattering cross section
        sqe: S(Q,E) functor
        Qrange, Erange: range of Q and E
        '''
        Emin, Emax = Erange
        Qmin, Qmax = Qrange
        return b.SQEkernel(
            absorption_cross_section, scattering_cross_section,
            sqe, Qmin, Qmax, Emin, Emax )
    

    def linearlyinterpolateddos_bp(
        e0, de, n, Z):
        '''create boost python object of LinearlyInterpolatedDOS
        
        e0: minimum phonon energy. float
        de: phonon energy step. float
        n: number of points.
        Z: values of DOS at the energy points defined by (e0, de, n)
        '''
        Z1 = b.vector_double( n )
        for i in range(n): Z1[i] = Z[i]
        
        return b.LinearlyInterpolatedDOS_dbl( e0, de, n, Z1 )
    

    def ndarray( npyarr ):
        '''create boost python instance of NdArray object
    arguments:
        npyarr: numpy array. it must be a contiguous array.
        '''
        import numpy
        assert npyarr.dtype == numpy.double, "only work for double array for this time"
        
        import numpyext
        ptr = numpyext.getdataptr( npyarr )
        
        import bpext
        wp = bpext.wrap_native_ptr( ptr )
        
        shape = b.vector_uint( 0 )
        for i in npyarr.shape: shape.append( i )

        factory = 'new_NdArray_dblarr_%d' % len(shape)
        a1 = getattr(binding,factory)( wp, shape )
        a1.origin = npyarr # keep a reference to avoid seg fault
        return a1

    pass # end of BoostPythonBinding


extend( New )



# method __getitem__ to replace the boost python generated __getitem__
def bp_ndarray_getitem(self, indexes):
    cindexes = b.vector_uint( 0 )
    for ind in indexes: cindexes.append( ind )
    return self._getitem_bp( cindexes )


# go thru ndarray bp types and change interfaces
def _fix_bp_ndarray_interface( ):
    for i in range( 1,7 ):
        clsname = 'NdArray_dblarr_%d' % i
        cls = getattr( b, clsname )
        cls._getitem_bp = cls.__getitem__
        cls.__getitem__ = bp_ndarray_getitem
        continue
    return


_fix_bp_ndarray_interface()
        

# version
__id__ = "$Id$"

# End of file 
