#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(Sqe,filename='Sqe',comment=''):
  """Takes numpy Sqe in with shape (N_e,N_q) and writes to binary file."""
  with open(filename,'wb') as f:
    f.write(pack('<64s',b'Sqe'))
    f.write(pack('<i',version))
    f.write(pack('<1024s',comment.encode('ascii')))
    f.write(pack('<i',Sqe.shape[0]))
    f.write(pack('<i',Sqe.shape[1]))
    Sqe = tuple( Sqe.reshape(-1) )
    f.write(pack('<%id' % len(Sqe),*Sqe))
  return

def read(filename='Sqe'):
  """Takes filename, returns a tuple with information and Sqe as a numpy."""
  with open(filename,'rb') as stream:
    f = stream.read()
  i = 0
  filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
  version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
  comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
  N_e,N_q   = unpack('<2i',f[i:i+2*intSize])            ; i += 2*intSize
  Sqe       = unpack('<%id' % (N_e*N_q),f[i:])
  Sqe = numpy.array(Sqe)
  Sqe.shape = (N_e,N_q)
  return (filetype.strip(b'\x00').decode(),version,comment.strip(b'\x00').decode()),Sqe

