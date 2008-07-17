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


def merge( directories, newdir, newpacketsize = None ):
    
    from mcni.neutron_storage import storage
    
    assert len(directories)>0
    
    dir0 = directories[0]
    packetsize = storage( dir0 ).packetsize()

    if newpacketsize is None: newpacketsize = packetsize
    out = storage( newdir, 'w', packetsize = newpacketsize )

    for directory in directories:
        
        info.log( ' * Working on directory %r' % directory )
        
        s = storage( directory, 'r' )

        for i in range( s.npackets() ):
            info.log( '  - packet %d' % i )
            neutrons = s.read( i )
            out.write( neutrons )
            continue
        
        continue
    
    return



# version
__id__ = "$Id$"

# End of file 
