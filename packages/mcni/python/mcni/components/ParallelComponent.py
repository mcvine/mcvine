#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                      California Institute of Technology
#                       (C) 2007-2009 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## Supports for parallel computing


import journal
info = journal.info( 'mpi' )



class ParallelComponent(object):

    '''Base class for components that can be parallelized.
    '''

    @property
    def mpi(self):
        mpi = getattr(self, '_mpi', None)
        if not mpi:
            mpi = self._mpi = MPI()
        return mpi

    @property
    def parallel(self):
        return self.mpi.parallel


class UniqueChannelGenerator(object):

    def __init__(self, start=10000):
        self.number = start
        return


    def __call__(self):
        r = self.number
        self.number += 1
        return r
    

class MPI(object):

    """mpi wrapper class used by parallelcomponent"""


    def __init__(self):
        try:
            from mcni.utils import mpi
            rank = mpi.rank; size = mpi.size
            if size <= 1:
                size = 1
                parallel = False
            else:
                parallel = True
        except:
            rank = 0
            size = 1
            parallel = False
            pass

        info.log( "rank %d of %d" % (rank, size) )

        self.size = size
        self.rank = rank
        self.parallel = parallel
        self.engine = mpi
        return

    _unique_channel_generator = UniqueChannelGenerator()
    def getUniqueChannel(self):
        return self.__class__._unique_channel_generator()
    

    def send( self, obj, peer, tag):
        return self.engine.send(obj, peer, tag)


    def receive(self, peer, tag):
        return self.engine.receive(peer, tag)


    def sendStr( self, s, peer, tag):
        return self.engine.sendStr(s, peer, tag)
    

    def receiveStr(self, peer, tag):
        return self.engine.receiveStr(peer, tag)


    def barrier(self):
        "a naive implementation of barrier"
        if self.size < 2:
            return
        c = self.getUniqueChannel()
        if self.rank == 0:
            for i in range(1, self.size):
                self.sendStr('', i, c)
        else:
            self.receiveStr(0, c)
        return
    

    pass # end of MPI


# End of file 
