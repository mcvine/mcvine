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



# This enrichment requires redefinition of several methods, such as _fini0_in_outputdir.
# Please see __init__.py for more details


def process(self, neutrons):
    iterationcount = self.__dict__.get('iterationcount')
    if iterationcount is None: iterationcount = 0
    ret = self.engine.process(neutrons)
    iterationcount += 1
    self.iterationcount = iterationcount
    
    # save monitor data to a histogram
    hout = self._histogram_output()
    self._save_histogram(hout)
    self._save_histogram('%s.%s' % (hout, iterationcount))
    return ret


def _fini_in_outputdir(self):
    if not self._showHelpOnly:
        self._save_histogram_in_outputdir(self._histogram_output())
    self._fini0_in_outputdir()
    return


def _histogram_output(self):
    filename = self.inventory.filename
    b, ext = os.path.splitext(filename)
    f = '%s.h5' % b
    return f


def _save_histogram(self, filename):
    def _():
        return self._save_histogram_in_outputdir(filename)
    return self._in_outputdir(_)


def _save_histogram_in_outputdir(self, filename):
    engine = self.__dict__.get('engine')
    # if engine has not been established, skip
    if engine is None: return

    # get the histogram to output
    h = self._get_histogram( )

    # remove old file
    if self.overwrite_datafiles and os.path.exists( filename ): os.remove( filename )

    # dump
    from histogram.hdf import dump
    dump( h, filename, '/', 'c')
    return


methods = [
    'process',
    '_fini_in_outputdir',
    '_save_histogram',
    '_save_histogram_in_outputdir',
    '_histogram_output',
    ]


import os


# version
__id__ = "$Id$"

# End of file 
