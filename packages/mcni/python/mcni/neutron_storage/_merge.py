#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
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

        if neutrons:
            out.write(neutrons)
        continue
    return

# End of file
