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


from struct import pack, unpack
from .idfneutron import version, headerfmtstr, headersize, neutronsfmtstr, ndblsperneutron, filetype, neutronsize



def checkformat(filename=None, stream=None):
    """check whether the given file is in the right format
    return: 1-format good;  0-no good
    """
    if not stream: stream = open(filename, 'rb')
    stream.seek(0)
    h = stream.read(headersize)
    filetype1, version1, comment, N = unpack( headerfmtstr, f[ : headersize] )
    return filetype == filetype1 and version == version1



def count(filename=None, stream=None):
    'return number of neutrons'
    if not stream: stream = open(filename, 'rb')
    stream.seek(0,2); end = stream.tell()
    return (end-headersize)//neutronsize


def totalintensity(filename=None, stream=None):
    'return sum of intensities of all neutrons'
    neutrons = read(filename=filename, stream=stream)
    if neutrons is None:
        return 0
    # XXX: the last double is the probability
    return neutrons[:, -1].sum()


def read(filename=None, stream=None, start=None, n=None):
    """read neutrons[start:end] from given file (or stream)
    """
    if not stream: stream = open(filename, 'rb')
    if start is None and n is None:
        start = 0
        n = count(stream=stream)
        
    assert start is not None and n is not None

    # nothing to read, just return
    if n == 0:
        return
    
    assert start >= 0 and n > 0
    stream.seek(headersize+neutronsize*start)
    s = stream.read(n*neutronsize)
    neutrons = numpy.fromstring(s, numpy.double)
    neutrons.shape = -1, ndblsperneutron
    return neutrons


def readall(filename=None, stream=None):
    if stream is None:
        stream = open(filename,'rb')
    # read everything
    stream.seek(0)
    f = stream.read()
    #
    filetype, version, comment, N = unpack( headerfmtstr, f[ : headersize] )

    neutrons = numpy.fromstring( f[headersize:], numpy.double )

    neutrons.shape = -1, ndblsperneutron
    return (
        filetype.strip(b'\x00').decode(), version,
        comment.strip(b'\x00').decode(), neutrons
    )


def write( neutrons, filename='neutrons', comment = '', stream=None):
    assert neutrons.dtype == numpy.double
    if not stream:
        stream=open(filename,'wb')
    header = pack(
        headerfmtstr, 
        filetype.encode('ascii'), version,
        comment.encode('ascii'), len(neutrons)
    )
    stream.write( header )
    neutrons.shape = -1,
    stream.write( neutrons.tostring() )
    return


def append(neutrons, filename=None, stream=None):
    if not stream: stream = open(filename, 'ab')
    stream.write(neutrons.tostring() )
    return



def test():
    import numpy
    N = 100

    # read/write
    neutrons = numpy.arange( N*ndblsperneutron, dtype = numpy.double )
    neutrons.shape = -1, ndblsperneutron
    filename = 'neutrons.dat'
    write( neutrons, filename )
    filetype, version, comment, neutrons = read( filename )
    assert neutrons.shape == (N, ndblsperneutron)

    # write/append/read
    filename = 'neutrons.dat'
    write( neutrons, filename)
    append(neutrons, filename)
    filetype, version, comment, neutrons = read( filename )
    assert neutrons.shape == (N*2, ndblsperneutron)
    
    a = neutrons.copy()
    a.shape = -1,
    for i in range(N*ndblsperneutron):
        assert a[i] == i
        assert a[i+N*ndblsperneutron] == i
        continue

    # count
    assert count(filename) == 2*N

    # read one neutron
    neutrons1 = read(filename, start=2, n=1)
    assert len(neutrons1) == 1
    neutron1 = neutrons1[0]
    assert neutron1[0] == 2*ndblsperneutron
    return


if __name__ == '__main__': test()


# version
__id__ = "$Id$"

#  End of file 
