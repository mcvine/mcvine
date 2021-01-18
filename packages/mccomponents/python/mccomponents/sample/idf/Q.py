#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(Q,filename='Q',comment=''):
  """Takes numpy Q in with shape (N_q,D) and writes to binary file."""
  with open(filename,'wb') as f:
    f.write(pack('<64s',b'Q'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment.encode('ascii')))
    f.write(pack('<i',Q.shape[1]))
    f.write(pack('<i',Q.shape[0]))
    Q = tuple( Q.reshape(-1) )
    f.write(pack('<%id' % len(Q),*Q))
  return

def read(filename='Q'):
  """Takes filename, returns a tuple with information and Q as a numpy."""
  with open(filename,'rb') as stream:
    f = stream.read()
  i = 0
  filetype,= unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
  version, = unpack('<i',f[i:i+intSize])               ; i += intSize
  comment, = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
  D,N_q    = unpack('<2i',f[i:i+2*intSize])            ; i += 2*intSize
  Q        = unpack('<%id' % (N_q*D),f[i:])
  Q = numpy.array(Q)
  Q.shape = (N_q,D)
  return (filetype.strip(b'\x00').decode(),version,comment.strip(b'\x00').decode()),Q

