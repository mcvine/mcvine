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


def extend( component ):
    '''enrich the interfrace for the given pyre-mcstas component'''
    klass = component.__class__
    kname = component.Engine.info.name
    exec 'import %s as m' % kname
    for methodname in m.methods:
        method = getattr( m, methodname )
        setattr( klass, methodname, method )
        continue
    klass._fini0 = klass._fini
    klass._fini = _fini
    return


def _fini(self):
    self._save_histogram()
    self._fini0()
    return


# version
__id__ = "$Id$"

# End of file 
