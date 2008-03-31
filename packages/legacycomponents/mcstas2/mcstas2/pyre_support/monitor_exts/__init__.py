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

    # component specific extension
    kname = component.Engine.info.name
    exec 'import %s as m' % kname
    _extend( klass, m, m.methods )

    # common extension
    #  !need to save _fini0 first!
    klass._fini0 = klass._fini
    import common
    _extend( klass, common, common.methods )
    
    return



def _extend( klass, depository, methods ):
    for methodname in methods:
        method = getattr(depository, methodname )
        setattr( klass, methodname, method )
        continue
    return


methods = [ '_fini', '_save_histogram' ]


# version
__id__ = "$Id$"

# End of file 
