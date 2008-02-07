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


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage.idfneutron import ndblsperneutron, filesize

from mcni.pyre_support.AbstractComponent import AbstractComponent

class NeutronFromStorage( AbstractComponent ):


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = '' )
        pass
    

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


    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        return


    def _init(self):
        AbstractComponent._init(self)
        
        path = self.path = os.path.abspath( self.path )
        
        if not os.path.exists( path ):
            raise IOError , "path %r does not exist" % path
        
        if not os.path.isdir( path ):
            raise IOError , "path %r is not a directory" % path

        packetsize = long(
            open( os.path.join( path, packetsizefile ) ).read() )
        neutronfilesize = filesize( packetsize )
        
        entries = os.listdir( path )
        
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
        
        self.neutronfiles = neutronfiles
        self.packetsize = packetsize
        self.index = 0
        return

    pass # end of Source


import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
