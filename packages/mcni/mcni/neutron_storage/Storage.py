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


import journal
debug = journal.debug('NeutronStorage')


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage import ndblsperneutron



class Storage:


    '''storage of neutrons

    Implementation:
    Saves neutrons to a data file.
    The data file is in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1).
    '''

    
    def __init__(self, path, mode = 'r', 
                 packetsize = None, buffersize=10000):
        """
        path: path of the storage
        mode: mode of operation
          r: read
          w: write
          a: append
        packetsize: used in "r" mode. The size of the neutron packet being read
        buffersize: used in "w"/"a" mode. The size of writing buffer (unit: neutron)
        """

        path = self.path = os.path.abspath( path )
        debug.log('storage path: %s' % path)

        # checking inputs
        if mode in ['w'] and os.path.exists( path ):
            msg = 'path %r already exists. if you want to append neutron event files to '\
                  'that directory, please use mode "a" to append' % path
            raise RuntimeError, msg
        
        #if not os.path.exists( path ) and mode in ['w']: os.makedirs( path )

        if not os.path.exists( path ) and mode in ['r', 'a']:
            raise RuntimeError, "Neutron storage at %r has not been established" % path

        if os.path.isdir( path ):
            raise IOError , "path %r is a directory" % path

        
        # init
        self.mode = mode
        self._readonly = mode in ['r']

        # file stream
        self.stream = open(path, mode)
        self._closed = False

        #
        self._buffersize = buffersize
        debug.log("buffer size: %s" % buffersize)
        
        import mcni
        self._buffer = mcni.neutron_buffer(0)

        # in write mode, let us initialize the file by writing 
        # an empty neutron buffer
        if self.mode == 'w':
            self._write_header(self.stream)

        # read mode:
        if self._readonly:
            self._packetsize = packetsize
            self._position = 0 # initial position to start reading
            self._ntotal = idfio.count(stream=self.stream)
            debug.log('packet size: %s' % packetsize)
            debug.log('total size: %s' % self._ntotal)
        return


    def write(self, neutrons):
        'write neutrons'
        path = self.path
        
        if self._readonly:
            raise RuntimeError, "Neutron storage at %r was opened read" % path
        
        # now write the neutrons
        self._dump( neutrons )
        return neutrons


    def seek(self, offset, whence, wrap=True):
        if not self._readonly:
            raise RuntimeError, "seek only works for read operation"

        ntotal = self._ntotal
        
        if whence in ['start', 0]:
            self._position = offset
            debug.log('seek from start: position is now %s' % self._position)
        elif whence in ['current', 1]:
            self._position += offset
            debug.log('seek from current position: position is now %s' % self._position)
        elif whence in ['end', 2]:
            self._position = self._ntotal + offset
            debug.log('seek from end: position is now %s' % self._position)
        else:
            raise ValueError, "whence=%s: not supported" % whence

        if wrap:
            self._position %= ntotal
            debug.log('wrap position: position is now %s' % self._position)
        else:
            if self._position >= ntotal or self._position < 0:
                raise RuntimeError, "new position %s out of bound" % self._position
        return


    def tell(self):
        return self._position


    def read(self, n=None, asnpyarr = False, wrap=True):
        """read (n) neutrons from the current position.

        n: optional. number of neutrons. if None, read all neutrons
        wrap: if true, will wrap around to the start when reach the end of file. so you can read forever
        asnpyarr: if true, returns numpy array instead of neutron array
        """
        path = self.path
        if not self._readonly:
            raise RuntimeError, "Neutron storage %r was opened for write" % path

        position = self._position
        debug.log('my current position: %s' % position)
        
        # n defaults to packetsize
        n = n or self._packetsize
        debug.log('number of neutrons to read: %s' % n)

        # total number of neutrons in the file
        ntotal = self._ntotal
        debug.log('total number of neutrons in the storage: %s' % ntotal)

        # no default, read all is left
        if n is None:
            n = ntotal - position
            debug.log('n was given as None, now set to %s' % n)
            
        # next position of cursor
        nextpostion = position + n
        debug.log('next cursor position: %s' % nextpostion)
        
        if nextpostion < ntotal:
            # if it is not beyond the end of file, just read
            debug.log('no wrapping needed because next-cursor-position<ntotal')
            npyarr = idfio.read(stream=self.stream, start=position, n=n)
            debug.log('read %s neutrons start from %s' % (n, position))
            self._position = nextpostion
            debug.log('set my position to %s' % self._position)

        else:
            # if out of bound, read to the end of file
            n1 = ntotal-position
            npyarr = idfio.read(
                stream=self.stream, start=position, n=n1)
            
            # if wrap, restart from the beginning
            if wrap:
                n2 = n-n1
                # n2 may be still larger than ntotal 
                # we may need to read the whole file several times
                if n2 >= ntotal:
                    ntimes = n2/ntotal
                    allneutrons = idfio.read(stream=self.stream)
                    for i in range(ntimes):
                        npyarr = numpy.concatenate((npyarr, allneutrons))
                        continue
                    # now n2 is maller than ntotal
                    n2 = n2 - ntimes * ntotal
                    assert n2 < ntotal
                    
                if n2>0:
                    npyarr2 = idfio.read(
                        stream=self.stream, start=0, n=n2)
                    npyarr = numpy.concatenate((npyarr, npyarr2))
                self._position = n2
            else:
                self._position = ntotal

        # npy array?
        if asnpyarr: return npyarr
        
        from mcni.neutron_storage import neutrons_from_npyarr
        neutrons = neutrons_from_npyarr( npyarr )
        
        return neutrons


    def packetsize(self):
        return self._packetsize


    def flush(self):
        buffer = self._buffer
        self._write_neutrons(self._buffer)
        buffer.clear()
        return


    def close(self):
        if not self._closed:
            if not self._readonly:
                self.flush()
            self.stream.close()
            self._closed = True
        return


    def __del__(self): self.close()


    def _dump(self, neutrons):
        buffer = self._buffer
        # current size of buffer
        currentbuffersize = len(buffer)
        
        # number of new neutrons 
        nnew = len(neutrons)
        
        # total number of neutrons
        N = currentbuffersize + nnew

        if N >= self._buffersize:
            # if the total number of neutrons is larger than the
            # buffer size, just dump all into the file
            self._write_neutrons(self._buffer)
            self._write_neutrons(neutrons)
            # and clear the buffer
            buffer.clear()
        else:
            # otherwise, add the neutrons to the buffer
            buffer.append(neutrons, 0, nnew)

        return


    def _write_neutrons(self, neutrons):
        # from mcni.neutron_storage import dump
        # dump( packet, os.path.join( self.path, filename ) )

        stream = self.stream
        arr = neutrons_as_npyarr(neutrons)
        idfio.append(arr, stream=stream)
        return 


    def _write_header(self, stream):
        # create header by writing empty neutron buffer
        buffer = mcni.neutron_buffer(0)
        arr = neutrons_as_npyarr( buffer )
        idfio.write(arr, stream=stream)
        return
    
    
    pass # end of Source


from idfneutron import filesize
import idf_usenumpy as idfio
from mcni.neutron_storage import neutrons_as_npyarr
import mcni

import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
