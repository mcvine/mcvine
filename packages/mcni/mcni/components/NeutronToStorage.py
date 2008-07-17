#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


category = 'monitors'


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage import ndblsperneutron

from mcni.AbstractComponent import AbstractComponent

class NeutronToStorage( AbstractComponent ):


    '''Save neutrons to data files.

    This component saves neutrons to data files in a directory
    of your choice. The data files are in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the directory where neutron files
    will be saved.
    '''


    def __init__(self, name, path, append = False, packetsize = None):
        
        AbstractComponent.__init__(self, name)

        if not append and os.path.exists( path ):
            raise RuntimeError, "Neutron storage %r already exists. To append neutrons to this storage, please use keyword 'append=1'" % path
        
        from mcni.neutron_storage import storage
        self._storage = storage( path, mode = 'w', packetsize = packetsize ) 
        return


    def process(self, neutrons):
        self._storage.write( neutrons )
        return neutrons

    pass # end of Source


import os


# version
__id__ = "$Id$"

# End of file 
