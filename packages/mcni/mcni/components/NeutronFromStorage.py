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


category = 'sources'

import journal
debug = journal.debug('NeutronStorage')


from mcni.neutron_storage.idfneutron import ndblsperneutron, filesize

from ParallelComponent import ParallelComponent
from mcni.AbstractComponent import AbstractComponent

class NeutronFromStorage( ParallelComponent, AbstractComponent ):


    '''Load neutrons from a neutron data file.

    This component loads neutrons from a data file 
    of your choice. The data file should be in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the file.
    '''

    def process(self, neutrons):
        # number of neutrons
        n = len(neutrons)
        
        # mpi
        if self.parallel:
            self._setCursor(self.mpiSize, n)

        # read as numpy array
        npyarr = self._storage.read(n, asnpyarr=True)
        if len(npyarr):
            debug.log(npyarr[0])
        else:
            debug.log("no neutrons")
        
        # convert to neutron buffer 
        from mcni.neutron_storage import neutrons_from_npyarr
        neutrons = neutrons_from_npyarr( npyarr, neutrons )

        if len(neutrons):
            debug.log(neutrons[0])
        
        return neutrons


    def _setCursor(self, mpisize, n):
        # each node reads a chunk of neutrons of size n
        # increment cursor at the master node and send
        # cursors to each node.
        channel = self.getUniqueChannel()
        if self.mpiRank == 0:
            cursor = self._cursor
            for i in range(1, mpisize):
                self.mpiSend(self._cursor+i*n, i, channel)
                continue
        else:
            cursor = self.mpiReceive(0, channel)

        # at each node, seek to the position specified by cursor
        self._storage.seek(cursor, 'start')
        
        # increment my cursor to jump over all neutrons
        # read by all nodes
        if self.mpiRank == 0:
            self._cursor += mpisize*n
            
        return

    
    def __init__(self, name, path):
        AbstractComponent.__init__(self, name)
        
        path = self.path = os.path.abspath( path )
        
        if not os.path.exists( path ):
            raise IOError , "path %r does not exist" % path
        
        if os.path.isdir( path ):
            raise IOError , "path %r is a directory" % path

        from mcni.neutron_storage import storage
        self._storage = storage( path, 'r' )
        if self.parallel:
            # master node keeps the cursor
            if self.mpiRank == 0:
                self._cursor = 0
        return


    pass # end of Source


import os, math, numpy

# version
__id__ = "$Id$"

# End of file 
