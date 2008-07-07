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


def extend(klass):
    # this is not a good implementation
    # this assumes that all _fini steps will be performed
    # in the _outputdir directory.
    # for now this seems to be no problem, but this
    # is vulnerable.
    klass._fini_in_outputdir = klass._fini
    def _fini(self):
        import os
        curdir = os.path.abspath( os.curdir )
        if self._outputdir: os.chdir( self._outputdir )
        klass._fini_in_outputdir(self)
        os.chdir( curdir )
        return
    klass._fini = _fini
    
    return klass


# version
__id__ = "$Id$"

# End of file 
