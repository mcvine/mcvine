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

name = 'mpi4py'

from . import logger


def _mpi():
    global size, rank, world
    try:
        from mpi4py import MPI
        logger.info( '* mpi4py available\n' )
    except ImportError:
        logger.warn( '** mpi4py NOT available\n' )
        rank = 0
        size = 0
        return
    world = MPI.COMM_WORLD
    rank = world.Get_rank()
    size = world.Get_size()
    return
rank = None
world = None
size = None
_mpi()


def send( obj, peer, tag):
    return world.send(obj, dest=peer, tag=tag)


def receive(peer, tag):
    return world.recv(source=peer, tag=tag)


sendStr = send
receiveStr = receive


# version
__id__ = "$Id$"

# End of file 
