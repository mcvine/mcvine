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



from mcni.neutron_storage import ndblsperneutron

from mcni.AbstractComponent import AbstractComponent

class NeutronToStorage( AbstractComponent ):


    '''Save neutrons to data files.

    This component saves neutrons to a data file
    of your choice. The data file is in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the file.
    '''


    def __init__(self, name, path, append = False):
        
        AbstractComponent.__init__(self, name)

        if not append and os.path.exists( path ):
            raise RuntimeError, "Neutron storage %r already exists. To append neutrons to this storage, please use keyword 'append=1'" % path
        
        if append: mode='a'
        else: mode = 'w'
        
        from mcni.neutron_storage import storage
        self._storage = storage( path, mode = mode) 
        return


    def process(self, neutrons):
        self._storage.write( neutrons )
        return neutrons


    def close(self):
        self._storage.close()
        return


    
    pass # end of NeutronToStorage


import os


# version
__id__ = "$Id$"

# End of file 
