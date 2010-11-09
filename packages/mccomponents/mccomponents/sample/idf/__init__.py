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

import os

def readSQE( datapath, Q = 'Q', E = 'E', Sqe = 'Sqe' ):
    'read idf Q,E,Sqe and construct a S(Q,E) histogram'
    qpath = os.path.join( datapath, Q )
    import Q
    q = Q.read( qpath)[1]
    q.shape = q.size,

    epath = os.path.join( datapath, E )
    import E
    e = E.read( epath)[1]
    e.shape = e.size,

    sqepath = os.path.join( datapath, Sqe )
    import Sqe
    s = Sqe.read( sqepath)[1]

    import histogram as H
    qaxis = H.axis( 'Q', boundaries = q )
    eaxis = H.axis( 'energy', boundaries = e )
    return H.histogram(
        'S(Q,E)',
        [qaxis, eaxis],
        data = s )



def writeSQE( sqehist, datapath = '.', Q='Q', E = 'E', Sqe = 'Sqe' ):
    'write a S(Q,E) histogram to the given directory in idf format'
    qaxis = sqehist.axisFromName('Q')
    eaxis = sqehist.axisFromName('energy')

    q = qaxis.binBoundaries().asNumarray()
    e = eaxis.binBoundaries().asNumarray()

    q.shape = len(q), 1
    from Q import write as writeQ
    writeQ(q, os.path.join( datapath, Q) )

    from E import write as writeE
    writeE(e, os.path.join( datapath, E) )

    data = sqehist.data().storage().asNumarray()
    from Sqe import write as writeSqe
    writeSqe(data, os.path.join( datapath, Sqe) )
    return



def readDispersion(
    datapath, Omega2 = 'Omega2', Polarizations = 'Polarizations',
    Qgridinfo = 'Qgridinfo', DOS = 'DOS'):
    "read dispersion in idf format"

    Qgridinfo = os.path.join( datapath, Qgridinfo )
    Omega2 = os.path.join( datapath, Omega2 )
    Polarizations = os.path.join( datapath, Polarizations )
    DOS = os.path.join( datapath, DOS )

    from DOS import read
    dummy, v, Z = read( DOS )
    # v is in terahertz, and it is not angular frequency
    from math import pi
    E = v * 2*pi * 1e12 * hertz2mev
    dos = E,Z

    from Qgridinfo import read
    reciprocalcell, ngridpnts = read( Qgridinfo )

    from Omega2 import read as readOmega2
    omega2 = readOmega2( Omega2 )[1]
    #!!!
    # sometime omega2 has negative values. have to make sure all values are
    # positive
    omega2[ omega2<0 ] = 0
    
    import numpy as N
    energies = N.sqrt(omega2) * hertz2mev

    from Polarizations import read as readP
    polarizations = readP( Polarizations )[1]
    
    N_q, N_b_times_D, N_b, D, temp = polarizations.shape
    assert temp == 2
    
    assert N_b_times_D == N_b*D
    assert D == len( ngridpnts )
    assert D == len( reciprocalcell )
    import operator
    assert N_q == reduce( operator.mul, ngridpnts )

    polarizations.shape = ngridpnts + (N_b_times_D, N_b, D, 2)
    
    energies.shape = ngridpnts + (N_b_times_D, )

    nAtoms = N_b
    dimension = D
    #Qaxes = [
    #    (0, length(reciprocalcell[i]) / (ngridpnts[i] - 1), ngridpnts[i])
    #    for i in range( D )
    #    ]
    Qaxes = zip(reciprocalcell, ngridpnts)
    return nAtoms, dimension, Qaxes, polarizations, energies, dos


def length( vector ):
    import numpy.linalg as nl
    return nl.norm( vector )


def _hertz2meV():
    import units
    SI = units.SI
    m = SI.meter; kg = SI.kilogram; s = SI.second
    hbar = 1.05457148e-34 * m**2 * kg /s
    hertz = 1 / s
    meV = units.energy.meV
    return hbar * hertz / meV

hertz2mev = _hertz2meV()
    


# version
__id__ = "$Id$"

# End of file 
