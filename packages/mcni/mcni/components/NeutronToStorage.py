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


category = 'monitors'


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage import ndblsperneutron

from mcni.AbstractComponent import AbstractComponent

class NeutronToStorage( AbstractComponent ):


    '''Save neutrons to data files.

    This component saves neutrons to data files in a directory
    of your choice. The data files are in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the directory where neutron files
    will be saved.
    '''


    def __init__(self, name, path, append = False, packetsize = None):
        AbstractComponent.__init__(self, name)

        path = self.path = os.path.abspath( path )

        if os.path.exists( path ):
            msg = 'path %r already exists. if you want to append neutron event files to '\
                  'that directory, please set "append" to True' % path
            if not append: raise msg
            pass
        
        if not os.path.exists( path ): os.makedirs( path )
        
        if not os.path.isdir( path ):
            raise IOError , "path %r is not a directory" % path

        import mcni
        self._buffer = mcni.neutron_buffer(0)

        from _neutron_storage_impl import packetsize_store
        self._packetsize_store = packetsize_store( os.path.join( self.path, packetsizefile ) )

        if packetsize:
            # if user supplied a packet size
            
            size = self._packetsize_store.getsize()

            if size:
                #if there is also a predefined packet size, we should
                #compare this predefined size to the user defined size
                if  size != packetsize:
                    # if they don't match, we cannot continue
                    msg = "This neutron storage has a predefined size of %s, "\
                          "and you cannot change its size to %s." % (
                        size, packetsize )
            else:
                #if there is no predefined packet size, this store
                #is fresh. we need to set its packet size.
                self._packetsize_store.setsize( packetsize )
                
        return


    def process(self, neutrons):
        path = self.path
        
        n = len(neutrons)

        # check packet size. if packet size has not been
        # set, use n as packet size
        packetsize = self._getpacketsize()
        if packetsize is None :
            # packet size is not set.
            msg = 'packet size is not set for this storage. '\
                  'will use the size of the input neutron buffer '\
                  'as the packet size.'
            import warnings
            warnings.warn( msg )
            self._setpacketsize( n )
            pass

        # now write the neutrons
        self._dump( neutrons )
        return neutrons


    def _dump(self, neutrons):
        buffer = self._buffer

        packetsize = self._getpacketsize()

        # total number of neutrons
        N = len(buffer) + len(neutrons)
        
        # if not overflow, just add neutron to buffer
        if N < packetsize:
            buffer.append( neutrons, 0, len(neutrons) )
        else:
            #overflow
            npackets = N/packetsize
            # write the first packet by
            #  1. fill the buffer
            npatch = packetsize - len(buffer)
            buffer.append( neutrons, 0,  npatch)
            #  2. write the buffer
            self._write_packet( buffer )

            # now write (npackets-1) packets
            start = npatch
            for i in range( npackets - 1 ):
                buffer.clear()
                buffer.append( neutrons, start, start + packetsize )
                self._write_packet( buffer )
                start += packetsize
                continue

            # move the remained neutrons to buffer
            buffer.clear()
            buffer.append( neutrons, start, len(neutrons) )

        return


    def _write_packet(self, packet):
        n = len(packet)
        packetsize = self._getpacketsize()
        
        if n != packetsize:
            raise RuntimeError , "packet size for neutron store %r is %d, "\
                  "but input neutron packet has size %d" % (
                self.path, packetsize, n )

        filename = self._uniquefilename()

        from mcni.neutron_storage import dump
        dump( packet, os.path.join( self.path, filename ) )

        return 
    
    
    def _getpacketsize(self):
        return self._packetsize_store.getsize()


    def _setpacketsize(self, n):
        return self._packetsize_store.setsize( n )


    def _uniquefilename(self):
        entries = os.listdir( self.path )
        numbers = []
        for entry in entries:
            try: n = int( entry )
            except: continue
            numbers.append( n )
            continue
        if len(numbers) == 0: return '0'
        return str( max(numbers) + 1 )
    

    pass # end of Source


def filesize( n ):
    '''calculate neutron file size given number of neutrons
    '''
    return titlesize + versionsize + commentsize + nsize + n * neutronsize


import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
