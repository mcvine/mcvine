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


from mcni.neutron_storage import ndblsperneutron



class Storage:


    '''storage of neutrons

    Implementation:
    Saves neutrons to data files in a directory.
    The data files are in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1).
    '''


    def __init__(self, path, mode = 'r', packetsize = None):

        self._readonly = self._writeonly = False
        
        path = self.path = os.path.abspath( path )

        if mode in ['w'] and os.path.exists( path ):
            msg = 'path %r already exists. if you want to append neutron event files to '\
                  'that directory, please use mode "a" to append' % path
            raise msg
        
        if not os.path.exists( path ) and mode in ['w']: os.makedirs( path )

        if not os.path.exists( path ) and mode in ['r']:
            raise "Neutron storage at %r has not been established" % path

        if mode in ['r']: self._readonly = True
        if mode in ['w']: self._writeonly = True
        
        if not os.path.isdir( path ):
            raise IOError , "path %r is not a directory" % path

        import mcni
        self._buffer = mcni.neutron_buffer(0)

        packetsize_path = os.path.join( self.path, packetsizefile ) 
        if self._readonly and not os.path.exists(packetsize_path):
            raise RuntimeError, "neutron store at %r is not valid. %r missing" % (self.path, packetsize_path )
        from _neutron_storage_impl import packetsize_store
        self._packetsize_store = packetsize_store( packetsize_path )

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
                    raise RuntimeError, msg
            else:
                #if there is no predefined packet size, this store
                #is fresh. we need to set its packet size.
                self._packetsize_store.setsize( packetsize )
                
        return


    def write(self, neutrons):
        'write a packet of neutrons'
        path = self.path
        
        if self._readonly:
            raise RuntimeError, "Neutron storage at %r was opened read-only" % path
        
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


    def npackets(self):
        "number of packets"
        files = self._neutronfiles()
        return len(files)


    def read(self, packetindex, asnpyarr = False):
        if self._writeonly:
            raise RuntimeError, "Neutron storage %r is opened for write only" % self.path
        
        from mcni.neutron_storage import readneutrons_asnpyarr

        if packetindex >= self.npackets():
            raise RuntimeError, "Invalid packet index: %s. Should be in the range [0, %d]" % (packetindex, self.npackets()-1 )
        
        neutronfiles = self._neutronfiles()
        npyarr = readneutrons_asnpyarr( neutronfiles[ packetindex ] )

        if asnpyarr: return npyarr
        
        from mcni.neutron_storage import neutrons_from_npyarr
        neutrons = neutrons_from_npyarr( npyarr )
        
        return neutrons


    def packetsize(self):
        return self._getpacketsize()


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
    

    def _neutronfilesize(self):
        packetsize = self._getpacketsize()
        if packetsize is None: raise RuntimeError, "neutron storage not established: %s"  % self.path
        neutronfilesize = filesize( packetsize )
        return neutronfilesize



    def _neutronfiles(self):
        if not self._readonly: return self._list_neutronfiles()
        key = '_neutronfiles_list'
        ret = self.__dict__.get( key )
        if ret is None:
            ret = self._list_neutronfiles()
            setattr( self, key, ret )
        return ret
            


    def _list_neutronfiles(self):
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


from idfneutron import filesize

import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
