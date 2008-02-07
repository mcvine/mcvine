#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


## read write neutrons to files in idf/Neutron format
## this implementation use numpy's tostring and fromstring and only works on
## little-endian machines.

import numpy

version=1

from struct import calcsize, pack
intSize = calcsize('<i')
longlongsize = calcsize('<q')
dubSize = calcsize('<d')
strSize = calcsize('<s')


def read( filename ):
    s=open(filename,'r').read()
    pointer = 0
    size = 64
    filetype = s[pointer: pointer + size]
    pointer += size

    size = intSize
    version = numpy.fromstring( s[pointer: pointer+size], int )[0]
    pointer += size

    size = 1024
    comment = s[pointer: pointer + size]
    pointer += size
    
    size = longlongsize
    N = numpy.fromstring( s[pointer: pointer+size], numpy.int64 )[0]
    pointer += size

    neutrons = numpy.fromstring( s[pointer:], numpy.double )

    neutrons.shape = -1, 10
    return filetype.strip('\x00'),version,comment.strip('\x00'),neutrons


def write( neutrons, filename='neutrons', comment = '' ):
    assert neutrons.dtype == numpy.double
    f=open(filename,'w')
    f.write(pack('<64s','Neutron'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment))
    f.write(pack('<q',len(neutrons)))
    
    neutrons.shape = -1,
    f.write( neutrons.tostring() )
    return


def test():
    import numpy
    neutrons = numpy.arange( 10000000, dtype = numpy.double )
    neutrons.shape = -1, 10
    filename = 'neutrons.dat'
    write( neutrons, filename )
    filetype, version, comment, neutrons = read( filename )
    #print neutrons
    return


if __name__ == '__main__': test()


# version
__id__ = "$Id$"

#  End of file 
