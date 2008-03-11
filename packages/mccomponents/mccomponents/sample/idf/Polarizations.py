#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(Pols,filename='Polarizations',comment=''):
    """Takes numpy Polarizations with shape (N_q,N_b*D,N_b,D) and writes \n
    to binary file."""
    f=open(filename,'w')
    f.write(pack('<64s','Polarizations'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment))
    res = numpy.zeros( Pols.shape + (2,) )
    res[:,:,:,:,0] = numpy.real(Pols)
    res[:,:,:,:,1] = numpy.imag(Pols)
    f.write(pack('<i',res.shape[3]))
    f.write(pack('<i',res.shape[2]))
    f.write(pack('<i',res.shape[0]))
    #  print res.shape
    res = tuple( res.reshape( (-1) ) )
    f.write( pack('<%id' % len(res),*res) )
    #  print 'len',len(res)
    return

def read(filename='Polarizations'):
    """Takes filename, returns a tuple with information and Polarizations \n
    as a numpy."""
    f=open(filename,'r').read()
    i = 0
    filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
    version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
    comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
    D,N_b,N_q = unpack('<3i',f[i:i+3*intSize])            ; i += 3*intSize
    #  print D, N_b, N_q, N_q*N_b*D*N_b*D*2
    res       = unpack('<%id' % (N_q*N_b*D*N_b*D*2),f[i:])
    res = numpy.array(res)
    res.shape = (N_q,N_b*D,N_b,D,2)
    return (filetype.strip('\x00'),version,comment.strip('\x00')),res

