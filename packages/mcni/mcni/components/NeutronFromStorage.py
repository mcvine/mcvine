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


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage.idfneutron import ndblsperneutron, filesize

from mcni.AbstractComponent import AbstractComponent

class NeutronFromStorage( AbstractComponent ):


    '''Load neutrons from data files.

    This component loads neutrons from data files in a directory
    of your choice. The data files should be in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the directory where neutron files
    were saved.
    '''

    def process(self, neutrons):
        n = len(neutrons)
        packetsize = self._storage.packetsize()
        
        if n%packetsize != 0:
            raise 'neutron buffer size = %d, packet size = %d, %d %s %d != 0' % (
                n, packetsize, n, '%', packetsize )
        
        index = self.index
        npacketstoread = n/packetsize
        npacketsinstorage = self._storage.npackets()

        # numpy array to store neutrons read from files
        npyarr = numpy.zeros( (n, ndblsperneutron), numpy.double )
        
        # read and insert
        for i in range(npacketstoread):
            npyarr[i*packetsize : (i+1)*packetsize] = self._storage.read( index, asnpyarr = 1 )
            index = (index+1) % npacketsinstorage
            continue
        
        self.index = index

        from mcni.neutron_storage import neutrons_from_npyarr
        neutrons = neutrons_from_npyarr( npyarr, neutrons )
        
        return neutrons


    def __init__(self, name, path):
        AbstractComponent.__init__(self, name)
        
        path = self.path = os.path.abspath( path )
        
        if not os.path.exists( path ):
            raise IOError , "path %r does not exist" % path
        
        if not os.path.isdir( path ):
            raise IOError , "path %r is not a directory" % path

        self.index = 0

        from mcni.neutron_storage import storage
        self._storage = storage( path, 'r' )
        return


    pass # end of Source


import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
