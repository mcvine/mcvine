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



def storage( *args, **kwds ):
    from .Storage import Storage
    return Storage( *args, **kwds )


def merge_and_normalize(filename, outputs_dir, overwrite_datafiles=True):
    """merge_and_normalize('scattered-neutrons', 'out')
    """
    # find all output files
    from mcni.components.outputs import n_mcsamples_files, mcs_sum
    import glob, os
    pattern = os.path.join(outputs_dir, '*', filename)
    nsfiles = glob.glob(pattern)
    n_mcsamples = n_mcsamples_files(outputs_dir)
    assert len(nsfiles) == n_mcsamples, \
        "neutron storage files %s does not match #mcsample files %s" %(
        len(nsfiles), n_mcsamples)
    if not nsfiles:
        return None, None

    # output
    out = os.path.join(outputs_dir, filename)
    if overwrite_datafiles:
        if os.path.exists(out):
            os.remove(out)
    # merge
    from mcni.neutron_storage import merge
    merge(nsfiles, out)

    # number of neutron events totaly in the neutron file
    from mcni.neutron_storage.idf_usenumpy import count
    nevts = count(out)

    # load number_of_mc_samples
    mcs = mcs_sum(outputs_dir)

    # normalization factor. this is a bit tricky!!!
    nfactor = mcs/nevts

    # normalize
    from mcni.neutron_storage import normalize
    normalize(out, nfactor)
    return


def merge( *args, **kwds ):
    from .merge import merge
    merge( *args, **kwds )
    return


def normalize(neutronsfile, N, output=None):
    """normalize the neutrons in the given file by the factor N"""
    # create a temporary output file
    import os
    if not output:
        import tempfile
        pdir = os.path.dirname(neutronsfile)
        fd, tmpout = tempfile.mkstemp(dir=pdir)
        os.close(fd)
        os.remove(tmpout)
    else:
        tmpout = None
    #
    _normalize(neutronsfile, N, output=tmpout or output)
    #
    if tmpout:
        os.rename(tmpout, neutronsfile)
    return


def _normalize(input, N, output):
    """normalize the neutrons in the given file by the factor N
    and save it in the output
    """
    import os
    input = os.path.abspath(input)
    output = os.path.abspath(output)
    # guards
    assert input != output
    if os.path.exists(output):
        raise IOError('%s already exists' % output)
    # total # of neutrons
    remain = count(input)
    # output storage
    out = storage(output, mode='w')
    # input storage
    input = storage(input)
    #
    chunk = int(1e6)
    # 
    from mcni import neutron_buffer
    nb = neutron_buffer(0)
    while remain:
        n = min(remain, chunk)
        # read
        neutrons = input.read(n, asnpyarr=True)
        # normalize
        neutrons[:, -1] /= N
        # write
        nb.from_npyarr(neutrons)
        out.write(nb)
        #
        remain -= n
        continue
    return


def dump( neutrons, filename ):
    '''dump neutrons to the given file
    neutrons: a boost python instance of Neutron::Events, which can be
        created by mcni.neutron_buffer
    filename: path to the file where neutrons will be written
    '''

    arr = neutrons_as_npyarr( neutrons )
    
    from .idf_usenumpy import write
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
    from .idf_usenumpy import readall
    filetype, version, comment, neutrons = readall( filename )
    from .idfneutron import version as ver, filetype as ft
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

    cevents = binding.cevents_from_npyarr( arr )
    
    neutrons.fromCevents( cevents, n )

    return neutrons


def neutrons_as_npyarr( neutrons ):
    '''copy data from a boost python instance of Neutron::Events
    to a numpy array'''
    n = len(neutrons)
    ceventsnpyarr = numpy.zeros( n*ndblsperneutron, numpy.double )
    
    cevents = binding.cevents_from_npyarr( ceventsnpyarr )
    neutrons.toCevents( cevents, n )
    
    return ceventsnpyarr



import numpy
from .idfneutron import ndblsperneutron
from .idf_usenumpy import count
from mcni.bindings import current as binding


# version
__id__ = "$Id$"

# End of file 
