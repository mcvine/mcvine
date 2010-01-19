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


import journal
info = journal.info( 'neutron_storage' )


def merge(paths, newpath):
    '''merge neutron files to one neutron file

    it is assumed that the neutrons in the input files were
    normalized correctly so that we can merge them directly.
    '''
    
    from mcni.neutron_storage import storage
    
    assert len(paths)>0
    
    out = storage(newpath, 'w')

    for path in paths:
        
        info.log( ' * Working on %r' % path )
        
        s = storage(path, 'r')
        neutrons = s.read()

        out.write(neutrons)
        continue
    
    return



# version
__id__ = "$Id$"

# End of file 
