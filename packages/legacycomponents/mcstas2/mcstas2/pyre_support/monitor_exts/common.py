#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



## This enrichment requires redefinition of _fini0_in_outputdir. see __init__.py for more details


import os

def _fini_in_outputdir(self):
    self._save_histogram()
    self._fini0_in_outputdir()
    return


def _histogram_output(self):
    filename = self.inventory.filename
    b, ext = os.path.splitext(filename)
    f = '%s.h5' % b
    return f


def _save_histogram( self ):
    engine = self.__dict__.get('engine')
    if engine is None: return
    h = self._get_histogram( )
    f = self._histogram_output( )
    if self.overwrite_datafiles and os.path.exists( f ): os.remove( f )
    from histogram.hdf import dump
    dump( h, f, '/', 'c')
    return


methods = [ '_fini_in_outputdir', '_save_histogram', '_histogram_output' ]


# version
__id__ = "$Id$"

# End of file 
