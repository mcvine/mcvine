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


from mcni.neutron_storage.idfneutron import ndblsperneutron, filesize

from mcni.AbstractComponent import AbstractComponent

class NeutronFromStorage( AbstractComponent ):


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
        if hasmpi:
            from mcni.utils import mpiutil
            mpisize = mpiutil.world.size
            # each node reads a chunk of neutrons of size n
            # increment cursor at the master node and send
            # cursors to each node.
            channel = 100
            if mpiutil.rank == 0:
                cursor = self._cursor
                for i in range(1, mpisize):
                    mpiutil.send(self._cursor+i*n, i, channel)
                    continue
            else:
                cursor = mpiutil.receive(0, channel)
            # increment my cursor to jump over all neutrons
            # read by all nodes
            if mpiutil.rank == 0:
                self._cursor += mpisize*n
            # at each node, jump to the position specified by cursor
            self._storage.seek(cursor, 'start')

        # read as numpy array
        npyarr = self._storage.read(n, asnpyarr=True)
        
        # convert to neutron buffer 
        from mcni.neutron_storage import neutrons_from_npyarr
        neutrons = neutrons_from_npyarr( npyarr, neutrons )
        
        return neutrons


    def __init__(self, name, path):
        AbstractComponent.__init__(self, name)
        
        path = self.path = os.path.abspath( path )
        
        if not os.path.exists( path ):
            raise IOError , "path %r does not exist" % path
        
        if os.path.isdir( path ):
            raise IOError , "path %r is a directory" % path

        from mcni.neutron_storage import storage
        self._storage = storage( path, 'r' )
        if hasmpi:
            # master node keeps the cursor
            from mcni.utils.mpiutil import rank as mpirank
            if mpirank == 0:
                self._cursor = 0
        return


    pass # end of Source


import os, math, numpy

try:
    import mpi
except ImportError:
    hasmpi = False
else:
    hasmpi = True


# version
__id__ = "$Id$"

# End of file 
