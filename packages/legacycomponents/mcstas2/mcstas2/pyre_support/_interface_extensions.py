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
        def _(): return self._fini_in_outputdir()
        self._in_outputdir(_)
        return
    klass._fini = _fini
    
    def _in_outputdir(self, func):
        import os
        curdir = os.path.abspath( os.curdir )
        if self._outputdir: os.chdir( self._outputdir )
        ret = func()
        os.chdir( curdir )
        return ret
    klass._in_outputdir = _in_outputdir

    def process(self, neutrons):
        return self.engine.process(neutrons)
    klass.process = process

    return klass


# version
__id__ = "$Id$"

# End of file 
