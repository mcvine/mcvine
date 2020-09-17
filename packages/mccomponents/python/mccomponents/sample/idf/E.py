#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(E,filename='E',comment=''):
  """Takes numpy E in with shape (N_e) and writes to binary file."""
  f=open(filename,'wb')
  f.write(pack('<64s',b'E'))
  f.write(pack('<i',version))
  f.write(pack('<1024s',comment.encode('ascii')))
  f.write(pack('<i',E.shape[0]))
  E = tuple( E )
  f.write(pack('<%id' % len(E),*E))
  return

def read(filename='E'):
  """Takes filename, returns a tuple with information and E as a numpy."""
  f=open(filename,'rb').read()
  i = 0
  filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
  version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
  comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
  N_e       = unpack('<i',f[i:i+intSize])               ; i += intSize
  E         = unpack('<%id' % (N_e),f[i:])
  E = numpy.array(E)
  return (filetype.strip(b'\x00').decode(),version,comment.strip(b'\x00').decode()),E

