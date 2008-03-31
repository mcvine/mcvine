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



## This enrichment requires redefinition of _fini0. see __init__.py for more details


def _fini(self):
    self._save_histogram()
    self._fini0()
    return


def _save_histogram( self ):
    engine = self.__dict__.get('engine')
    if engine is None: return
    h = self._get_histogram( )
    filename = self.inventory.filename
    import os
    b, ext = os.path.splitext(filename)
    f = '%s.h5' % b
    from histogram.hdf import dump
    dump( h, f, '/', 'c')
    return


methods = [ '_fini', '_save_histogram' ]


# version
__id__ = "$Id$"

# End of file 
