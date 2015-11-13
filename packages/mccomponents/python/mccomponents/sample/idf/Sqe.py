#!/usr/bin/python

import numpy
from struct import pack,unpack,calcsize

version=1

intSize = calcsize('<i')
dubSize = calcsize('<d')
strSize = calcsize('<s')

def write(Sqe,filename='Sqe',comment=''):
  """Takes numpy Sqe in with shape (N_e,N_q) and writes to binary file."""
  f=open(filename,'w')
  f.write(pack('<64s','Sqe'))
  f.write(pack('<i',version))
  f.write(pack('<1024s',comment))
  f.write(pack('<i',Sqe.shape[0]))
  f.write(pack('<i',Sqe.shape[1]))
  Sqe = tuple( Sqe.reshape(-1) )
  f.write(pack('<%id' % len(Sqe),*Sqe))
  return

def read(filename='Sqe'):
  """Takes filename, returns a tuple with information and Sqe as a numpy."""
  f=open(filename,'r').read()
  i = 0
  filetype, = unpack('<64s',f[i:i+64*strSize])          ; i += 64*strSize
  version,  = unpack('<i',f[i:i+intSize])               ; i += intSize
  comment,  = unpack('<1024s',f[i:i+1024*strSize])      ; i += 1024*strSize
  N_e,N_q   = unpack('<2i',f[i:i+2*intSize])            ; i += 2*intSize
  Sqe       = unpack('<%id' % (N_e*N_q),f[i:])
  Sqe = numpy.array(Sqe)
  Sqe.shape = (N_e,N_q)
  return (filetype.strip('\x00'),version,comment.strip('\x00')),Sqe

