#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(Omega2,filename='Omega2',comment='',D=3):
    """Takes numpy Omega2 in with shape (N_q,N_b*D) and writes to binary file."""
    f=open(filename,'wb')
    f.write(pack('<64s',b'Omega2'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment.encode('ascii')))
    #f.write(pack('<i',Omega2.shape[2]))
    f.write(pack('<i',D))
    # maybe there should be some further checking on integer division below:
    f.write(pack('<i',Omega2.shape[1] / D))
    f.write(pack('<i',Omega2.shape[0]))
    Omega2 = tuple( Omega2.reshape(-1) )
    f.write(pack('<%id' % len(Omega2),*Omega2))
    return

def read(filename='Omega2'):
    """Takes filename, returns a tuple with information and Omega2 as a numpy."""
    f=open(filename,'rb').read()
    i = 0
    filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
    version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
    comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
    D,N_b,N_q = unpack('<3i',f[i:i+3*intSize])            ; i += 3*intSize
    Omega2    = unpack('<%id' % (N_q*N_b*D),f[i:])
    Omega2 = numpy.array(Omega2)
    Omega2.shape = (N_q,N_b*D)
    filetype = filetype.strip( b'\x00' ).decode()
    assert filetype == 'Omega2', "File %s is not in correct format" % filename
    return (filetype,version,comment.strip(b'\x00').decode()),Omega2

