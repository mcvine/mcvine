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


from struct import pack, unpack
from .idfneutron import version, headerfmtstr, headersize, neutronsfmtstr, ndblsperneutron, filetype


def read( filename ):
    f=open(filename,'r').read()
    filetype, version, comment, N = unpack( headerfmtstr, f[ : headersize] )
    neutrons = unpack(neutronsfmtstr % (N*ndblsperneutron,),f[headersize:])
    neutrons = numpy.array(neutrons, dtype = numpy.double)
    neutrons.shape = -1, ndblsperneutron
    return filetype.strip('\x00'),version,comment.strip('\x00'),neutrons


def write( neutrons, filename='neutrons', comment = '' ):
    assert neutrons.dtype == numpy.double
    f=open(filename,'w')
    f.write( pack(headerfmtstr, filetype, version, comment, len(neutrons) ) )
    neutrons = tuple( neutrons.reshape(-1) )
    f.write(pack(neutronsfmtstr % len(neutrons),*neutrons))
    return


def test():
    import numpy
    neutrons = numpy.arange( 100000, dtype = numpy.double )
    neutrons.shape = -1, ndblsperneutron
    filename = 'neutrons.dat'
    write( neutrons, filename )
    neutrons = read( filename )
    return


if __name__ == '__main__': test()


# version
__id__ = "$Id$"

#  End of file 
