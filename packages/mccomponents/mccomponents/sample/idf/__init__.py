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
    
    qpath = os.path.join( datapath, Q )
    import Q
    q = Q.read( qpath)[1]

    epath = os.path.join( datapath, E )
    import E
    e = E.read( epath)[1]

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




# version
__id__ = "$Id$"

# End of file 
