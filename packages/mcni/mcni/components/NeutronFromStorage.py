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
        packetsize = self.packetsize
        if n%packetsize != 0:
            raise 'neutron buffer size = %d, packet size = %d, %d \% %d != 0' % (
                n, packetsize, n, packetsize )
        index = self.index
        npackets = n/packetsize

        # numpy array to store neutrons read from files
        npyarr = numpy.zeros( (n, ndblsperneutron), numpy.double )
        
        from mcni.neutron_storage import readneutrons_asnpyarr

        # all neutron files in the directory
        neutronfiles = self.neutronfiles
        # number of neutron files
        nfiles = len(neutronfiles)
        # read and insert
        for i in range(npackets):
            npyarr[i*packetsize : (i+1)*packetsize] = readneutrons_asnpyarr(
                neutronfiles[ index ] )
            index = (index+1) % nfiles
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
        self.packetsize = self._packetsize()
        self.neutronfiles = self._neutronfiles()
        return


    def _packetsize(self):
        path = self.path
        packetsize = long(
            open( os.path.join( path, packetsizefile ) ).read() )
        return packetsize


    def _neutronfilesize(self):
        packetsize = self._packetsize()
        neutronfilesize = filesize( packetsize )
        return neutronfilesize


    def _neutronfiles(self):
        path = self.path
        entries = os.listdir( path )
        neutronfilesize = self._neutronfilesize()
        
        neutronfiles = []
        for entry in entries:
            file = os.path.join( path, entry )
            if not os.path.isfile( file ): continue
            if open(file).read(7) != 'Neutron': continue
            if os.path.getsize( file ) != neutronfilesize : continue
            neutronfiles.append( file )
            continue

        if len(neutronfiles) == 0:
            raise RuntimeError , "no neutron file in %r" % path

        return neutronfiles

    pass # end of Source


import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
