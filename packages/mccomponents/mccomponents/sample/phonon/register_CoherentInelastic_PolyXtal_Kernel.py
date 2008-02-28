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

#factory method that wraps boost python binding
def linearlyinterpolateddos_bp(
    e0, de, n, Z):
    '''create boost python object of LinearlyInterpolatedDOS

    e0: minimum phonon energy. float
    de: phonon energy step. float
    n: number of points.
    Z: values of DOS at the energy points defined by (e0, de, n)
    '''
    import mccomponents.mccomponentsbp as b
    Z1 = b.vector_double( n )
    for i in range(n): Z1[i] = Z[i]
    
    return b.LinearlyInterpolatedDOS_dbl( e0, de, n, Z1 )



# version
__id__ = "$Id$"

# End of file 
