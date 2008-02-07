#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## load and dump neutrons to data file. file format is specified
## in svn://danse.us/inelastic/idf/Neutron.v1


import numpy

from idfneutron import ndblsperneutron

def dump( neutrons, filename ):
    '''dump neutrons to the given file
    neutrons: a boost python instance of Neutron::Events, which can be
        created by mcni.neutron_buffer
    filename: path to the file where neutrons will be written
    '''

    arr = neutrons_as_npyarr( neutrons )
    
    from idf_usenumpy import write
    write( arr, filename )
    return


def load( filename ):
    '''load neutrons from the given file

    return:  a boost python instance of Neutron::Events, which can be
        created by mcni.neutron_buffer
    '''
    neutrons = readneutrons_asnpyarr( filename )
    neutrons = neutrons_from_npyarr( neutrons )
    return neutrons


def readneutrons_asnpyarr( filename ):
    from idf_usenumpy import read
    filetype, version, comment, neutrons = read( filename )
    from idfneutron import version as ver, filetype as ft
    assert filetype == ft
    assert version == ver
    return neutrons


def neutrons_from_npyarr( arr, neutrons = None ):
    '''copy data from a numpy array to a boost python instance of
    Neutron::Events.

    arr: the numpy array
    neutrons: the Neutron::Events instance where data will be copied.
      if None, a new instance will be created.
    '''
    shape = arr.shape
    assert shape[1] == ndblsperneutron
    n = len(arr)

    if neutrons is None:
        import mcni
        neutrons = mcni.neutron_buffer( n )
        pass

    n = min( n, len(neutrons) )

    cevents = cevents_from_npyarr( arr )
    
    neutrons.fromCevents( cevents, n )

    return neutrons


def neutrons_as_npyarr( neutrons ):
    '''copy data from a boost python instance of Neutron::Events
    to a numpy array'''
    n = len(neutrons)
    ceventsnpyarr = numpy.zeros( n*ndblsperneutron, numpy.double )

    cevents = cevents_from_npyarr( ceventsnpyarr )
    neutrons.toCevents( cevents, n )
    
    return ceventsnpyarr


def cevents_from_npyarr( npyarr ):
    '''convert a numpy array to a boost-python instance of Neutron::cEvent pointer'''
    from numpyext import getdataptr
    ptr = getdataptr( npyarr )
    from bpext import wrap_ptr
    import mcni
    cevents = wrap_ptr( ptr, 'cNeutronEvent' )
    return cevents


# version
__id__ = "$Id$"

# End of file 
