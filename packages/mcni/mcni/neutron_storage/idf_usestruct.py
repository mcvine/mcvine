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
## this implementation use struct and is more compatible.

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
longlongsize = calcsize('<q')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def read( filename ):
    f=open(filename,'r').read()
    i = 0
    filetype,= unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
    version, = unpack('<i',f[i:i+intSize])               ; i += intSize
    comment, = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
    N,       = unpack('<q',f[i:i+longlongsize])          ; i += longlongsize
    neutrons = unpack('<%id' % (N*10,),f[i:])
    neutrons = numpy.array(neutrons)
    neutrons.shape = -1, 10
    return filetype.strip('\x00'),version,comment.strip('\x00'),neutrons


def write( neutrons, filename='neutrons', comment = '' ):
    assert neutrons.dtype == numpy.double
    f=open(filename,'w')
    f.write(pack('<64s','Neutron'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment))
    f.write(pack('<q',len(neutrons)))
    neutrons = tuple( neutrons.reshape(-1) )
    f.write(pack('<%id' % len(neutrons),*neutrons))
    return


def test():
    import numpy
    neutrons = numpy.arange( 10000000, dtype = numpy.double )
    neutrons.shape = -1, 10
    filename = 'neutrons.dat'
    write( neutrons, filename )
    neutrons = read( filename )
    return


if __name__ == '__main__': test()


# version
__id__ = "$Id$"

#  End of file 
