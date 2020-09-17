#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(E,DOS,filename='DOS',comment='', E_unit='TeraHz'):
    """Takes numpy DOS in with shape (N_e) and writes to binary file."""
    if E_unit == 'TeraHz':
        pass
    elif E_unit == 'meV':
        from .units import hertz2mev
        from math import pi
        E = E/hertz2mev/1e12/2/pi
    else:
        raise NotImplementedError("energy unit: %s" % E_unit)
    f=open(filename,'wb')
    f.write(pack('<64s',b'DOS'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment.encode('ascii')))
    f.write(pack('<i',DOS.shape[0]))
    f.write(pack('<d',E[1]-E[0]))
    DOS = tuple( DOS )
    f.write(pack('<%id' % len(DOS),*DOS))
    return

def read(filename='DOS'):
    """Takes filename, returns a tuple with information and DOS as a numpy."""
    f=open(filename,'rb').read()
    i = 0
    filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
    version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
    comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
    N_Bins,   = unpack('<i',f[i:i+intSize])               ; i += intSize
    dE,       = unpack('<d',f[i:i+dubSize])               ; i += dubSize
    DOS       = unpack('<%id' % (N_Bins),f[i:])
    DOS = numpy.array(DOS)
    E = numpy.arange(0,(N_Bins-0.1)*dE,dE)
    return (filetype.strip(b'\x00').decode(),version,comment.strip(b'\x00').decode()),E,DOS

