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



class UniqueChannelGenerator(object):

    def __init__(self, start=10000):
        self.number = start
        return


    def __call__(self):
        r = self.number
        self.number += 1
        return r
    


class ParallelComponent(object):

    '''Base class for components that can be parallelized.
    '''

    try:
        from mcni.utils import mpi
        mpiRank = mpi.rank; mpiSize = mpi.size
        if mpiSize <= 1:
            mpiSize = 1
            parallel = False
        else:
            parallel = True
    except:
        mpiRank = 0
        mpiSize = 1
        parallel = False
        pass

    info.log( "rank %d of %d" % (mpiRank, mpiSize ) )


    _unique_channel_generator = UniqueChannelGenerator()
    def getUniqueChannel(self):
        return self.__class__._unique_channel_generator()
    

    def mpiSend( self, obj, peer, tag):
        return self.mpi.send(obj, peer, tag)


    def mpiReceive(self, peer, tag):
        return self.mpi.receive(peer, tag)


    def mpiSendStr( self, s, peer, tag):
        return self.mpi.sendStr(s, peer, tag)
    

    def mpiReceiveStr(self, peer, tag):
        return self.mpi.receiveStr(peer, tag)


    def mpiBarrier(self):
        "a naive implementation of barrier"
        if self.mpiSize < 2:
            return
        c = self.getUniqueChannel()
        if self.mpiRank == 0:
            for i in range(1, self.mpiSize):
                self.mpiSendStr('', i, c)
        else:
            self.mpiReceiveStr(0, c)
        return
    

    pass # end of ParallelComponent


# version
__id__ = "$Id$"

# End of file 
