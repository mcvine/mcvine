# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

#mpi
def _mpi():
    global rank, world
    try:
        import mpi
    except ImportError:
        rank = 0
        return
    world = mpi.world()
    rank = world.rank
    return
rank = None
world = None
_mpi()


import pickle

def send( obj, peer, tag):
    s = pickle.dumps( obj )
    return sendStr( s, peer, tag )


def receive(peer, tag):
    s = receiveStr( peer, tag )
    obj = pickle.loads( s )
    return obj


def sendStr( s, peer, tag):

    port = world.port(peer=peer, tag=tag)
    
    msg = "Machine %s: sending string of length %d to peer %s with tag %s" % (
        rank, len(s), peer, tag)
    info.log( msg )
    
    port.send(s)
    
    msg = "Machine %s: sent string of length %d to peer %s with tag %s" % (
        rank, len(s), peer, tag) 
    info.log( msg )
    return


def receiveStr(peer, tag):
    port = world.port(peer=peer, tag=tag)
    s = port.receive()
    msg = "Machine %s: received string of length %d from peer %s with tag %s" % (
        rank, len(s), peer, tag)
    info.log( msg )
    return s


import journal
info = journal.info( 'mcni.utils.mpiutil' )


# version
__id__ = "$Id$"

# End of file 
