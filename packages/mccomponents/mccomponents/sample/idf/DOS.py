#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(E,DOS,filename='DOS',comment=''):
    """Takes numpy DOS in with shape (N_e) and writes to binary file."""
    f=open(filename,'w')
    f.write(pack('<64s','DOS'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment))
    f.write(pack('<i',DOS.shape[0]))
    f.write(pack('<d',E[1]-E[0]))
    DOS = tuple( DOS )
    f.write(pack('<%id' % len(DOS),*DOS))
    return

def read(filename='DOS'):
    """Takes filename, returns a tuple with information and DOS as a numpy."""
    f=open(filename,'r').read()
    i = 0
    filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
    version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
    comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
    N_Bins,   = unpack('<i',f[i:i+intSize])               ; i += intSize
    dE,       = unpack('<d',f[i:i+dubSize])               ; i += dubSize
    DOS       = unpack('<%id' % (N_Bins),f[i:])
    DOS = numpy.array(DOS)
    E = numpy.arange(0,(N_Bins-0.1)*dE,dE)
    return (filetype.strip('\x00'),version,comment.strip('\x00')),E,DOS

