#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

name = 'pyre'

from . import info
import pickle, sys

def _mpi():
    global size, rank, world
    try:
        import mpi
        if not mpi.inParallel():
            sys.stderr.write( "** pyre mpi binding: failed to load\n" )
            rank = 0
            return
        sys.stderr.write( "* pyre mpi available\n" )
    except ImportError:
        sys.stderr.write( "** pyre mpi NOT available\n" )
        rank = 0
        return
    world = mpi.world()
    rank = world.rank
    size = world.size
    return
rank = None
world = None
_mpi()


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


# version
__id__ = "$Id$"

# End of file 
